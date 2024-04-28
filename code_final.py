import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
import azure.cognitiveservices.speech as speechsdk
import time
import random


class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__()
        
        self.bind("<Escape>", self.close_app)

        # Set initial window size
        self.geometry("1200x800")
        self.title("AI-based Elementary English Adventures")

        # Make the window non-resizable
        self.resizable(False, False)

        # Container to hold all pages
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}  # Dictionary to store all pages

        # Create and add pages to the dictionary
        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, PageFive, PageSix, PageSeven, PageEight, PageNine, PageTen):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Show the start page initially
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        
    def close_app(self, event):
        self.destroy()

#HomePage
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__()
        tk.Frame.__init__(self, parent)

        # Load the background image
        image = Image.open("pic.jpeg")
        image = image.resize((1200, 800), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        # Create a label to hold the background image
        background_label = ttk.Label(self, image=photo)
        background_label.image = photo  # Keep a reference to the image to prevent it from being garbage collected
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        '''

        label = ttk.Label(self, text="Learning Modes",font=("Comic Sans MS", 28))
        label.pack(padx=10, pady=10)
        '''

        style = ttk.Style()
        style.theme_use("default")

        style.configure("TButton",
                        foreground="#000000",
                        background="#a6892b",
                        width = 25,
                        font=("Comic Sans MS",18),
                        padding=[10,10,10,10])
        # Customize button properties
        button1 = ttk.Button(self, text="Practice Mode 練習模式",
                             style="TButton",
                             width = 30,
                             command=lambda: controller.show_frame(PageOne))
        button1.pack(pady=20,side="top")  # 10cm spacing below the button

        button2 = ttk.Button(self, text="Test Mode 測試模式",
                             style="TButton",
                             width = 30,
                             command=lambda: controller.show_frame(PageTwo))
        button2.pack(pady=20,side="top")  # 10cm spacing below the button

        button3 = ttk.Button(self, text="Games - 遊戲",
                             style="TButton",
                             width = 30,
                             command=lambda: controller.show_frame(PageThree))
        button3.pack(pady=20)  # 10cm spacing below the button

#PracticeMode
class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__()
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        image = Image.open("pic.jpeg")
        image = image.resize((1200, 800), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        # Create a label to hold the background image
        background_label = ttk.Label(self, image=photo)
        background_label.image = photo  # Keep a reference to the image to prevent it from being garbage collected
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        label = ttk.Label(self, text="Practice Mode", font = ("Comic Sans MS", 15))
        label.pack(pady=10, padx=10)

        style = ttk.Style()
        style.theme_use("default")

        style.configure("TButton",
                        foreground="#000000",
                        background="#a6892b",
                        width = 300,
                        font=("Comic Sans MS",20),
                        padding=[10,10,10,10])

        button = ttk.Button(self, text="Home Page",
                            style="TButton",
                            command=lambda: controller.show_frame(StartPage))
        button.pack(side="left", pady=20)

        button = ttk.Button(self, text="Back",
                            style="TButton",
                            command=lambda: controller.show_frame(StartPage))
        button.pack(side="right", pady=20)


        # Button to execute the code
        button1 = ttk.Button(self, text="Vocabulary - 詞彙",
                                     style="TButton",
                                     width = 30,
                                     command=self.run_tts)
        button1.pack(side="top", pady=20)
        
        button2 = ttk.Button(self, text="Sentence Construction - 句子构造",
                                     style="TButton",
                                     width = 30,
                                     command=self.run_tts)
        button2.pack(side="top", pady=20)
        

    def run_tts(self):

        vocabulary = {
            "Book": "书",
            "chair": "椅子",
            "doctor": "医生",
            "read": "读"
        }

        # Define and assign the Speech API key and region
        speech_key = "51ea1f1487cb413eb0ed452817ed6ef7"
        speech_region = "japaneast"

        # Speech Config for English
        speech_config_en = speechsdk.SpeechConfig(subscription=speech_key, region=speech_region)
        speech_config_en.speech_synthesis_voice_name = 'en-US-JennyNeural'

        # Speech Config for Chinese
        speech_config_zh = speechsdk.SpeechConfig(subscription=speech_key, region=speech_region)
        speech_config_zh.speech_synthesis_voice_name = 'zh-CN-XiaoxiaoNeural'

        # Initialize English SpeechSynthesizer
        audio_config_synthesis_en = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
        speech_synthesizer_en = speechsdk.SpeechSynthesizer(speech_config=speech_config_en,
                                                            audio_config=audio_config_synthesis_en)

        # Initialize Chinese SpeechSynthesizer
        audio_config_synthesis_zh = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
        speech_synthesizer_zh = speechsdk.SpeechSynthesizer(speech_config=speech_config_zh,
                                                            audio_config=audio_config_synthesis_zh)

        # Read vocabulary words in English
        synthesis_result_en = speech_synthesizer_en.speak_text_async(
            "Repeat the words in English").get()

        # Read vocabulary words in Chinese
        synthesis_result_zh = speech_synthesizer_zh.speak_text_async(
            "用英語重複這些單字").get()

        if synthesis_result_en.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            print("Prompting to repeat English words")
        if synthesis_result_zh.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            print("Prompting to repeat Chinese words")

        for english_word, chinese_word in vocabulary.items():
            print("\nReading word:", english_word)

            recognized = False
            while not recognized:
                # Synthesize and play the speech for word in English
                synthesis_result_en = speech_synthesizer_en.speak_text_async(english_word).get()

                if synthesis_result_en.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
                    print("Reading word [{}] in English".format(english_word))
                elif synthesis_result_en.reason == speechsdk.ResultReason.Canceled:
                    cancellation_details = synthesis_result_en.cancellation_details
                    print("Speech synthesis in English canceled: {}".format(cancellation_details.reason))
                    if cancellation_details.reason == speechsdk.CancellationReason.Error:
                        if cancellation_details.error_details:
                            print("Error details: {}".format(cancellation_details.error_details))
                            print("Check if the speech resource key and region values are correctly set.")

                # Synthesize and play the speech for word in Chinese
                synthesis_result_zh = speech_synthesizer_zh.speak_text_async(chinese_word).get()

                if synthesis_result_zh.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
                    print("Reading word [{}] in Chinese".format(chinese_word))
                elif synthesis_result_zh.reason == speechsdk.ResultReason.Canceled:
                    cancellation_details = synthesis_result_zh.cancellation_details
                    print("Speech synthesis in Chinese canceled: {}".format(cancellation_details.reason))
                    if cancellation_details.reason == speechsdk.CancellationReason.Error:
                        if cancellation_details.error_details:
                            print("Error details: {}".format(cancellation_details.error_details))
                            print("Check if the speech resource key and region values are correctly set.")

                # Wait for speech to finish playing before recording student's speech
                time.sleep(2)

                # Record student's speech and recognize
                speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config_en,
                                                               audio_config=speechsdk.audio.AudioConfig(
                                                                   use_default_microphone=True))
                print("\nPlease read the word aloud:")
                speech_recognition_result = speech_recognizer.recognize_once_async().get()

                if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
                    spoken_text = speech_recognition_result.text.strip().rstrip('.')
                    print("Recognized: {}".format(spoken_text))

                    # Provide feedback
                    if spoken_text.lower() == english_word.lower():
                        print("Excellent!")
                        recognized = True
                    else:
                        print("Incorrect. Please repeat the word.")
                elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
                    print("No speech could be recognized. Please try again.")
                else:
                    print("Speech recognition canceled: {}".format(
                        speech_recognition_result.cancellation_details.reason))
                    
##############################################################################################################################################
#TestMode
from EnglishSpellingGame import EnglishSpellingGame
class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__()
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Test Mode", font=("Comic Sans MS", 15))
        label.pack(pady=10, padx=10)
        
        image = Image.open("pic.jpeg")
        image = image.resize((1200, 800), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        # Create a label to hold the background image
        background_label = ttk.Label(self, image=photo)
        background_label.image = photo  # Keep a reference to the image to prevent it from being garbage collected
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        style = ttk.Style()
        style.theme_use("default")
        style.configure("TButton",
                        foreground="#000000",
                        background="#76c6cc",
                        width = 25,
                        font=("Comic Sans MS",20),
                        padding=[10,10,10,10])
        
        # Button to execute the code
        button1 = ttk.Button(self, text="Vocabulary - 詞彙",
                                     style="TButton",
                                     width=30,
                                     command=self.run_tts)
        button1.pack(side="top", pady=10)
        
        button2 = ttk.Button(self, text="Sentence Construction - 句子构造",
                                     style="TButton",
                                     width=30,
                                     command=self.run_tts)
        button2.pack(side="top", pady=10)
        
        button3 = ttk.Button(self, text="Spelling bee - 拼字比賽",width=30, style="TButton", command=lambda: controller.show_frame(PageTen))
        button3.pack(side="top", pady=10)
                             
                             
        button3.pack(side="top", pady=10)
        
        button4 = ttk.Button(self,text="Trivia Quiz - 問答遊戲",
                             style="TButton",
                             width=30
                             )
        button4.pack(side="top",pady=10)
        
        button = ttk.Button(self, text="Homepage",
                            style="TButton",
                            command=lambda: controller.show_frame(StartPage))
        button.pack(side=tk.LEFT,padx=10, pady=0)

        button = ttk.Button(self, text="Back",
                            style="TButton",
                            command=lambda: controller.show_frame(StartPage))
        button.pack(side=tk.RIGHT, padx=10,pady=0)
        
        
        

    def run_tts(self):

        vocabulary = {
            "Book": "书",
            "chair": "椅子",
            "doctor": "医生",
            "read": "读"
        }

        # Define and assign the Speech API key and region
        speech_key = "51ea1f1487cb413eb0ed452817ed6ef7"
        speech_region = "japaneast"

        # Speech Config for English
        speech_config_en = speechsdk.SpeechConfig(subscription=speech_key, region=speech_region)
        speech_config_en.speech_synthesis_voice_name = 'en-US-JennyNeural'

        # Speech Config for Chinese
        speech_config_zh = speechsdk.SpeechConfig(subscription=speech_key, region=speech_region)
        speech_config_zh.speech_synthesis_voice_name = 'zh-CN-XiaoxiaoNeural'

        # Initialize Chinese SpeechSynthesizer
        audio_config_synthesis_zh = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
        speech_synthesizer_zh = speechsdk.SpeechSynthesizer(speech_config=speech_config_zh,
                                                            audio_config=audio_config_synthesis_zh)

        # Read vocabulary words in Chinese
        synthesis_result_zh = speech_synthesizer_zh.speak_text_async(
            "现在我们要学习中文词汇。请跟我重复以下词汇:").get()

        if synthesis_result_zh.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            print("Prompting to repeat Chinese words")

        for english_word, chinese_word in vocabulary.items():
            print("\nReading word:", english_word)

            recognized = False
            while not recognized:
                # Synthesize and play the speech for word in Chinese
                synthesis_result_zh = speech_synthesizer_zh.speak_text_async(chinese_word).get()

                if synthesis_result_zh.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
                    print("Reading word [{}] in Chinese".format(chinese_word))
                elif synthesis_result_zh.reason == speechsdk.ResultReason.Canceled:
                    cancellation_details = synthesis_result_zh.cancellation_details
                    print("Speech synthesis in Chinese canceled: {}".format(cancellation_details.reason))
                    if cancellation_details.reason == speechsdk.CancellationReason.Error:
                        if cancellation_details.error_details:
                            print("Error details: {}".format(cancellation_details.error_details))
                            print("Check if the speech resource key and region values are correctly set.")

                # Wait for speech to finish playing before recording student's speech
                time.sleep(2)

                # Record student's speech and recognize
                speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config_en,
                                                               audio_config=speechsdk.audio.AudioConfig(
                                                                   use_default_microphone=True))
                print("\nPlease read the word aloud in English:")
                speech_recognition_result = speech_recognizer.recognize_once_async().get()

                if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
                    spoken_text = speech_recognition_result.text.strip().rstrip('.')
                    print("Recognized: {}".format(spoken_text))

                    # Provide feedback
                    if spoken_text.lower() == english_word.lower():
                        print("Excellent!")
                        recognized = True
                    else:
                        print("Incorrect. Please repeat the word.")
                elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
                    print("No speech could be recognized. Please try again.")
                else:
                    print("Speech recognition canceled: {}".format(
                        speech_recognition_result.cancellation_details.reason))
                    
# Import the EnglishSpellingGame class
from EnglishSpellingGame import EnglishSpellingGame
class PageTen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background="systemTransparent")  # Set background color to white
        # self.controller = controller

        # Load the background image
        image = Image.open("pic.jpeg")
        image = image.resize((1200, 800), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        # Create a label to hold the background image
        background_label = ttk.Label(self, image=photo)
        background_label.image = photo  # Keep a reference to the image to prevent it from being garbage collected
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        style = ttk.Style()
        style.theme_use("default")
        style.configure("TButton",
                        foreground="#000000",
                        background="#76c6cc",
                        width=15,
                        font=("Comic Sans MS", 14),
                        padding=[10, 10, 10, 10])

        # Button to navigate to the next page
        button_next = ttk.Button(self, text="上一頁",
                                 style="TButton",
                                 command=lambda: controller.show_frame(PageTwo))
        button_next.pack(side="bottom", pady=10)

        # Initialize the spelling game widget
        self.spelling_game = EnglishSpellingGame(self)

        # Button to start the spelling bee game
        button3 = ttk.Button(self, text="Start Spelling bee - 開始拼字比賽", style="TButton", command=self.start_game)
        button3.pack(side="top", fill="both", pady=50)

    def start_game(self):
        # Pack the spelling game and start it when the button is clicked
        self.spelling_game.pack(pady=10)
        self.spelling_game.start_game()  # Start the game

 ##########################################################################################################################       

#GamesMode
class PageThree(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background="white")  # Set background color to white

       
        
        image = Image.open("pic.jpeg")
        image = image.resize((1200, 800), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        # Create a label to hold the background image
        background_label = ttk.Label(self, image=photo)
        background_label.image = photo  # Keep a reference to the image to prevent it from being garbage collected
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        '''
        label = ttk.Label(self, text="Games - 遊戲", font=("Comic Sans MS", 25), background="systemTransparent")
        label.pack(pady=10, padx=10)
       '''

        style = ttk.Style()
        style.theme_use("default")

        style.configure("TButton",
                        foreground="#000000",
                        background="#76c6cc",
                        width = 25,
                        font=("Comic Sans MS",18),
                        padding=[10,10,10,10])

        # Button to go to Home Page
        button_home = ttk.Button(self, text="Back",
                                 style="TButton",
                                 command=lambda: controller.show_frame(StartPage))
        button_home.pack(side="bottom", pady=10)

        # Button to start visual games (go to PageOne)
        button_visual_games = ttk.Button(self, text="Start Visual Games",
                                         style="TButton",
                                         command=lambda: controller.show_frame(PageFour))

        button_visual_games.pack(side="bottom", pady=10)
class PageFour(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background="white")  # Set background color to white

        label = tk.Label(self, text="1", font=("Ravie", 25), background="white")
        label.pack(pady=10, padx=10)

        # Button to go to PageTwo
        button_page_two = tk.Button(self, text="Next 下一個", font=("Comic Sans MS", 15), width=10, height=3,
                                    background="light blue",
                                    command=lambda: controller.show_frame(PageFive))
        button_page_two.pack(side="bottom", pady=10)
        button_page_two.place(x=812, y=440)

        self.create_image_buttons()  # Create image buttons

        # Label to display the clicked button
        self.clicked_button_label = tk.Label(self, text="", font=("Helvetica", 18))
        self.clicked_button_label.pack()

        label = tk.Label(self, text="Car", font=("Comic Sans MS", 25), background="white")
        label.pack(side="bottom", pady=20, padx=20)

    def create_image_buttons(self):
        # Create Button 1
        image_path_1 = "planne.jpg"  # Replace with the path to your image for Button 1
        image_1 = ImageTk.PhotoImage(file=image_path_1)
        button1 = tk.Button(self, text="", width=320, height=250, image=image_1, compound=tk.CENTER, background="white",
                            borderwidth=0, highlightthickness=0,
                            command=lambda: self.button_click("Button 1", image_1))

        button1.pack()
        button1.place(x=8, y=150)

        # Create Button 2
        image_path_2 = "car.png"  # Replace with the path to your image for Button 2
        image_2 = ImageTk.PhotoImage(file=image_path_2)
        button2 = tk.Button(self, text="", width=320, height=250, image=image_2, compound=tk.LEFT, background="white",
                            borderwidth=0, highlightthickness=0,
                            command=lambda: self.button_click("Button 2", image_2))
        button2.pack()
        button2.place(x=338, y=150)

        # Create Button 3
        image_path_3 = "bus.jpg"  # Replace with the path to your image for Button 3
        image_3 = ImageTk.PhotoImage(file=image_path_3)
        button3 = tk.Button(self, text="", width=320, height=250, image=image_3, compound=tk.RIGHT, background="white",
                            borderwidth=0, highlightthickness=0,
                            command=lambda: self.button_click("Button 3", image_3))
        button3.pack()
        button3.place(x=667, y=150)

    def button_click(self, button_name, image):
        # Update the label to display the clicked image
        self.clicked_button_label.config(text=f"{button_name} clicked")

        # Replace these paths with the paths to your new images
        if button_name == "Button 1":
            new_image_path = "wrong.jpg"
            x = 8  # X coordinate for new image
            y = 30  # Y coordinate for new image

        elif button_name == "Button 2":
            new_image_path = "correct.jpg"
            x = 338  # X coordinate for new image
            y = 30  # Y coordinate for new image

        elif button_name == "Button 3":
            new_image_path = "wrong.jpg"
            x = 667  # X coordinate for new image
            y = 30  # Y coordinate for new image

        else:
            new_image_path = ""  # Default empty image path

        new_image = ImageTk.PhotoImage(file=new_image_path)
        self.clicked_button_label.config(image=new_image)
        self.clicked_button_label.image = new_image  # Keep a reference to prevent garbage collection
        self.clicked_button_label.place(x=x, y=y)
class PageFive(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background="white")  # Set background color to white

        label = tk.Label(self, text="2", font=("Comic Sans MS", 25), background="white")
        label.pack(pady=10, padx=10)

        # Button to go to PageThree
        button_page_three = tk.Button(self, text="Next", font=("Comic Sans MS", 15), width=10, height=3, background="light blue",
                                      command=lambda: controller.show_frame(PageSix))
        button_page_three.pack()
        button_page_three.place(x=812, y=440)

        self.create_image_buttons()  # Create image buttons

        # Label to display the clicked button
        self.clicked_button_label = tk.Label(self, text="", font=("Helvetica", 18))
        self.clicked_button_label.pack()

        label = tk.Label(self, text="Banana", font=("Comic Sans MS", 25), bg="white")
        label.pack(side="bottom", pady=20, padx=20)

    def create_image_buttons(self):
        # Create Button 1
        image_path_1 = "banana.jpg"  # Replace with the path to your image for Button 1
        image_1 = ImageTk.PhotoImage(file=image_path_1)
        button1 = tk.Button(self, text="", width=320, height=250, image=image_1, compound=tk.CENTER, background="white",
                            borderwidth=0, highlightthickness=0,
                            command=lambda: self.button_click("Button 1", image_1))

        button1.pack()
        button1.place(x=8, y=150)

        # Create Button 2
        image_path_2 = "apple.png"  # Replace with the path to your image for Button 2
        image_2 = ImageTk.PhotoImage(file=image_path_2)
        button2 = tk.Button(self, text="", width=320, height=250, image=image_2, compound=tk.LEFT, background="white",
                            borderwidth=0, highlightthickness=0,
                            command=lambda: self.button_click("Button 2", image_2))
        button2.pack()
        button2.place(x=338, y=150)

        # Create Button 3
        image_path_3 = "orange.jpg"  # Replace with the path to your image for Button 3
        image_3 = ImageTk.PhotoImage(file=image_path_3)
        button3 = tk.Button(self, text="", width=320, height=250, image=image_3, compound=tk.RIGHT, background="white",
                            borderwidth=0, highlightthickness=0,
                            command=lambda: self.button_click("Button 3", image_3))
        button3.pack()
        button3.place(x=667, y=150)

    def button_click(self, button_name, image):
        # Update the label to display the clicked image
        self.clicked_button_label.config(text=f"{button_name} clicked")

        # Replace these paths with the paths to your new images
        if button_name == "Button 1":
            new_image_path = "correct.jpg"
            x = 8  # X coordinate for new image
            y = 30  # Y coordinate for new image

        elif button_name == "Button 2":
            new_image_path = "wrong.jpg"
            x = 338  # X coordinate for new image
            y = 30  # Y coordinate for new image

        elif button_name == "Button 3":
            new_image_path = "wrong.jpg"
            x = 667  # X coordinate for new image
            y = 30  # Y coordinate for new image

        else:
            new_image_path = ""  # Default empty image path

        new_image = ImageTk.PhotoImage(file=new_image_path)
        self.clicked_button_label.config(image=new_image)
        self.clicked_button_label.image = new_image  # Keep a reference to prevent garbage collection
        self.clicked_button_label.place(x=x, y=y)


class PageSix(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background="white")  # Set background color to white

        label = tk.Label(self, text="3", font=("Comic Sans MS", 25), background="white")
        label.pack(pady=10, padx=10)

        # Button to go to PageFive
        # Button to go to PageTwo
        button_page_two = tk.Button(self, text="Next", font=("Comic Sans MS", 15), width=10, height=3,
                                    background="light blue",
                                    command=lambda: controller.show_frame(PageSeven))
        button_page_two.pack(side="bottom", pady=10)
        button_page_two.place(x=812, y=440)

        self.create_image_buttons()  # Create image buttons

        # Label to display the clicked button
        self.clicked_button_label = tk.Label(self, text="", font=("Helvetica", 18))
        self.clicked_button_label.pack()

        label = tk.Label(self, text="Teacher", font=("Comic Sans MS", 25), bg="white")
        label.pack(side="bottom", pady=20, padx=20)

    def create_image_buttons(self):
        # Create Button 1
        image_path_1 = "pilot.jpg"  # Replace with the path to your image for Button 1
        image_1 = ImageTk.PhotoImage(file=image_path_1)
        button1 = tk.Button(self, text="", width=320, height=250, image=image_1, compound=tk.CENTER, background="white",
                            borderwidth=0, highlightthickness=0,
                            command=lambda: self.button_click("Button 1", image_1))

        button1.pack()
        button1.place(x=8, y=150)

        # Create Button 2
        image_path_2 = "painter.jpg"  # Replace with the path to your image for Button 2
        image_2 = ImageTk.PhotoImage(file=image_path_2)
        button2 = tk.Button(self, text="", width=320, height=250, image=image_2, compound=tk.LEFT, background="white",
                            borderwidth=0, highlightthickness=0,
                            command=lambda: self.button_click("Button 2", image_2))
        button2.pack()
        button2.place(x=338, y=150)

        # Create Button 3
        image_path_3 = "teacher.jpg"  # Replace with the path to your image for Button 3
        image_3 = ImageTk.PhotoImage(file=image_path_3)
        button3 = tk.Button(self, text="", width=320, height=250, image=image_3, compound=tk.RIGHT, background="white",
                            borderwidth=0, highlightthickness=0,
                            command=lambda: self.button_click("Button 3", image_3))
        button3.pack()
        button3.place(x=667, y=150)

    def button_click(self, button_name, image):
        # Update the label to display the clicked image
        self.clicked_button_label.config(text=f"{button_name} clicked")

        # Replace these paths with the paths to your new images
        if button_name == "Button 1":
            new_image_path = "wrong.jpg"  
            x = 8  # X coordinate for new image
            y = 30  # Y coordinate for new image

        elif button_name == "Button 2":
            new_image_path = "wrong.jpg"
            x = 338  # X coordinate for new image
            y = 30  # Y coordinate for new image

        elif button_name == "Button 3":
            new_image_path = "correct.jpg"
            x = 667  # X coordinate for new image
            y = 30  # Y coordinate for new image

        else:
            new_image_path = ""  # Default empty image path

        new_image = ImageTk.PhotoImage(file=new_image_path)
        self.clicked_button_label.config(image=new_image)
        self.clicked_button_label.image = new_image  # Keep a reference to prevent garbage collection
        self.clicked_button_label.place(x=x, y=y)
class PageSeven(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background="white")  # Set background color to white

        label = tk.Label(self, text="4", font=("Comic Sans MS", 25), background="white")
        label.pack(pady=10, padx=10)

        # Button to go to PageSix
        # Button to go to PageTwo
        button_page_two = tk.Button(self, text="Next", font=("Comic Sans MS", 15), width=10, height=3,
                                    bg="light blue",
                                    command=lambda: controller.show_frame(PageEight))
        button_page_two.pack(side="bottom", pady=10)
        button_page_two.place(x=812, y=440)

        self.create_image_buttons()  # Create image buttons

        # Label to display the clicked button
        self.clicked_button_label = tk.Label(self, text="", font=("Helvetica", 18))
        self.clicked_button_label.pack()

        label = tk.Label(self, text="Cow", font=("Comic Sans MS", 25), background="white")
        label.pack(side="bottom", pady=20, padx=20)

    def create_image_buttons(self):
        # Create Button 1
        image_path_1 = "chicken.png"  # Replace with the path to your image for Button 1
        image_1 = ImageTk.PhotoImage(file=image_path_1)
        button1 = tk.Button(self, text="", width=320, height=250, image=image_1, compound=tk.CENTER, background="white",
                            borderwidth=0, highlightthickness=0,
                            command=lambda: self.button_click("Button 1", image_1))

        button1.pack()
        button1.place(x=8, y=150)

        # Create Button 2
        image_path_2 = "cow.jpg"  # Replace with the path to your image for Button 2
        image_2 = ImageTk.PhotoImage(file=image_path_2)
        button2 = tk.Button(self, text="", width=320, height=250, image=image_2, compound=tk.LEFT, background="white",
                            borderwidth=0, highlightthickness=0,
                            command=lambda: self.button_click("Button 2", image_2))
        button2.pack()
        button2.place(x=338, y=150)

        # Create Button 3
        image_path_3 = "dog.jpg"  # Replace with the path to your image for Button 3
        image_3 = ImageTk.PhotoImage(file=image_path_3)
        button3 = tk.Button(self, text="", width=320, height=250, image=image_3, compound=tk.RIGHT, background="white",
                            borderwidth=0, highlightthickness=0,
                            command=lambda: self.button_click("Button 3", image_3))
        button3.pack()
        button3.place(x=667, y=150)

    def button_click(self, button_name, image):
        # Update the label to display the clicked image
        self.clicked_button_label.config(text=f"{button_name} clicked")

        # Replace these paths with the paths to your new images
        if button_name == "Button 1":
            new_image_path = "wrong.jpg"
            x = 8  # X coordinate for new image
            y = 30  # Y coordinate for new image

        elif button_name == "Button 2":
            new_image_path = "correct.jpg"
            x = 338  # X coordinate for new image
            y = 30  # Y coordinate for new image

        elif button_name == "Button 3":
            new_image_path = "wrong.jpg"
            x = 667  # X coordinate for new image
            y = 30  # Y coordinate for new image

        else:
            new_image_path = ""  # Default empty image path

        new_image = ImageTk.PhotoImage(file=new_image_path)
        self.clicked_button_label.config(image=new_image)
        self.clicked_button_label.image = new_image  # Keep a reference to prevent garbage collection
        self.clicked_button_label.place(x=x, y=y)

class PageEight(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background="white")  # Set background color to white

        label = tk.Label(self, text="5", font=("Ravie", 25), background="white")
        label.pack(pady=10, padx=10)

        # Button to go to PageSeven
        # Button to go to PageTwo
        button_page_two = tk.Button(self, text="Next", font=("Ravie", 15), width=10, height=3,
                                    bg="light blue",
                                    command=lambda: controller.show_frame(PageNine))
        button_page_two.pack(side="bottom", pady=10)
        button_page_two.place(x=812, y=440)
        self.create_image_buttons()  # Create image buttons

        # Label to display the clicked button
        self.clicked_button_label = tk.Label(self, text="", font=("Helvetica", 18))
        self.clicked_button_label.pack()

        label = tk.Label(self, text="Playing table tennis", font=("Comic Sans MS", 25), background="white")
        label.pack(side="bottom", pady=20, padx=20)

    def create_image_buttons(self):
        # Create Button 1
        image_path_1 = "playFootball.jpg"  # Replace with the path to your image for Button 1
        image_1 = ImageTk.PhotoImage(file=image_path_1)
        button1 = tk.Button(self, text="", width=320, height=250, image=image_1, compound=tk.CENTER, background="white",
                            borderwidth=0, highlightthickness=0,
                            command=lambda: self.button_click("Button 1", image_1))

        button1.pack()
        button1.place(x=8, y=150)

        # Create Button 2
        image_path_2 = "playVolleyball.jpg"  # Replace with the path to your image for Button 2
        image_2 = ImageTk.PhotoImage(file=image_path_2)
        button2 = tk.Button(self, text="", width=320, height=250, image=image_2, compound=tk.LEFT, background="white",
                            borderwidth=0, highlightthickness=0,
                            command=lambda: self.button_click("Button 2", image_2))
        button2.pack()
        button2.place(x=338, y=150)

        # Create Button 3
        image_path_3 = "LPAYtBLEtENNIS.jpg"  # Replace with the path to your image for Button 3
        image_3 = ImageTk.PhotoImage(file=image_path_3)
        button3 = tk.Button(self, text="", width=320, height=250, image=image_3, compound=tk.RIGHT, background="white",
                            borderwidth=0, highlightthickness=0,
                            command=lambda: self.button_click("Button 3", image_3))
        button3.pack()
        button3.place(x=667, y=150)

    def button_click(self, button_name, image):
        # Update the label to display the clicked image
        self.clicked_button_label.config(text=f"{button_name} clicked")

        # Replace these paths with the paths to your new images
        if button_name == "Button 1":
            new_image_path = "wrong.jpg"
            x = 8  # X coordinate for new image
            y = 30  # Y coordinate for new image

        elif button_name == "Button 2":
            new_image_path = "wrong.jpg"
            x = 338  # X coordinate for new image
            y = 30  # Y coordinate for new image

        elif button_name == "Button 3":
            new_image_path = "correct.jpg"
            x = 667  # X coordinate for new image
            y = 30  # Y coordinate for new image

        else:
            new_image_path = ""  # Default empty image path

        new_image = ImageTk.PhotoImage(file=new_image_path)
        self.clicked_button_label.config(image=new_image)
        self.clicked_button_label.image = new_image  # Keep a reference to prevent garbage collection
        self.clicked_button_label.place(x=x, y=y)

class PageNine(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")  # Set background color to white

        label = tk.Label(self, text="6", font=("Ravie", 25), bg="white")
        label.pack(pady=10, padx=10)

        # Button to go to PageEight
        # Button to go to PageTwo
        button_page_two = tk.Button(self, text="Return", font=("Ravie", 15), width=10, height=3,
                                    bg="light blue",
                                    command=lambda: controller.show_frame(PageThree))
        button_page_two.pack(side="bottom", pady=10)
        button_page_two.place(x=812, y=440)

        self.create_image_buttons()  # Create image buttons

        # Label to display the clicked button
        self.clicked_button_label = tk.Label(self, text="", font=("Helvetica", 18))
        self.clicked_button_label.pack()

        label = tk.Label(self, text="Wash Face", font=("Ravie", 25), bg="white")
        label.pack(side="bottom", pady=20, padx=20)

    def create_image_buttons(self):
        # Create Button 1
        image_path_1 = "brushTeeth.jpg"  # Replace with the path to your image for Button 1
        image_1 = ImageTk.PhotoImage(file=image_path_1)
        button1 = tk.Button(self, text="", width=320, height=250, image=image_1, compound=tk.CENTER, bg="white",
                            borderwidth=0, highlightthickness=0,
                            command=lambda: self.button_click("Button 1", image_1))

        button1.pack()
        button1.place(x=8, y=150)

        # Create Button 2
        image_path_2 = "washFace.jpg"  # Replace with the path to your image for Button 2
        image_2 = ImageTk.PhotoImage(file=image_path_2)
        button2 = tk.Button(self, text="", width=320, height=250, image=image_2, compound=tk.LEFT, bg="white",
                            borderwidth=0, highlightthickness=0,
                            command=lambda: self.button_click("Button 2", image_2))
        button2.pack()
        button2.place(x=338, y=150)

        # Create Button 3
        image_path_3 = "cookFood.jpg"  # Replace with the path to your image for Button 3
        image_3 = ImageTk.PhotoImage(file=image_path_3)
        button3 = tk.Button(self, text="", width=320, height=250, image=image_3, compound=tk.RIGHT, bg="white",
                            borderwidth=0, highlightthickness=0,
                            command=lambda: self.button_click("Button 3", image_3))
        button3.pack()
        button3.place(x=667, y=150)

    def button_click(self, button_name, image):
        # Update the label to display the clicked image
        self.clicked_button_label.config(text=f"{button_name} clicked")

        # Replace these paths with the paths to your new images
        if button_name == "Button 1":
            new_image_path = "wrong.jpg"
            x = 8  # X coordinate for new image
            y = 30  # Y coordinate for new image

        elif button_name == "Button 2":
            new_image_path = "correct.jpg"
            x = 338  # X coordinate for new image
            y = 30  # Y coordinate for new image

        elif button_name == "Button 3":
            new_image_path = "wrong.jpg"
            x = 667  # X coordinate for new image
            y = 30  # Y coordinate for new image

        else:
            new_image_path = ""  # Default empty image path

        new_image = ImageTk.PhotoImage(file=new_image_path)
        self.clicked_button_label.config(image=new_image)
        self.clicked_button_label.image = new_image  # Keep a reference to prevent garbage collection
        self.clicked_button_label.place(x=x, y=y)

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()


