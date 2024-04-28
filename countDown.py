import tkinter as tk
from PIL import Image, ImageTk


class PictureViewerApp(tk.Tk):
    def __init__(self):
        # Initialize the Tkinter application
        super().__init__()

        # Set the size and title of the main window
        self.geometry("1000x550")
        self.resizable(False, False)
        self.title("Picture Viewer")

        # List of image file paths
        self.images = ["emo1.png", "emo2.png", "emo3.png"]

        # Index to keep track of the current image being displayed
        self.current_image_index = 0

        # Create a label widget to display images
        self.image_label = tk.Label(self)
        self.image_label.pack()

        # Button to start the picture loop
        self.start_button = tk.Button(self, text="Start Loop", command=self.start_picture_loop)
        self.start_button.pack()

    def start_picture_loop(self):
        # Disable the start button to prevent multiple clicks
        self.start_button.config(state=tk.DISABLED)

        # Start displaying images
        self.show_next_image()

    def show_next_image(self):
        # Check if all images have been displayed
        if self.current_image_index >= len(self.images):
            # Reset the index to start the loop again
            self.current_image_index = 0

        # Get the path of the current image
        image_path = self.images[self.current_image_index]

        # Open the image using PIL
        image = Image.open(image_path)

        # Resize the image to fit the window size without antialiasing
        image = image.resize((550, 550), Image.NEAREST)

        # Convert the image to Tkinter PhotoImage format
        photo = ImageTk.PhotoImage(image)

        # Display the image on the label
        self.image_label.config(image=photo)
        self.image_label.image = photo

        # Move to the next image after 1 second
        self.current_image_index += 1
        self.after(1000, self.show_next_image)


# Create an instance of the PictureViewerApp class and start the main event loop
app = PictureViewerApp()
app.mainloop()
