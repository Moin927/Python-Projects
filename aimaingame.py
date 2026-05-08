import tkinter as tk
import random

# Mapping choices
youDict = {"Snake": 1, "Water": -1, "Gun": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

# Function to play the game
def play(user_choice):
    computer_choice = random.choice([-1, 0, 1])
    result = ""

    if computer_choice == youDict[user_choice]:
        result = "It's a draw!"
    elif (computer_choice == -1 and youDict[user_choice] == 1) or \
         (computer_choice == 1 and youDict[user_choice] == 0) or \
         (computer_choice == 0 and youDict[user_choice] == -1):
        result = "You win!"
    else:
        result = "You lose!"

    # Update GUI
    user_label.config(text=f"You chose: {user_choice}")
    comp_label.config(text=f"Computer chose: {reverseDict[computer_choice]}")
    result_label.config(text=result)

# Create GUI window
root = tk.Tk()
root.title("Snake Water Gun Game")
root.geometry("300x300")

# Labels
user_label = tk.Label(root, text="You chose: ", font=('Arial', 12))
user_label.pack(pady=10)

comp_label = tk.Label(root, text="Computer chose: ", font=('Arial', 12))
comp_label.pack(pady=10)

result_label = tk.Label(root, text="Result: ", font=('Arial', 14, 'bold'))
result_label.pack(pady=20)

# Buttons
tk.Button(root, text="Snake", command=lambda: play("Snake"), width=10).pack(pady=5)
tk.Button(root, text="Water", command=lambda: play("Water"), width=10).pack(pady=5)
tk.Button(root, text="Gun", command=lambda: play("Gun"), width=10).pack(pady=5)

# Run the app
root.mainloop()
