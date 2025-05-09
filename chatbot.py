import tkinter as tk
from tkinter import scrolledtext
import random

class RuleBasedChatbot:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot 🤖")
        self.root.geometry("500x600")
        self.root.resizable(False, False)
        
        # Configure colors
        self.bg_color = "#f0f8ff"
        self.text_color = "#333333"
        self.bot_color = "#4169e1"
        self.user_color = "#2e8b57"
        
        # Create chat display
        self.chat_display = scrolledtext.ScrolledText(
            root, wrap=tk.WORD, width=55, height=25,
            font=("Arial", 11), bg="white", fg=self.text_color
        )
        self.chat_display.pack(pady=10, padx=10)
        self.chat_display.config(state=tk.DISABLED)
        
        # Create input frame
        input_frame = tk.Frame(root, bg=self.bg_color)
        input_frame.pack(pady=10)
        
        self.user_input = tk.Entry(
            input_frame, width=45, font=("Arial", 11),
            bg="white", relief=tk.GROOVE
        )
        self.user_input.pack(side=tk.LEFT, padx=5)
        self.user_input.bind("<Return>", self.send_message)
        
        send_btn = tk.Button(
            input_frame, text="Send", command=self.send_message,
            bg=self.bot_color, fg="white", font=("Arial", 11), relief=tk.GROOVE
        )
        send_btn.pack(side=tk.LEFT)
        
        # Initialize responses
        self.init_responses()
        
        # Welcome message
        self.display_message("Bot", "Hello! I'm a rule-based chatbot. Ask me about Python, say hello, or ask for a joke!")
    
    def init_responses(self):
        """Initialize all response patterns"""
        self.responses = {
            "greetings": {
                "patterns": ["hi", "hello", "hey", "greetings"],
                "responses": [
                    "Hello there! How can I help you?",
                    "Hi! What would you like to know?",
                    "Greetings! Ready to chat?"
                ]
            },
            "farewells": {
                "patterns": ["bye", "goodbye", "exit", "quit"],
                "responses": [
                    "Goodbye! Come back if you have more questions.",
                    "See you later!",
                    "Bye! It was nice chatting with you."
                ]
            },
            "python": {
                "patterns": ["what is python", "tell me about python", "python"],
                "responses": [
                    "Python is a high-level, interpreted programming language known for its simplicity and readability.",
                    "Python is great for beginners and experts alike! It's used for web dev, data science, AI, and more."
                ]
            },
            "jokes": {
                "patterns": ["joke", "make me laugh", "funny"],
                "responses": [
                    "Why don't scientists trust atoms? Because they make up everything!",
                    "How do you tell HTML from HTML5? Try it out in Internet Explorer. Did it work? No? It's HTML5."
                ]
            },
            "facts": {
                "patterns": ["fact", "interesting", "tell me something"],
                "responses": [
                    "Did you know Python was named after Monty Python, not the snake?",
                    "Fun fact: Python uses indentation for code blocks instead of curly braces!"
                ]
            }
        }
    
    def display_message(self, sender, message):
        """Display messages in the chat window"""
        self.chat_display.config(state=tk.NORMAL)
        
        # Configure tags for different senders
        if sender == "Bot":
            tag = "bot"
            color = self.bot_color
        else:
            tag = "user"
            color = self.user_color
        
        self.chat_display.tag_config(tag, foreground=color)
        
        self.chat_display.insert(tk.END, f"{sender}: {message}\n\n", tag)
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.see(tk.END)
    
    def send_message(self, event=None):
        """Process user input and generate response"""
        user_text = self.user_input.get().strip()
        if user_text:
            self.display_message("You", user_text)
            self.user_input.delete(0, tk.END)
            self.generate_response(user_text.lower())
    
    def generate_response(self, user_input):
        """Generate appropriate response based on rules"""
        response = None
        
        # Check all response categories
        for category in self.responses.values():
            for pattern in category["patterns"]:
                if pattern in user_input:
                    response = random.choice(category["responses"])
                    break
            if response:
                break
        
        # Default response if no match
        if not response:
            response = "I'm not sure I understand. Could you rephrase that?"
        
        self.display_message("Bot", response)

if __name__ == "__main__":
    root = tk.Tk()
    chatbot = RuleBasedChatbot(root)
    root.mainloop()
