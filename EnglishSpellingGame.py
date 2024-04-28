import tkinter as tk
from tkinter import ttk, messagebox
import azure.cognitiveservices.speech as speechsdk
from PIL import Image, ImageTk

class EnglishSpellingGame(tk.Frame):  # Modify this line
    def __init__(self,parent):
        super().__init__(parent)
        
        # Create GUI elements for spelling bee game
        self.word_label = ttk.Label(self, text="", font=("Comic Sans MS", 18))
        self.word_label.pack(pady=20)
        
        self.image_label = ttk.Label(self)
        self.image_label.pack(pady=10)
        
        self.entry = ttk.Entry(self, font=("Comic Sans MS", 14))  # Increase font size
        self.entry.pack(pady=10)
        
        self.check_button = ttk.Button(self, text="Check Spelling",width = 30, command=self.check_spelling)
        self.check_button.pack(pady=10)
        
        self.feedback_label = ttk.Label(self, text="", font=("Comic Sans MS", 12))
        self.feedback_label.pack(pady=10)
        
        self.score_label = ttk.Label(self, text=f"Score: 0/10", font=("Comic Sans MS", 12))
        self.score_label.pack(pady=5)
        
        self.timer_label = ttk.Label(self, text="Time Left: 60", font=("Comic Sans MS", 12))
        self.timer_label.pack(pady=5)
        
        self.restart_button = ttk.Button(self, text="Restart",width = 30, command=self.restart_game)
        self.restart_button.pack(pady=10)
        
        # Initialize word database
        self.words = ["book", "apple", "banana", "computer", "elephant", "guitar", "keyboard", "pencil", "orange", "table"]
        self.images = {
            "book": "book.jpg",
            "apple": "apple.png",
            "banana": "banana.png",
            "computer": "computer.jpg",
            "elephant": "elephant.png",
            "guitar": "guitar.png",
            "keyboard": "keyboard.jpg",
            "pencil": "pencil.png",
            "orange": "orange.png",
            "table": "table.png"
        }
        
        # Azure Cognitive Services Text-to-Speech configuration
        self.speech_key = "51ea1f1487cb413eb0ed452817ed6ef7"
        self.speech_region = "japaneast"
        
        # Game parameters
        self.score = 0
        self.total_words = 10
        self.remaining_time = 60  # reduced time for testing
        
        # Start the spelling bee game
        #self.generate_word()
        #self.update_timer()
        
        self.game_ongoing = False
        self.original_time = 60
        
        # Button to end the game and go back to the previous page
        self.end_game_button = ttk.Button(self, text="End Game", width = 30, command=self.end_game_and_go_back)
        self.end_game_button.pack(pady=10)
        
        # Rest of the code remains the same
    
    def end_game_and_go_back(self):
        
        self.entry.delete(0, tk.END)
        
        # Display a message box confirming the end of the game
        if messagebox.askyesno("End Game", "Are you sure you want to end the game?"):
            # Stop the timer
            self.game_ongoing = False
            
            # Go back to the previous page
            self.pack_forget()  # Hide the spelling game widget
            self.master.pack_forget()  # Hide the current frame (assuming it's a page frame)
    
    
    def generate_word(self):
        # Check if there are remaining words to display
        if len(self.words) > 0:
            # Select the next word from the list
            self.current_word = self.words.pop(0)
            
            # Display the word for the student to spell
            # self.word_label.config(text=f"Spell the word: {self.current_word}")
            
            # Display the image for the current word
            image_path = self.images.get(self.current_word, "default_image.png")
            image = Image.open(image_path)
            image = image.resize((150, 150), Image.NEAREST)  # Resize the image
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo  # Keep a reference to prevent garbage collection
            
            # Speak the word using Azure TTS
            self.text_to_speech(f"Spell the word: {self.current_word}")
        else:
            # If all words have been displayed, end the game
            self.game_over()

    def text_to_speech(self, text):
        # Configure Azure Cognitive Services Text-to-Speech
        speech_config = speechsdk.SpeechConfig(subscription=self.speech_key, region=self.speech_region)
        synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

        # Synthesize and play the text
        synthesizer.speak_text_async(text)

    def check_spelling(self):
        # Get the student's input from the entry field
        student_input = self.entry.get().strip().lower()

        # Check if student's input matches the current word
        if student_input == self.current_word:
            feedback = "Correct! Well done!"
            self.score += 1
        else:
            feedback = f"Incorrect. The correct spelling is '{self.current_word}'."

        # Update score label
        self.score_label.config(text=f"Score: {self.score}/{self.total_words}")

        # Display feedback
        self.feedback_label.config(text=feedback)
        
        # Reset the entry field for the next word
        self.entry.delete(0, tk.END)
        self.generate_word()

    def update_timer(self):
        if self.remaining_time > 0:
            self.remaining_time -= 1
            self.timer_label.config(text=f"Time Left: {self.remaining_time}")
            self.after(1000, self.update_timer)
        else:
            self.game_over()

    def game_over(self):
        self.entry.config(state="disabled")
        self.check_button.config(state="disabled")
        self.feedback_label.config(text=f"Game Over! Final score: {self.score}/{self.total_words}")
        messagebox.showinfo("Game Over", f"Time's up! Final score: {self.score}/{self.total_words}")

    def restart_game(self):
    # Reset game parameters
        self.score = 0
        self.remaining_time = 60
        self.words = ["book", "apple", "banana", "computer", "elephant", "guitar", "keyboard", "pencil", "orange", "table"]
        self.feedback_label.config(text="")
        self.entry.config(state="normal")
        self.check_button.config(state="normal")
        self.score_label.config(text="Score: 0/10")
        self.timer_label.config(text="Time Left: 60")
        # Start the game again
        self.generate_word()
        self.update_timer()
        
    def update_timer(self):
        if self.game_ongoing and self.remaining_time > 0:
            self.remaining_time -= 1
            self.timer_label.config(text=f"Time Left: {self.remaining_time}")
            self.after(1000, self.update_timer)
        elif self.game_ongoing:
            self.game_over()
    
    def reset_timer(self):
        # Reset the timer to the original time
        self.remaining_time = self.original_time
        self.timer_label.config(text=f"Time Left: {self.remaining_time}")
    
    
        
        
    def start_game(self):
        # Start the game
        self.reset_timer()
        self.generate_word()
        self.game_ongoing = True 
        self.update_timer()