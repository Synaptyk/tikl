# TIKL-26 v1 research report

## Winning layout

```text
J B L D F Q U O Y K
 R N T S C I E A H
  W P M G V Z X
```

TIKL-26 is a complete 26-letter permutation for an ordinary ANSI keyboard. It requires no mandatory chord, macro, prediction, or timing-sensitive action for ordinary letters.

## Holdout result

The frozen robust motor cost was **0.893070 with QWERTY = 1.0**, or 10.69% lower in the implemented objective. This is not a predicted typing-speed or health improvement.

| Layout | Robust cost | Reduction | Moved | Worst archetype |
|---|---:|---:|---:|---|
| QWERTY | 1.000000 | 0.00% | 0 | conventional touch |
| Dvorak | 0.907135 | 9.29% | 24 | index/middle dominant |
| Colemak | 0.923797 | 7.62% | 16 | index/middle dominant |
| Colemak-DH | 0.928128 | 7.19% | 21 | index/middle dominant |
| TIKL-Char | 0.893715 | 10.63% | 23 | mixed self-taught |
| TIKL-Token | 0.892528 | 10.75% | 25 | mixed self-taught |
| TIKL-Bridge | 0.904094 | 9.59% | 13 | mixed self-taught |
| TIKL-26 | 0.893070 | 10.69% | 25 | index/middle dominant |

## Movement diagnostics

For conventional touch typing, TIKL-26 produced 62.88% home-row letter use, 1.72% same-finger different-key bigrams, 0.25% same-finger trigrams, 3.00% two-row jumps, 43.85% hand alternation, 72.90% index/middle workload, 17.22% ring workload, and 9.88% pinky workload.

The index/middle-dominant model put 86.79% of letter work on index/middle fingers, with 3.68% pinky load. The mixed model produced 77.25% index/middle and 6.54% pinky load.

## Token contribution

Token, pre-token, and merge information produced a modest marginal gain, not a breakthrough. The common-objective difference between the character-only winner and TIKL-26 was 0.000645, or 0.065 QWERTY-normalised percentage points. A boundary-only hybrid slightly edged the full hybrid on holdout, so pre-token and merge-derived features did not show a reliable additional gain.

## Design space

Design A, the universal remap, is the recommended first trial. A thumb-enhanced Design B scored better under central motor assumptions but required timing-sensitive Alt/Option tap-hold behaviour and introduced compatibility risk.

## Limitations

The candidate requires longitudinal human testing. Corpus provenance is imperfect; finger parameters are priors; whole-hand motion, Shift, Backspace, fatigue, and learning are simplified; and the surviving active workspace does not include the exact original optimizer implementation.