import tkinter as tk
from tkinter import messagebox
import random

# Class to manage Flashcards
class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flashcard Quiz App")
        self.flashcards = []  # List to store flashcards
        self.score = 0  # Initialize score
        self.question_index = 0  # Index to keep track of the current flashcard in the quiz
        
        self.create_widgets()
    
    def create_widgets(self):
        # Frame for flashcard creation
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        # Question and answer input
        self.question_label = tk.Label(self.frame, text="Question:")
        self.question_label.grid(row=0, column=0, padx=10, pady=5)
        self.answer_label = tk.Label(self.frame, text="Answer:")
        self.answer_label.grid(row=1, column=0, padx=10, pady=5)
        
        self.question_entry = tk.Entry(self.frame, width=50)
        self.question_entry.grid(row=0, column=1, padx=10, pady=5)
        self.answer_entry = tk.Entry(self.frame, width=50)
        self.answer_entry.grid(row=1, column=1, padx=10, pady=5)
        
        self.add_button = tk.Button(self.frame, text="Add Flashcard", command=self.add_flashcard)
        self.add_button.grid(row=2, columnspan=2, pady=10)

        # Frame for quiz functionality
        self.quiz_frame = tk.Frame(self.root)
        self.quiz_frame.pack(pady=10)

        # Question label for quiz
        self.quiz_question_label = tk.Label(self.quiz_frame, text="Question will appear here", font=("Helvetica", 14))
        self.quiz_question_label.pack(pady=10)
        
        self.quiz_answer_entry = tk.Entry(self.quiz_frame, width=50)
        self.quiz_answer_entry.pack(pady=5)
        
        self.check_answer_button = tk.Button(self.quiz_frame, text="Check Answer", command=self.check_answer)
        self.check_answer_button.pack(pady=5)

        self.score_label = tk.Label(self.quiz_frame, text="Score: 0", font=("Helvetica", 12))
        self.score_label.pack(pady=5)

        self.start_quiz_button = tk.Button(self.quiz_frame, text="Start Quiz", command=self.start_quiz)
        self.start_quiz_button.pack(pady=5)

    def add_flashcard(self):
        question = self.question_entry.get()
        answer = self.answer_entry.get()

        if question and answer:
            self.flashcards.append((question, answer))
            messagebox.showinfo("Success", "Flashcard added successfully!")
            self.question_entry.delete(0, tk.END)
            self.answer_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please provide both question and answer.")

    def start_quiz(self):
        if not self.flashcards:
            messagebox.showwarning("No Flashcards", "Please add some flashcards before starting the quiz.")
            return
        
        self.score = 0
        self.update_score()
        self.question_index = 0
        self.ask_question()

    def ask_question(self):
        if self.question_index < len(self.flashcards):
            self.quiz_question_label.config(text=self.flashcards[self.question_index][0])
        else:
            self.end_quiz()

    def check_answer(self):
        user_answer = self.quiz_answer_entry.get().strip()
        correct_answer = self.flashcards[self.question_index][1]

        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            messagebox.showinfo("Correct", "That's the correct answer!")
        else:
            messagebox.showinfo("Incorrect", f"Oops! The correct answer was: {correct_answer}")

        self.question_index += 1
        self.quiz_answer_entry.delete(0, tk.END())

        # Ask next question
        self.ask_question()
        self.update_score()

    def update_score(self):
        self.score_label.config(text=f"Score: {self.score}")

    def end_quiz(self):
        messagebox.showinfo("Quiz Over", f"You completed the quiz! Your final score is: {self.score}")
        self.start_quiz_button.config(state="normal")

# Main execution
if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()