# Project2_logic.py
import csv
import tkinter as tk
from tkinter import messagebox

class DataHandler:
    def __init__(self):
        self.john_votes = 0
        self.jane_votes = 0

    def add_vote(self, candidate: str) -> None:
        if candidate.lower() == 'john':
            self.john_votes += 1
        elif candidate.lower() == 'jane':
            self.jane_votes += 1

    def save_votes(self) -> None:
        with open("votes.csv", "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Candidate", "Votes"])
            writer.writerow(["John", self.john_votes])
            writer.writerow(["Jane", self.jane_votes])

class CandidateMenu:
    def __init__(self, root, data_handler, update_label):
        self.root = root
        self.data_handler = data_handler
        self.update_label = update_label

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="CANDIDATE MENU")
        self.label.pack()

        self.john_button = tk.Button(self.root, text="John", command=lambda: self.vote('john'))
        self.john_button.pack()

        self.jane_button = tk.Button(self.root, text="Jane", command=lambda: self.vote('jane'))
        self.jane_button.pack()

    def vote(self, candidate):
        self.data_handler.add_vote(candidate)
        self.update_label(f"Vote for {candidate.capitalize()} recorded.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CandidateMenu(root, DataHandler(), lambda x: None)
    root.mainloop()
