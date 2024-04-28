import tkinter as tk
from PIL import Image, ImageTk
import os


def button_click(button_number):
    # Replace these paths with the paths to your images for each choice
    if button_number == 1:
        image_path = "s1.png"
    elif button_number == 2:
        image_path = "apple.png"
    elif button_number == 3:
        image_path = "s1.png"


    # Load the image
    image = Image.open(image_path)
    image = image.resize((100, 100))  # Resize the image if needed

    # Convert the image to Tkinter format
    photo = ImageTk.PhotoImage(image)

    # Update the label to display the image
    response_label.config(image=photo)
    response_label.image = photo  # Keep a reference to prevent garbage collection

# Create a Tkinter window
root = tk.Tk()
root.title("Buttons with Images")
# Set initial window size
root.geometry("1000x550")

# Make the window non-resizable
root.resizable(False, False)

# Load the background image
image = Image.open("r11.jpg")
image = image.resize((1000, 550), Image.LANCZOS)
photo = ImageTk.PhotoImage(image)

# Create a label to hold the background image
background_label = tk.Label(root, image=photo)
background_label.image = photo  # Keep a reference to the image to prevent it from being garbage collected
background_label.place(x=0, y=0, relwidth=1, relheight=1)

label = tk.Label(root, text="Chair", font=("Helvetica", 18))
label.pack(side="bottom", pady=20, padx=20)

# Create Button 1
image_path_1 = "s1.png"  # Replace with the path to your image for Button 1
image_1 = ImageTk.PhotoImage(file=image_path_1)
button1 = tk.Button(root, text="Button 1", width=320, height=250, image=image_1, compound=tk.LEFT, command=lambda: button_click(1))
button1.pack()

# Create Button 2
image_path_2 = "s1.png"  # Replace with the path to your image for Button 2
image_2 = ImageTk.PhotoImage(file=image_path_2)
button2 = tk.Button(root, text="Button 2", width=320, height=250, image=image_2, compound=tk.LEFT, command=lambda: button_click(2))
button2.pack()

# Create Button 3
image_path_3 = "s1.png"  # Replace with the path to your image for Button 3
image_3 = ImageTk.PhotoImage(file=image_path_3)
button3 = tk.Button(root, text="Button 3", width=320, height=250, image=image_3, compound=tk.RIGHT, command=lambda: button_click(3))
button3.pack()

# Create Button 4
image_path_4 = "s1.png"  # Replace with the path to your image for Button 4
image_4 = ImageTk.PhotoImage(file=image_path_4)
button4 = tk.Button(root, text="button4", width=120, height=50, image=image_4, compound=tk.RIGHT)
button4.pack()



button1.place(x=8, y=150)
button2.place(x=338, y=150)
button3.place(x=667, y=150)
button4.place(x=867, y=480)


# Create a label to display the response
response_label = tk.Label(root, text="")
response_label.pack()

# Run the Tkinter event loop
root.mainloop()
