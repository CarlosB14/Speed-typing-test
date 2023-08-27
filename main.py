import tkinter as tk
from utils import start_test, evaluate_test

window_configuration = tk.Tk()
window_configuration.title("Typing Test")
window_configuration.geometry("800x600")

label_test_phrase = tk.Label(window_configuration, text="Lets go!", font=("Verdana", 11))
label_test_phrase.pack(pady=10)

user_input_box = tk.Entry(window_configuration, font=("Verdana", 11))
user_input_box.pack(pady=10)

start_button = tk.Button(window_configuration, text="Start Test", command = lambda: start_test(label_test_phrase, user_input_box))
start_button.pack()

evaluate_button = tk.Button(window_configuration, text="Evaluate", command = lambda: evaluate_test(label_test_phrase, user_input_box, result_message_label))
evaluate_button.pack()

result_message_label = tk.Label(window_configuration, text="", font=("Verdana", 11))
result_message_label.pack(pady=10)


# Loop that runs the GUI until the user closes the window
window_configuration.mainloop()
