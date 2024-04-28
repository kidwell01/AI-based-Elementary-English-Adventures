import tkinter as tk
from tkinter import ttk


class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Set initial window size
        self.geometry("1000x550")

        # Make the window non-resizable
        self.resizable(False, False)

        # Container to hold all pages
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}  # Dictionary to store all pages

        # Create and add pages to the dictionary
        for F in (
                # Pages for home page.
                StartPage, PageOne, PageTwo, PageThree,

                # Pages linked to PageThree.
                PageFour, PageFive, PageSix, PageSeven, PageEight, PageNine,

                # Pages linked to PageOne.
                    # Vocabulary Practice Pages (in PageOne).
                PageEleven, PageTwelve, PageThirteen, PageFourteen,
                    # Sentence Construction Pages (in PageOne).
                Page15, Page16, Page17, Page18, Page19,Page20, Page21, Page22, Page23, Page24, Page25, Page30, Page31
        ):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Show the start page initially
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


from PIL import Image, ImageTk


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Load the background image
        image = Image.open("jungle.jpg")
        image = image.resize((1000, 550), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        # Create a label to hold the background image
        background_label = tk.Label(self, image=photo)
        background_label.image = photo  # Keep a reference to the image to prevent it from being garbage collected
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        style = ttk.Style()
        style.theme_use("default")
        style.layout('TButton', [('Button.border',
                                {'children': [('Button.padding',
                                {'children': [('Button.label', 
                                {'sticky': 'nswe'})], 
                                'sticky': 'nswe'})],
                                'sticky': 'nswe', 
                                'border': '20'})])

        style.configure("TButton",
                        foreground="#000000",
                        background="#76c6cc",
                        width = 25,
                        font=("Comic Sans MS",22),
                        #padding=[10,10,10,10])
        )

        # Customize button properties
        button1 = ttk.Button(self, text="Practice Mode 練習模式", width=20, style = 'TButton',
                             command=lambda: controller.show_frame(PageOne))
        button1.pack(pady=(0, 10), side="top")  # 10cm spacing below the button

        button2 = ttk.Button(self, text="Test Mode 測試模式", width=20, style = 'TButton',
                             command=lambda: controller.show_frame(PageTwo))
        button2.pack(pady=(0, 10), side="top")  # 10cm spacing below the button

        button3 = ttk.Button(self, text="Extras", width=20, style = 'TButton',
                             command=lambda: controller.show_frame(PageThree))
        button3.pack(pady=(0, 10))  # 10cm spacing below the button

        # Customize StartPage here
        # You can add more widgets like labels, buttons, etc., and arrange them as needed


import azure.cognitiveservices.speech as speechsdk


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Load the background image
        image = Image.open("jungle.jpg")
        image = image.resize((1000, 550), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        # Create a label to hold the background image
        background_label = tk.Label(self, image=photo)
        background_label.image = photo  # Keep a reference to the image to prevent it from being garbage collected
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        label = tk.Label(self, text="練習模式", font=("Cascadia Mono ExtraLight", 15), width=15, height=1,
                         bg="light green")
        label.pack(pady=10, padx=10)

        self.button_read_text = tk.Button(self, text="音訊指導", font=("Cascadia Mono ExtraLight", 15),
                                          bg="light green", command=self.read_custom_chinese_text)
        self.button_read_text.place(x=8, y=30, width=200, height=50)  # Initial position and size



        # Create a label below the button
        self.custom_label = tk.Label(self, text="指示：\n1. 點選麥克風圖示。\n2. 我能說出圖中事物的名稱。\n3. 現在跟我來，立即再說一次。"
                                                "\n4. 你可以練習說三次來檢查你的發音。"
                                                "\n5. 如果你說錯了或三遍都沒有說完，我會告訴你正確的發音，然後再試一次。"
                                                "\n6. 點擊右下角的「下一步」按鈕，可以看到下一張圖片。",

                                     font=("Cascadia Mono ExtraLight", 15), bg="yellow", justify="left")

        self.custom_label.place(x=8, y=90, width=700, height=190)  # Initial position and size

        button = tk.Button(self, text="Home Page 首頁", font=("Cascadia Mono ExtraLight", 15), width=15, height=1,
                           bg="light green",
                           command=lambda: controller.show_frame(StartPage))
        button.pack(side="bottom", pady=20)

        button_next = tk.Button(self, text="Vocabualry Practice \n 詞彙練習", font=("Cascadia Mono ExtraLight", 15), width=15,
                                height=1,
                                bg="light green", command=lambda: controller.show_frame(PageEleven))
        button_next.pack()
        button_next.place(x=700, y=87, width=300, height=60)

        button_next = tk.Button(self, text="Sentence Construction \n 造句練習", font=("Cascadia Mono ExtraLight", 15), width=15,
                                height=1,
                                bg="light green", command=lambda: controller.show_frame(Page15))
        button_next.pack()
        button_next.place(x=700, y=220, width=300, height=60)

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

        # Add code here to read the Chinese text aloud
        # You can use any text-to-speech library or service to achieve this

        # Customize PageOne here
        # You can add more widgets like labels, buttons, etc., and arrange them as needed


from tkinter import Label, Frame, Button
from PIL import Image, ImageTk
import time


class PageEleven(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")  # Set background color to white
        self.controller = controller

        # Button to navigate to the next page
        button_next = tk.Button(self, text="下一個", font=("Cascadia Mono ExtraLight", 15), width=15, height=1,
                                bg="light green", command=lambda: controller.show_frame(PageTwelve))
        button_next.pack()
        button_next.place(x=812, y=440, width=200, height=50)

        # Button to navigate to the next page
        button_next = tk.Button(self, text="上一頁", font=("Cascadia Mono ExtraLight", 15), width=15, height=1,
                                bg="light green", command=lambda: controller.show_frame(PageOne))
        button_next.pack()
        button_next.place(x=8, y=440, width=200, height=50)

        # Run Code Button
        button_run_code = tk.Button(self, bg="white", borderwidth=0, highlightthickness=0,
                                    command=self.run_code)
        image = tk.PhotoImage(file="mc.png")  # Specify the path to your image file
        button_run_code.config(image=image)
        button_run_code.image = image  # Keep a reference to avoid garbage collection
        button_run_code.pack()
        button_run_code.place(x=762, y=0, width=250, height=250)

        # Load image
        self.image = Image.open("book.jpg")  # Replace "your_image.jpg" with the path to your image
        self.image = self.image.resize((550, 520), Image.NEAREST)  # Resize the image without ANTIALIAS
        self.photo = ImageTk.PhotoImage(self.image)

        # Display image
        self.image_label = Label(self, image=self.photo, borderwidth=0, highlightthickness=0)
        self.image_label.pack()

    def run_code(self):
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
                synthesis_result = speech_synthesizer_en.speak_text_async(word).get()

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
                            synthesis_result = speech_synthesizer_cn.speak_text_async("正确").get()
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
        self.configure(bg="white")  # Set background color to white
        self.controller = controller

        # Button to navigate to the next page
        button_next = tk.Button(self, text="下一個", font=("Cascadia Mono ExtraLight", 15), width=15, height=1,
                                bg="light green", command=lambda: controller.show_frame(PageThirteen))
        button_next.pack()
        button_next.place(x=812, y=440, width=200, height=50)

        # Button to navigate to the next page
        button_next = tk.Button(self, text="上一頁", font=("Cascadia Mono ExtraLight", 15), width=15, height=1,
                                bg="light green", command=lambda: controller.show_frame(PageEleven))
        button_next.pack()
        button_next.place(x=8, y=440, width=200, height=50)

        # Run Code Button
        button_run_code = tk.Button(self, bg="white", borderwidth=0, highlightthickness=0,
                                    command=self.run_code2)
        image = tk.PhotoImage(file="mc.png")  # Specify the path to your image file
        button_run_code.config(image=image)
        button_run_code.image = image  # Keep a reference to avoid garbage collection
        button_run_code.pack()
        button_run_code.place(x=762, y=0, width=250, height=250)

        # Load image
        self.image = Image.open("chair.png")  # Replace "your_image.jpg" with the path to your image
        self.image = self.image.resize((550, 520), Image.NEAREST)  # Resize the image without ANTIALIAS
        self.photo = ImageTk.PhotoImage(self.image)

        # Display image
        self.image_label = Label(self, image=self.photo, borderwidth=0, highlightthickness=0)
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
                synthesis_result = speech_synthesizer_en.speak_text_async(word).get()

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
                            synthesis_result = speech_synthesizer_cn.speak_text_async("正确").get()
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
        self.configure(bg="white")  # Set background color to white
        self.controller = controller

        # Button to navigate to the next page
        button_next = tk.Button(self, text="下一個", font=("Cascadia Mono ExtraLight", 15), width=15, height=1,
                                bg="light green", command=lambda: controller.show_frame(PageFourteen))
        button_next.pack()
        button_next.place(x=812, y=440, width=200, height=50)

        # Button to navigate to the next page
        button_next = tk.Button(self, text="上一頁", font=("Cascadia Mono ExtraLight", 15), width=15, height=1,
                                bg="light green", command=lambda: controller.show_frame(PageTwelve))
        button_next.pack()
        button_next.place(x=8, y=440, width=200, height=50)

        # Run Code Button
        button_run_code = tk.Button(self, bg="white", borderwidth=0, highlightthickness=0,
                                    command=self.run_code2)
        image = tk.PhotoImage(file="mc.png")  # Specify the path to your image file
        button_run_code.config(image=image)
        button_run_code.image = image  # Keep a reference to avoid garbage collection
        button_run_code.pack()
        button_run_code.place(x=762, y=0, width=250, height=250)

        # Load image
        self.image = Image.open("doctor.png")  # Replace "your_image.jpg" with the path to your image
        self.image = self.image.resize((550, 520), Image.NEAREST)  # Resize the image without ANTIALIAS
        self.photo = ImageTk.PhotoImage(self.image)

        # Display image
        self.image_label = Label(self, image=self.photo, borderwidth=0, highlightthickness=0)
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
                synthesis_result = speech_synthesizer_en.speak_text_async(word).get()

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
                            synthesis_result = speech_synthesizer_cn.speak_text_async("正确").get()
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
        self.configure(bg="white")  # Set background color to white
        self.controller = controller

        # Button to navigate to the next page
        button_next = tk.Button(self, text="Finish 結束", font=("Cascadia Mono ExtraLight", 15), width=15,
                                height=1,
                                bg="light green", command=lambda: controller.show_frame(PageOne))
        button_next.pack()
        button_next.place(x=812, y=440, width=200, height=50)

        # Button to navigate to the next page
        button_next = tk.Button(self, text="上一頁", font=("Cascadia Mono ExtraLight", 15), width=15, height=1,
                                bg="light green", command=lambda: controller.show_frame(PageThirteen))
        button_next.pack()
        button_next.place(x=8, y=440, width=200, height=50)

        # Run Code Button
        button_run_code = tk.Button(self, bg="white", borderwidth=0, highlightthickness=0,
                                    command=self.run_code2)
        image = tk.PhotoImage(file="mc.png")  # Specify the path to your image file
        button_run_code.config(image=image)
        button_run_code.image = image  # Keep a reference to avoid garbage collection
        button_run_code.pack()
        button_run_code.place(x=762, y=0, width=250, height=250)

        # Load image
        self.image = Image.open("bus.jpg")  # Replace "your_image.jpg" with the path to your image
        self.image = self.image.resize((550, 520), Image.NEAREST)  # Resize the image without ANTIALIAS
        self.photo = ImageTk.PhotoImage(self.image)

        # Display image
        self.image_label = Label(self, image=self.photo, borderwidth=0, highlightthickness=0)
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
                synthesis_result = speech_synthesizer_en.speak_text_async(word).get()

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
                            synthesis_result = speech_synthesizer_cn.speak_text_async("正确").get()
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
        self.configure(bg="white")  # Set background color to white
        self.controller = controller

        # Button to navigate to the next page
        button_next = tk.Button(self, text="下一個", font=("Cascadia Mono ExtraLight", 15), width=15, height=1,
                                bg="light green", command=lambda: controller.show_frame(Page16))
        button_next.pack()
        button_next.place(x=812, y=440, width=200, height=50)

        # Button to navigate to the next page
        button_next = tk.Button(self, text="上一頁", font=("Cascadia Mono ExtraLight", 15), width=15, height=1,
                                bg="light green", command=lambda: controller.show_frame(PageOne))
        button_next.pack()
        button_next.place(x=8, y=440, width=200, height=50)

        button_next = tk.Button(self, text="Home Page 主页",
                                font=("Cascadia Mono ExtraLight", 15), width=15,
                                height=1,
                                bg="light green",
                                command=lambda: controller.show_frame(PageOne))
        button_next.pack()
        button_next.place(x=10, y=10, width=200, height=50)

        # Run Code Button
        button_run_code = tk.Button(self, bg="white", borderwidth=0, highlightthickness=0,
                                    command=self.run_code2)
        image = tk.PhotoImage(file="mc.png")  # Specify the path to your image file
        button_run_code.config(image=image)
        button_run_code.image = image  # Keep a reference to avoid garbage collection
        button_run_code.pack()
        button_run_code.place(x=762, y=0, width=250, height=250)

        # Load image
        self.image = Image.open("wakeUp.png")  # Replace "your_image.jpg" with the path to your image
        self.image = self.image.resize((550, 520), Image.NEAREST)  # Resize the image without ANTIALIAS
        self.photo = ImageTk.PhotoImage(self.image)

        # Display image
        self.image_label = Label(self, image=self.photo, borderwidth=0, highlightthickness=0)
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
                synthesis_result = speech_synthesizer_en.speak_text_async(word).get()

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
                            synthesis_result = speech_synthesizer_cn.speak_text_async("正确").get()
                            break
                        else:
                            # Incorrect recognition
                            if attempt < max_attempts:
                                # Synthesize "Wrong, please try again" in Chinese
                                print("Wrong, please try again.")
                                synthesis_result = speech_synthesizer_cn.speak_text_async(
                                    "錯誤，請重試，圖中的東西是. Wake Up").get()
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
        vocabulary = ["Wake Up", ]
        tts_prompt_vocabulary(vocabulary)


class Page16(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")  # Set background color to white
        self.controller = controller

        # Button to navigate to the next page
        button_next = tk.Button(self, text="下一個", font=("Cascadia Mono ExtraLight", 15), width=15, height=1,
                                bg="light green", command=lambda: controller.show_frame(Page17))
        button_next.pack()
        button_next.place(x=812, y=440, width=200, height=50)

        # Button to navigate to the next page
        button_next = tk.Button(self, text="上一頁", font=("Cascadia Mono ExtraLight", 15), width=15, height=1,
                                bg="light green", command=lambda: controller.show_frame(Page15))
        button_next.pack()
        button_next.place(x=8, y=440, width=200, height=50)

        button_next = tk.Button(self, text="Home Page 主页",
                                font=("Cascadia Mono ExtraLight", 15), width=15,
                                height=1,
                                bg="light green",
                                command=lambda: controller.show_frame(PageOne))
        button_next.pack()
        button_next.place(x=10, y=10, width=200, height=50)

        # Run Code Button
        button_run_code = tk.Button(self, bg="white", borderwidth=0, highlightthickness=0,
                                    command=self.run_code2)
        image = tk.PhotoImage(file="mc.png")  # Specify the path to your image file
        button_run_code.config(image=image)
        button_run_code.image = image  # Keep a reference to avoid garbage collection
        button_run_code.pack()
        button_run_code.place(x=762, y=0, width=250, height=250)

        # Load image
        self.image = Image.open("takeShower.png")  # Replace "your_image.jpg" with the path to your image
        self.image = self.image.resize((550, 520), Image.NEAREST)  # Resize the image without ANTIALIAS
        self.photo = ImageTk.PhotoImage(self.image)

        # Display image
        self.image_label = Label(self, image=self.photo, borderwidth=0, highlightthickness=0)
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
                synthesis_result = speech_synthesizer_en.speak_text_async(word).get()

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
                            synthesis_result = speech_synthesizer_cn.speak_text_async("正确").get()
                            break
                        else:
                            # Incorrect recognition
                            if attempt < max_attempts:
                                # Synthesize "Wrong, please try again" in Chinese
                                print("Wrong, please try again.")
                                synthesis_result = speech_synthesizer_cn.speak_text_async(
                                    "錯誤，請重試，圖中的東西是. Have Shower").get()
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
        vocabulary = ["Have Shower", ]
        tts_prompt_vocabulary(vocabulary)



class Page17(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")  # Set background color to white
        self.controller = controller

        # Button to navigate to the next page
        button_next = tk.Button(self, text="下一個", font=("Cascadia Mono ExtraLight", 15), width=15, height=1,
                                bg="light green", command=lambda: controller.show_frame(Page18))
        button_next.pack()
        button_next.place(x=812, y=440, width=200, height=50)

        # Button to navigate to the next page
        button_next = tk.Button(self, text="上一頁", font=("Cascadia Mono ExtraLight", 15), width=15, height=1,
                                bg="light green", command=lambda: controller.show_frame(Page16))
        button_next.pack()
        button_next.place(x=8, y=440, width=200, height=50)

        button_next = tk.Button(self, text="Home Page 主页",
                                font=("Cascadia Mono ExtraLight", 15), width=15,
                                height=1,
                                bg="light green",
                                command=lambda: controller.show_frame(PageOne))
        button_next.pack()
        button_next.place(x=10, y=10, width=200, height=50)

        # Run Code Button
        button_run_code = tk.Button(self, bg="white", borderwidth=0, highlightthickness=0,
                                    command=self.run_code2)
        image = tk.PhotoImage(file="mc.png")  # Specify the path to your image file
        button_run_code.config(image=image)
        button_run_code.image = image  # Keep a reference to avoid garbage collection
        button_run_code.pack()
        button_run_code.place(x=762, y=0, width=250, height=250)

        # Load image
        self.image = Image.open("dress.jpg")  # Replace "your_image.jpg" with the path to your image
        self.image = self.image.resize((550, 520), Image.NEAREST)  # Resize the image without ANTIALIAS
        self.photo = ImageTk.PhotoImage(self.image)

        # Display image
        self.image_label = Label(self, image=self.photo, borderwidth=0, highlightthickness=0)
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
                synthesis_result = speech_synthesizer_en.speak_text_async(word).get()

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
                            synthesis_result = speech_synthesizer_cn.speak_text_async("正确").get()
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
        self.configure(bg="white")  # Set background color to white
        self.controller = controller

        # Button to navigate to the next page
        button_next = tk.Button(self, text="下一個", font=("Cascadia Mono ExtraLight", 15), width=15, height=1,
                                bg="light green", command=lambda: controller.show_frame(Page19))
        button_next.pack()
        button_next.place(x=812, y=440, width=200, height=50)

        # Button to navigate to the next page
        button_next = tk.Button(self, text="上一頁", font=("Cascadia Mono ExtraLight", 15), width=15, height=1,
                                bg="light green", command=lambda: controller.show_frame(Page17))
        button_next.pack()
        button_next.place(x=8, y=440, width=200, height=50)

        button_next = tk.Button(self, text="Home Page 主页",
                                font=("Cascadia Mono ExtraLight", 15), width=15,
                                height=1,
                                bg="light green",
                                command=lambda: controller.show_frame(PageOne))
        button_next.pack()
        button_next.place(x=10, y=10, width=200, height=50)

        # Run Code Button
        button_run_code = tk.Button(self, bg="white", borderwidth=0, highlightthickness=0,
                                    command=self.run_code2)
        image = tk.PhotoImage(file="mc.png")  # Specify the path to your image file
        button_run_code.config(image=image)
        button_run_code.image = image  # Keep a reference to avoid garbage collection
        button_run_code.pack()
        button_run_code.place(x=762, y=0, width=250, height=250)

        # Load image
        self.image = Image.open("haveBreakfast.png")  # Replace "your_image.jpg" with the path to your image
        self.image = self.image.resize((550, 520), Image.NEAREST)  # Resize the image without ANTIALIAS
        self.photo = ImageTk.PhotoImage(self.image)

        # Display image
        self.image_label = Label(self, image=self.photo, borderwidth=0, highlightthickness=0)
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
                synthesis_result = speech_synthesizer_en.speak_text_async(word).get()

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
                            synthesis_result = speech_synthesizer_cn.speak_text_async("正确").get()
                            break
                        else:
                            # Incorrect recognition
                            if attempt < max_attempts:
                                # Synthesize "Wrong, please try again" in Chinese
                                print("Wrong, please try again.")
                                synthesis_result = speech_synthesizer_cn.speak_text_async(
                                    "錯誤，請重試，圖中的東西是. Have Breakfast").get()
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
        vocabulary = ["Have Breakfast", ]
        tts_prompt_vocabulary(vocabulary)


class Page19(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")  # Set background color to white
        self.controller = controller

        # Button to navigate to the next page
        button_next = tk.Button(self, text="下一個", font=("Cascadia Mono ExtraLight", 15), width=15, height=1,
                                bg="light green", command=lambda: controller.show_frame(Page20))
        button_next.pack()
        button_next.place(x=812, y=440, width=200, height=50)

        # Button to navigate to the next page
        button_next = tk.Button(self, text="上一頁", font=("Cascadia Mono ExtraLight", 15), width=15, height=1,
                                bg="light green", command=lambda: controller.show_frame(Page18))
        button_next.pack()
        button_next.place(x=8, y=440, width=200, height=50)

        button_next = tk.Button(self, text="Home Page 主页",
                                font=("Cascadia Mono ExtraLight", 15), width=15,
                                height=1,
                                bg="light green",
                                command=lambda: controller.show_frame(PageOne))
        button_next.pack()
        button_next.place(x=10, y=10, width=200, height=50)

        # Run Code Button
        button_run_code = tk.Button(self, bg="white", borderwidth=0, highlightthickness=0,
                                    command=self.run_code2)
        image = tk.PhotoImage(file="mc.png")  # Specify the path to your image file
        button_run_code.config(image=image)
        button_run_code.image = image  # Keep a reference to avoid garbage collection
        button_run_code.pack()
        button_run_code.place(x=762, y=0, width=250, height=250)

        # Load image
        self.image = Image.open("brushTeeth.png")  # Replace "your_image.jpg" with the path to your image
        self.image = self.image.resize((550, 520), Image.NEAREST)  # Resize the image without ANTIALIAS
        self.photo = ImageTk.PhotoImage(self.image)

        # Display image
        self.image_label = Label(self, image=self.photo, borderwidth=0, highlightthickness=0)
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
                synthesis_result = speech_synthesizer_en.speak_text_async(word).get()

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
                            synthesis_result = speech_synthesizer_cn.speak_text_async("正确").get()
                            break
                        else:
                            # Incorrect recognition
                            if attempt < max_attempts:
                                # Synthesize "Wrong, please try again" in Chinese
                                print("Wrong, please try again.")
                                synthesis_result = speech_synthesizer_cn.speak_text_async(
                                    "錯誤，請重試，圖中的東西是. Clean My Teeth").get()
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
        vocabulary = ["Clean My Teeth", ]
        tts_prompt_vocabulary(vocabulary)


class Page20(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")  # Set background color to white
        self.controller = controller

        # Button to navigate to the next page
        button_next = tk.Button(self, text="下一個", font=("Cascadia Mono ExtraLight", 15), width=15, height=1,
                                bg="light green", command=lambda: controller.show_frame(Page21))
        button_next.pack()
        button_next.place(x=812, y=440, width=200, height=50)

        # Button to navigate to the next page
        button_next = tk.Button(self, text="上一頁", font=("Cascadia Mono ExtraLight", 15), width=15, height=1,
                                bg="light green", command=lambda: controller.show_frame(Page19))
        button_next.pack()
        button_next.place(x=8, y=440, width=200, height=50)

        button_next = tk.Button(self, text="Home Page 主页",
                                font=("Cascadia Mono ExtraLight", 15), width=15,
                                height=1,
                                bg="light green",
                                command=lambda: controller.show_frame(PageOne))
        button_next.pack()
        button_next.place(x=10, y=10, width=200, height=50)

        # Run Code Button
        button_run_code = tk.Button(self, bg="white", borderwidth=0, highlightthickness=0,
                                    command=self.run_code2)
        image = tk.PhotoImage(file="mc.png")  # Specify the path to your image file
        button_run_code.config(image=image)
        button_run_code.image = image  # Keep a reference to avoid garbage collection
        button_run_code.pack()
        button_run_code.place(x=762, y=0, width=250, height=250)

        # Load image
        self.image = Image.open("goToSchool.png")  # Replace "your_image.jpg" with the path to your image
        self.image = self.image.resize((550, 520), Image.NEAREST)  # Resize the image without ANTIALIAS
        self.photo = ImageTk.PhotoImage(self.image)

        # Display image
        self.image_label = Label(self, image=self.photo, borderwidth=0, highlightthickness=0)
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
                synthesis_result = speech_synthesizer_en.speak_text_async(word).get()

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
                            synthesis_result = speech_synthesizer_cn.speak_text_async("正确").get()
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
                self.configure(bg="white")  # Set background color to white
                self.controller = controller

                # Button to navigate to the next page
                button_next = tk.Button(self, text="下一個", font=("Cascadia Mono ExtraLight", 15), width=15, height=1,
                                        bg="light green", command=lambda: controller.show_frame(Page22))
                button_next.pack()
                button_next.place(x=812, y=440, width=200, height=50)

                # Button to navigate to the next page
                button_next = tk.Button(self, text="上一頁", font=("Cascadia Mono ExtraLight", 15), width=15, height=1,
                                        bg="light green", command=lambda: controller.show_frame(Page20))
                button_next.pack()
                button_next.place(x=8, y=440, width=200, height=50)

                button_next = tk.Button(self, text="Home Page 主页",
                                        font=("Cascadia Mono ExtraLight", 15), width=15,
                                        height=1,
                                        bg="light green",
                                        command=lambda: controller.show_frame(PageOne))
                button_next.pack()
                button_next.place(x=10, y=10, width=200, height=50)

                # Run Code Button
                button_run_code = tk.Button(self, bg="white", borderwidth=0, highlightthickness=0,
                                            command=self.run_code2)
                image = tk.PhotoImage(file="mc.png")  # Specify the path to your image file
                button_run_code.config(image=image)
                button_run_code.image = image  # Keep a reference to avoid garbage collection
                button_run_code.pack()
                button_run_code.place(x=762, y=0, width=250, height=250)

                # Load image
                self.image = Image.open("haveLunch.png")  # Replace "your_image.jpg" with the path to your image
                self.image = self.image.resize((550, 520), Image.NEAREST)  # Resize the image without ANTIALIAS
                self.photo = ImageTk.PhotoImage(self.image)

                # Display image
                self.image_label = Label(self, image=self.photo, borderwidth=0, highlightthickness=0)
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
                        synthesis_result = speech_synthesizer_en.speak_text_async(word).get()

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
                                    synthesis_result = speech_synthesizer_cn.speak_text_async("正确").get()
                                    break
                                else:
                                    # Incorrect recognition
                                    if attempt < max_attempts:
                                        # Synthesize "Wrong, please try again" in Chinese
                                        print("Wrong, please try again.")
                                        synthesis_result = speech_synthesizer_cn.speak_text_async(
                                            "錯誤，請重試，圖中的東西是. Have Lunch").get()
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
                vocabulary = ["Have Lunch", ]
                tts_prompt_vocabulary(vocabulary)

class Page22(tk.Frame):
                    def __init__(self, parent, controller):
                        tk.Frame.__init__(self, parent)
                        self.configure(bg="white")  # Set background color to white
                        self.controller = controller

                        # Button to navigate to the next page
                        button_next = tk.Button(self, text="下一個", font=("Cascadia Mono ExtraLight", 15), width=15,
                                                height=1,
                                                bg="light green", command=lambda: controller.show_frame(Page23))
                        button_next.pack()
                        button_next.place(x=812, y=440, width=200, height=50)

                        # Button to navigate to the next page
                        button_next = tk.Button(self, text="上一頁", font=("Cascadia Mono ExtraLight", 15), width=15,
                                                height=1,
                                                bg="light green", command=lambda: controller.show_frame(Page21))
                        button_next.pack()
                        button_next.place(x=8, y=440, width=200, height=50)

                        button_next = tk.Button(self, text="Home Page 主页",
                                                font=("Cascadia Mono ExtraLight", 15), width=15,
                                                height=1,
                                                bg="light green",
                                                command=lambda: controller.show_frame(PageOne))
                        button_next.pack()
                        button_next.place(x=10, y=10, width=200, height=50)

                        # Run Code Button
                        button_run_code = tk.Button(self, bg="white", borderwidth=0, highlightthickness=0,
                                                    command=self.run_code2)
                        image = tk.PhotoImage(file="mc.png")  # Specify the path to your image file
                        button_run_code.config(image=image)
                        button_run_code.image = image  # Keep a reference to avoid garbage collection
                        button_run_code.pack()
                        button_run_code.place(x=762, y=0, width=250, height=250)

                        # Load image
                        self.image = Image.open("goHome.png")  # Replace "your_image.jpg" with the path to your image
                        self.image = self.image.resize((550, 520), Image.NEAREST)  # Resize the image without ANTIALIAS
                        self.photo = ImageTk.PhotoImage(self.image)

                        # Display image
                        self.image_label = Label(self, image=self.photo, borderwidth=0, highlightthickness=0)
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
                                synthesis_result = speech_synthesizer_en.speak_text_async(word).get()

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
                                            synthesis_result = speech_synthesizer_cn.speak_text_async("正确").get()
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
                                self.configure(bg="white")  # Set background color to white
                                self.controller = controller

                                # Button to navigate to the next page
                                button_next = tk.Button(self, text="下一個", font=("Cascadia Mono ExtraLight", 15),
                                                        width=15, height=1,
                                                        bg="light green",
                                                        command=lambda: controller.show_frame(Page24))
                                button_next.pack()
                                button_next.place(x=812, y=440, width=200, height=50)

                                # Button to navigate to the next page
                                button_next = tk.Button(self, text="上一頁", font=("Cascadia Mono ExtraLight", 15),
                                                        width=15, height=1,
                                                        bg="light green", command=lambda: controller.show_frame(Page22))
                                button_next.pack()
                                button_next.place(x=8, y=440, width=200, height=50)

                                button_next = tk.Button(self, text="Home Page 主页",
                                                        font=("Cascadia Mono ExtraLight", 15), width=15,
                                                        height=1,
                                                        bg="light green",
                                                        command=lambda: controller.show_frame(PageOne))
                                button_next.pack()
                                button_next.place(x=10, y=10, width=200, height=50)

                                # Run Code Button
                                button_run_code = tk.Button(self, bg="white", borderwidth=0, highlightthickness=0,
                                                            command=self.run_code2)
                                image = tk.PhotoImage(file="mc.png")  # Specify the path to your image file
                                button_run_code.config(image=image)
                                button_run_code.image = image  # Keep a reference to avoid garbage collection
                                button_run_code.pack()
                                button_run_code.place(x=762, y=0, width=250, height=250)

                                # Load image
                                self.image = Image.open(
                                    "haveDineer.png")  # Replace "your_image.jpg" with the path to your image
                                self.image = self.image.resize((550, 520),
                                                               Image.NEAREST)  # Resize the image without ANTIALIAS
                                self.photo = ImageTk.PhotoImage(self.image)

                                # Display image
                                self.image_label = Label(self, image=self.photo, borderwidth=0, highlightthickness=0)
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
                                        synthesis_result = speech_synthesizer_en.speak_text_async(word).get()

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
                                                        "正确").get()
                                                    break
                                                else:
                                                    # Incorrect recognition
                                                    if attempt < max_attempts:
                                                        # Synthesize "Wrong, please try again" in Chinese
                                                        print("Wrong, please try again.")
                                                        synthesis_result = speech_synthesizer_cn.speak_text_async(
                                                            "錯誤，請重試，圖中的東西是. Have Dinner").get()
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
                                vocabulary = ["Have Dinner", ]
                                tts_prompt_vocabulary(vocabulary)

class Page24(tk.Frame):
                                    def __init__(self, parent, controller):
                                        tk.Frame.__init__(self, parent)
                                        self.configure(bg="white")  # Set background color to white
                                        self.controller = controller

                                        # Button to navigate to the next page
                                        button_next = tk.Button(self, text="下一個",
                                                                font=("Cascadia Mono ExtraLight", 15), width=15,
                                                                height=1,
                                                                bg="light green",
                                                                command=lambda: controller.show_frame(Page25))
                                        button_next.pack()
                                        button_next.place(x=812, y=440, width=200, height=50)

                                        # Button to navigate to the next page
                                        button_next = tk.Button(self, text="上一頁",
                                                                font=("Cascadia Mono ExtraLight", 15), width=15,
                                                                height=1,
                                                                bg="light green",
                                                                command=lambda: controller.show_frame(Page23))
                                        button_next.pack()
                                        button_next.place(x=8, y=440, width=200, height=50)

                                        button_next = tk.Button(self, text="Home Page 主页",
                                                                font=("Cascadia Mono ExtraLight", 15), width=15,
                                                                height=1,
                                                                bg="light green",
                                                                command=lambda: controller.show_frame(PageOne))
                                        button_next.pack()
                                        button_next.place(x=10, y=10, width=200, height=50)

                                        # Run Code Button
                                        button_run_code = tk.Button(self, bg="white", borderwidth=0,
                                                                    highlightthickness=0,
                                                                    command=self.run_code2)
                                        image = tk.PhotoImage(file="mc.png")  # Specify the path to your image file
                                        button_run_code.config(image=image)
                                        button_run_code.image = image  # Keep a reference to avoid garbage collection
                                        button_run_code.pack()
                                        button_run_code.place(x=762, y=0, width=250, height=250)

                                        # Load image
                                        self.image = Image.open(
                                            "doHomework.png")  # Replace "your_image.jpg" with the path to your image
                                        self.image = self.image.resize((550, 520),
                                                                       Image.NEAREST)  # Resize the image without ANTIALIAS
                                        self.photo = ImageTk.PhotoImage(self.image)

                                        # Display image
                                        self.image_label = Label(self, image=self.photo, borderwidth=0,
                                                                 highlightthickness=0)
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
                                                synthesis_result = speech_synthesizer_en.speak_text_async(word).get()

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
                                                                "正确").get()
                                                            break
                                                        else:
                                                            # Incorrect recognition
                                                            if attempt < max_attempts:
                                                                # Synthesize "Wrong, please try again" in Chinese
                                                                print("Wrong, please try again.")
                                                                synthesis_result = speech_synthesizer_cn.speak_text_async(
                                                                    "錯誤，請重試，圖中的東西是. Do Homework").get()
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
                                        vocabulary = ["Do Homework", ]
                                        tts_prompt_vocabulary(vocabulary)
class Page25(tk.Frame):
                                            def __init__(self, parent, controller):
                                                tk.Frame.__init__(self, parent)
                                                self.configure(bg="white")  # Set background color to white
                                                self.controller = controller

                                                # Button to navigate to the next page
                                                button_next = tk.Button(self, text="下一個",
                                                                        font=("Cascadia Mono ExtraLight", 15), width=15,
                                                                        height=1,
                                                                        bg="light green",
                                                                        command=lambda: controller.show_frame(PageOne))
                                                button_next.pack()
                                                button_next.place(x=812, y=440, width=200, height=50)

                                                # Button to navigate to the next page
                                                button_next = tk.Button(self, text="上一頁",
                                                                        font=("Cascadia Mono ExtraLight", 15), width=15,
                                                                        height=1,
                                                                        bg="light green",
                                                                        command=lambda: controller.show_frame(Page24))
                                                button_next.pack()
                                                button_next.place(x=8, y=440, width=200, height=50)

                                                # Run Code Button
                                                button_run_code = tk.Button(self, bg="white", borderwidth=0,
                                                                            highlightthickness=0,
                                                                            command=self.run_code2)
                                                image = tk.PhotoImage(
                                                    file="mc.png")  # Specify the path to your image file
                                                button_run_code.config(image=image)
                                                button_run_code.image = image  # Keep a reference to avoid garbage collection
                                                button_run_code.pack()
                                                button_run_code.place(x=762, y=0, width=250, height=250)

                                                # Load image
                                                self.image = Image.open(
                                                    "gotoBed.png")  # Replace "your_image.jpg" with the path to your image
                                                self.image = self.image.resize((550, 520),
                                                                               Image.NEAREST)  # Resize the image without ANTIALIAS
                                                self.photo = ImageTk.PhotoImage(self.image)

                                                # Display image
                                                self.image_label = Label(self, image=self.photo, borderwidth=0,
                                                                         highlightthickness=0)
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
                                                        synthesis_result = speech_synthesizer_en.speak_text_async(
                                                            word).get()

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
                                                                        "正确").get()
                                                                    break
                                                                else:
                                                                    # Incorrect recognition
                                                                    if attempt < max_attempts:
                                                                        # Synthesize "Wrong, please try again" in Chinese
                                                                        print("Wrong, please try again.")
                                                                        synthesis_result = speech_synthesizer_cn.speak_text_async(
                                                                            "錯誤，請重試，圖中的東西是. Go to bed").get()
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
                                                vocabulary = ["Go to bed", ]
                                                tts_prompt_vocabulary(vocabulary)



from ScrambleWordGame import ScrambleWordGame  # Import the ScrambleWordGame class
class Page30(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")  # Set background color to white
        self.controller = controller

        # Load the background image
        image = Image.open("jungle.jpg")
        image = image.resize((1000, 550), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        # Create a label to hold the background image
        background_label = tk.Label(self, image=photo)
        background_label.image = photo  # Keep a reference to the image to prevent it from being garbage collected
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Button to navigate to the next page
        button_next = tk.Button(self, text="下一個",
                                font=("Cascadia Mono ExtraLight", 15), width=15,
                                height=1,
                                bg="light green",
                                command=lambda: controller.show_frame(PageThree))
        button_next.pack()
        button_next.place(x=812, y=440, width=200, height=50)

        # Button to navigate to the next page
        button_next = tk.Button(self, text="上一頁",
                                font=("Cascadia Mono ExtraLight", 15), width=15,
                                height=1,
                                bg="light green",
                                command=lambda: controller.show_frame(PageThree))
        button_next.pack()
        button_next.place(x=8, y=440, width=200, height=50)

        # Add the ScrambleWordGame widget to PageOne
        self.scramble_game = ScrambleWordGame(self)
        self.scramble_game.pack(pady=20)




from EnglishSpellingGame import EnglishSpellingGame  # Import the EnglishSpellingGame class
class Page31(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")  # Set background color to white
        self.controller = controller

        # Load the background image
        image = Image.open("jungle.jpg")
        image = image.resize((1000, 550), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        # Create a label to hold the background image
        background_label = tk.Label(self, image=photo)
        background_label.image = photo  # Keep a reference to the image to prevent it from being garbage collected
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Button to navigate to the next page
        button_next = tk.Button(self, text="下一個",
                                font=("Cascadia Mono ExtraLight", 15), width=15,
                                height=1,
                                bg="light green",
                                command=lambda: controller.show_frame(PageThree))
        button_next.pack()
        button_next.place(x=812, y=440, width=200, height=50)

        # Button to navigate to the next page
        button_next = tk.Button(self, text="上一頁",
                                font=("Cascadia Mono ExtraLight", 15), width=15,
                                height=1,
                                bg="light green",
                                command=lambda: controller.show_frame(PageThree))
        button_next.pack()
        button_next.place(x=8, y=440, width=200, height=50)

        # Add the EnglishSpellingGame widget to PageOne
        self.spelling_game = EnglishSpellingGame(self)
        self.spelling_game.pack(pady=20)






























class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Test Mode", font=("Ravie", 15))
        label.pack(pady=10, padx=10)


        button = tk.Button(self, text="Home Page", font=("Ravie", 15), width=15, height=1, bg="light green",
                           command=lambda: controller.show_frame(StartPage))
        button.pack(side="bottom", pady=20)





































import tkinter as tk
class PageThree(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")  # Set background color to white

        # Load the background image
        image = Image.open("jungle.jpg")
        image = image.resize((1000, 550), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        # Create a label to hold the background image
        background_label = tk.Label(self, image=photo)
        background_label.image = photo  # Keep a reference to the image to prevent it from being garbage collected
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        label = tk.Label(self, text="Games 遊戲", font=("Cascadia Mono ExtraLight", 15), width=15, height=1,
                         bg="white")
        label.pack(pady=10, padx=10)

        # Button to go to Home Page
        button_home = tk.Button(self, text="Home Page 首頁",font=("Cascadia Mono ExtraLight", 15), width=20,
                                height=1, bg="light green",
                                command=lambda: controller.show_frame(StartPage))
        button_home.pack(side="bottom", pady=10)

        button_home = tk.Button(self, text="Start Scrabled words",font=("Cascadia Mono ExtraLight", 15), width=20,
                                height=1, bg="light green",
                                command=lambda: controller.show_frame(Page30))
        button_home.pack(side="bottom", pady=10)

        button_home = tk.Button(self, text="Start SpellingGme",font=("Cascadia Mono ExtraLight", 15), width=20,
                                height=1, bg="light green",
                                command=lambda: controller.show_frame(Page31))
        button_home.pack(side="bottom", pady=10)





        # Button to start visual games (go to PageOne)
        button_visual_games = tk.Button(self,
                                        text="Start Visual Games (match text with picture) 開始視覺遊戲（將文字與圖片相配）",
                                        font=("Cascadia Mono ExtraLight", 15), width=70, height=1, bg="orange",
                                        command=lambda: controller.show_frame(PageFour))

        button_visual_games.pack(side="bottom", pady=10)



class PageFour(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")  # Set background color to white

        label = tk.Label(self, text="1", font=("Ravie", 25), bg="white")
        label.pack(pady=10, padx=10)

        # Button to go to PageTwo
        button_page_two = tk.Button(self, text="Next 下一個", font=("Ravie", 15), width=10, height=3,
                                    bg="light blue",
                                    command=lambda: controller.show_frame(PageFive))
        button_page_two.pack(side="bottom", pady=10)
        button_page_two.place(x=812, y=440)

        self.create_image_buttons()  # Create image buttons

        # Label to display the clicked button
        self.clicked_button_label = tk.Label(self, text="", font=("Helvetica", 18))
        self.clicked_button_label.pack()

        label = tk.Label(self, text="Car 車", font=("Ravie", 25), bg="white")
        label.pack(side="bottom", pady=20, padx=20)

    def create_image_buttons(self):
        # Create Button 1
        image_path_1 = "planne.jpg"  # Replace with the path to your image for Button 1
        image_1 = ImageTk.PhotoImage(file=image_path_1)
        button1 = tk.Button(self, text="", width=320, height=250, image=image_1, compound=tk.CENTER, bg="white",
                            borderwidth=0, highlightthickness=0,
                            command=lambda: self.button_click("Button 1", image_1))

        button1.pack()
        button1.place(x=8, y=150)

        # Create Button 2
        image_path_2 = "car.png"  # Replace with the path to your image for Button 2
        image_2 = ImageTk.PhotoImage(file=image_path_2)
        button2 = tk.Button(self, text="", width=320, height=250, image=image_2, compound=tk.LEFT, bg="white",
                            borderwidth=0, highlightthickness=0,
                            command=lambda: self.button_click("Button 2", image_2))
        button2.pack()
        button2.place(x=338, y=150)

        # Create Button 3
        image_path_3 = "bus.jpg"  # Replace with the path to your image for Button 3
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


class PageFive(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")  # Set background color to white

        label = tk.Label(self, text="2", font=("Ravie", 25), bg="white")
        label.pack(pady=10, padx=10)

        # Button to go to PageThree
        button_page_three = tk.Button(self, text="Next", font=("Ravie", 15), width=10, height=3, bg="light blue",
                                      command=lambda: controller.show_frame(PageSix))
        button_page_three.pack()
        button_page_three.place(x=812, y=440)

        self.create_image_buttons()  # Create image buttons

        # Label to display the clicked button
        self.clicked_button_label = tk.Label(self, text="", font=("Helvetica", 18))
        self.clicked_button_label.pack()

        label = tk.Label(self, text="Banana", font=("Ravie", 25), bg="white")
        label.pack(side="bottom", pady=20, padx=20)

    def create_image_buttons(self):
        # Create Button 1
        image_path_1 = "banana.jpg"  # Replace with the path to your image for Button 1
        image_1 = ImageTk.PhotoImage(file=image_path_1)
        button1 = tk.Button(self, text="", width=320, height=250, image=image_1, compound=tk.CENTER, bg="white",
                            borderwidth=0, highlightthickness=0,
                            command=lambda: self.button_click("Button 1", image_1))

        button1.pack()
        button1.place(x=8, y=150)

        # Create Button 2
        image_path_2 = "apple.png"  # Replace with the path to your image for Button 2
        image_2 = ImageTk.PhotoImage(file=image_path_2)
        button2 = tk.Button(self, text="", width=320, height=250, image=image_2, compound=tk.LEFT, bg="white",
                            borderwidth=0, highlightthickness=0,
                            command=lambda: self.button_click("Button 2", image_2))
        button2.pack()
        button2.place(x=338, y=150)

        # Create Button 3
        image_path_3 = "orange.jpg"  # Replace with the path to your image for Button 3
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
        self.configure(bg="white")  # Set background color to white

        label = tk.Label(self, text="3", font=("Ravie", 25), bg="white")
        label.pack(pady=10, padx=10)

        # Button to go to PageFive
        # Button to go to PageTwo
        button_page_two = tk.Button(self, text="Next", font=("Ravie", 15), width=10, height=3,
                                    bg="light blue",
                                    command=lambda: controller.show_frame(PageSeven))
        button_page_two.pack(side="bottom", pady=10)
        button_page_two.place(x=812, y=440)

        self.create_image_buttons()  # Create image buttons

        # Label to display the clicked button
        self.clicked_button_label = tk.Label(self, text="", font=("Helvetica", 18))
        self.clicked_button_label.pack()

        label = tk.Label(self, text="Teacher", font=("Ravie", 25), bg="white")
        label.pack(side="bottom", pady=20, padx=20)

    def create_image_buttons(self):
        # Create Button 1
        image_path_1 = "pilot.jpg"  # Replace with the path to your image for Button 1
        image_1 = ImageTk.PhotoImage(file=image_path_1)
        button1 = tk.Button(self, text="", width=320, height=250, image=image_1, compound=tk.CENTER, bg="white",
                            borderwidth=0, highlightthickness=0,
                            command=lambda: self.button_click("Button 1", image_1))

        button1.pack()
        button1.place(x=8, y=150)

        # Create Button 2
        image_path_2 = "painter.jpg"  # Replace with the path to your image for Button 2
        image_2 = ImageTk.PhotoImage(file=image_path_2)
        button2 = tk.Button(self, text="", width=320, height=250, image=image_2, compound=tk.LEFT, bg="white",
                            borderwidth=0, highlightthickness=0,
                            command=lambda: self.button_click("Button 2", image_2))
        button2.pack()
        button2.place(x=338, y=150)

        # Create Button 3
        image_path_3 = "teacher.jpg"  # Replace with the path to your image for Button 3
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
        self.configure(bg="white")  # Set background color to white

        label = tk.Label(self, text="4", font=("Ravie", 25), bg="white")
        label.pack(pady=10, padx=10)

        # Button to go to PageSix
        # Button to go to PageTwo
        button_page_two = tk.Button(self, text="Next", font=("Ravie", 15), width=10, height=3,
                                    bg="light blue",
                                    command=lambda: controller.show_frame(PageEight))
        button_page_two.pack(side="bottom", pady=10)
        button_page_two.place(x=812, y=440)

        self.create_image_buttons()  # Create image buttons

        # Label to display the clicked button
        self.clicked_button_label = tk.Label(self, text="", font=("Helvetica", 18))
        self.clicked_button_label.pack()

        label = tk.Label(self, text="Cow", font=("Ravie", 25), bg="white")
        label.pack(side="bottom", pady=20, padx=20)

    def create_image_buttons(self):
        # Create Button 1
        image_path_1 = "chicken.png"  # Replace with the path to your image for Button 1
        image_1 = ImageTk.PhotoImage(file=image_path_1)
        button1 = tk.Button(self, text="", width=320, height=250, image=image_1, compound=tk.CENTER, bg="white",
                            borderwidth=0, highlightthickness=0,
                            command=lambda: self.button_click("Button 1", image_1))

        button1.pack()
        button1.place(x=8, y=150)

        # Create Button 2
        image_path_2 = "cow.jpg"  # Replace with the path to your image for Button 2
        image_2 = ImageTk.PhotoImage(file=image_path_2)
        button2 = tk.Button(self, text="", width=320, height=250, image=image_2, compound=tk.LEFT, bg="white",
                            borderwidth=0, highlightthickness=0,
                            command=lambda: self.button_click("Button 2", image_2))
        button2.pack()
        button2.place(x=338, y=150)

        # Create Button 3
        image_path_3 = "dog.jpg"  # Replace with the path to your image for Button 3
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


class PageEight(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")  # Set background color to white

        label = tk.Label(self, text="5", font=("Ravie", 25), bg="white")
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

        label = tk.Label(self, text="Playing table tennis", font=("Ravie", 25), bg="white")
        label.pack(side="bottom", pady=20, padx=20)

    def create_image_buttons(self):
        # Create Button 1
        image_path_1 = "playFootball.jpg"  # Replace with the path to your image for Button 1
        image_1 = ImageTk.PhotoImage(file=image_path_1)
        button1 = tk.Button(self, text="", width=320, height=250, image=image_1, compound=tk.CENTER, bg="white",
                            borderwidth=0, highlightthickness=0,
                            command=lambda: self.button_click("Button 1", image_1))

        button1.pack()
        button1.place(x=8, y=150)

        # Create Button 2
        image_path_2 = "playVolleyball.jpg"  # Replace with the path to your image for Button 2
        image_2 = ImageTk.PhotoImage(file=image_path_2)
        button2 = tk.Button(self, text="", width=320, height=250, image=image_2, compound=tk.LEFT, bg="white",
                            borderwidth=0, highlightthickness=0,
                            command=lambda: self.button_click("Button 2", image_2))
        button2.pack()
        button2.place(x=338, y=150)

        # Create Button 3
        image_path_3 = "LPAYtBLEtENNIS.jpg"  # Replace with the path to your image for Button 3
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

