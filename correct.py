from tkinter import *
from textblob import TextBlob

# Create the main window
root = Tk()
root.title("Spell Checker - AI NLP Project")
root.geometry("500x250")
root.config(bg="lightpink")

# Variables
text_input = StringVar()
result = StringVar()

# Function to correct spelling
def checkSpelling():
    word = text_input.get()
    if word.strip() == "":
        result.set("Please enter a word.")
        return
    blob = TextBlob(word)
    corrected = blob.correct()
    result.set(f"The corrected word is: {corrected}")

# Title Label
Label(root, text="Spell Checker Tool", font=("Helvetica", 20, "bold"), bg="lightblue", fg="navy").pack(pady=10)

# Input Prompt
Label(root, text="Enter a word:", font=("Helvetica", 14), bg="lightblue").pack()

# Input Entry
Entry(root, textvariable=text_input, font=("Helvetica", 14), width=40).pack(pady=5)

# Result Display
Label(root, textvariable=result, font=("Helvetica", 14, "italic"), bg="lightblue", fg="darkgreen").pack(pady=10)

# Button to check spelling
Button(root, text="Check Spelling", command=checkSpelling,
       font=("Helvetica", 14), bg="gray", fg="white", padx=10, pady=5).pack()

# Exit button
Button(root, text="Exit", command=root.destroy,
       font=("Helvetica", 10), bg="red", fg="white", padx=8).pack(pady=10)

# Start GUI loop
root.mainloop()
