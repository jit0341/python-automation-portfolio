import tkinter as tk
import random

quotes = [
    "Believe you can and you're halfway there.",
    "Do something today that your future self will thank you for.",
    "Push yourself, because no one else is going to do it for you.",
    "The only way to do great work is to love what you do.",
    "Stay positive, work hard, make it happen."
]

def display_quote():
    selected_quote = random.choice(quotes)
    quote_label.config(text=selected_quote)

# Setup GUI window
window = tk.Tk()
window.title("Quote App")
window.geometry("400x200")
window.configure(bg="#f0f0f0")

# Title Label
title_label = tk.Label(window, text="🌟 Motivational Quote App", font=("Helvetica", 14, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

# Quote Display
quote_label = tk.Label(window, text="", wraplength=350, font=("Arial", 12), bg="#f0f0f0", fg="#333")
quote_label.pack(pady=20)

# Button to Show Quote
quote_button = tk.Button(window, text="Show Quote", command=display_quote, bg="#007ACC", fg="white", font=("Arial", 12, "bold"))
quote_button.pack()

# Run App
window.mainloop()