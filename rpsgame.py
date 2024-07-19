import tkinter as tk
import random

def winner(user_i, comp_i):
    if user_i == comp_i:
        return "Tie!", 0, 0
    elif (user_i == 'Rock' and comp_i == 'Scissors') or \
         (user_i == 'Scissors' and comp_i == 'Paper') or \
         (user_i == 'Paper' and comp_i == 'Rock'):
        return "You win!", 1, 0
    else:
        return "Computer wins!", 0, 1

def play(user_i):
    global user_score, computer_score
    comp_i = random.choice(['Rock', 'Paper', 'Scissors'])
    result, user_point, computer_point = winner(user_i, comp_i)
    user_score += user_point
    computer_score += computer_point
    result_label.config(text=f"Computer chose: {comp_i}\n{result}")
    score_label.config(text=f"Score - You: {user_score}  Computer: {computer_score}")

def on_choice(user_i):
    play(user_i)
    play_again_button.pack(pady=10)

def reset():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="")
    score_label.config(text=f"Score - You: {user_score}  Computer: {computer_score}")
    play_again_button.pack_forget()

user_score = 0
computer_score = 0

root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.configure(background='#00cedc') 

label = tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=('Century Gothic', 22), bg='#00cedc')
label.pack(pady=10)

rock_button = tk.Button(root, text="Rock", width=10, command=lambda: on_choice('Rock'), bg='#000000', fg='white')
rock_button.pack(pady=5)

paper_button = tk.Button(root, text="Paper", width=10, command=lambda: on_choice('Paper'), bg='#000000', fg='white')
paper_button.pack(pady=5)

scissors_button = tk.Button(root, text="Scissors", width=10, command=lambda: on_choice('Scissors'), bg='#000000', fg='white')
scissors_button.pack(pady=5)

result_label = tk.Label(root, text="", font=('Century Gothic', 18), bg='#00cedc')  
result_label.pack(pady=20)

score_label = tk.Label(root, text=f"Score - You: {user_score}  Computer: {computer_score}", font=('Century Gothic', 18), bg='#00cedc')
score_label.pack(pady=10)

play_again_button = tk.Button(root, text="Play Again", width=10, command=reset, bg='#000000', fg='white')

root.mainloop()
