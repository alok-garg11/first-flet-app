import flet as ft

# Define a question object
class Question:
  def __init__(self, text, choices, answer):
    self.text = text
    self.choices = choices
    self.answer = answer

# Define some example questions
questions = [
  Question("What is the capital of France?", ["London", "Paris", "Berlin"], 1),
  Question("What is the largest planet in our solar system?", ["Jupiter", "Mars", "Earth"], 0),
]

# Track current question and score
current_question = 0
score = 0

def show_question(page: ft.Page):
  global current_question

  # Clear previous content
  page.clean()
  # Display question text
  page.add(ft.Text(questions[current_question].text))

  # Create radio buttons for choices
  radio_buttons = []
  for i, choice in enumerate(questions[current_question].choices):
    radio_buttons.append(ft.RadioGroup(content=ft.Column([
        ft.Radio(value=str(i),
                 label=choice)]),
      on_change=lambda e: check_answer(page, e.control.value)))
  page.add(ft.Row(controls=radio_buttons))

def check_answer(page: ft.Page, choice):
  global current_question, score

  # Check if selected answer matches correct answer
  if int(choice) == questions[current_question].answer:
    score += 1
    page.add(ft.Text("Correct!"))
  else:
    page.add(ft.Text(f"Incorrect. The answer is {questions[current_question].choices[questions[current_question].answer]}"))

  # Check if it's the last question
  if current_question == len(questions) - 1:
    page.add(ft.Text(f"You scored {score} out of {len(questions)}"))
  else:
    current_question += 1
    show_question(page)

  # Update the page
  page.update()

def main(page: ft.Page):
  show_question(page)

ft.app(target=main)
