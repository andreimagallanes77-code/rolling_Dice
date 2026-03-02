print("          Welcome to Rolling Dice          ")
import tkinter as tk
import random

root = tk.Tk()
root.title("Rolling Dice")
root.geometry("400x400")
root.configure(background="#1e1e2f")
total_score = 0
rolling = False

dice_faces = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]

title_label = tk.Label(root, text="Dice Roller",
                       font=("Arial", 24, "bold"),
                       background="#1e1e2f", foreground="white")
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

    if count > 0:
        random_face = random.choice(dice_faces)
        dice_label.config(text=random_face)
        root.after(100, animate_roll, count - 1)
    else:
        roll = random.randint(1, 6)
        dice_label.config(text=dice_faces[roll - 1])
        result_label.config(text=f"You rolled: {roll}")
        total_score += roll
        total_label.config(text=f"Total: {total_score}")
        rolling = False

def roll_dice():
    global rolling
    if not rolling:
        rolling = True
        animate_roll()

def reset_game():
    global total_score
    total_score = 0
    total_label.config(text="Total: 0")
    result_label.config(text="Press Roll!")
    dice_label.config(text="⚀")

roll_button = tk.Button(root, text="🎲 Roll",
                        font=("Arial", 14, "bold"),
                        background="#00ffcc", foreground="black",
                        width=10, command=roll_dice)
roll_button.pack(pady=10)

reset_button = tk.Button(root, text="Reset",
                         font=("Arial", 12),
                         background="#ff4444", foreground="white",
                         width=10, command=reset_game)
reset_button.pack(pady=5)

root.mainloop()