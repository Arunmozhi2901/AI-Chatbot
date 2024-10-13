import tkinter as tk
from tkinter import scrolledtext, messagebox
import random

class Chatbot:
    def __init__(self, master):
        self.master = master
        self.master.title("Chatbot")
        self.master.geometry("450x550")
        self.master.configure(bg="#34495E")

        # Chat area
        self.chat_area = scrolledtext.ScrolledText(master, state='disabled', wrap='word', height=20, width=50, bg="#ECF0F1", fg="#34495E", font=("Helvetica", 12))
        self.chat_area.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # User input area
        self.user_input = tk.Entry(master, width=35, font=("Helvetica", 12), bg="#FFFFFF", fg="#34495E")
        self.user_input.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        self.user_input.bind("<Return>", self.send_message)

        # Send button
        self.send_button = tk.Button(master, text="Send", command=self.send_message, bg="#3498DB", fg="white", font=("Helvetica", 12, "bold"), activebackground="#2980B9")
        self.send_button.grid(row=1, column=1, padx=10, pady=10)

        # Clear button
        self.clear_button = tk.Button(master, text="Clear", command=self.clear_chat, bg="#E74C3C", fg="white", font=("Helvetica", 12, "bold"), activebackground="#C0392B")
        self.clear_button.grid(row=2, column=0, padx=10, pady=10, sticky='w')

        # Predefined questions dropdown
        self.question_var = tk.StringVar(master)
        self.question_var.set("Select a question")
        self.questions_menu = tk.OptionMenu(master, self.question_var, "How are you?", "What's your name?", "Tell me a joke", "Help me", command=self.predefined_question)
        self.questions_menu.grid(row=2, column=1, padx=10, pady=10, sticky='e')

        # Configure grid
        master.grid_rowconfigure(0, weight=1)
        master.grid_columnconfigure(0, weight=1)

        # Initial message
        self.display_message("Bot: Hello! How can I assist you today? 😊")

    def send_message(self, event=None):
        user_text = self.user_input.get()
        if user_text:
            self.display_message(f"You: {user_text}")
            self.user_input.delete(0, tk.END)
            response = self.get_response(user_text)
            self.display_message(f"Bot: {response} 😊")

    def predefined_question(self, question):
        response = self.get_response(question)
        self.display_message(f"Bot: {response} 😊")

    def display_message(self, message):
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, message + "\n")
        self.chat_area.config(state='disabled')
        self.chat_area.see(tk.END)

    def clear_chat(self):
        self.chat_area.config(state='normal')
        self.chat_area.delete(1.0, tk.END)
        self.chat_area.config(state='disabled')

    def get_response(self, user_input):
        user_input = user_input.lower()
        if "hello" in user_input or "hi" in user_input:
            return "Hello! How can I assist you today?"
        elif "how are you" in user_input:
            return random.choice(["I'm just a computer program, but I'm here to help you!", "Feeling great! Thanks for asking!"])
        elif "what is your name" in user_input or "what's your name" in user_input:
            return "I'm a simple chatbot created to assist you."
        elif "help" in user_input:
            return "Sure! You can ask me about general information or say 'exit' to close the chat."
        elif "joke" in user_input:
            return random.choice(["Why did the scarecrow win an award? Because he was outstanding in his field!", 
                                  "Why don't scientists trust atoms? Because they make up everything!"])
        elif "exit" in user_input:
            self.master.quit()
            return "Goodbye! Have a great day!"
        else:
            return "I'm sorry, I don't understand that."

if __name__ == "__main__":
    root = tk.Tk()
    chatbot = Chatbot(root)
    root.mainloop()
