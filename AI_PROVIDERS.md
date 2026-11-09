# AI provider map

This project intentionally uses a provider-neutral design. It does not claim that every provider is connected or free.

## Included documented integration

### ElevenLabs MCP — optional
Official hosted MCP: `https://api.elevenlabs.io/v1/mcp`
The official documentation describes speech, voices, transcription, sound effects, music, images and video generation through its creative workflows. Actual availability, model choices, limits and credit costs depend on account/workspace. OAuth authorization is required.

## Local application tools (not AI models)

- Roblox Studio built-in MCP: lets Claude Code interact with the actual Studio session. It can inspect/edit the place, run scripts, playtest and capture screenshots as documented by Roblox.
- Blender MCP: lets an MCP client interact with a running Blender instance through its Python API. It is a tool bridge, not a generative AI model.

## Other providers

No speculative provider endpoints are preconfigured. Add an adapter only after verifying:
1. Official documentation and current endpoint.
2. Authentication method and secret storage.
3. Supported operations (image, video, voice, music, lip-sync).
4. Pricing, credits, rate limits and terms.
5. Output download and local file handoff.
6. Error handling and retry policy.

## Provider adapter contract

Each future adapter should expose:
- `capabilities`: explicit supported media operations
- `estimate_cost`: when provider exposes pricing/credits
- `generate`: one requested task
- `poll`: asynchronous job status
- `download`: verified output to project output folder
- `validate`: file type, dimensions, duration and checksum
- `cleanup`: remove temporary files only with safe path checks

Never claim that a provider supports lip-sync, consistent characters, or video editing unless its current official docs confirm it.
