# Project2_gui.py
import tkinter as tk
from tkinter import messagebox
from Project2_logic import DataHandler, CandidateMenu

class VotingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Voting System")

        self.data_handler = DataHandler()

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="VOTE MENU")
        self.label.pack()

        self.vote_button = tk.Button(self.root, text="Vote", command=self.show_candidate_menu)
        self.vote_button.pack()

        self.exit_button = tk.Button(self.root, text="Exit", command=self.exit_program)
        self.exit_button.pack()

    def show_candidate_menu(self):
        candidate_menu = CandidateMenu(self.root, self.data_handler, self.update_label)

    def update_label(self, message):
        self.label.config(text=message)

    def exit_program(self):
        self.data_handler.save_votes()
        total_votes = self.data_handler.john_votes + self.data_handler.jane_votes
        message = f"Votes saved. John {self.data_handler.john_votes}, Jane {self.data_handler.jane_votes}, Total {total_votes}"
        messagebox.showinfo("Voting Results", message)
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = VotingApp(root)
    root.mainloop()
