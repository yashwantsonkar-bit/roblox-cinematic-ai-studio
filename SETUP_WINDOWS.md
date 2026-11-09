# Windows setup

This guide is tailored for Windows + Claude Code + Roblox Studio + Blender 5.2.x.

## A. Roblox Studio built-in MCP (recommended)

Roblox now documents a built-in Studio MCP server and specifically lists Claude Code as a supported quick-connect client.

1. Open Roblox Studio and the target place.
2. Open Assistant.
3. Click `...` → `Manage MCP Servers`.
4. Enable `Studio as MCP server`.
5. Under Quick connect, enable Claude Code.
6. Confirm Studio shows a connected-client indicator.
7. In Claude Code, verify the connection and ask it to list connected Studio instances and inspect the correct place before editing.

Official instructions: https://create.roblox.com/docs/studio/mcp

The optional template in `templates/claude-mcp.windows.example.json` shows the documented Windows command form. Prefer Studio's Quick connect because it can configure the client automatically.

## B. Blender MCP

Official Blender Lab MCP requires Blender 5.1 or newer, an add-on, an MCP server, and an MCP-capable client. Blender 5.2.x meets the documented version requirement.

1. Read the official setup and security warning: https://www.blender.org/lab/mcp-server/
2. Install the Blender Lab repository/add-on from the official Blender Lab extension repository.
3. Install Git and `uv` if not already available.
4. Clone the official server repository, for example:
   `git clone https://projects.blender.org/lab/blender_mcp.git C:\AI\blender_mcp`
5. Install/run according to the official setup. The current documented Windows MCP client example uses `uv` and the `mcp` subfolder.
6. Copy the Blender entry from `templates/claude-mcp.windows.example.json` into your project `.mcp.json`, replacing `C:\\AI\\blender_mcp\\mcp` with the actual path.
7. Start Blender, enable the add-on, then start Claude Code and verify Blender MCP tools are visible.
8. Test read-only scene inspection first. Only then allow controlled edits.

Security: the official Blender MCP can execute LLM-generated Python code inside Blender without protective guards. Use a separate project copy and do not keep sensitive files open in the same Blender session.

Official setup: https://projects.blender.org/lab/blender_mcp/wiki/Setup

## C. ElevenLabs MCP (optional)

ElevenLabs documents a hosted MCP endpoint:
`https://api.elevenlabs.io/v1/mcp`

Connect it from a compatible MCP client and complete its OAuth authorization. The available features depend on your workspace/account and may consume credits. Review permissions and pricing before authorizing. Do not store credentials in this repository.

Official docs: https://elevenlabs.io/docs/eleven-api/resources/mcp-server

## D. FFmpeg (optional)

Install FFmpeg from a trusted distribution and ensure `ffmpeg` is on PATH. Verify with:
`ffmpeg -version`

FFmpeg is for local video/audio assembly, not AI generation.

## E. Install the skill

Copy:
`skills\roblox-video-production`
to:
`%USERPROFILE%\.claude\skills\roblox-video-production`

Restart Claude Code or reload skills according to your installed Claude Code version. In Claude Code, invoke `/roblox-video-production` or ask for a Roblox video; confirm that the skill is discovered.

## F. Verify

Run:
`python scripts\check_environment.py`

Then in Claude Code:
- list available MCP servers/tools
- list connected Roblox Studio instances
- inspect Blender connection
- do a read-only test before any scene modifications
