<p align="center"><img src="banner.svg" alt="xnfinite: agents that work through the night" width="100%"></p>

I build AI agents that work on their own, and the systems that keep them honest.

**[Nightlab](https://nightlab-agent.github.io/)** is the AI agent I created. It picks its own work and writes the code, and other agents review it before it ships. It now works with a second agent on a different model.

**6** changes merged into **4** outside projects · **14** public tools · [videos of the work](https://www.youtube.com/@NightlabBC)

## Merged into other people's projects

Nightlab's pull requests, accepted by the people who run these projects.

| Project | Stars | Change |
| --- | --- | --- |
| [hslee16/Archy](https://github.com/hslee16/Archy) | 8 | [fix(dsm): name the near misses when --focus or --package matches nothing (#643)](https://github.com/hslee16/Archy/pull/716) |
| [nrzz/claude-cost-guard](https://github.com/nrzz/claude-cost-guard) | 1 | [Note in budget show when a model budget matches no model in the history](https://github.com/nrzz/claude-cost-guard/pull/8) |
| [nrzz/claude-cost-guard](https://github.com/nrzz/claude-cost-guard) | 1 | [Note when budget set --model matches no model in the history](https://github.com/nrzz/claude-cost-guard/pull/6) |
| [software-mansion/argent](https://github.com/software-mansion/argent) | 3,157 | [fix: exit 128+signo when tail is killed in server logs -f](https://github.com/software-mansion/argent/pull/1724) |
| [AlanEdward19/waymark](https://github.com/AlanEdward19/waymark) | 3 | [fix: name all six MCP tools in the start-up context](https://github.com/AlanEdward19/waymark/pull/83) |
| [hslee16/Archy](https://github.com/hslee16/Archy) | 8 | [fix(cli,diff,dsm): name the path when a file option is given a directory (#647)](https://github.com/hslee16/Archy/pull/679) |

## What Nightlab has built

- [subagent-spend](https://github.com/nightlab-agent/subagent-spend): Claude Code plugin: a spend cap for interactive sessions, and per-subagent tokens, rate-limit windows, context fill...
- [agent-undo](https://github.com/nightlab-agent/agent-undo): Claude Code mod: lists the Edit and Write calls Claude Code and its subagents make in a session, hunk by hunk, and in a...
- [file-trail](https://github.com/nightlab-agent/file-trail): Claude Code mod: which file each Read, Edit and Write touched
- [message-times](https://github.com/nightlab-agent/message-times): Claude Code plugin: puts the time on each prompt and each reply in Claude Code's main transcript view, and keeps the...
- [agents-skills](https://github.com/nightlab-agent/agents-skills): Claude Code plugin: lets Claude Code use the skills in .agents/skills/ by copying each one into .claude/skills/ at...
- [date-check](https://github.com/nightlab-agent/date-check): Claude Code mod: checks the dates and times Claude Code writes into changelogs, logs, release notes and handoffs...
- [prompt-state](https://github.com/nightlab-agent/prompt-state): Claude Code mod: shows under the prompt what Claude Code is doing
- [plan-names](https://github.com/nightlab-agent/plan-names): Claude Code mod: saves every approved plan as plans/\<date\>-\<title\>.md in your project, and keeps the earlier version...
- [interrupt-hook](https://github.com/nightlab-agent/interrupt-hook): Claude Code plugin: Escape skips the Stop hook, so this runs your command when you stop a turn with Escape, with a...
- [opencode-subagent-cap](https://github.com/nightlab-agent/opencode-subagent-cap): opencode plugin: cap how many subagents
- [plugin-lag](https://github.com/nightlab-agent/plugin-lag): Shows which of your installed Claude Code marketplace plugins are pinned to a commit that lags the plugin's upstream...
- [codex-config-sync](https://github.com/nightlab-agent/codex-config-sync): Share one Codex config.toml across machines
- [npm-release-check](https://github.com/nightlab-agent/npm-release-check): Look at what npm pack would ship before you release: secrets and private files in the tarball, missing entry points...
- [mod-ready](https://github.com/nightlab-agent/mod-ready): A Claude Code mod template whose one release check runs validate, tests, a type check and npm pack

## My own projects

- [icm-ops](https://github.com/xnfinite/icm-ops): skills that keep an agent's workspace honest, for Claude Code, Codex and others
- [webmcp-verified](https://github.com/xnfinite/webmcp-verified): tools for MCP and WebMCP agents that answer from real data
- [nightcore-sdk](https://github.com/xnfinite/nightcore-sdk): an SDK for verified WebAssembly execution, in Rust, Python and TypeScript

<sub>Numbers and lists come from GitHub's public data, updated 2026-11-04. Agent-built work is labelled as agent-built.</sub>
