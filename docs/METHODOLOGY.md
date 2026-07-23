# Methodology snapshot

The initial layout was selected from a multi-start computational search over ANSI geometry. The model included character frequencies, same-key and same-finger sequences, row jumps, rolls, direction reversals, hand balance, static reach, finger effort, spaces, word/morpheme paths, token-internal paths, cross-token boundaries, and pre-token/merge-derived path-shape features.

Three population models were aggregated: conventional touch, index/middle-dominant self-taught, and mixed self-taught. The reported weights were 0.45, 0.35, and 0.20, with a worst-archetype regret term.

The primary scientific result was modest: under the common hybrid holdout objective, the full hybrid improved from 0.893715 for the character-only winner to 0.893070.

## Reproducibility status

The numerical snapshot and mapping survive, but the exact one-off optimizer implementation is not available in the active project workspace. This repository therefore publishes the result as a frozen research snapshot and does not yet claim end-to-end reproducibility. Reconstructing the optimizer and independently reproducing the scorecard is an explicit roadmap item.