import tkinter as tk
from tkinter import messagebox


class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz App")

        self.questions = [
            {
                'question': "What is the capital of France?",
                'options': ["Paris", "London", "Berlin", "Madrid"],
                'correct_answer': "Paris"
            },
            {
                'question': "Who wrote 'Hamlet'?",
                'options': ["Shakespeare", "Dickens", "Hemingway", "Twain"],
                'correct_answer': "Shakespeare"
            },
            {
                'question': "What is the powerhouse of the cell?",
                'options': ["Mitochondrion", "Nucleus", "Ribosome", "Endoplasmic reticulum"],
                'correct_answer': "Mitochondrion"
            }
        ]

        self.current_question_idx = 0
        self.score = 0

        self.question_label = tk.Label(master, text="")
        self.question_label.pack(pady=10)

        self.radio_var = tk.IntVar()
        self.radio_buttons = []
        for idx in range(4):
            radio_button = tk.Radiobutton(master, text="", variable=self.radio_var, value=idx)
            self.radio_buttons.append(radio_button)
            radio_button.pack(anchor=tk.W)

        self.next_button = tk.Button(master, text="Next", command=self.next_question)
        self.next_button.pack(pady=10)

        self.show_question()

    def show_question(self):
        question = self.questions[self.current_question_idx]
        self.question_label.config(text=question['question'])
        for idx, option in enumerate(question['options']):
            self.radio_buttons[idx].config(text=option)
        self.radio_var.set(-1)

    def next_question(self):
        selected_index = self.radio_var.get()
        if selected_index == -1:
            messagebox.showwarning("Warning", "Please select an answer.")
            return

        question = self.questions[self.current_question_idx]
        correct_answer = question['correct_answer']
        selected_answer = question['options'][selected_index]

        if selected_answer == correct_answer:
            self.score += 1

        self.current_question_idx += 1

        if self.current_question_idx < len(self.questions):
            self.show_question()
        else:
            messagebox.showinfo("Quiz Complete", f"Quiz complete! You scored {self.score}/{len(self.questions)}")
            self.master.destroy()


# Create the main window
root = tk.Tk()
app = QuizApp(root)
root.mainloop()
