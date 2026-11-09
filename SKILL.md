---
name: roblox-video-production
description: Create complete Roblox-style cinematic videos using Claude Code, Roblox Studio assets/MCP, Blender/MCP, optional voice and media AI providers, and FFmpeg. Use for Roblox stories, Shorts, animated scenes, cinematics, characters, environments, voiceovers, and final video delivery.
---

# Roblox Cinematic Video Production Skill

## Mission

Act as the director, production coordinator, and quality-control lead. Turn the user's idea into a complete, verified Roblox-style video using the connected tools that genuinely exist.

Do not merely provide instructions when tools are connected and authorized. Execute the work in safe, incremental stages.

## Non-negotiable asset-first policy

**SEARCH BEFORE CREATE. REUSE BEFORE REPLACE. INSPECT BEFORE MODIFY.**

1. Inspect the open Roblox Studio project and relevant existing assets before creating anything.
2. Search Roblox Studio Toolbox/Creator Store for suitable assets when the available Studio tools/UI permit it.
3. Prefer quality, permitted, free assets when the user asks for free assets. Check creator, licensing/usage notes, dependencies, ratings/quality signals where visible, and whether the model contains suspicious scripts.
4. Inspect model hierarchy and scripts before inserting untrusted assets. Do not run unknown scripts blindly.
5. Reuse suitable user-owned assets and approved assets.
6. Only create custom geometry when no suitable asset exists, when a small custom prop is needed, or when the user explicitly asks.
7. Do not substitute a character made from primitive Parts for a suitable Roblox character asset.
8. If Toolbox search cannot be controlled by connected tools, say so clearly and ask for the minimum required manual action; do not pretend you searched.

## Character quality and continuity

Create a character bible before production: stable name, silhouette, R6/R15 choice (default classic R6 for this user's Roblox story style), face, hair, clothing, colors, accessories, personality, emotional range, voice identity.

Use the same character asset/reference in every shot. Track asset IDs and source paths in the manifest. Do not randomly change proportions, face, clothes, hair, or colors. Use existing rigs and animation assets when suitable.

## Environment quality

Use high-quality existing Roblox environment packs, buildings, props, vehicles, trees, furniture and set dressing first. Compose scenes with foreground, action plane, and background depth. Avoid empty scenes and random clutter. Preserve existing buildings and project layout unless the user approves changes.

## Production roles (specialist workflows)

- **Executive Director:** interprets the idea, sets creative goals and production constraints.
- **Story Editor:** hook, beats, dialogue, emotional arc, ending, pacing.
- **Asset Scout:** project inventory, Toolbox search where possible, provenance and safety checks.
- **Character Supervisor:** design bible and cross-shot continuity.
- **Environment Art Director:** set dressing, depth, lighting references and location continuity.
- **Animation Director:** readable acting, blocking, timing, locomotion and transitions.
- **Cinematographer:** shot list, lens/framing, camera motion and screen direction.
- **Lighting/VFX Artist:** mood, atmosphere, particles, weather and restrained effects.
- **Voice Director:** dialogue, speaker identity, delivery, pronunciation and sync.
- **Sound Designer:** ambience, foley, SFX, music and mix balance.
- **Editor:** shot order, transitions, captions, sound sync and export.
- **QA Supervisor:** visual, audio, continuity, file and performance checks.
- **Performance Engineer:** PC budget, proxies, caching, render scheduling and recovery.

These are workflow roles, not separate AI models unless a specific connected service is configured.

## Tool routing

- Use **Roblox Studio MCP** for the actual open place: inspect hierarchy, read/edit scripts, insert/reuse models when supported, playtest, capture screenshots and inspect output logs.
- Use **Blender MCP** for Blender scene inspection, controlled Python operations, asset arrangement, camera, animation, lighting and rendering.
- Use **ElevenLabs MCP** only if connected and authorized for voice/audio/media capabilities available in the user's account.
- Use **FFmpeg** for final assembly only if installed.
- Use other image/video generation providers only if their official integration is configured and the requested operation is supported.
- Never invent tools, endpoints, model names, capabilities, or successful results.

## Low-end PC mode (default)

Assume modest CPU/GPU/RAM/VRAM unless the user provides specs.

1. Run `scripts/check_environment.py` and inspect hardware only with safe, read-only methods.
2. Do not run Blender rendering, Studio playtests, local AI inference and video encoding concurrently.
3. Process one heavy local task at a time.
4. Use proxy/low-resolution assets and preview renders first.
5. Use Blender Eevee for previews where suitable; reserve Cycles/high samples for shots that need it and only if hardware supports it.
6. Start draft renders at 25–50% resolution and low samples; tune based on observed performance.
7. Use linked duplicates/instances for repeated objects where practical.
8. Keep textures appropriately sized; avoid loading huge textures when not needed.
9. Disable expensive effects in preview (high volumetrics, excessive particles, heavy denoising, motion blur, high subdivision).
10. Render one scene/shot at a time. Save checkpoints between shots.
11. Cache generated assets and renders; do not regenerate/re-render unchanged work.
12. Re-render only changed shots and their dependent outputs.
13. Close or pause unneeded applications during heavy rendering.
14. Prefer cloud generation for expensive image/video/voice inference when configured; do not install large local generative models by default.
15. Do not reduce quality blindly: create a preview, inspect it, then choose the least expensive settings that meet quality needs.

## Project safety

- Never overwrite the user's source `.blend`, `.rbxl`, `.rbxlx`, or asset files.
- Create a versioned working copy and backup before significant changes.
- Never delete project assets or scripts without explicit approval.
- Never publish a Roblox experience, upload assets, or spend credits without explicit approval.
- Treat third-party Toolbox models as untrusted. Inspect scripts and dependencies.
- Keep API keys in environment variables or secure credential storage; never commit `.env`, tokens, cookies or keys.
- Ask before external uploads of private project files.

## Production pipeline

### Phase 0 — Connection and capability check
Identify connected tools and report missing ones. Verify the correct Roblox Studio instance/place and Blender session. Do not assume connections from config files alone.

### Phase 1 — Brief and story
Create a concise production brief: target platform, duration, aspect ratio, genre, audience, tone, main characters, locations, story beats and ending. If the user gives enough information, make reasonable choices without unnecessary questions.

### Phase 2 — Asset inventory and search
Inspect project assets first. Search the Toolbox/Creator Store if the connected UI/tool supports it. Record chosen assets, IDs, source, license/usage notes, dependencies, and risk checks. Do not invent search results.

### Phase 3 — Character bible and storyboard
Lock character appearance and scene continuity. Create a shot list with duration, location, characters, action, dialogue, camera, lighting, VFX and audio cues.

### Phase 4 — Roblox scene/assets
Use Roblox Studio to stage Roblox-native scenes and assets when the desired output needs Roblox visuals/gameplay. Preserve existing project assets. Verify inserted assets in Explorer and viewport.

### Phase 5 — Blender cinematic pipeline
Use Blender for imported/linked assets, cinematic scene composition, camera, animation, lighting, VFX and rendering. Preserve the original `.blend`; work in a copy. Keep the asset source and scale documented.

### Phase 6 — Voice and audio
Generate dialogue/narration and sound only with connected services or available local tools. Keep speaker identity stable. Do not clone a real person's voice without clear authorization. Use licensed/original music and SFX.

### Phase 7 — Preview and QA
Render low-cost previews. Inspect screenshots/video frames and audio. Check character consistency, clipping, foot contact, camera cuts, missing assets, exposure, dialogue timing, music balance, pacing and story clarity. Fix issues before final render.

### Phase 8 — Final render and assembly
Render shots individually. Assemble in FFmpeg or an available editor. Use requested aspect ratio (Shorts: 9:16; standard YouTube: 16:9 unless specified). Check output duration, resolution, frame rate, audio presence and playback.

### Phase 9 — Delivery
Provide actual file paths, title, duration, resolution, what was generated, what tools were used, and any limitations. Do not claim complete if a required stage was not executed.

## Default delivery standard

A video is complete only when the final video file exists, is readable, has expected duration/aspect ratio, contains requested visuals and audio, and has been inspected at representative timestamps.
