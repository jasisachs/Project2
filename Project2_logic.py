import csv
import tkinter as tk
from tkinter import messagebox

class DataHandler:
    """Class to handle voting data."""

    def __init__(self) -> None:
        """Initialize vote counts."""
        self.john_votes: int = 0
        self.jane_votes: int = 0

    def add_vote(self, candidate: str) -> None:
        """Add a vote for the specified candidate."""
        if candidate.lower() == 'john':
            self.john_votes += 1
        elif candidate.lower() == 'jane':
            self.jane_votes += 1

    def save_votes(self) -> None:
        """Save vote counts to a CSV file."""
        with open("votes.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Candidate", "Votes"])
            writer.writerow(["John", self.john_votes])
            writer.writerow(["Jane", self.jane_votes])

class CandidateMenu:
    """Class to display the candidate voting menu."""

    def __init__(self, root: tk.Tk, data_handler: DataHandler, update_label: callable) -> None:
        """Initialize the candidate menu."""
        self.root = root
        self.data_handler = data_handler
        self.update_label = update_label

        self.create_widgets()

    def create_widgets(self) -> None:
        """Create GUI widgets for candidate menu."""
        self.label = tk.Label(self.root, text="CANDIDATE MENU")
        self.label.pack()

        self.john_button = tk.Button(self.root, text="John", command=lambda: self.vote('john'))
        self.john_button.pack()

        self.jane_button = tk.Button(self.root, text="Jane", command=lambda: self.vote('jane'))
        self.jane_button.pack()

    def vote(self, candidate: str) -> None:
        """Record a vote for the selected candidate."""
        self.data_handler.add_vote(candidate)
        self.update_label(f"Vote for {candidate.capitalize()} recorded.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CandidateMenu(root, DataHandler(), lambda x: None)
    root.mainloop()
