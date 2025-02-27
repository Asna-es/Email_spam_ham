import tkinter as tk
from tkinter import messagebox
import pickle

# Load the trained model
with open("Naive_Bayes_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Load the CountVectorizer
with open("Vectorizer (2).pkl", "rb") as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)
def classify_email():
    email_text = email_input.get("1.0", tk.END).strip()
    
    if not email_text:
        messagebox.showerror("Error", "Please enter an email text")
        return

    # Transform input using CountVectorizer
    email_vector = vectorizer.transform([email_text])  

    # Predict spam or ham
    prediction = model.predict(email_vector)[0]
    result = "Spam" if prediction == 1 else "Ham"

    result_label.config(text=f"Classification: {result}", fg="red" if result == "Spam" else "green")

# Create Tkinter window
root = tk.Tk()
root.title("Email Spam Classifier")
root.geometry("400x300")

# Email Input
tk.Label(root, text="Enter Email Text:", font=("Arial", 12)).pack(pady=5)
email_input = tk.Text(root, height=6, width=40)
email_input.pack()

# Predict Button
predict_button = tk.Button(root, text="Classify", command=classify_email, font=("Arial", 12), bg="blue", fg="white")
predict_button.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=10)

# Run the GUI
root.mainloop()