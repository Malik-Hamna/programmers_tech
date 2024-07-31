import tkinter as tk
from tkinter import messagebox
import random

class Quiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.root.geometry("500x400")

        self.show_welcome_screen()

    def show_welcome_screen(self):
        self.clear_screen()
        welcome_label = tk.Label(self.root, text="Welcome to the Quiz Game!", font=("Cursive", 18), bg="#765385", fg="white")
        welcome_label.pack(pady=50)

        start_button = tk.Button(self.root, text="Start Quiz", font=("Arial", 14), width=20, command=self.start_quiz)
        start_button.pack(pady=20)

        exit_button = tk.Button(self.root, text="Exit", font=("Arial", 14), width=20, command=self.root.destroy)
        exit_button.pack(pady=20)

    def start_quiz(self):
        self.clear_screen()
        self.setup_quiz_interface()
        self.next_question()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def setup_quiz_interface(self):
        L1 = tk.Label(self.root, text="Quiz app", font=("Cursive", 18), bg="#765385", fg="white")
        L1.place(x=180, y=10)

        self.questions = [
            {
                "question": "Which is the largest planet in the Solar System?",
                "options": ["Jupiter", "Mars", "Neptune", "Earth"],
                "answer": "Jupiter"
            },
            {
                "question": "What is necessary for life?",
                "options": ["Water", "Oxygen", "Whatsapp", "Girlfriend"],
                "answer": "Water"
            },
            {
                "question": "Which bird cannot fly?",
                "options": ["Hen", "Goose", "Duck", "Ostrich"],
                "answer": "Ostrich"
            },
            {
                "question": "What is the world's fastest bird?",
                "options": ["Duck", "Falcon", "Eagle", "Vulture"],
                "answer": "Falcon"
            },
            {
                "question": "How many dots appear on a pair of dice?",
                "options": ["24", "12", "42", "36"],
                "answer": "42"
            },
            {
                "question": "Who is the last prophet of Allah?",
                "options": ["Muhammad", "Esa", "Musa", "Ibrahim"],
                "answer": "Muhammad"
            },
            {
                "question": "How many hearts does an octopus have?",
                "options": ["3", "2", "1", "7"],
                "answer": "3"
            },
            {
                "question": "What planet is closest to the sun?",
                "options": ["Jupiter", "Mercury", "Mars", "Neptune"],
                "answer": "Mercury"
            }
        ]
        
        self.score = 0
        self.current_question = 0

        self.question_label = tk.Label(self.root, text="", font=("Arial", 14), wraplength=400)
        self.question_label.pack(pady=50)

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(self.root, text="", font=("Arial", 14), width=30, command=lambda i=i: self.check_answer(i))
            button.pack(pady=10)
            self.option_buttons.append(button)

        self.score_label = tk.Label(self.root, text="Score: 0", font=("Arial", 14))
        self.score_label.pack(pady=20)

    def next_question(self):
        self.reset_buttons()
        if self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            self.question_label.config(text=question["question"])
            options = question["options"]
            random.shuffle(options)
            for i in range(4):
                self.option_buttons[i].config(text=options[i])
            self.score_label.config(text="Score: {}".format(self.score))
        else:
            self.end_game()

    def reset_buttons(self):
        for button in self.option_buttons:
            button.config(bg="SystemButtonFace")

    def check_answer(self, selected_option):
        question = self.questions[self.current_question]
        selected_answer = self.option_buttons[selected_option].cget("text")
        correct_answer = question["answer"]

        if selected_answer == correct_answer:
            self.option_buttons[selected_option].config(bg="green")
            self.score += 1
        else:
            self.option_buttons[selected_option].config(bg="red")
            for i, option in enumerate(question["options"]):
                if option == correct_answer:
                    self.option_buttons[i].config(bg="green")

        self.score_label.config(text="Score: {}".format(self.score))
        self.current_question += 1
        self.root.after(1000, self.next_question)

    def end_game(self):
        messagebox.showinfo("Game Over", "Quiz has ended! \nYour Score: {}".format(self.score))
        self.root.destroy()


root = tk.Tk()
quiz_game = Quiz(root)
root.mainloop()
