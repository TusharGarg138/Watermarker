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

# ---------------- UI ----------------
root = Tk()
root.title("🔥 Add a Watermark Like a Boss 🔥")
root.geometry("550x500")
root.config(bg="#f0f0ff")


# Default selection
selected_color = StringVar()
selected_color.set("White")

# Image preview area
img_label = Label(root, bg="#f0f0ff")
img_label.pack(pady=10)

# Text input
Label(root, text="Enter Watermark Text:", bg="#f0f0ff", font=("Arial", 12)).pack()
text_entry = Entry(root, width=30, font=("Arial", 12))
text_entry.pack(pady=5)

# Color dropdown
Label(root, text="Choose Text Color:", bg="#f0f0ff", font=("Arial", 12)).pack()
color_menu = OptionMenu(root, selected_color, *colors.keys())
color_menu.pack(pady=5)

# Buttons
Button(root, text="Choose Image", command=choose_image, bg="#007acc", fg="white", font=("Arial", 12)).pack(pady=10)
Button(root, text="Save Watermarked Image", command=save_image, bg="#28a745", fg="white", font=("Arial", 12)).pack()

root.mainloop()
