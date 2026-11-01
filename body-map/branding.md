# Body map — palette in use

How the interactive map applies the Corpus Nova palette (`notes/branding/STYLE.md`).

| Element | Token | Hex |
|---|---|---|
| Active / hovered region (stroke + label) | `signal` | `#2F6F6A` |
| Active region soft fill, Map panel background | `signal-soft` | `#DCEEEB` |
| Inactive region outlines, rules, panel borders | `line` | `#E5E2DC` |
| Secondary labels, captions, units | `mute` | `#6B7280` |
| Primary text | `ink` | `#0B0F14` |
| Background (light) | `paper` | `#F7F5F2` |

- Only one thing is signal-coloured at a time: the region under the cursor (or pinned).
- Chrome = 1 px hairlines in `line`, labels in `mute`; no shadows, gradients, or 3D bevels.
- Dark mode: background `ink`, text `paper`; `signal` stays unchanged.
- `alert #8B3A3A` only for rare warnings (e.g. pressure out of range), never decoration.
- Mark/wordmark: `figures/branding/cn-mark.png` in the corner; `cn-mark-pulse.gif` for loading only.
- License: MIT for Corpus Nova payloads; third-party atlas meshes keep their own licenses.
