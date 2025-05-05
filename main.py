from tkinter import Tk, filedialog, Label, Button, Entry, StringVar, OptionMenu
from PIL import Image, ImageTk, ImageDraw, ImageFont

# Global to store final image
watermarked_img = None

# Define some fun colors for text
colors = {
    "White": (255, 255, 255, 180),
    "Red": (255, 0, 0, 180),
    "Blue": (0, 0, 255, 180),
    "Green": (0, 255, 0, 180),
    "Yellow": (255, 255, 0, 180),
    "Pink": (255, 105, 180, 180)
}



