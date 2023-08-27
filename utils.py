import random
import timeit
import tkinter as tk

test_phrases = [
    "The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog.",
    "Programming is both an art and a science. It requires creativity and logic.",
    "In a world full of technology, adaptability is the key to success.",
    "Learning new skills is a lifelong journey. It's never too late to start.",
    "Python is a versatile and powerful programming language used in various fields.",
    "Efficiency and accuracy are crucial in software development.",
    "Coding is like solving puzzles. It's both challenging and rewarding.",
    "Practice makes perfect. Keep coding and improving your skills.",
    "The internet is a vast resource of knowledge and information.",
    "Success in coding requires dedication, patience, and a love for learning."
    "Many people say that life isn't like a bed of roses. I beg to differ. I think that life is quite like a bed of roses. Just like life, a bed of roses looks pretty on the outside, but when you're in it, you find that it is nothing but thorns and pain. I myself have been pricked quite badly."
]


def start_test(phrase_label, user_input):
    phrase = random.choice(test_phrases)
    phrase_label.config(text=phrase)
    user_input.delete(0, tk.END)
    global start_time
    start_time = timeit.default_timer()


def evaluate_test(phrase_label, user_input, result_label):
    end_time = timeit.default_timer()
    total_time = end_time - start_time
    phrase = phrase_label.cget("text")
    user_entry = user_input.get()
    
    if phrase == user_entry:
        result_label.config(text=f"Correct! Time: {total_time:.2f} seconds\n It is {beats_per_minute(total_time, phrase):.2f} BPM")
    else:
        result_label.config(text=f"Incorrect. Try again.")

def beats_per_minute(total_time, phrase):
    return len(phrase) / (total_time / 60)