# -*- coding: utf-8 -*-

# @autor: Matheus Felipe
# @github: github.com/matheusfelipeog

# Builtin
import tkinter as tk

# Módulo próprio
from app.calculadora import Calculadora

DO_KEYBINDS = True

if __name__ == '__main__':
    master = tk.Tk()
    main = Calculadora(master)
    if DO_KEYBINDS: main._bind_keyboard()
    main.start()
