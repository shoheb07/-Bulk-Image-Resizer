import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

selected_files = []
output_folder = ""


def select_images():
    global selected_files
    selected_files = filedialog.askopenfilenames(
        title="Select Images",
        filetypes=[
            ("Image Files", "*.jpg *.jpeg *.png *.bmp *.gif *.tiff *.webp")
        ]
    )
    lbl_files.config(text=f"{len(selected_files)} image(s) selected")


def select_output():
    global output_folder
    output_folder = filedialog.askdirectory(title="Select Output Folder")
    if output_folder:
        lbl_output.config(text=output_folder)


def resize_images():
    if not selected_files:
        messagebox.showerror("Error", "Please select images.")
        return

    if not output_folder:
        messagebox.showerror("Error", "Please select output folder.")
        return

    try:
        width = int(width_entry.get())
        height = int(height_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Width and Height must be numbers.")
        return

    success = 0

    for file in selected_files:
        try:
            img = Image.open(file)
            resized = img.resize((width, height), Image.Resampling.LANCZOS)

            filename = os.path.basename(file)
            save_path = os.path.join(output_folder, filename)

            resized.save(save_path)
            success += 1

        except Exception as e:
            print(e)

    messagebox.showinfo(
        "Completed",
        f"{success} image(s) resized successfully."
    )


root = tk.Tk()
root.title("Bulk Image Resizer")
root.geometry("450x350")
root.resizable(False, False)

title = tk.Label(
    root,
    text="Bulk Image Resizer",
    font=("Arial", 18, "bold")
)
title.pack(pady=15)

tk.Button(
    root,
    text="Select Images",
    width=20,
    command=select_images
).pack()

lbl_files = tk.Label(root, text="No images selected")
lbl_files.pack(pady=5)

tk.Label(root, text="Width").pack()
width_entry = tk.Entry(root)
width_entry.pack()

tk.Label(root, text="Height").pack()
height_entry = tk.Entry(root)
height_entry.pack()

tk.Button(
    root,
    text="Select Output Folder",
    width=20,
    command=select_output
).pack(pady=10)

lbl_output = tk.Label(root, text="No output folder selected")
lbl_output.pack()

tk.Button(
    root,
    text="Resize Images",
    bg="green",
    fg="white",
    width=20,
    command=resize_images
).pack(pady=20)

root.mainloop()
