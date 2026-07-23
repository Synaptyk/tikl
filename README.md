# TIKL

**Token-Informed Keyboard Layout** - open-source research into keyboard mapping using language-model tokenisation, language statistics, human motor models, and computational optimisation.

> TIKL is also a nod to “tickling the keys”.

## Primary research layout: TIKL-26 v1

Physical ANSI QWERTY positions produce:

```text
J B L D F Q U O Y K
 R N T S C I E A H
  W P M G V Z X
```

Space, punctuation, numbers, Shift, Control, Alt/Option, Command/Windows, Enter, Backspace, Tab, Escape, and navigation remain conventional.

The frozen research snapshot scored **0.893070 with QWERTY normalised to 1.0** under its implemented multi-population motor objective. That is a computed model result, not a predicted WPM gain or medical claim.

## What makes TIKL different?

TIKL treats LLM-token structure as evidence for recurring human-typed character paths. Tokens are never typed as macros: ordinary key actions still produce ordinary characters. The project combines character n-grams, word and morpheme paths, tokenizer-internal paths, token boundaries, keyboard geometry, and multiple typing styles.

The original ablation found that token information added a **small marginal refinement**, not a breakthrough. The character-only candidate already captured most of the gain. TIKL publishes that null-to-modest result rather than forcing the token hypothesis to appear stronger than it was.

## Install and test

See [INSTALL.md](INSTALL.md), then use the mapping for your platform:

- Windows: AutoHotkey v2
- macOS: Karabiner-Elements
- Linux: XKB or keyd

Start with the [learning guide](docs/LEARNING.md) and use the [six-week trial protocol](docs/TRIAL_PROTOCOL.md).

## Repository status

This repository begins with the frozen TIKL-26 v1 research snapshot, mappings, evidence tables, and learning materials. The exact one-off optimisation runtime that produced the snapshot is not present in the active workspace and is therefore **not represented as fully reproducible yet**. Reconstructing and independently validating the optimizer is the first major engineering milestone.

## Domains

- **tikl.my** - public project identity
- **tikl.dev** - technical and contributor portal

## License

Code, mappings, and documentation are licensed under [Apache License 2.0](LICENSE). Third-party datasets and tokenizer assets are not redistributed unless their terms expressly permit it.
