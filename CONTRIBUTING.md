# Contributing to TIKL

TIKL welcomes improvements to corpus provenance, motor models, tokenizer analysis, optimisation, mappings, validation, documentation, and real-user trials.

## Principles

1. Separate computed findings from assumptions and human measurements.
2. Never present model-cost reductions as WPM or health improvements.
3. Keep source-separated train, validation, and holdout evaluation.
4. Do not redistribute datasets or model assets without explicit permission.
5. Preserve one-key/one-character behaviour in the primary alphabet layer.
6. Report null and negative results.

## Workflow

Open an issue before major methodological changes. Work on a branch, submit a pull request, and include validation evidence. Explain changes to corpus weights, motor priors, tokenizer families, or selection criteria. Never tune a candidate against the frozen holdout and then report it as untouched.