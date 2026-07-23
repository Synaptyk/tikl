# Install TIKL-26 v1

```text
Physical: Q W E R T Y U I O P
Output:   J B L D F Q U O Y K

Physical:  A S D F G H J K L
Output:    R N T S C I E A H

Physical:   Z X C V B N M
Output:     W P M G V Z X
```

Space, punctuation, numbers, Enter, Backspace, Tab, Escape, Shift, Control, Alt/Option, Command/Windows, and navigation stay conventional.

## Windows

Install AutoHotkey v2 and run `mappings/windows/tikl26-physical-shortcuts.ahk`. The recommended profile disables text remapping while Ctrl, Alt, or Win is held, preserving familiar physical QWERTY shortcut locations.

## macOS

Copy `mappings/macos/tikl26-physical-shortcuts.json` into Karabiner-Elements’ complex-modifications assets directory, then enable the rule.

## Linux

Copy `mappings/linux/tikl26` to your XKB symbols directory and select `tikl26(basic)`, or adapt the supplied keyd configuration. Plain XKB makes shortcuts follow produced keysyms.

## Recovery

Keep an on-screen keyboard or second input device available during first installation. Do not enable the layout at login, disk-encryption, firmware, or recovery screens until verified.