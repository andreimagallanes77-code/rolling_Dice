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

title_label = tk.Label(root, txt="Dice Roller",
                       font=("Arial", 24, "bold"),
                       bg="#1e1e2f", fg="white")
title_label.pack(pady=20)

dice_label = tk.Label(root, text="⚀",
                      font=("Arial", 120)