#Requires AutoHotkey v2.0
#SingleInstance Force
; TIKL-26 v1. Text remaps are disabled while Ctrl, Alt, or Win is held.
#HotIf !(GetKeyState("Ctrl", "P") || GetKeyState("Alt", "P") || GetKeyState("LWin", "P") || GetKeyState("RWin", "P"))
SC010::j
SC011::b
SC012::l
SC013::d
SC014::f
SC015::q
SC016::u
SC017::o
SC018::y
SC019::k
SC01E::r
SC01F::n
SC020::t
SC021::s
SC022::c
SC023::i
SC024::e
SC025::a
SC026::h
SC02C::w
SC02D::p
SC02E::m
SC02F::g
SC030::v
SC031::z
SC032::x
#HotIf
