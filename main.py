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



def choose_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
    if not file_path:
        return

    watermark_text = text_entry.get()
    if not watermark_text:
        watermark_text = "© YourName"

    chosen_color = colors[selected_color.get()]

    # Open image
    im = Image.open(file_path).convert("RGBA")
    txt_layer = Image.new("RGBA", im.size, (255, 255, 255, 0))
    font = ImageFont.truetype("arial.ttf", 40)

    draw = ImageDraw.Draw(txt_layer)

    # Draw watermark text in selected color
    draw.text((20, 20), watermark_text, font=font, fill=chosen_color)

    # Merge layers
    global watermarked_img
    watermarked_img = Image.alpha_composite(im, txt_layer).convert("RGB")

    # Resize for preview
    preview = watermarked_img.resize((400, 300))
    tk_img = ImageTk.PhotoImage(preview)
    img_label.config(image=tk_img)
    img_label.image = tk_img

def save_image():
    if watermarked_img:
        save_path = filedialog.asksaveasfilename(defaultextension=".jpg",
                                                filetypes=[("JPEG files", "*.jpg"), ("PNG files", "*.png")])
        if save_path:
            watermarked_img.save(save_path)
            print("Image saved at:", save_path)


