"""Rebuild the live sections of the xnfinite profile page from public GitHub data.

Only what the GitHub API returns goes on the page, each line linked to its source.
Writes README.md from template.md. Stops without writing if GitHub gives no data, and
leaves the file alone when nothing but the date would change.
"""
import datetime
import json
import os
import pathlib
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

AGENT = "nightlab-agent"
OWNER = "xnfinite"
HERE = pathlib.Path(__file__).resolve().parent
SKIP_TOOLS = ("Moved to", "Frozen", "Images that")
LONGEST_LINE = 120


def get(path):
    request = urllib.request.Request(
        "https://api.github.com" + path,
        headers={"Accept": "application/vnd.github+json", "User-Agent": "xnfinite-profile"},
    )
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        request.add_header("Authorization", "Bearer " + token)
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def merged_prs():
    query = urllib.parse.quote(f"author:{AGENT} is:pr is:merged -user:{AGENT} -user:{OWNER}")
    found = get(f"/search/issues?q={query}&per_page=100&sort=updated")
    if found["incomplete_results"]:
        sys.exit("GitHub search was incomplete; README left as it is.")
    return found["items"], found["total_count"]


def safe(text):
    text = " ".join(text.split())
    return re.sub(r"([\\|\[\]<>`])", r"\\\1", text)


def stars_of(full_name):
    try:
        return f"{get('/repos/' + full_name)['stargazers_count']:,}"
    except urllib.error.HTTPError:
        return "-"


def merged_table(prs):
    rows = ["| Project | Stars | Change |", "| --- | --- | --- |"]
    stars = {}
    for pr in sorted(prs, key=lambda p: p["closed_at"], reverse=True):
        full_name = pr["repository_url"].split("/repos/")[1]
        if full_name not in stars:
            stars[full_name] = stars_of(full_name)
        rows.append(
            f"| [{full_name}](https://github.com/{full_name}) | {stars[full_name]} "
            f"| [{safe(pr['title'])}]({pr['html_url']}) |"
        )
    return "\n".join(rows)


def short(description):
    text = re.split(r"\. |; | \(", " ".join(description.split()), maxsplit=1)[0].rstrip(".")
    if len(text) > LONGEST_LINE:
        text = text[:LONGEST_LINE].rsplit(" ", 1)[0].rstrip(",:") + "..."
    return safe(text)


def is_tool(repo):
    description = repo["description"] or ""
    return (
        not repo["fork"]
        and description
        and not description.startswith(SKIP_TOOLS)
        and "Moved to" not in description
        and not repo["name"].endswith(".github.io")
    )


def tools_list(repos):
    own = sorted(filter(is_tool, repos), key=lambda r: r["pushed_at"], reverse=True)
    lines = [f"- [{r['name']}]({r['html_url']}): {short(r['description'])}" for r in own]
    return "\n".join(lines), len(own)


def without_date(text):
    return re.sub(r"updated \d{4}-\d{2}-\d{2}", "updated", text)


def main():
    prs, merged_count = merged_prs()
    repos = get(f"/users/{AGENT}/repos?per_page=100&sort=pushed")
    if not prs or not repos:
        sys.exit("GitHub returned no data; README left as it is.")
    tools, tool_count = tools_list(repos)
    projects = {p["repository_url"] for p in prs}
    text = (HERE / "template.md").read_text(encoding="utf-8")
    values = {
        "{{MERGED_TABLE}}": merged_table(prs),
        "{{TOOLS}}": tools,
        "{{MERGED_COUNT}}": str(merged_count),
        "{{PROJECT_COUNT}}": str(len(projects)),
        "{{TOOL_COUNT}}": str(tool_count),
        "{{UPDATED}}": datetime.date.today().isoformat(),
    }
    for key, value in values.items():
        text = text.replace(key, value)
    target = HERE / "README.md"
    if target.exists() and without_date(target.read_text(encoding="utf-8")) == without_date(text):
        return
    target.write_text(text, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
