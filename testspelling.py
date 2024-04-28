import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
import azure.cognitiveservices.speech as speechsdk
import time
import random
from EnglishSpellingGame import EnglishSpellingGame


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
        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, PageFive,
                  PageSix, PageSeven, PageEight, PageNine, PageTen, PageEleven,
                  PageTwelve, PageThirteen, PageFourteen,Page15, Page16, Page17,
                  Page18, Page19,Page20, Page21, Page22, Page23, Page24, Page25):
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
       
        style = ttk.Style()
        style.theme_use("default")

        style.configure("TButton",
                        foreground="#000000",
                        background="#76c6cc",
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


##########################################################################################################################
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

        label = ttk.Label(self, text="Practice Mode 練習模式",
                          background = "#76c6cc",
                          font = ("Comic Sans MS", 25))
        label.pack(pady=10, padx=10)

       
        label = ttk.Label(self, text="練習模式指示", font=("Comic Sans MS", 25),
                         background="#76c6cc")
        label.pack(pady=10, padx=10)
        
             
        style = ttk.Style()
        style.theme_use("default")

        style.configure("TButton",
                        foreground="#000000",
                        background="#76c6cc",
                        width = 25,
                        font=("Times New Roman",18),
                        padding=[10,10,10,10])
        
        button_read_text = ttk.Button(self, text="音訊指導",
                                           style="TButton",
                                           width = 20,
                                           command=self.read_custom_chinese_text)
        button_read_text.pack(pady = 10,padx = 10)
        
        # Create a label below the button
        instr_label = ttk.Label(self, text="\n1. 點選麥克風圖示。\n2. 我能說出圖中事物的名稱。\n3. 現在跟我來，立即再說一次。"
                                                "\n4. 你可以練習說三次來檢查你的發音。"
                                                "\n5. 如果你說錯了或三遍都沒有說完，我會告訴你正確的發音，然後再試一次。"
                                                "\n6. 點擊右下角的「下一步」按鈕，可以看到下一張圖片。",
                                     font=("Comic Sans MS", 18), background="#eddf13", justify="left")
        instr_label.pack(pady=20,padx = 10)
      
        # Button to execute the code
        button1 = ttk.Button(self, text="Vocabulary 詞彙",
                                     style="TButton",
                                    width = 25,
                                     command=lambda: controller.show_frame(PageEleven))
        button1.pack(side="top", pady=20)
       
        
        button2 = ttk.Button(self, text="Sentence Construction 句子构造",
                                     style="TButton",
                                     width = 25,
                                     command=lambda: controller.show_frame(Page15))
        button2.pack(side="top", pady=40)
        
        button3 = ttk.Button(self, text="Homepage 首頁",
                            style="TButton",
                            width = 15,
                            command=lambda: controller.show_frame(StartPage))
        button3.pack(side="left", pady=40, padx = 10)
        
        button4 = ttk.Button(self, text="Back 後退",
                            style="TButton",
                            width = 15,
                            command=lambda: controller.show_frame(StartPage))
        button4.pack(side="right", pady=40, padx = 10)
       
        
    def read_custom_chinese_text(self):
        # Customize the Chinese text you want to read
        chinese_text = ("你好.  指示：\n1. 點選麥克風圖示。\n2. 我能說出圖中事物的名稱。\n3. 現在跟我來，立即再說一次。"
                        "\n4.你可以練習說三次來檢查你的發音。"
                        "\n5.如果你說錯了或三遍都沒有說完，我會告訴你正確的發音，然後再試一次。"
                        "\n6. 點擊右下角的「下一步」按鈕，可以看到下一張圖片。")

        # Configure the Azure Text-to-Speech service
        speech_config = speechsdk.SpeechConfig(subscription="51ea1f1487cb413eb0ed452817ed6ef7", region="japaneast")

        # Specify the Chinese voice
        speech_config.speech_synthesis_voice_name = "zh-TW-HsiaoYuNeural"

        # Initialize the SpeechSynthesizer
        speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

        # Synthesize and play the speech for the Chinese text
        result = speech_synthesizer.speak_text_async(chinese_text).get()

        if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            print("Speech synthesis completed.")
        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = result.cancellation_details
            print("Speech synthesis canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                if cancellation_details.error_details:
                    print("Error details: {}".format(cancellation_details.error_details))
                    
    #############################################VOCABULARY##############################################################################################################################################   
class PageEleven(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background="#FFFFFF")  # Set background color to white
        self.controller = controller
        
       
        style = ttk.Style()
        style.theme_use("default")

        style.configure("TButton",
                        foreground="#000000",
                        background="#76c6cc",
                        width = 15,
                        font=("Comic Sans MS",18),
                        padding=[10,10,10,10])

        # Button to navigate to the next page
        button_next = ttk.Button(self, text="Next 下一個",style = 'TButton',
                                command=lambda: controller.show_frame(PageTwelve))
        button_next.pack()
        button_next.place(x=950, y=700, width=200, height=50)

        # Button to navigate to the next page
        button_next = ttk.Button(self, text="Back 後退",style = 'TButton',
                                command=lambda: controller.show_frame(PageOne))
        button_next.pack()
        button_next.place(x=10, y=700, width=200, height=50)

        # Run Code Button
        button_run_code = tk.Button(self,
                                    command=self.run_code)
        image = tk.PhotoImage(file="mc.png") 
        button_run_code.config(image=image)
        button_run_code.image = image  
        button_run_code.pack()
        button_run_code.place(x=950, y=100,width=250, height=250)# width=250, height=250)
        
        label = ttk.Label(self, text="Book", font=("Comic Sans MS", 25),background="#FFFFFF")
        label.pack(pady=10)

        # Load image
        self.image = Image.open("book.jpg")  
        self.image = self.image.resize((450, 430), Image.NEAREST) 
        self.photo = ImageTk.PhotoImage(self.image)

        # Display image
        self.image_label = ttk.Label(self, image = self.photo)
        self.image_label.pack(pady = 10)

    def run_code(self):

        def tts_prompt_vocabulary(vocabulary):
            # Define and assign the Speech API key and region
            speech_key = "51ea1f1487cb413eb0ed452817ed6ef7"
            speech_region = "japaneast"

            # Speech Config for English
            speech_config_en = speechsdk.SpeechConfig(subscription=speech_key, region=speech_region)
            speech_config_en.speech_synthesis_voice_name = 'zh-CN-XiaoxiaoNeural'

            # Speech Config for Chinese
            speech_config_cn = speechsdk.SpeechConfig(subscription=speech_key, region=speech_region)
            speech_config_cn.speech_synthesis_voice_name = 'zh-CN-XiaoxiaoNeural'  # Chinese voice

            # Initialize SpeechSynthesizer
            audio_config_synthesis = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
            speech_synthesizer_en = speechsdk.SpeechSynthesizer(speech_config=speech_config_en,
                                                                audio_config=audio_config_synthesis)
            speech_synthesizer_cn = speechsdk.SpeechSynthesizer(speech_config=speech_config_cn,
                                                                audio_config=audio_config_synthesis)

            for word in vocabulary:
                print("\nReading word:", word)

                # Synthesize and play the speech for word
                synthesis_result = speech_synthesizer_en.speak_text_async("跟著我重複一遍: " + word).get()
                
                if synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
                    print("Reading word [{}]".format(word))
                elif synthesis_result.reason == speechsdk.ResultReason.Canceled:
                    cancellation_details = synthesis_result.cancellation_details
                    print("Speech synthesis canceled: {}".format(cancellation_details.reason))
                    if cancellation_details.reason == speechsdk.CancellationReason.Error:
                        if cancellation_details.error_details:
                            print("Error details: {}".format(cancellation_details.error_details))
                            print("Check if the speech resource key and region values are correctly set.")

                # Record student's speech and recognize
                max_attempts = 3
                for attempt in range(1, max_attempts + 1):
                    print("\nAttempt", attempt)
                    print("Please read the word aloud:")

                    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config_en,
                                                                   audio_config=speechsdk.audio.AudioConfig(
                                                                       use_default_microphone=True))
                    speech_recognition_result = speech_recognizer.recognize_once_async().get()

                    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
                        spoken_text = speech_recognition_result.text.strip().rstrip('.')
                        print("Recognized: {}".format(spoken_text))

                        # Provide feedback
                        if spoken_text.lower() == word.lower():
                            # Correct recognition
                            print("Correct!")
                            # Synthesize "Correct" in Chinese
                            synthesis_result = speech_synthesizer_cn.speak_text_async("正確，點擊下一步繼續。").get()
                            break
                        else:
                            # Incorrect recognition
                            if attempt < max_attempts:
                                # Synthesize "Wrong, please try again" in Chinese
                                print("Wrong, please try again.")
                                synthesis_result = speech_synthesizer_cn.speak_text_async(
                                    "錯誤，請重試，圖中的東西是. book").get()
                            else:
                                # Maximum attempts reached, synthesize the correct word in Chinese
                                print("Maximum attempts reached. The correct word is:", word)
                                # Synthesize the correct word in Chinese and then in English
                                synthesis_result = speech_synthesizer_cn.speak_text_async("正确单词是").get()
                                synthesis_result = speech_synthesizer_en.speak_text_async(word).get()
                                break

                    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
                        print("No speech could be recognized. Please try again.")
                        # Speak "say what you see loud" in Chinese
                        synthesis_result = speech_synthesizer_cn.speak_text_async(
                            "用英語再試一次。大聲說出你所看到的").get()
                    else:
                        print("Speech recognition canceled: {}".format(
                            speech_recognition_result.cancellation_details.reason))

        # Sample vocabulary
        vocabulary = ["Book", ]

        # Run the function with sample vocabulary
        tts_prompt_vocabulary(vocabulary)
        
class PageTwelve(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background="#FFFFFF")  # Set background color to white
        self.controller = controller
        
        
        style = ttk.Style()
        style.theme_use("default")

        style.configure("TButton",
                        foreground="#000000",
                        background="#76c6cc",
                        width = 25,
                        font=("Comic Sans MS",20),
                        padding=[10,10,10,10])

        # Button to navigate to the next page
        button_next = ttk.Button(self, text="Next 下一個",style = 'TButton', width = 15,
                                command=lambda: controller.show_frame(PageThirteen))
        button_next.pack()
        button_next.place(x=950, y=700, width=200, height=50)

        # Button to navigate to the next page
        button_next = ttk.Button(self, text="Back 後退",style = 'TButton', width = 15,
                                command=lambda: controller.show_frame(PageEleven))
        button_next.pack()
        button_next.place(x=10, y=700, width=200, height=50)

        # Run Code Button
        button_run_code = ttk.Button(self,
                                    command=self.run_code2)
        image = tk.PhotoImage(file="mc.png") 
        button_run_code.config(image=image)
        button_run_code.image = image  
        button_run_code.pack()
        button_run_code.place(x=950, y=100, width=250, height=250)
        # Load image
        self.image = Image.open("chair.png")  # Replace "your_image.jpg" with the path to your image
        self.image = self.image.resize((450, 430), Image.NEAREST)  # Resize the image without ANTIALIAS
        self.photo = ImageTk.PhotoImage(self.image)
        
        label = ttk.Label(self, text="Chair", font=("Comic Sans MS", 30),background="#FFFFFF")
        label.pack(pady=20)

        # Display image
        self.image_label = ttk.Label(self, image=self.photo)
        self.image_label.pack()

    def run_code2(self):
        import azure.cognitiveservices.speech as speechsdk

        def tts_prompt_vocabulary(vocabulary):
            # Define and assign the Speech API key and region
            speech_key = "51ea1f1487cb413eb0ed452817ed6ef7"
            speech_region = "japaneast"

            # Speech Config for English
            speech_config_en = speechsdk.SpeechConfig(subscription=speech_key, region=speech_region)
            speech_config_en.speech_synthesis_voice_name = 'zh-CN-XiaoxiaoNeural'

            # Speech Config for Chinese
            speech_config_cn = speechsdk.SpeechConfig(subscription=speech_key, region=speech_region)
            speech_config_cn.speech_synthesis_voice_name = 'zh-CN-XiaoxiaoNeural'  # Chinese voice

            # Initialize SpeechSynthesizer
            audio_config_synthesis = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
            speech_synthesizer_en = speechsdk.SpeechSynthesizer(speech_config=speech_config_en,
                                                                audio_config=audio_config_synthesis)
            speech_synthesizer_cn = speechsdk.SpeechSynthesizer(speech_config=speech_config_cn,
                                                                audio_config=audio_config_synthesis)

            for word in vocabulary:
                print("\nReading word:", word)

                # Synthesize and play the speech for word
                synthesis_result = speech_synthesizer_en.speak_text_async("跟著我重複一遍: " + word).get()

                if synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
                    print("Reading word [{}]".format(word))
                elif synthesis_result.reason == speechsdk.ResultReason.Canceled:
                    cancellation_details = synthesis_result.cancellation_details
                    print("Speech synthesis canceled: {}".format(cancellation_details.reason))
                    if cancellation_details.reason == speechsdk.CancellationReason.Error:
                        if cancellation_details.error_details:
                            print("Error details: {}".format(cancellation_details.error_details))
                            print("Check if the speech resource key and region values are correctly set.")

                # Record student's speech and recognize
                max_attempts = 3
                for attempt in range(1, max_attempts + 1):
                    print("\nAttempt", attempt)
                    print("Please read the word aloud:")

                    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config_en,
                                                                   audio_config=speechsdk.audio.AudioConfig(
                                                                       use_default_microphone=True))
                    speech_recognition_result = speech_recognizer.recognize_once_async().get()

                    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
                        spoken_text = speech_recognition_result.text.strip().rstrip('.')
                        print("Recognized: {}".format(spoken_text))

                        # Provide feedback
                        if spoken_text.lower() == word.lower():
                            # Correct recognition
                            print("Correct!")
                            # Synthesize "Correct" in Chinese
                            synthesis_result = speech_synthesizer_cn.speak_text_async("正確，點擊下一步繼續").get()
                            break
                        else:
                            # Incorrect recognition
                            if attempt < max_attempts:
                                # Synthesize "Wrong, please try again" in Chinese
                                print("Wrong, please try again.")
                                synthesis_result = speech_synthesizer_cn.speak_text_async(
                                    "錯誤，請重試，圖中的東西是. chair").get()
                            else:
                                # Maximum attempts reached, synthesize the correct word in Chinese
                                print("Maximum attempts reached. The correct word is:", word)
                                # Synthesize the correct word in Chinese and then in English
                                synthesis_result = speech_synthesizer_cn.speak_text_async("正确单词是").get()
                                synthesis_result = speech_synthesizer_en.speak_text_async(word).get()
                                break

                    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
                        print("No speech could be recognized. Please try again.")
                        # Speak "say what you see loud" in Chinese
                        synthesis_result = speech_synthesizer_cn.speak_text_async(
                            "用英語再試一次。大聲說出你所看到的").get()
                    else:
                        print("Speech recognition canceled: {}".format(
                            speech_recognition_result.cancellation_details.reason))

        # Sample vocabulary
        vocabulary = ["Chair", ]
        tts_prompt_vocabulary(vocabulary)

class PageThirteen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background="#FFFFFF")  # Set background color to white
        self.controller = controller
        
        style = ttk.Style()
        style.theme_use("default")

        style.configure("TButton",
                        foreground="#000000",
                        background="#76c6cc",
                        width = 25,
                        font=("Comic Sans MS",20),
                        padding=[10,10,10,10])

        # Button to navigate to the next page
        button_next = ttk.Button(self, text="Next 下一個",style = 'TButton',
                                command=lambda: controller.show_frame(PageFourteen))
        button_next.pack()
        button_next.place(x=950, y=700, width=200, height=50)
        
        # Button to navigate to the next page
        button_next = ttk.Button(self, text="Back 後退",style = 'TButton',
                                command=lambda: controller.show_frame(PageTwelve))
        button_next.pack()
        button_next.place(x=10, y=700, width=200, height=50)
        
        button_run_code = ttk.Button(self,
                                    command=self.run_code2)
        image = tk.PhotoImage(file="mc.png")  # Specify the path to your image file
        button_run_code.config(image=image)
        button_run_code.image = image  # Keep a reference to avoid garbage collection
        button_run_code.pack()
        button_run_code.place(x=950, y=100,width=250, height=250)
        
        label = ttk.Label(self, text="Doctor", font=("Comic Sans MS", 25),background="#FFFFFF")
        label.pack(pady=10)
        # Load image
        self.image = Image.open("doctor.png")  # Replace "your_image.jpg" with the path to your image
        self.image = self.image.resize((450, 430), Image.NEAREST)  # Resize the image without ANTIALIAS
        self.photo = ImageTk.PhotoImage(self.image)

        # Display image
        self.image_label =ttk.Label(self, image=self.photo)
        self.image_label.pack()

    def run_code2(self):
        import azure.cognitiveservices.speech as speechsdk

        def tts_prompt_vocabulary(vocabulary):
            # Define and assign the Speech API key and region
            speech_key = "51ea1f1487cb413eb0ed452817ed6ef7"
            speech_region = "japaneast"

            # Speech Config for English
            speech_config_en = speechsdk.SpeechConfig(subscription=speech_key, region=speech_region)
            speech_config_en.speech_synthesis_voice_name = 'zh-CN-XiaoxiaoNeural'

            # Speech Config for Chinese
            speech_config_cn = speechsdk.SpeechConfig(subscription=speech_key, region=speech_region)
            speech_config_cn.speech_synthesis_voice_name = 'zh-CN-XiaoxiaoNeural'  # Chinese voice

            # Initialize SpeechSynthesizer
            audio_config_synthesis = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
            speech_synthesizer_en = speechsdk.SpeechSynthesizer(speech_config=speech_config_en,
                                                                audio_config=audio_config_synthesis)
            speech_synthesizer_cn = speechsdk.SpeechSynthesizer(speech_config=speech_config_cn,
                                                                audio_config=audio_config_synthesis)

            for word in vocabulary:
                print("\nReading word:", word)

                # Synthesize and play the speech for word
                synthesis_result = speech_synthesizer_en.speak_text_async("跟著我重複一遍: " + word).get()

                if synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
                    print("Reading word [{}]".format(word))
                elif synthesis_result.reason == speechsdk.ResultReason.Canceled:
                    cancellation_details = synthesis_result.cancellation_details
                    print("Speech synthesis canceled: {}".format(cancellation_details.reason))
                    if cancellation_details.reason == speechsdk.CancellationReason.Error:
                        if cancellation_details.error_details:
                            print("Error details: {}".format(cancellation_details.error_details))
                            print("Check if the speech resource key and region values are correctly set.")

                # Record student's speech and recognize
                max_attempts = 3
                for attempt in range(1, max_attempts + 1):
                    print("\nAttempt", attempt)
                    print("Please read the word aloud:")

                    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config_en,
                                                                   audio_config=speechsdk.audio.AudioConfig(
                                                                       use_default_microphone=True))
                    speech_recognition_result = speech_recognizer.recognize_once_async().get()

                    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
                        spoken_text = speech_recognition_result.text.strip().rstrip('.')
                        print("Recognized: {}".format(spoken_text))

                        # Provide feedback
                        if spoken_text.lower() == word.lower():
                            # Correct recognition
                            print("Correct!")
                            # Synthesize "Correct" in Chinese
                            synthesis_result = speech_synthesizer_cn.speak_text_async("正確，點擊下一步繼續").get()
                            break
                        else:
                            # Incorrect recognition
                            if attempt < max_attempts:
                                # Synthesize "Wrong, please try again" in Chinese
                                print("Wrong, please try again.")
                                synthesis_result = speech_synthesizer_cn.speak_text_async(
                                    "錯誤，請重試，圖中的東西是. Doctor").get()
                            else:
                                # Maximum attempts reached, synthesize the correct word in Chinese
                                print("Maximum attempts reached. The correct word is:", word)
                                # Synthesize the correct word in Chinese and then in English
                                synthesis_result = speech_synthesizer_cn.speak_text_async("正确单词是").get()
                                synthesis_result = speech_synthesizer_en.speak_text_async(word).get()
                                break

                    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
                        print("No speech could be recognized. Please try again.")
                        # Speak "say what you see loud" in Chinese
                        synthesis_result = speech_synthesizer_cn.speak_text_async(
                            "用英語再試一次。大聲說出你所看到的").get()
                    else:
                        print("Speech recognition canceled: {}".format(
                            speech_recognition_result.cancellation_details.reason))

        # Sample vocabulary
        vocabulary = ["Doctor", ]
        tts_prompt_vocabulary(vocabulary)
        
class PageFourteen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background="#FFFFFF")  # Set background color to white
        self.controller = controller
        
        style = ttk.Style()
        style.theme_use("default")

        style.configure("TButton",
                        foreground="#000000",
                        background="#76c6cc",
                        width = 25,
                        font=("Comic Sans MS",20),
                        padding=[10,10,10,10])

        # Button to navigate to the next page
        button_next = ttk.Button(self, text="Finish 結束",style = 'TButton',
                                command=lambda: controller.show_frame(PageOne))
        button_next.pack()
        button_next.place(x=950, y=700, width=200, height=50)

        
        # Button to navigate to the next page
        button_next = ttk.Button(self, text="Back 後退",style = 'TButton',
                                command=lambda: controller.show_frame(PageThirteen))
        button_next.pack()
        button_next.place(x=10, y=700, width=200, height=50)
        
        # Run Code Button
        button_run_code = ttk.Button(self,
                                    command=self.run_code2)
        image = tk.PhotoImage(file="mc.png")  # Specify the path to your image file
        button_run_code.config(image=image)
        button_run_code.image = image  # Keep a reference to avoid garbage collection
        button_run_code.pack()
        button_run_code.place(x=950, y=100,width=250, height=250)
        
        label = ttk.Label(self, text="Bus", font=("Comic Sans MS", 25),background="#FFFFFF")
        label.pack(pady=10)

        # Load image
        self.image = Image.open("bus.jpg")  # Replace "your_image.jpg" with the path to your image
        self.image = self.image.resize((450, 430), Image.NEAREST)  # Resize the image without ANTIALIAS
        self.photo = ImageTk.PhotoImage(self.image)

        # Display image
        self.image_label = ttk.Label(self, image=self.photo)
        self.image_label.pack()

    def run_code2(self):
        def tts_prompt_vocabulary(vocabulary):
            # Define and assign the Speech API key and region
            speech_key = "51ea1f1487cb413eb0ed452817ed6ef7"
            speech_region = "japaneast"

            # Speech Config for English
            speech_config_en = speechsdk.SpeechConfig(subscription=speech_key, region=speech_region)
            speech_config_en.speech_synthesis_voice_name = 'zh-CN-XiaoxiaoNeural'

            # Speech Config for Chinese
            speech_config_cn = speechsdk.SpeechConfig(subscription=speech_key, region=speech_region)
            speech_config_cn.speech_synthesis_voice_name = 'zh-CN-XiaoxiaoNeural'  # Chinese voice

            # Initialize SpeechSynthesizer
            audio_config_synthesis = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
            speech_synthesizer_en = speechsdk.SpeechSynthesizer(speech_config=speech_config_en,
                                                                audio_config=audio_config_synthesis)
            speech_synthesizer_cn = speechsdk.SpeechSynthesizer(speech_config=speech_config_cn,
                                                                audio_config=audio_config_synthesis)

            for word in vocabulary:
                print("\nReading word:", word)

                # Synthesize and play the speech for word
                synthesis_result = speech_synthesizer_en.speak_text_async("跟著我重複一遍: " + word).get()

                if synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
                    print("Reading word [{}]".format(word))
                elif synthesis_result.reason == speechsdk.ResultReason.Canceled:
                    cancellation_details = synthesis_result.cancellation_details
                    print("Speech synthesis canceled: {}".format(cancellation_details.reason))
                    if cancellation_details.reason == speechsdk.CancellationReason.Error:
                        if cancellation_details.error_details:
                            print("Error details: {}".format(cancellation_details.error_details))
                            print("Check if the speech resource key and region values are correctly set.")

                # Record student's speech and recognize
                max_attempts = 3
                for attempt in range(1, max_attempts + 1):
                    print("\nAttempt", attempt)
                    print("Please read the word aloud:")

                    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config_en,
                                                                   audio_config=speechsdk.audio.AudioConfig(
                                                                       use_default_microphone=True))
                    speech_recognition_result = speech_recognizer.recognize_once_async().get()

                    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
                        spoken_text = speech_recognition_result.text.strip().rstrip('.')
                        print("Recognized: {}".format(spoken_text))

                        # Provide feedback
                        if spoken_text.lower() == word.lower():
                            # Correct recognition
                            print("Correct!")
                            # Synthesize "Correct" in Chinese
                            synthesis_result = speech_synthesizer_cn.speak_text_async("正確，點擊下一步繼續").get()
                            break
                        else:
                            # Incorrect recognition
                            if attempt < max_attempts:
                                # Synthesize "Wrong, please try again" in Chinese
                                print("Wrong, please try again.")
                                synthesis_result = speech_synthesizer_cn.speak_text_async(
                                    "錯誤，請重試，圖中的東西是.bus").get()
                            else:
                                # Maximum attempts reached, synthesize the correct word in Chinese
                                print("Maximum attempts reached. The correct word is:", word)
                                # Synthesize the correct word in Chinese and then in English
                                synthesis_result = speech_synthesizer_cn.speak_text_async("正确单词是").get()
                                synthesis_result = speech_synthesizer_en.speak_text_async(word).get()
                                break

                    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
                        print("No speech could be recognized. Please try again.")
                        # Speak "say what you see loud" in Chinese
                        synthesis_result = speech_synthesizer_cn.speak_text_async(
                            "用英語再試一次。大聲說出你所看到的").get()
                    else:
                        print("Speech recognition canceled: {}".format(
                            speech_recognition_result.cancellation_details.reason))

        # Sample vocabulary
        vocabulary = ["Bus", ]
        tts_prompt_vocabulary(vocabulary)
       

class Page15(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background="#FFFFFF")  # Set background color to white
        self.controller = controller
        
        style = ttk.Style()
        style.theme_use("default")

        style.configure("TButton",
                        foreground="#000000",
                        background="#76c6cc",
                        width = 25,
                        font=("Comic Sans MS",20),
                        padding=[10,10,10,10])

        # Button to navigate to the next page
        button_next = ttk.Button(self, text="Next 下一個",style = 'TButton',
                                command=lambda: controller.show_frame(Page16))
        button_next.pack()
        button_next.place(x=950, y=700, width=200, height=50)

        # Button to navigate to the next page
        button_next = ttk.Button(self, text="Back 後退",style = 'TButton',
                                command=lambda: controller.show_frame(PageOne))
        button_next.pack()
        button_next.place(x=10, y=700, width=200, height=50)
        
        button_next = ttk.Button(self, text="Home Page 主页",
                                style = 'TButton',  
                                command=lambda: controller.show_frame(PageOne))
        button_next.pack()
        button_next.place(x=10, y=10, width=200, height=50)

        # Run Code Button
        button_run_code = ttk.Button(self,
                                    command=self.run_code2)
        image = tk.PhotoImage(file="mc.png")  # Specify the path to your image file
        button_run_code.config(image=image)
        button_run_code.image = image  # Keep a reference to avoid garbage collection
        button_run_code.pack()
        button_run_code.place(x=950, y=100,width=250, height=250)
        
        label = ttk.Label(self, text="Wake up", font=("Comic Sans MS", 25),background="#FFFFFF")
        label.pack(pady=10)

        # Load image
        self.image = Image.open("wakeUp.png")  # Replace "your_image.jpg" with the path to your image
        self.image = self.image.resize((450, 430), Image.NEAREST)  # Resize the image without ANTIALIAS
        self.photo = ImageTk.PhotoImage(self.image)

        # Display image
        self.image_label = ttk.Label(self, image=self.photo)
        self.image_label.pack()

    def run_code2(self):
      
        def tts_prompt_vocabulary(vocabulary):
            # Define and assign the Speech API key and region
            speech_key = "51ea1f1487cb413eb0ed452817ed6ef7"
            speech_region = "japaneast"

            # Speech Config for English
            speech_config_en = speechsdk.SpeechConfig(subscription=speech_key, region=speech_region)
            speech_config_en.speech_synthesis_voice_name = 'zh-CN-XiaoxiaoNeural'

            # Speech Config for Chinese
            speech_config_cn = speechsdk.SpeechConfig(subscription=speech_key, region=speech_region)
            speech_config_cn.speech_synthesis_voice_name = 'zh-CN-XiaoxiaoNeural'  # Chinese voice

            # Initialize SpeechSynthesizer
            audio_config_synthesis = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
            speech_synthesizer_en = speechsdk.SpeechSynthesizer(speech_config=speech_config_en,
                                                                audio_config=audio_config_synthesis)
            speech_synthesizer_cn = speechsdk.SpeechSynthesizer(speech_config=speech_config_cn,
                                                                audio_config=audio_config_synthesis)

            for word in vocabulary:
                print("\nReading word:", word)

                # Synthesize and play the speech for word
                synthesis_result = speech_synthesizer_en.speak_text_async("跟著我重複一遍: " + word).get()

                if synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
                    print("Reading word [{}]".format(word))
                elif synthesis_result.reason == speechsdk.ResultReason.Canceled:
                    cancellation_details = synthesis_result.cancellation_details
                    print("Speech synthesis canceled: {}".format(cancellation_details.reason))
                    if cancellation_details.reason == speechsdk.CancellationReason.Error:
                        if cancellation_details.error_details:
                            print("Error details: {}".format(cancellation_details.error_details))
                            print("Check if the speech resource key and region values are correctly set.")

                # Record student's speech and recognize
                max_attempts = 3
                for attempt in range(1, max_attempts + 1):
                    print("\nAttempt", attempt)
                    print("Please read the word aloud:")

                    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config_en,
                                                                   audio_config=speechsdk.audio.AudioConfig(
                                                                       use_default_microphone=True))
                    speech_recognition_result = speech_recognizer.recognize_once_async().get()

                    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
                        spoken_text = speech_recognition_result.text.strip().rstrip('.')
                        print("Recognized: {}".format(spoken_text))

                        # Provide feedback
                        if spoken_text.lower() == word.lower():
                            # Correct recognition
                            print("Correct!")
                            # Synthesize "Correct" in Chinese
                            synthesis_result = speech_synthesizer_cn.speak_text_async("正確，點擊下一步繼續").get()
                            break
                        else:
                            # Incorrect recognition
                            if attempt < max_attempts:
                                # Synthesize "Wrong, please try again" in Chinese
                                print("Wrong, please try again.")
                                synthesis_result = speech_synthesizer_cn.speak_text_async(
                                    "錯誤，請重試，圖中的東西是. Wake up").get()
                            else:
                                # Maximum attempts reached, synthesize the correct word in Chinese
                                print("Maximum attempts reached. The correct word is:", word)
                                # Synthesize the correct word in Chinese and then in English
                                synthesis_result = speech_synthesizer_cn.speak_text_async("正确单词是").get()
                                synthesis_result = speech_synthesizer_en.speak_text_async(word).get()
                                break

                    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
                        print("No speech could be recognized. Please try again.")
                        # Speak "say what you see loud" in Chinese
                        synthesis_result = speech_synthesizer_cn.speak_text_async(
                            "用英語再試一次。大聲說出你所看到的").get()
                    else:
                        print("Speech recognition canceled: {}".format(
                            speech_recognition_result.cancellation_details.reason))

        # Sample vocabulary
        vocabulary = ["Wake up", ]
        tts_prompt_vocabulary(vocabulary)

class Page16(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background="#FFFFFF")  # Set background color to white
        self.controller = controller
        
        style = ttk.Style()
        style.theme_use("default")

        style.configure("TButton",
                        foreground="#000000",
                        background="#76c6cc",
                        width = 25,
                        font=("Comic Sans MS",20),
                        padding=[10,10,10,10])


        # Button to navigate to the next page
        button_next = ttk.Button(self, text="Next 下一個", style = 'TButton',
                                command=lambda: controller.show_frame(Page17))
        button_next.pack()
        button_next.place(x=950, y=700, width=200, height=50)

        # Button to navigate to the next page
        button_next = ttk.Button(self, text="Back 後退",style = 'TButton',
                                command=lambda: controller.show_frame(Page15))
        button_next.pack()
        button_next.place(x=10, y=700, width=200, height=50)

        button_next = ttk.Button(self, text="Home Page 主页",
                                style = 'TButton',  
                                command=lambda: controller.show_frame(PageOne))
        button_next.pack()
        button_next.place(x=10, y=10, width=200, height=50)

        # Run Code Button
        button_run_code = ttk.Button(self, 
                                    command=self.run_code2)
        image = tk.PhotoImage(file="mc.png")  # Specify the path to your image file
        button_run_code.config(image=image)
        button_run_code.image = image  # Keep a reference to avoid garbage collection
        button_run_code.pack()
        button_run_code.place(x=950, y=100, width=250, height=250)
        
        label = ttk.Label(self, text="Take a shower", font=("Comic Sans MS", 25),background="#FFFFFF")
        label.pack(pady=10)

        # Load image
        self.image = Image.open("takeShower.png")  # Replace "your_image.jpg" with the path to your image
        self.image = self.image.resize((450, 430), Image.NEAREST)  # Resize the image without ANTIALIAS
        self.photo = ImageTk.PhotoImage(self.image)

        # Display image
        self.image_label = ttk.Label(self, image=self.photo)
        self.image_label.pack()

    def run_code2(self):
        import azure.cognitiveservices.speech as speechsdk

        def tts_prompt_vocabulary(vocabulary):
            # Define and assign the Speech API key and region
            speech_key = "51ea1f1487cb413eb0ed452817ed6ef7"
            speech_region = "japaneast"

            # Speech Config for English
            speech_config_en = speechsdk.SpeechConfig(subscription=speech_key, region=speech_region)
            speech_config_en.speech_synthesis_voice_name = 'zh-CN-XiaoxiaoNeural'

            # Speech Config for Chinese
            speech_config_cn = speechsdk.SpeechConfig(subscription=speech_key, region=speech_region)
            speech_config_cn.speech_synthesis_voice_name = 'zh-CN-XiaoxiaoNeural'  # Chinese voice

            # Initialize SpeechSynthesizer
            audio_config_synthesis = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
            speech_synthesizer_en = speechsdk.SpeechSynthesizer(speech_config=speech_config_en,
                                                                audio_config=audio_config_synthesis)
            speech_synthesizer_cn = speechsdk.SpeechSynthesizer(speech_config=speech_config_cn,
                                                                audio_config=audio_config_synthesis)

            for word in vocabulary:
                print("\nReading word:", word)

                # Synthesize and play the speech for word
                synthesis_result = speech_synthesizer_en.speak_text_async("跟著我重複一遍: " + word).get()
                if synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
                    print("Reading word [{}]".format(word))
                elif synthesis_result.reason == speechsdk.ResultReason.Canceled:
                    cancellation_details = synthesis_result.cancellation_details
                    print("Speech synthesis canceled: {}".format(cancellation_details.reason))
                    if cancellation_details.reason == speechsdk.CancellationReason.Error:
                        if cancellation_details.error_details:
                            print("Error details: {}".format(cancellation_details.error_details))
                            print("Check if the speech resource key and region values are correctly set.")

                # Record student's speech and recognize
                max_attempts = 3
                for attempt in range(1, max_attempts + 1):
                    print("\nAttempt", attempt)
                    print("Please read the word aloud:")

                    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config_en,
                                                                   audio_config=speechsdk.audio.AudioConfig(
                                                                       use_default_microphone=True))
                    speech_recognition_result = speech_recognizer.recognize_once_async().get()

                    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
                        spoken_text = speech_recognition_result.text.strip().rstrip('.')
                        print("Recognized: {}".format(spoken_text))

                        # Provide feedback
                        if spoken_text.lower() == word.lower():
                            # Correct recognition
                            print("Correct!")
                            # Synthesize "Correct" in Chinese
                            synthesis_result = speech_synthesizer_cn.speak_text_async("正確，點擊下一步繼續").get()
                            break
                        else:
                            # Incorrect recognition
                            if attempt < max_attempts:
                                # Synthesize "Wrong, please try again" in Chinese
                                print("Wrong, please try again.")
                                synthesis_result = speech_synthesizer_cn.speak_text_async(
                                    "錯誤，請重試，圖中的東西是. Take a shower").get()
                            else:
                                # Maximum attempts reached, synthesize the correct word in Chinese
                                print("Maximum attempts reached. The correct word is:", word)
                                # Synthesize the correct word in Chinese and then in English
                                synthesis_result = speech_synthesizer_cn.speak_text_async("正确单词是").get()
                                synthesis_result = speech_synthesizer_en.speak_text_async(word).get()
                                break

                    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
                        print("No speech could be recognized. Please try again.")
                        # Speak "say what you see loud" in Chinese
                        synthesis_result = speech_synthesizer_cn.speak_text_async(
                            "用英語再試一次。大聲說出你所看到的").get()
                    else:
                        print("Speech recognition canceled: {}".format(
                            speech_recognition_result.cancellation_details.reason))

        # Sample vocabulary
        vocabulary = ["Take a shower", ]
        tts_prompt_vocabulary(vocabulary)


class Page17(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background="#FFFFFF")  # Set background color to white
        self.controller = controller
        
        style = ttk.Style()
        style.theme_use("default")

        style.configure("TButton",
                        foreground="#000000",
                        background="#76c6cc",
                        width = 25,
                        font=("Comic Sans MS",20),
                        padding=[10,10,10,10])


        # Button to navigate to the next page
        button_next = ttk.Button(self, text="Next 下一個", style = 'TButton',
                                command=lambda: controller.show_frame(Page18))
        button_next.place(x=950, y=700, width=200, height=50)

        # Button to navigate to the next page
        button_next = ttk.Button(self, text="Back 後退",style = 'TButton',
                                command=lambda: controller.show_frame(Page16))
        button_next.pack()
        button_next.place(x=10, y=700, width=200, height=50)

        button_next = ttk.Button(self, text="Home Page 主页",
                                style = 'TButton',  
                                command=lambda: controller.show_frame(PageOne))
        button_next.pack()
        button_next.place(x=10, y=10, width=200, height=50)
        
        label = ttk.Label(self, text="Get dressed", font=("Comic Sans MS", 25),background="#FFFFFF")
        label.pack(pady=10)

        # Run Code Button
        button_run_code = ttk.Button(self,
                                    command=self.run_code2)
        image = tk.PhotoImage(file="mc.png")  # Specify the path to your image file
        button_run_code.config(image=image)
        button_run_code.image = image  # Keep a reference to avoid garbage collection
        button_run_code.pack()
        button_run_code.place(x=950, y=100, width=250, height=250)

        # Load image
        self.image = Image.open("dress.jpg")  # Replace "your_image.jpg" with the path to your image
        self.image = self.image.resize((450, 430), Image.NEAREST)  # Resize the image without ANTIALIAS
        self.photo = ImageTk.PhotoImage(self.image)

        # Display image
        self.image_label = ttk.Label(self, image=self.photo)
        self.image_label.pack()

    def run_code2(self):
        import azure.cognitiveservices.speech as speechsdk

        def tts_prompt_vocabulary(vocabulary):
            # Define and assign the Speech API key and region
            speech_key = "51ea1f1487cb413eb0ed452817ed6ef7"
            speech_region = "japaneast"

            # Speech Config for English
            speech_config_en = speechsdk.SpeechConfig(subscription=speech_key, region=speech_region)
            speech_config_en.speech_synthesis_voice_name = 'zh-CN-XiaoxiaoNeural'

            # Speech Config for Chinese
            speech_config_cn = speechsdk.SpeechConfig(subscription=speech_key, region=speech_region)
            speech_config_cn.speech_synthesis_voice_name = 'zh-CN-XiaoxiaoNeural'  # Chinese voice

            # Initialize SpeechSynthesizer
            audio_config_synthesis = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
            speech_synthesizer_en = speechsdk.SpeechSynthesizer(speech_config=speech_config_en,
                                                                audio_config=audio_config_synthesis)
            speech_synthesizer_cn = speechsdk.SpeechSynthesizer(speech_config=speech_config_cn,
                                                                audio_config=audio_config_synthesis)

            for word in vocabulary:
                print("\nReading word:", word)

                # Synthesize and play the speech for word
                synthesis_result = speech_synthesizer_en.speak_text_async("跟著我重複一遍: " + word).get()

                if synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
                    print("Reading word [{}]".format(word))
                elif synthesis_result.reason == speechsdk.ResultReason.Canceled:
                    cancellation_details = synthesis_result.cancellation_details
                    print("Speech synthesis canceled: {}".format(cancellation_details.reason))
                    if cancellation_details.reason == speechsdk.CancellationReason.Error:
                        if cancellation_details.error_details:
                            print("Error details: {}".format(cancellation_details.error_details))
                            print("Check if the speech resource key and region values are correctly set.")

                # Record student's speech and recognize
                max_attempts = 3
                for attempt in range(1, max_attempts + 1):
                    print("\nAttempt", attempt)
                    print("Please read the word aloud:")

                    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config_en,
                                                                   audio_config=speechsdk.audio.AudioConfig(
                                                                       use_default_microphone=True))
                    speech_recognition_result = speech_recognizer.recognize_once_async().get()

                    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
                        spoken_text = speech_recognition_result.text.strip().rstrip('.')
                        print("Recognized: {}".format(spoken_text))

                        # Provide feedback
                        if spoken_text.lower() == word.lower():
                            # Correct recognition
                            print("Correct!")
                            # Synthesize "Correct" in Chinese
                            synthesis_result = speech_synthesizer_cn.speak_text_async("正確，點擊下一步繼續").get()
                            break
                        else:
                            # Incorrect recognition
                            if attempt < max_attempts:
                                # Synthesize "Wrong, please try again" in Chinese
                                print("Wrong, please try again.")
                                synthesis_result = speech_synthesizer_cn.speak_text_async(
                                    "錯誤，請重試，圖中的東西是. Get Dressed").get()
                            else:
                                # Maximum attempts reached, synthesize the correct word in Chinese
                                print("Maximum attempts reached. The correct word is:", word)
                                # Synthesize the correct word in Chinese and then in English
                                synthesis_result = speech_synthesizer_cn.speak_text_async("正确单词是").get()
                                synthesis_result = speech_synthesizer_en.speak_text_async(word).get()
                                break

                    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
                        print("No speech could be recognized. Please try again.")
                        # Speak "say what you see loud" in Chinese
                        synthesis_result = speech_synthesizer_cn.speak_text_async(
                            "用英語再試一次。大聲說出你所看到的").get()
                    else:
                        print("Speech recognition canceled: {}".format(
                            speech_recognition_result.cancellation_details.reason))

        # Sample vocabulary
        vocabulary = ["Get Dressed", ]
        tts_prompt_vocabulary(vocabulary)
class Page18(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background="#FFFFFF")  # Set background color to white
        self.controller = controller
        
        style = ttk.Style()
        style.theme_use("default")

        style.configure("TButton",
                        foreground="#000000",
                        background="#76c6cc",
                        width = 25,
                        font=("Comic Sans MS",20),
                        padding=[10,10,10,10])


        # Button to navigate to the next page
        button_next = ttk.Button(self, text="Next 下一個", style = 'TButton',
                                command=lambda: controller.show_frame(Page19))
        button_next.place(x=950, y=700, width=200, height=50)

        # Button to navigate to the next page
        button_next = ttk.Button(self, text="Back 後退",style = 'TButton',
                                command=lambda: controller.show_frame(Page17))
        button_next.pack()
        button_next.place(x=10, y=700, width=200, height=50)

        button_next = ttk.Button(self, text="Home Page 主页",
                                style = 'TButton',  
                                command=lambda: controller.show_frame(PageOne))
        button_next.pack()
        button_next.place(x=10, y=10, width=200, height=50)
        
        label = ttk.Label(self, text="Eat breakfast", font=("Comic Sans MS", 25),background="#FFFFFF")
        label.pack(pady=10)


        # Run Code Button
        button_run_code = ttk.Button(self,
                                    command=self.run_code2)
        image = tk.PhotoImage(file="mc.png")  # Specify the path to your image file
        button_run_code.config(image=image)
        button_run_code.image = image  # Keep a reference to avoid garbage collection
        button_run_code.pack()
        button_run_code.place(x=950, y=100, width=250, height=250)

        # Load image
        self.image = Image.open("haveBreakfast.png")  # Replace "your_image.jpg" with the path to your image
        self.image = self.image.resize((450, 430), Image.NEAREST)  # Resize the image without ANTIALIAS
        self.photo = ImageTk.PhotoImage(self.image)

        # Display image
        self.image_label = ttk.Label(self, image=self.photo)
        self.image_label.pack()

    def run_code2(self):
        import azure.cognitiveservices.speech as speechsdk

        def tts_prompt_vocabulary(vocabulary):
            # Define and assign the Speech API key and region
            speech_key = "51ea1f1487cb413eb0ed452817ed6ef7"
            speech_region = "japaneast"

            # Speech Config for English
            speech_config_en = speechsdk.SpeechConfig(subscription=speech_key, region=speech_region)
            speech_config_en.speech_synthesis_voice_name = 'zh-CN-XiaoxiaoNeural'

            # Speech Config for Chinese
            speech_config_cn = speechsdk.SpeechConfig(subscription=speech_key, region=speech_region)
            speech_config_cn.speech_synthesis_voice_name = 'zh-CN-XiaoxiaoNeural'  # Chinese voice

            # Initialize SpeechSynthesizer
            audio_config_synthesis = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
            speech_synthesizer_en = speechsdk.SpeechSynthesizer(speech_config=speech_config_en,
                                                                audio_config=audio_config_synthesis)
            speech_synthesizer_cn = speechsdk.SpeechSynthesizer(speech_config=speech_config_cn,
                                                                audio_config=audio_config_synthesis)

            for word in vocabulary:
                print("\nReading word:", word)

                # Synthesize and play the speech for word
                synthesis_result = speech_synthesizer_en.speak_text_async("跟著我重複一遍: " + word).get()

                if synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
                    print("Reading word [{}]".format(word))
                elif synthesis_result.reason == speechsdk.ResultReason.Canceled:
                    cancellation_details = synthesis_result.cancellation_details
                    print("Speech synthesis canceled: {}".format(cancellation_details.reason))
                    if cancellation_details.reason == speechsdk.CancellationReason.Error:
                        if cancellation_details.error_details:
                            print("Error details: {}".format(cancellation_details.error_details))
                            print("Check if the speech resource key and region values are correctly set.")

                # Record student's speech and recognize
                max_attempts = 3
                for attempt in range(1, max_attempts + 1):
                    print("\nAttempt", attempt)
                    print("Please read the word aloud:")

                    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config_en,
                                                                   audio_config=speechsdk.audio.AudioConfig(
                                                                       use_default_microphone=True))
                    speech_recognition_result = speech_recognizer.recognize_once_async().get()

                    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
                        spoken_text = speech_recognition_result.text.strip().rstrip('.')
                        print("Recognized: {}".format(spoken_text))

                        # Provide feedback
                        if spoken_text.lower() == word.lower():
                            # Correct recognition
                            print("Correct!")
                            # Synthesize "Correct" in Chinese
                            synthesis_result = speech_synthesizer_cn.speak_text_async("正確，點擊下一步繼續").get()
                            break
                        else:
                            # Incorrect recognition
                            if attempt < max_attempts:
                                # Synthesize "Wrong, please try again" in Chinese
                                print("Wrong, please try again.")
                                synthesis_result = speech_synthesizer_cn.speak_text_async(
                                    "錯誤，請重試，圖中的東西是. Eat Breakfast").get()
                            else:
                                # Maximum attempts reached, synthesize the correct word in Chinese
                                print("Maximum attempts reached. The correct word is:", word)
                                # Synthesize the correct word in Chinese and then in English
                                synthesis_result = speech_synthesizer_cn.speak_text_async("正确单词是").get()
                                synthesis_result = speech_synthesizer_en.speak_text_async(word).get()
                                break

                    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
                        print("No speech could be recognized. Please try again.")
                        # Speak "say what you see loud" in Chinese
                        synthesis_result = speech_synthesizer_cn.speak_text_async(
                            "用英語再試一次。大聲說出你所看到的").get()
                    else:
                        print("Speech recognition canceled: {}".format(
                            speech_recognition_result.cancellation_details.reason))

        # Sample vocabulary
        vocabulary = ["Eat Breakfast", ]
        tts_prompt_vocabulary(vocabulary)

class Page19(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background="#FFFFFF")  # Set background color to white
        self.controller = controller
        
        style = ttk.Style()
        style.theme_use("default")

        style.configure("TButton",
                        foreground="#000000",
                        background="#76c6cc",
                        width = 25,
                        font=("Comic Sans MS",20),
                        padding=[10,10,10,10])
        # Button to navigate to the next page
        button_next = ttk.Button(self, text="Next 下一個", style = 'TButton',
                                command=lambda: controller.show_frame(Page20))
        button_next.place(x=950, y=700, width=200, height=50)

        # Button to navigate to the next page
        button_next = ttk.Button(self, text="Back 後退",style = 'TButton',
                                command=lambda: controller.show_frame(Page18))
        button_next.pack()
        button_next.place(x=10, y=700, width=200, height=50)

        button_next = ttk.Button(self, text="Home Page 主页",
                                style = 'TButton',  
                                command=lambda: controller.show_frame(PageOne))
        button_next.pack()
        button_next.place(x=10, y=10, width=200, height=50)
        
        label = ttk.Label(self, text="Brush my teeth", font=("Comic Sans MS", 25),background="#FFFFFF")
        label.pack(pady=10)


        # Run Code Button
        button_run_code = ttk.Button(self,
                                    command=self.run_code2)
        image = tk.PhotoImage(file="mc.png")  # Specify the path to your image file
        button_run_code.config(image=image)
        button_run_code.image = image  # Keep a reference to avoid garbage collection
        button_run_code.pack()
        button_run_code.place(x=950, y=100, width=250, height=250)

        # Load image
        self.image = Image.open("brushTeeth.png")  # Replace "your_image.jpg" with the path to your image
        self.image = self.image.resize((450, 430), Image.NEAREST)  # Resize the image without ANTIALIAS
        self.photo = ImageTk.PhotoImage(self.image)

        # Display image
        self.image_label = ttk.Label(self, image=self.photo)
        self.image_label.pack()

    def run_code2(self):
        import azure.cognitiveservices.speech as speechsdk

        def tts_prompt_vocabulary(vocabulary):
            # Define and assign the Speech API key and region
            speech_key = "51ea1f1487cb413eb0ed452817ed6ef7"
            speech_region = "japaneast"

            # Speech Config for English
            speech_config_en = speechsdk.SpeechConfig(subscription=speech_key, region=speech_region)
            speech_config_en.speech_synthesis_voice_name = 'zh-CN-XiaoxiaoNeural'

            # Speech Config for Chinese
            speech_config_cn = speechsdk.SpeechConfig(subscription=speech_key, region=speech_region)
            speech_config_cn.speech_synthesis_voice_name = 'zh-CN-XiaoxiaoNeural'  # Chinese voice

            # Initialize SpeechSynthesizer
            audio_config_synthesis = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
            speech_synthesizer_en = speechsdk.SpeechSynthesizer(speech_config=speech_config_en,
                                                                audio_config=audio_config_synthesis)
            speech_synthesizer_cn = speechsdk.SpeechSynthesizer(speech_config=speech_config_cn,
                                                                audio_config=audio_config_synthesis)

            for word in vocabulary:
                print("\nReading word:", word)

                # Synthesize and play the speech for word
                synthesis_result = speech_synthesizer_en.speak_text_async("跟著我重複一遍: " + word).get()

                if synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
                    print("Reading word [{}]".format(word))
                elif synthesis_result.reason == speechsdk.ResultReason.Canceled:
                    cancellation_details = synthesis_result.cancellation_details
                    print("Speech synthesis canceled: {}".format(cancellation_details.reason))
                    if cancellation_details.reason == speechsdk.CancellationReason.Error:
                        if cancellation_details.error_details:
                            print("Error details: {}".format(cancellation_details.error_details))
                            print("Check if the speech resource key and region values are correctly set.")

                # Record student's speech and recognize
                max_attempts = 3
                for attempt in range(1, max_attempts + 1):
                    print("\nAttempt", attempt)
                    print("Please read the word aloud:")

                    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config_en,
                                                                   audio_config=speechsdk.audio.AudioConfig(
                                                                       use_default_microphone=True))
                    speech_recognition_result = speech_recognizer.recognize_once_async().get()

                    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
                        spoken_text = speech_recognition_result.text.strip().rstrip('.')
                        print("Recognized: {}".format(spoken_text))

                        # Provide feedback
                        if spoken_text.lower() == word.lower():
                            # Correct recognition
                            print("Correct!")
                            # Synthesize "Correct" in Chinese
                            synthesis_result = speech_synthesizer_cn.speak_text_async("正確，點擊下一步繼續").get()
                            break
                        else:
                            # Incorrect recognition
                            if attempt < max_attempts:
                                # Synthesize "Wrong, please try again" in Chinese
                                print("Wrong, please try again.")
                                synthesis_result = speech_synthesizer_cn.speak_text_async(
                                    "錯誤，請重試，圖中的東西是. Brush My Teeth").get()
                            else:
                                # Maximum attempts reached, synthesize the correct word in Chinese
                                print("Maximum attempts reached. The correct word is:", word)
                                # Synthesize the correct word in Chinese and then in English
                                synthesis_result = speech_synthesizer_cn.speak_text_async("正确单词是").get()
                                synthesis_result = speech_synthesizer_en.speak_text_async(word).get()
                                break

                    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
                        print("No speech could be recognized. Please try again.")
                        # Speak "say what you see loud" in Chinese
                        synthesis_result = speech_synthesizer_cn.speak_text_async(
                            "用英語再試一次。大聲說出你所看到的").get()
                    else:
                        print("Speech recognition canceled: {}".format(
                            speech_recognition_result.cancellation_details.reason))

        # Sample vocabulary
        vocabulary = ["Brush My Teeth", ]
        tts_prompt_vocabulary(vocabulary)

class Page20(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background="#FFFFFF")  # Set background color to white
        self.controller = controller
        
        style = ttk.Style()
        style.theme_use("default")

        style.configure("TButton",
                        foreground="#000000",
                        background="#76c6cc",
                        width = 25,
                        font=("Comic Sans MS",20),
                        padding=[10,10,10,10])
        # Button to navigate to the next page
        button_next = ttk.Button(self, text="Next 下一個", style = 'TButton',
                                command=lambda: controller.show_frame(Page21))
        button_next.place(x=950, y=700, width=200, height=50)

        # Button to navigate to the next page
        button_next = ttk.Button(self, text="Back 後退",style = 'TButton',
                                command=lambda: controller.show_frame(Page19))
        button_next.pack()
        button_next.place(x=10, y=700, width=200, height=50)

        button_next = ttk.Button(self, text="Home Page 主页",
                                style = 'TButton',  
                                command=lambda: controller.show_frame(PageOne))
        button_next.pack()
        button_next.place(x=10, y=10, width=200, height=50)

        # Run Code Button
        button_run_code = ttk.Button(self,
                                    command=self.run_code2)
        image = tk.PhotoImage(file="mc.png")  # Specify the path to your image file
        button_run_code.config(image=image)
        button_run_code.image = image  # Keep a reference to avoid garbage collection
        button_run_code.pack()
        button_run_code.place(x=950, y=100, width=250, height=250)
        
        label = ttk.Label(self, text="Go to school", font=("Comic Sans MS", 25),background="#FFFFFF")
        label.pack(pady=10)


        # Load image
        self.image = Image.open("goToSchool.png")  # Replace "your_image.jpg" with the path to your image
        self.image = self.image.resize((450, 430), Image.NEAREST)  # Resize the image without ANTIALIAS
        self.photo = ImageTk.PhotoImage(self.image)

        # Display image
        self.image_label = ttk.Label(self, image=self.photo)
        self.image_label.pack()

    def run_code2(self):
        import azure.cognitiveservices.speech as speechsdk

        def tts_prompt_vocabulary(vocabulary):
            # Define and assign the Speech API key and region
            speech_key = "51ea1f1487cb413eb0ed452817ed6ef7"
            speech_region = "japaneast"

            # Speech Config for English
            speech_config_en = speechsdk.SpeechConfig(subscription=speech_key, region=speech_region)
            speech_config_en.speech_synthesis_voice_name = 'zh-CN-XiaoxiaoNeural'

            # Speech Config for Chinese
            speech_config_cn = speechsdk.SpeechConfig(subscription=speech_key, region=speech_region)
            speech_config_cn.speech_synthesis_voice_name = 'zh-CN-XiaoxiaoNeural'  # Chinese voice

            # Initialize SpeechSynthesizer
            audio_config_synthesis = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
            speech_synthesizer_en = speechsdk.SpeechSynthesizer(speech_config=speech_config_en,
                                                                audio_config=audio_config_synthesis)
            speech_synthesizer_cn = speechsdk.SpeechSynthesizer(speech_config=speech_config_cn,
                                                                audio_config=audio_config_synthesis)

            for word in vocabulary:
                print("\nReading word:", word)

                # Synthesize and play the speech for word
                synthesis_result = speech_synthesizer_en.speak_text_async("跟著我重複一遍: " + word).get()

                if synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
                    print("Reading word [{}]".format(word))
                elif synthesis_result.reason == speechsdk.ResultReason.Canceled:
                    cancellation_details = synthesis_result.cancellation_details
                    print("Speech synthesis canceled: {}".format(cancellation_details.reason))
                    if cancellation_details.reason == speechsdk.CancellationReason.Error:
                        if cancellation_details.error_details:
                            print("Error details: {}".format(cancellation_details.error_details))
                            print("Check if the speech resource key and region values are correctly set.")

                # Record student's speech and recognize
                max_attempts = 3
                for attempt in range(1, max_attempts + 1):
                    print("\nAttempt", attempt)
                    print("Please read the word aloud:")

                    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config_en,
                                                                   audio_config=speechsdk.audio.AudioConfig(
                                                                       use_default_microphone=True))
                    speech_recognition_result = speech_recognizer.recognize_once_async().get()

                    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
                        spoken_text = speech_recognition_result.text.strip().rstrip('.')
                        print("Recognized: {}".format(spoken_text))

                        # Provide feedback
                        if spoken_text.lower() == word.lower():
                            # Correct recognition
                            print("Correct!")
                            # Synthesize "Correct" in Chinese
                            synthesis_result = speech_synthesizer_cn.speak_text_async("正確，點擊下一步繼續").get()
                            break
                        else:
                            # Incorrect recognition
                            if attempt < max_attempts:
                                # Synthesize "Wrong, please try again" in Chinese
                                print("Wrong, please try again.")
                                synthesis_result = speech_synthesizer_cn.speak_text_async(
                                    "錯誤，請重試，圖中的東西是. Go To School").get()
                            else:
                                # Maximum attempts reached, synthesize the correct word in Chinese
                                print("Maximum attempts reached. The correct word is:", word)
                                # Synthesize the correct word in Chinese and then in English
                                synthesis_result = speech_synthesizer_cn.speak_text_async("正确单词是").get()
                                synthesis_result = speech_synthesizer_en.speak_text_async(word).get()
                                break

                    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
                        print("No speech could be recognized. Please try again.")
                        # Speak "say what you see loud" in Chinese
                        synthesis_result = speech_synthesizer_cn.speak_text_async(
                            "用英語再試一次。大聲說出你所看到的").get()
                    else:
                        print("Speech recognition canceled: {}".format(
                            speech_recognition_result.cancellation_details.reason))

        # Sample vocabulary
        vocabulary = ["Go To School", ]
        tts_prompt_vocabulary(vocabulary)

class Page21(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background="#FFFFFF")  # Set background color to white
        self.controller = controller
        
        style = ttk.Style()
        style.theme_use("default")

        style.configure("TButton",
                        foreground="#000000",
                        background="#76c6cc",
                        width = 25,
                        font=("Comic Sans MS",20),
                        padding=[10,10,10,10])
        # Button to navigate to the next page
        button_next = ttk.Button(self, text="Next 下一個", style = 'TButton',
                                command=lambda: controller.show_frame(Page22))
        button_next.place(x=950, y=700, width=200, height=50)

        # Button to navigate to the next page
        button_next = ttk.Button(self, text="Back 後退",style = 'TButton',
                                command=lambda: controller.show_frame(Page20))
        button_next.pack()
        button_next.place(x=10, y=700, width=200, height=50)

        button_next = ttk.Button(self, text="Home Page 主页",
                                style = 'TButton',  
                                command=lambda: controller.show_frame(PageOne))
        button_next.pack()
        button_next.place(x=10, y=10, width=200, height=50)

        # Run Code Button
        button_run_code = ttk.Button(self,
                                    command=self.run_code2)
        image = tk.PhotoImage(file="mc.png")  # Specify the path to your image file
        button_run_code.config(image=image)
        button_run_code.image = image  # Keep a reference to avoid garbage collection
        button_run_code.pack()
        button_run_code.place(x=950, y=100, width=250, height=250)
        
        label = ttk.Label(self, text="Eat lunch", font=("Comic Sans MS", 25),background="#FFFFFF")
        label.pack(pady=10)


        # Load image
        self.image = Image.open("haveLunch.png")  # Replace "your_image.jpg" with the path to your image
        self.image = self.image.resize((450, 430), Image.NEAREST)  # Resize the image without ANTIALIAS
        self.photo = ImageTk.PhotoImage(self.image)

        # Display image
        self.image_label = ttk.Label(self, image=self.photo)
        self.image_label.pack()

    def run_code2(self):
        import azure.cognitiveservices.speech as speechsdk

        def tts_prompt_vocabulary(vocabulary):
            # Define and assign the Speech API key and region
            speech_key = "51ea1f1487cb413eb0ed452817ed6ef7"
            speech_region = "japaneast"

            # Speech Config for English
            speech_config_en = speechsdk.SpeechConfig(subscription=speech_key, region=speech_region)
            speech_config_en.speech_synthesis_voice_name = 'zh-CN-XiaoxiaoNeural'

            # Speech Config for Chinese
            speech_config_cn = speechsdk.SpeechConfig(subscription=speech_key, region=speech_region)
            speech_config_cn.speech_synthesis_voice_name = 'zh-CN-XiaoxiaoNeural'  # Chinese voice

            # Initialize SpeechSynthesizer
            audio_config_synthesis = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
            speech_synthesizer_en = speechsdk.SpeechSynthesizer(speech_config=speech_config_en,
                                                                audio_config=audio_config_synthesis)
            speech_synthesizer_cn = speechsdk.SpeechSynthesizer(speech_config=speech_config_cn,
                                                                audio_config=audio_config_synthesis)

            for word in vocabulary:
                print("\nReading word:", word)

                # Synthesize and play the speech for word
                synthesis_result = speech_synthesizer_en.speak_text_async("跟著我重複一遍: " + word).get()

                if synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
                    print("Reading word [{}]".format(word))
                elif synthesis_result.reason == speechsdk.ResultReason.Canceled:
                    cancellation_details = synthesis_result.cancellation_details
                    print("Speech synthesis canceled: {}".format(cancellation_details.reason))
                    if cancellation_details.reason == speechsdk.CancellationReason.Error:
                        if cancellation_details.error_details:
                            print("Error details: {}".format(cancellation_details.error_details))
                            print("Check if the speech resource key and region values are correctly set.")

                # Record student's speech and recognize
                max_attempts = 3
                for attempt in range(1, max_attempts + 1):
                    print("\nAttempt", attempt)
                    print("Please read the word aloud:")

                    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config_en,
                                                                    audio_config=speechsdk.audio.AudioConfig(
                                                                        use_default_microphone=True))
                    speech_recognition_result = speech_recognizer.recognize_once_async().get()

                    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
                        spoken_text = speech_recognition_result.text.strip().rstrip('.')
                        print("Recognized: {}".format(spoken_text))

                        # Provide feedback
                        if spoken_text.lower() == word.lower():
                            # Correct recognition
                            print("Correct!")
                            # Synthesize "Correct" in Chinese
                            synthesis_result = speech_synthesizer_cn.speak_text_async("正確，點擊下一步繼續").get()
                            break
                        else:
                            # Incorrect recognition
                            if attempt < max_attempts:
                                # Synthesize "Wrong, please try again" in Chinese
                                print("Wrong, please try again.")
                                synthesis_result = speech_synthesizer_cn.speak_text_async(
                                    "錯誤，請重試，圖中的東西是. Eat Lunch").get()
                            else:
                                # Maximum attempts reached, synthesize the correct word in Chinese
                                print("Maximum attempts reached. The correct word is:", word)
                                # Synthesize the correct word in Chinese and then in English
                                synthesis_result = speech_synthesizer_cn.speak_text_async("正确单词是").get()
                                synthesis_result = speech_synthesizer_en.speak_text_async(word).get()
                                break

                    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
                        print("No speech could be recognized. Please try again.")
                        # Speak "say what you see loud" in Chinese
                        synthesis_result = speech_synthesizer_cn.speak_text_async(
                            "用英語再試一次。大聲說出你所看到的").get()
                    else:
                        print("Speech recognition canceled: {}".format(
                            speech_recognition_result.cancellation_details.reason))

        # Sample vocabulary
        vocabulary = ["Eat Lunch", ]
        tts_prompt_vocabulary(vocabulary)

class Page22(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background="#FFFFFF")  # Set background color to white
        self.controller = controller
        
        style = ttk.Style()
        style.theme_use("default")

        style.configure("TButton",
                        foreground="#000000",
                        background="#76c6cc",
                        width = 25,
                        font=("Comic Sans MS",20),
                        padding=[10,10,10,10])
        # Button to navigate to the next page
        button_next = ttk.Button(self, text="Next 下一個", style = 'TButton',
                                command=lambda: controller.show_frame(Page23))
        button_next.place(x=950, y=700, width=200, height=50)

        # Button to navigate to the next page
        button_next = ttk.Button(self, text="Back 後退",style = 'TButton',
                                command=lambda: controller.show_frame(Page21))
        button_next.pack()
        button_next.place(x=10, y=700, width=200, height=50)

        button_next = ttk.Button(self, text="Home Page 主页",
                                style = 'TButton',  
                                command=lambda: controller.show_frame(PageOne))
        button_next.pack()
        button_next.place(x=10, y=10, width=200, height=50)

        # Run Code Button
        button_run_code = ttk.Button(self,
                                    command=self.run_code2)
        image = tk.PhotoImage(file="mc.png")  # Specify the path to your image file
        button_run_code.config(image=image)
        button_run_code.image = image  # Keep a reference to avoid garbage collection
        button_run_code.pack()
        button_run_code.place(x=950, y=100, width=250, height=250)
        
        label = ttk.Label(self, text="Go home", font=("Comic Sans MS", 25),background="#FFFFFF")
        label.pack(pady=10)


        # Load image
        self.image = Image.open("goHome.png")  # Replace "your_image.jpg" with the path to your image
        self.image = self.image.resize((450, 430), Image.NEAREST)  # Resize the image without ANTIALIAS
        self.photo = ImageTk.PhotoImage(self.image)

        # Display image
        self.image_label = ttk.Label(self, image=self.photo)
        self.image_label.pack()

    def run_code2(self):
        import azure.cognitiveservices.speech as speechsdk

        def tts_prompt_vocabulary(vocabulary):
            # Define and assign the Speech API key and region
            speech_key = "51ea1f1487cb413eb0ed452817ed6ef7"
            speech_region = "japaneast"

            # Speech Config for English
            speech_config_en = speechsdk.SpeechConfig(subscription=speech_key, region=speech_region)
            speech_config_en.speech_synthesis_voice_name = 'zh-CN-XiaoxiaoNeural'

            # Speech Config for Chinese
            speech_config_cn = speechsdk.SpeechConfig(subscription=speech_key, region=speech_region)
            speech_config_cn.speech_synthesis_voice_name = 'zh-CN-XiaoxiaoNeural'  # Chinese voice

            # Initialize SpeechSynthesizer
            audio_config_synthesis = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
            speech_synthesizer_en = speechsdk.SpeechSynthesizer(speech_config=speech_config_en,
                                                                audio_config=audio_config_synthesis)
            speech_synthesizer_cn = speechsdk.SpeechSynthesizer(speech_config=speech_config_cn,
                                                                audio_config=audio_config_synthesis)

            for word in vocabulary:
                print("\nReading word:", word)

                # Synthesize and play the speech for word
                synthesis_result = speech_synthesizer_en.speak_text_async("跟著我重複一遍: " + word).get()

                if synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
                    print("Reading word [{}]".format(word))
                elif synthesis_result.reason == speechsdk.ResultReason.Canceled:
                    cancellation_details = synthesis_result.cancellation_details
                    print("Speech synthesis canceled: {}".format(cancellation_details.reason))
                    if cancellation_details.reason == speechsdk.CancellationReason.Error:
                        if cancellation_details.error_details:
                            print("Error details: {}".format(cancellation_details.error_details))
                            print(
                                "Check if the speech resource key and region values are correctly set.")

                # Record student's speech and recognize
                max_attempts = 3
                for attempt in range(1, max_attempts + 1):
                    print("\nAttempt", attempt)
                    print("Please read the word aloud:")

                    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config_en,
                                                                    audio_config=speechsdk.audio.AudioConfig(
                                                                        use_default_microphone=True))
                    speech_recognition_result = speech_recognizer.recognize_once_async().get()

                    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
                        spoken_text = speech_recognition_result.text.strip().rstrip('.')
                        print("Recognized: {}".format(spoken_text))

                        # Provide feedback
                        if spoken_text.lower() == word.lower():
                            # Correct recognition
                            print("Correct!")
                            # Synthesize "Correct" in Chinese
                            synthesis_result = speech_synthesizer_cn.speak_text_async("正確，點擊下一步繼續").get()
                            break
                        else:
                            # Incorrect recognition
                            if attempt < max_attempts:
                                # Synthesize "Wrong, please try again" in Chinese
                                print("Wrong, please try again.")
                                synthesis_result = speech_synthesizer_cn.speak_text_async(
                                    "錯誤，請重試，圖中的東西是. Go Home").get()
                            else:
                                # Maximum attempts reached, synthesize the correct word in Chinese
                                print("Maximum attempts reached. The correct word is:", word)
                                # Synthesize the correct word in Chinese and then in English
                                synthesis_result = speech_synthesizer_cn.speak_text_async(
                                    "正确单词是").get()
                                synthesis_result = speech_synthesizer_en.speak_text_async(word).get()
                                break

                    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
                        print("No speech could be recognized. Please try again.")
                        # Speak "say what you see loud" in Chinese
                        synthesis_result = speech_synthesizer_cn.speak_text_async(
                            "用英語再試一次。大聲說出你所看到的").get()
                    else:
                        print("Speech recognition canceled: {}".format(
                            speech_recognition_result.cancellation_details.reason))

        # Sample vocabulary
        vocabulary = ["Go Home", ]
        tts_prompt_vocabulary(vocabulary)

class Page23(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background="#FFFFFF")  # Set background color to white
        self.controller = controller
        
        style = ttk.Style()
        style.theme_use("default")

        style.configure("TButton",
                        foreground="#000000",
                        background="#76c6cc",
                        width = 25,
                        font=("Comic Sans MS",20),
                        padding=[10,10,10,10])
        # Button to navigate to the next page
        button_next = ttk.Button(self, text="Next 下一個", style = 'TButton',
                                command=lambda: controller.show_frame(Page24))
        button_next.place(x=950, y=700, width=200, height=50)

        # Button to navigate to the next page
        button_next = ttk.Button(self, text="Back 後退",style = 'TButton',
                                command=lambda: controller.show_frame(Page22))
        button_next.pack()
        button_next.place(x=10, y=700, width=200, height=50)

        button_next = ttk.Button(self, text="Home Page 主页",
                                style = 'TButton',  
                                command=lambda: controller.show_frame(PageOne))
        button_next.pack()
        button_next.place(x=10, y=10, width=200, height=50)
        
        label = ttk.Label(self, text="Eat dinner", font=("Comic Sans MS", 25),background="#FFFFFF")
        label.pack(pady=10)


        # Run Code Button
        button_run_code = ttk.Button(self,
                                    command=self.run_code2)
        image = tk.PhotoImage(file="mc.png")  # Specify the path to your image file
        button_run_code.config(image=image)
        button_run_code.image = image  # Keep a reference to avoid garbage collection
        button_run_code.pack()
        button_run_code.place(x=950, y=100, width=250, height=250)

        # Load image
        self.image = Image.open(
            "haveDineer.png")  # Replace "your_image.jpg" with the path to your image
        self.image = self.image.resize((450, 430),
                                        Image.NEAREST)  # Resize the image without ANTIALIAS
        self.photo = ImageTk.PhotoImage(self.image)

        # Display image
        self.image_label = ttk.Label(self, image=self.photo)
        self.image_label.pack()

    def run_code2(self):
        import azure.cognitiveservices.speech as speechsdk

        def tts_prompt_vocabulary(vocabulary):
            # Define and assign the Speech API key and region
            speech_key = "51ea1f1487cb413eb0ed452817ed6ef7"
            speech_region = "japaneast"

            # Speech Config for English
            speech_config_en = speechsdk.SpeechConfig(subscription=speech_key,
                                                        region=speech_region)
            speech_config_en.speech_synthesis_voice_name = 'zh-CN-XiaoxiaoNeural'

            # Speech Config for Chinese
            speech_config_cn = speechsdk.SpeechConfig(subscription=speech_key,
                                                        region=speech_region)
            speech_config_cn.speech_synthesis_voice_name = 'zh-CN-XiaoxiaoNeural'  # Chinese voice

            # Initialize SpeechSynthesizer
            audio_config_synthesis = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
            speech_synthesizer_en = speechsdk.SpeechSynthesizer(speech_config=speech_config_en,
                                                                audio_config=audio_config_synthesis)
            speech_synthesizer_cn = speechsdk.SpeechSynthesizer(speech_config=speech_config_cn,
                                                                audio_config=audio_config_synthesis)

            for word in vocabulary:
                print("\nReading word:", word)

                # Synthesize and play the speech for word
                synthesis_result = speech_synthesizer_en.speak_text_async("跟著我重複一遍: " + word).get()

                if synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
                    print("Reading word [{}]".format(word))
                elif synthesis_result.reason == speechsdk.ResultReason.Canceled:
                    cancellation_details = synthesis_result.cancellation_details
                    print("Speech synthesis canceled: {}".format(cancellation_details.reason))
                    if cancellation_details.reason == speechsdk.CancellationReason.Error:
                        if cancellation_details.error_details:
                            print(
                                "Error details: {}".format(cancellation_details.error_details))
                            print(
                                "Check if the speech resource key and region values are correctly set.")

                # Record student's speech and recognize
                max_attempts = 3
                for attempt in range(1, max_attempts + 1):
                    print("\nAttempt", attempt)
                    print("Please read the word aloud:")

                    speech_recognizer = speechsdk.SpeechRecognizer(
                        speech_config=speech_config_en,
                        audio_config=speechsdk.audio.AudioConfig(
                            use_default_microphone=True))
                    speech_recognition_result = speech_recognizer.recognize_once_async().get()

                    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
                        spoken_text = speech_recognition_result.text.strip().rstrip('.')
                        print("Recognized: {}".format(spoken_text))

                        # Provide feedback
                        if spoken_text.lower() == word.lower():
                            # Correct recognition
                            print("Correct!")
                            # Synthesize "Correct" in Chinese
                            synthesis_result = speech_synthesizer_cn.speak_text_async(
                                "正確，點擊下一步繼續").get()
                            break
                        else:
                            # Incorrect recognition
                            if attempt < max_attempts:
                                # Synthesize "Wrong, please try again" in Chinese
                                print("Wrong, please try again.")
                                synthesis_result = speech_synthesizer_cn.speak_text_async(
                                    "錯誤，請重試，圖中的東西是. Eat Dinner").get()
                            else:
                                # Maximum attempts reached, synthesize the correct word in Chinese
                                print("Maximum attempts reached. The correct word is:", word)
                                # Synthesize the correct word in Chinese and then in English
                                synthesis_result = speech_synthesizer_cn.speak_text_async(
                                    "正确单词是").get()
                                synthesis_result = speech_synthesizer_en.speak_text_async(
                                    word).get()
                                break

                    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
                        print("No speech could be recognized. Please try again.")
                        # Speak "say what you see loud" in Chinese
                        synthesis_result = speech_synthesizer_cn.speak_text_async(
                            "用英語再試一次。大聲說出你所看到的").get()
                    else:
                        print("Speech recognition canceled: {}".format(
                            speech_recognition_result.cancellation_details.reason))

        # Sample vocabulary
        vocabulary = ["Eat Dinner", ]
        tts_prompt_vocabulary(vocabulary)

class Page24(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background="#FFFFFF")  # Set background color to white
        self.controller = controller
        
        style = ttk.Style()
        style.theme_use("default")

        style.configure("TButton",
                        foreground="#000000",
                        background="#76c6cc",
                        width = 25,
                        font=("Comic Sans MS",20),
                        padding=[10,10,10,10])
        # Button to navigate to the next page
        button_next = ttk.Button(self, text="Next 下一個", style = 'TButton',
                                command=lambda: controller.show_frame(Page25))
        button_next.place(x=950, y=700, width=200, height=50)

        # Button to navigate to the next page
        button_next = ttk.Button(self, text="Back 後退",style = 'TButton',
                                command=lambda: controller.show_frame(Page23))
        button_next.pack()
        button_next.place(x=10, y=700, width=200, height=50)

        button_next = ttk.Button(self, text="Home Page 主页",
                                style = 'TButton',  
                                command=lambda: controller.show_frame(PageOne))
        button_next.pack()
        button_next.place(x=10, y=10, width=200, height=50)

        # Run Code Button
        button_run_code = ttk.Button(self,
                                    command=self.run_code2)
        image = tk.PhotoImage(file="mc.png")  # Specify the path to your image file
        button_run_code.config(image=image)
        button_run_code.image = image  # Keep a reference to avoid garbage collection
        button_run_code.pack()
        button_run_code.place(x=950, y=100, width=250, height=250)
        
        label = ttk.Label(self, text="Do my homework", font=("Comic Sans MS", 25),background="#FFFFFF")
        label.pack(pady=10)


        # Load image
        self.image = Image.open(
            "doHomework.png")  # Replace "your_image.jpg" with the path to your image
        self.image = self.image.resize((450, 430),
                                        Image.NEAREST)  # Resize the image without ANTIALIAS
        self.photo = ImageTk.PhotoImage(self.image)

        # Display image
        self.image_label = ttk.Label(self, image=self.photo)
        self.image_label.pack()

    def run_code2(self):
        import azure.cognitiveservices.speech as speechsdk

        def tts_prompt_vocabulary(vocabulary):
            # Define and assign the Speech API key and region
            speech_key = "51ea1f1487cb413eb0ed452817ed6ef7"
            speech_region = "japaneast"

            # Speech Config for English
            speech_config_en = speechsdk.SpeechConfig(subscription=speech_key,
                                                        region=speech_region)
            speech_config_en.speech_synthesis_voice_name = 'zh-CN-XiaoxiaoNeural'

            # Speech Config for Chinese
            speech_config_cn = speechsdk.SpeechConfig(subscription=speech_key,
                                                        region=speech_region)
            speech_config_cn.speech_synthesis_voice_name = 'zh-CN-XiaoxiaoNeural'  # Chinese voice

            # Initialize SpeechSynthesizer
            audio_config_synthesis = speechsdk.audio.AudioOutputConfig(
                use_default_speaker=True)
            speech_synthesizer_en = speechsdk.SpeechSynthesizer(
                speech_config=speech_config_en,
                audio_config=audio_config_synthesis)
            speech_synthesizer_cn = speechsdk.SpeechSynthesizer(
                speech_config=speech_config_cn,
                audio_config=audio_config_synthesis)

            for word in vocabulary:
                print("\nReading word:", word)

                # Synthesize and play the speech for word
                synthesis_result = speech_synthesizer_en.speak_text_async("跟著我重複一遍: " + word).get()

                if synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
                    print("Reading word [{}]".format(word))
                elif synthesis_result.reason == speechsdk.ResultReason.Canceled:
                    cancellation_details = synthesis_result.cancellation_details
                    print("Speech synthesis canceled: {}".format(
                        cancellation_details.reason))
                    if cancellation_details.reason == speechsdk.CancellationReason.Error:
                        if cancellation_details.error_details:
                            print("Error details: {}".format(
                                cancellation_details.error_details))
                            print(
                                "Check if the speech resource key and region values are correctly set.")

                # Record student's speech and recognize
                max_attempts = 3
                for attempt in range(1, max_attempts + 1):
                    print("\nAttempt", attempt)
                    print("Please read the word aloud:")

                    speech_recognizer = speechsdk.SpeechRecognizer(
                        speech_config=speech_config_en,
                        audio_config=speechsdk.audio.AudioConfig(
                            use_default_microphone=True))
                    speech_recognition_result = speech_recognizer.recognize_once_async().get()

                    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
                        spoken_text = speech_recognition_result.text.strip().rstrip('.')
                        print("Recognized: {}".format(spoken_text))

                        # Provide feedback
                        if spoken_text.lower() == word.lower():
                            # Correct recognition
                            print("Correct!")
                            # Synthesize "Correct" in Chinese
                            synthesis_result = speech_synthesizer_cn.speak_text_async(
                                "正確，點擊下一步繼續").get()
                            break
                        else:
                            # Incorrect recognition
                            if attempt < max_attempts:
                                # Synthesize "Wrong, please try again" in Chinese
                                print("Wrong, please try again.")
                                synthesis_result = speech_synthesizer_cn.speak_text_async(
                                    "錯誤，請重試，圖中的東西是. Do My Homework").get()
                            else:
                                # Maximum attempts reached, synthesize the correct word in Chinese
                                print("Maximum attempts reached. The correct word is:",
                                        word)
                                # Synthesize the correct word in Chinese and then in English
                                synthesis_result = speech_synthesizer_cn.speak_text_async(
                                    "正确单词是").get()
                                synthesis_result = speech_synthesizer_en.speak_text_async(
                                    word).get()
                                break

                    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
                        print("No speech could be recognized. Please try again.")
                        # Speak "say what you see loud" in Chinese
                        synthesis_result = speech_synthesizer_cn.speak_text_async(
                            "用英語再試一次。大聲說出你所看到的").get()
                    else:
                        print("Speech recognition canceled: {}".format(
                            speech_recognition_result.cancellation_details.reason))

        # Sample vocabulary
        vocabulary = ["Do My Homework", ]
        tts_prompt_vocabulary(vocabulary)
class Page25(tk.Frame):
                                           
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background="#FFFFFF")  # Set background color to white
        self.controller = controller
        
        style = ttk.Style()
        style.theme_use("default")

        style.configure("TButton",
                        foreground="#000000",
                        background="#76c6cc",
                        width = 25,
                        font=("Comic Sans MS",20),
                        padding=[10,10,10,10])
        # Button to navigate to the next page
        button_next = ttk.Button(self, text="Finish 結束", style = 'TButton',
                                command=lambda: controller.show_frame(PageOne))
        button_next.place(x=950, y=700, width=200, height=50)

        # Button to navigate to the next page
        button_next = ttk.Button(self, text="Back 後退",style = 'TButton',
                                command=lambda: controller.show_frame(Page24))
        button_next.pack()
        button_next.place(x=10, y=700, width=200, height=50)

        button_next = ttk.Button(self, text="Home Page 主页",
                                style = 'TButton',  
                                command=lambda: controller.show_frame(PageOne))
        button_next.pack()
        button_next.place(x=10, y=10, width=200, height=50)

        # Run Code Button
        button_run_code = ttk.Button(self,
                                    command=self.run_code2)
        image = tk.PhotoImage(
            file="mc.png")  # Specify the path to your image file
        button_run_code.config(image=image)
        button_run_code.image = image  # Keep a reference to avoid garbage collection
        button_run_code.pack()
        button_run_code.place(x=950, y=100, width=250, height=250)
        
        label = ttk.Label(self, text="Go to sleep", font=("Comic Sans MS", 25),background="#FFFFFF")
        label.pack(pady=10)


        # Load image
        self.image = Image.open(
            "gotoBed.png")  # Replace "your_image.jpg" with the path to your image
        self.image = self.image.resize((450, 430),
                                        Image.NEAREST)  # Resize the image without ANTIALIAS
        self.photo = ImageTk.PhotoImage(self.image)

        # Display image
        self.image_label = ttk.Label(self, image=self.photo)
        self.image_label.pack()

    def run_code2(self):
        import azure.cognitiveservices.speech as speechsdk

        def tts_prompt_vocabulary(vocabulary):
            # Define and assign the Speech API key and region
            speech_key = "51ea1f1487cb413eb0ed452817ed6ef7"
            speech_region = "japaneast"

            # Speech Config for English
            speech_config_en = speechsdk.SpeechConfig(subscription=speech_key,
                                                        region=speech_region)
            speech_config_en.speech_synthesis_voice_name = 'zh-CN-XiaoxiaoNeural'

            # Speech Config for Chinese
            speech_config_cn = speechsdk.SpeechConfig(subscription=speech_key,
                                                        region=speech_region)
            speech_config_cn.speech_synthesis_voice_name = 'zh-CN-XiaoxiaoNeural'  # Chinese voice

            # Initialize SpeechSynthesizer
            audio_config_synthesis = speechsdk.audio.AudioOutputConfig(
                use_default_speaker=True)
            speech_synthesizer_en = speechsdk.SpeechSynthesizer(
                speech_config=speech_config_en,
                audio_config=audio_config_synthesis)
            speech_synthesizer_cn = speechsdk.SpeechSynthesizer(
                speech_config=speech_config_cn,
                audio_config=audio_config_synthesis)

            for word in vocabulary:
                print("\nReading word:", word)

                # Synthesize and play the speech for word
                synthesis_result = speech_synthesizer_en.speak_text_async("跟著我重複一遍: " + word).get()

                if synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
                    print("Reading word [{}]".format(word))
                elif synthesis_result.reason == speechsdk.ResultReason.Canceled:
                    cancellation_details = synthesis_result.cancellation_details
                    print("Speech synthesis canceled: {}".format(
                        cancellation_details.reason))
                    if cancellation_details.reason == speechsdk.CancellationReason.Error:
                        if cancellation_details.error_details:
                            print("Error details: {}".format(
                                cancellation_details.error_details))
                            print(
                                "Check if the speech resource key and region values are correctly set.")

                # Record student's speech and recognize
                max_attempts = 3
                for attempt in range(1, max_attempts + 1):
                    print("\nAttempt", attempt)
                    print("Please read the word aloud:")

                    speech_recognizer = speechsdk.SpeechRecognizer(
                        speech_config=speech_config_en,
                        audio_config=speechsdk.audio.AudioConfig(
                            use_default_microphone=True))
                    speech_recognition_result = speech_recognizer.recognize_once_async().get()

                    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
                        spoken_text = speech_recognition_result.text.strip().rstrip(
                            '.')
                        print("Recognized: {}".format(spoken_text))

                        # Provide feedback
                        if spoken_text.lower() == word.lower():
                            # Correct recognition
                            print("Correct!")
                            # Synthesize "Correct" in Chinese
                            synthesis_result = speech_synthesizer_cn.speak_text_async(
                                "正確，點擊下一步繼續").get()
                            break
                        else:
                            # Incorrect recognition
                            if attempt < max_attempts:
                                # Synthesize "Wrong, please try again" in Chinese
                                print("Wrong, please try again.")
                                synthesis_result = speech_synthesizer_cn.speak_text_async(
                                    "錯誤，請重試，圖中的東西是. Go to sleep").get()
                            else:
                                # Maximum attempts reached, synthesize the correct word in Chinese
                                print(
                                    "Maximum attempts reached. The correct word is:",
                                    word)
                                # Synthesize the correct word in Chinese and then in English
                                synthesis_result = speech_synthesizer_cn.speak_text_async(
                                    "正确单词是").get()
                                synthesis_result = speech_synthesizer_en.speak_text_async(
                                    word).get()
                                break

                    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
                        print(
                            "No speech could be recognized. Please try again.")
                        # Speak "say what you see loud" in Chinese
                        synthesis_result = speech_synthesizer_cn.speak_text_async(
                            "用英語再試一次。大聲說出你所看到的").get()
                    else:
                        print("Speech recognition canceled: {}".format(
                            speech_recognition_result.cancellation_details.reason))

        # Sample vocabulary
        vocabulary = ["Go to sleep", ]
        tts_prompt_vocabulary(vocabulary)


    
##############################################################################################################################################
#TestMode
class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__()
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Test Mode 測試模式",
                          background = "#76c6cc",
                          font=("Comic Sans MS", 20))
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
        
        level_label = ttk.Label(self, text = "Level 1:", font=("Comic Sans MS",20), background="#00FF00")#FF0000
        level_label.pack(pady = 10,padx = 10)
        
        # Button to execute the code
        button1 = ttk.Button(self, text="Vocabulary 詞彙",
                                     style="TButton",
                                     width=25)
                                     #command=self.run_tts)
        button1.pack(side="top", pady=10)
        
        button4 = ttk.Button(self,text="Matching Games 配對遊戲",
                             style="TButton",
                             width=25
                             )
        button4.pack(side="top",pady=10)
        
        level_label = ttk.Label(self, text = "Level 2:", font=("Comic Sans MS",20), background="#FFFF00") #FFFF00
        level_label.pack(pady = 10,padx = 10)
        
        
        button2 = ttk.Button(self, text="Sentence Construction 句子构造",
                                     style="TButton",
                                     width=25)
                                     #command=self.run_tts)
        button2.pack(side="top", pady=10)
        
        button3 = ttk.Button(self, text="Spelling bee 拼字比賽",width=25, style="TButton", command=lambda: controller.show_frame(PageTen))
        button3.pack(side="top", pady=10)
    
                             
        level_label = ttk.Label(self, text = "Level 3:", font=("Comic Sans MS",20), background="#FF0000") #00FF00
        level_label.pack(pady = 10,padx = 10)
        
    
        button5 = ttk.Button(self,text="Scrambled Words 亂序詞",
                             style="TButton",
                             width=25
                             )
        button5.pack(side="top",pady=10)
        
        button = ttk.Button(self, text="Homepage 首頁",
                            style="TButton", width = 15,
                            command=lambda: controller.show_frame(StartPage))
        button.pack(side=tk.LEFT,padx=10, pady=0)

        button = ttk.Button(self, text="Back 後退",
                            style="TButton",width = 15,
                            command=lambda: controller.show_frame(StartPage))
        button.pack(side=tk.RIGHT, padx=10,pady=0)
        
# Import the EnglishSpellingGame class
from EnglishSpellingGame import EnglishSpellingGame
class PageTen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background="#FFFFFF")  # Set background color to white
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
                        width=25,
                        font=("Comic Sans MS", 18),
                        padding=[10, 10, 10, 10])

        # Button to navigate to the next page
        button_next = ttk.Button(self, text="Back 後退",
                                 style="TButton",width = 25,
                                 command=lambda: controller.show_frame(PageTwo))
        button_next.pack(side="bottom", pady=10)

        # Initialize the spelling game widget
        self.spelling_game = EnglishSpellingGame(self)

        # Button to start the spelling bee game
        button3 = ttk.Button(self, text="Start Spelling bee 開始拼字比賽", style="TButton", command=self.start_game)
        button3.pack(side = "bottom", pady=10)
        
        

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
                        width = 30,
                        font=("Comic Sans MS",18),
                        padding=[10,10,10,10])

        # Button to go to Home Page
        button_home = ttk.Button(self, text="Back 後退",
                                 style="TButton",
                                 command=lambda: controller.show_frame(StartPage))
        button_home.pack(side="bottom", pady=10)

        # Button to start visual games (go to PageOne)
        button_visual_games = ttk.Button(self, text="Start Visual Games",
                                         style="TButton",
                                         command=lambda: controller.show_frame(PageFour))

        button_visual_games.pack(side="bottom", pady=10)
        
##########################################################################################################################

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
        
##########################################################################################################################

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
##########################################################################################################################

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
        
##########################################################################################################################

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
        
##########################################################################################################################

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
        
##########################################################################################################################

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
##########################################################################################################################

