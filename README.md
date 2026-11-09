# Roblox Cinematic AI Studio Ultimate

A Windows-first, low-end-PC-aware production repository for making Roblox-style cinematic videos with:

- **Claude Code** as director/orchestrator
- **Roblox Studio built-in MCP** for inspecting, editing and playtesting the actual Roblox project
- **Blender MCP** for 3D scene, camera, animation and rendering work
- **ElevenLabs MCP (optional)** for voice, sound, music, and its available creative-generation tools
- **FFmpeg (optional)** for assembling clips, voice, music and captions

> This repository is an automation framework, not a bundle of paid AI models. It does not contain API keys, paid credits, or magically enable services. You must install/authorize each external tool yourself.

## Key principles

1. **Search before create. Reuse before replace. Inspect before modify.**
2. Prefer quality existing Roblox assets and approved free Creator Store assets over primitive placeholder builds.
3. Preserve original project files; make backups before destructive changes.
4. Low-end PC first: one heavy local task at a time, proxies, draft renders, caching, scene-by-scene processing.
5. Never claim success until the output or live application state has been verified.
6. Never upload/publish a Roblox experience or spend paid generation credits without explicit approval.

## Repository layout

- `skills/roblox-video-production/SKILL.md` — installable Claude Code skill
- `workflows/` — detailed production playbooks
- `config/` — MCP examples and performance settings
- `scripts/` — safe environment checks and project scaffolding
- `templates/` — example Claude Code MCP configuration
- `docs/` — setup, security, troubleshooting and provider guide

## Quick start (Windows)

1. Extract this repository to a stable folder, e.g. `C:\AI\roblox-cinematic-ai-studio-ultimate`.
2. Install Claude Code, Roblox Studio, Blender 5.2.x, Python 3.11+ and FFmpeg (optional).
3. Read `docs/SETUP_WINDOWS.md`.
4. Enable Roblox Studio's built-in MCP in Studio Assistant → `...` → Manage MCP Servers → Enable Studio as MCP server → Quick connect → Claude Code.
5. Install the Blender MCP add-on and server using `docs/SETUP_WINDOWS.md`.
6. Optionally connect ElevenLabs MCP if you have an account and want to use its paid/credit-based services.
7. Copy/merge `templates/claude-mcp.windows.example.json` into your project's `.mcp.json`. Replace the Blender path placeholder. Do not overwrite an existing config; merge entries.
8. Put the skill folder under `~/.claude/skills/roblox-video-production/` (Windows: `%USERPROFILE%\.claude\skills\roblox-video-production\`) or use the skill from this repo according to your Claude Code version's skill discovery behavior.
9. Run `python scripts/check_environment.py`.

## What is actually integrated?

| Tool | Role | Included here |
|---|---|---|
| Claude Code | Plans and coordinates work | Skill and workflows |
| Roblox Studio MCP | Real Studio session control | Official connection template/instructions |
| Blender MCP | Blender scene inspection/control/render workflow | Official setup instructions + MCP template |
| ElevenLabs MCP | Voice/audio and other account-enabled creative tools | Optional hosted MCP entry |
| FFmpeg | Local video assembly | Detection and usage guidance |
| Image/video model providers | Generate additional visuals/clips if configured | Provider-neutral adapter contract only |

**Important:** Blender and Roblox Studio are applications/tools, not AI models. ElevenLabs is a connected AI service. Other providers must be added only after checking their current official API/MCP documentation. No fake integrations are included.

## Safety

MCP tools can modify open projects. Blender MCP can execute generated Python inside Blender; Roblox Studio MCP can read and modify the open place. Connect only tools you trust, keep backups, and review destructive actions.
