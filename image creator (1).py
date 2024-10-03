import os
import tkinter as tk
from tkinter import ttk, filedialog, simpledialog, colorchooser, messagebox
from PIL import Image, ImageDraw, ImageFont, ImageTk


def select_image():
    global image_path
    image_path = filedialog.askopenfilename(title="Select Image", filetypes=(("Image files", "*.jpg;*.jpeg;*.png"), ("All files", "*.*")))
    if image_path:
        img = Image.open(image_path)
        img.thumbnail((150, 150)) 
        img = ImageTk.PhotoImage(img)
        image_label.config(image=img)
        image_label.image = img  

def choose_save_directory():
    global save_directory
    save_directory = filedialog.askdirectory(title="Choose Save Directory")

def create_images():
    global image_path
    if image_path:
        text_position = simpledialog.askstring("Text Position", "Enter text position (x, y):").split(",")
        text_x = int(text_position[0])
        text_y = int(text_position[1])
        
        selected_font = font_combobox.get()
        font_size = simpledialog.askinteger("Font Size", "Enter font size:")
        font_color = colorchooser.askcolor(title="Choose Font Color")[1]
        font = ImageFont.truetype(selected_font, font_size)
        
        names = names_entry.get("1.0", tk.END).split('\n')
        
        for name in names:
            if name.strip(): 
                img = Image.open(image_path)
                img = img.convert("RGB")  
                
                draw = ImageDraw.Draw(img)

                name_to_display = arabic_reshaper.reshape(name)
                name_to_display = get_display(name_to_display)

                text_bbox = draw.textbbox((0, 0), name_to_display, font=font)

                text_width = text_bbox[2] - text_bbox[0]
                text_height = text_bbox[3] - text_bbox[1]

                text_x_center = text_x - text_width / 2
                text_y_center = text_y - text_height / 2

                draw.text((text_x_center, text_y_center), name_to_display, fill=font_color, font=font)
                
                save_path = os.path.join(save_directory, f"{name}.jpg")
                img.save(save_path, format="JPEG")
        
        messagebox.showinfo("Success", "Images created successfully!")

def paste_from_clipboard():
    clipboard_text = root.clipboard_get()
    names_entry.insert(tk.END, clipboard_text)

def copy_to_clipboard():
    selected_text = names_entry.get(tk.SEL_FIRST, tk.SEL_LAST)
    root.clipboard_clear()
    root.clipboard_append(selected_text)

root = tk.Tk()
root.title("Image Creator")

select_image_button = tk.Button(root, text="Select Image", command=select_image)
select_image_button.pack(pady=10)

image_label = tk.Label(root)
image_label.pack()

names_label = tk.Label(root, text="Enter names (one per line):")
names_label.pack()
names_entry = tk.Text(root, height=5)
names_entry.pack()

paste_button = tk.Button(root, text="Paste from Clipboard", command=paste_from_clipboard)
paste_button.pack(pady=5)

copy_button = tk.Button(root, text="Copy Selected Text", command=copy_to_clipboard)
copy_button.pack(pady=5)

font_label = tk.Label(root, text="Select Font:")
font_label.pack()
font_combobox = ttk.Combobox(root, values=os.listdir(r'C:\Windows\fonts'), width=50)
font_combobox.pack()

choose_save_dir_button = tk.Button(root, text="Choose Save Directory", command=choose_save_directory)
choose_save_dir_button.pack(pady=5)

create_images_button = tk.Button(root, text="Create Images", command=create_images)
create_images_button.pack(pady=10)

root.mainloop()