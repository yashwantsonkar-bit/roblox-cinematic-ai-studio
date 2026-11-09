# Low-end PC performance plan

## Default profile

- One heavy local task at a time.
- Preview resolution: 50% (drop to 25% if needed).
- Preview samples: 8–16 for Cycles drafts; use Eevee when appropriate.
- Final render settings are chosen per scene after preview.
- Scene-by-scene processing.
- Cache enabled; re-render only changed shots.
- Avoid local generative AI models by default.
- Keep Roblox Studio and Blender open only when needed.

## Practical rules

1. Do not import every asset in the library into one scene. Select only what the shot needs.
2. Prefer optimized meshes and sensible texture sizes.
3. Use instances/linked duplicates for repeated props.
4. Hide/offload out-of-shot assets where safe.
5. Avoid unnecessary subdivision, volumetrics, high-resolution shadows and excessive particles during previews.
6. Keep a working `.blend` copy and save checkpoints.
7. Render an image/short preview before a full sequence.
8. Encode final clips after render, not concurrently with heavy Blender rendering.
9. Monitor free disk space before rendering; image sequences can consume substantial storage.
10. If memory pressure occurs, close Studio or Blender between pipeline stages rather than forcing concurrent work.

These are starting values, not a guarantee that every scene will run smoothly. Large scenes can still exceed low-end hardware.
