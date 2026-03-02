print("Welcome to Rolling Dice")
import tkinter as tk
import random

root = tk.Tk()
root.title("Rolling Dice")
root.geometry("400x400")
root.configure(backround="#1e1e2f")

total_score = 0
rolling = False

dice_faces = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]

title_label = tk.Label(root, text="Dice Roller",
                       font=("Arial", 24, "bold"),
                       backround="#1e1e2f", foreground="white")
title_label.pack(pady=20)

dice_label = tk.Label(root, text="⚀",
                      font=("Arial", 120),
                      background="#1e1e2f", foreground="#00ffcc")
dice_label.pack(pady=10)

result_label = tk.Label(root, text="Press Roll!",
                        font=("Arial", 14),
                        background="#1e1e2f", foreground="white")
result_label.pack(pady=5)

total_label = tk.Label(root, text="Total: 0",
                       font=("Arial", 16, "bold"),
                       background="#1e1e2f", foreground="#ffcc00")
total_label.pack(pady=10)

def animate_roll(count=10):
    global total_score, rolling



