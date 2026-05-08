import tkinter as tk
from tkinter import messagebox
import random

class GuessingGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🎯 Number Guessing Game")
        self.root.geometry("400x300")
        self.root.config(bg="#f0f8ff")

        self.reset_game()

        tk.Label(root, text="Guess a number between 1 and 100:", font=("Arial", 12), bg="#f0f8ff").pack(pady=10)

        self.entry = tk.Entry(root, font=("Arial", 14), justify='center')
        self.entry.pack(pady=5)

        self.feedback = tk.Label(root, text="", font=("Arial", 12), fg="blue", bg="#f0f8ff")
        self.feedback.pack(pady=5)

        self.attempts_label = tk.Label(root, text="Attempts: 0", font=("Arial", 12), bg="#f0f8ff")
        self.attempts_label.pack(pady=5)

        tk.Button(root, text="Submit Guess", command=self.check_guess, font=("Arial", 12), bg="#add8e6").pack(pady=10)
        tk.Button(root, text="Restart Game", command=self.reset_game, font=("Arial", 10), bg="#d3f9d8").pack(pady=5)

    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        if hasattr(self, 'feedback'):
            self.feedback.config(text="")
            self.attempts_label.config(text="Attempts: 0")
        if hasattr(self, 'entry'):
            self.entry.delete(0, tk.END)

    def check_guess(self):
        guess = self.entry.get()
        try:
            guess = int(guess)
        except ValueError:
            self.feedback.config(text="❌ Please enter a valid number.")
            return

        self.attempts += 1
        self.attempts_label.config(text=f"Attempts: {self.attempts}")

        if guess < self.secret_number:
            self.feedback.config(text="📈 Try a higher number.")
        elif guess > self.secret_number:
            self.feedback.config(text="📉 Try a lower number.")
        else:
            self.feedback.config(text=f"🎉 Correct! The number was {self.secret_number}.")
            messagebox.showinfo("Congratulations!", f"You guessed it in {self.attempts} attempts!")
            self.reset_game()

# Launch the game
root = tk.Tk()
game = GuessingGameGUI(root)
root.mainloop()
