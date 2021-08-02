import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import numpy as np

path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')


def file_opener():
    file_path_dic = filedialog.askopenfilename(
        filetypes=(("jpg file", "*.jpg"), ("png file", '*.png'), ("All files", "*.*"), ("jpeg file", "*.jpeg")))
    print(file_path_dic)
    file_path.delete('1.0', tk.END)
    file_path.insert(tk.END, file_path_dic)


def file_save_path_opener():
    file_save_path_dic = filedialog.askdirectory()
    global path
    path = file_save_path_dic


def process():
    path_of_file = file_path.get("1.0", tk.END)
    content = watermark_content.get("1.0", tk.END)
    if file_path.compare("end-1c", "==", "1.0") :
        messagebox.showerror("show error", "Please select the file")
    elif watermark_content.compare("end-1c", "==", "1.0"):
        messagebox.showwarning("show warning", "NO watermark")
    file_name_ = file_name.get("1.0", tk.END)
    font_size_ = size_of_font_value.get()
    format_of_image_ = format_of_image.get()
    path_of_file = path_of_file.strip('\n')
    content = content.strip('\n')
    file_name_ = file_name_.strip('\n')
    if file_name.compare("end-1c", "==", "1.0"):
        file_name_ = "/WaterMark"

    # Image water mark
    im = Image.open(path_of_file)
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype('arial.ttf', font_size_)
    draw.text((10,50), content, (255, 0, 0), font=font)

    file_name_ += format_of_image_
    file_name_ = '/'+file_name_
    final_path = path+file_name_

    if format_of_image_ == ".jpg":
        im = im.convert("RGB")
        im.save(final_path, 'JPEG')
    else:
        im.save(final_path)


def reset():
    file_path.delete('1.0', tk.END)
    watermark_content.delete('1.0', tk.END)
    file_name.delete('1.0', tk.END)
    font_size.set(14)


screen = tk.Tk()
screen.title("Watermark to Image")
screen.minsize(width=800, height=600)
screen.config(padx=20, pady=20, bg='#0A1931')

# file_path label
file_path_label = tk.Label(screen, text="Choose a file", font=("Montserrat", 16), bg="#0A1931", fg='#FFC947')
file_path_label.grid(sticky="W", row=0, column=0, padx=10)

# file_path
file_path = tk.Text(screen, width=35, height=1, font=("Courier New", 20), background="#EFEFEF")
file_path.grid(sticky="W", row=0, column=1, pady=10)

# file_path Button
browse = tk.Button(screen, text="Browse", font=("Montserrat", 18), highlightbackground="#185ADB", fg="#fff", width=10,
                   command=lambda: file_opener())
browse.grid(sticky="W", row=0, column=3, pady=10, padx=10)

# watermark content label
watermark_content_label = tk.Label(screen, text="Watermark Text", font=("Montserrat", 16), bg="#0A1931", fg='#FFC947')
watermark_content_label.grid(sticky="W", row=1, column=0, padx=10)

# watermark
watermark_content = tk.Text(screen, width=25, height=4, font=("Courier New", 20), background="#EFEFEF")
watermark_content.grid(sticky="W", row=1, column=1, pady=15)

# font size content label
font_size_label = tk.Label(screen, text="Font size", font=("Montserrat", 16), bg="#0A1931", fg='#FFC947', borderwidth=0)
font_size_label.grid(sticky="W", row=2, column=0, pady=15, padx=10)

size_of_font_value = tk.IntVar()
font_size = tk.Scale(screen, width=20, length=300, variable=size_of_font_value, from_=14, to=200, orient=tk.HORIZONTAL,
                     bg="#0A1931",
                     fg="#fceac2", font=("Montserrat", 18))
font_size.grid(sticky="W", row=2, column=1)

# format of the file

format_label = tk.Label(screen, text="File Format", font=("Montserrat", 16), bg="#0A1931", fg='#FFC947',
                        borderwidth=0)
format_label.grid(sticky="W", row=6, column=0, padx=10)

format_of_image = tk.StringVar()
format_R1 = tk.Radiobutton(screen, text=".jpg", variable=format_of_image, value=".jpg", bg="#0A1931", fg='#fceac2',
                           activeforeground='blue',
                           state="active")
format_R1.grid(sticky="W", row=5, column=1)

format_R2 = tk.Radiobutton(screen, text=".png", variable=format_of_image, value=".png", bg="#0A1931", fg='#fceac2',
                           activebackground='blue')
format_R2.grid(sticky="W", row=6, column=1)

format_R3 = tk.Radiobutton(screen, text=".bmp", variable=format_of_image, value=".bmp", bg="#0A1931", fg='#fceac2',
                           activebackground='blue')
format_R3.grid(sticky="W", row=7, column=1)

format_R4 = tk.Radiobutton(screen, text=".gif", variable=format_of_image, value=".gif", bg="#0A1931", fg='#fceac2',
                           activebackground='blue')
format_R4.grid(sticky="W", row=8, column=1)

#  file name of the file

file_name_label = tk.Label(screen, text="Save As", font=("Montserrat", 16), bg="#0A1931", fg='#FFC947')
file_name_label.grid(sticky="W", row=9, column=0, padx=10, pady=20)

file_name = tk.Text(screen, width=10, height=1, font=("Courier New", 20), background="#EFEFEF")
file_name.grid(sticky="W", row=9, column=1, pady=10)

file_name_default = tk.Label(screen, text="or Default(WaterMark)", font=("Montserrat", 14), bg="#0A1931", fg='#fceac2')
file_name_default.grid(row=9, column=1, padx=80)

#  save file of the file

save_file_label = tk.Label(screen, text="Save to", font=("Montserrat", 16), bg="#0A1931", fg='#FFC947')
save_file_label.grid(sticky="W", row=10, column=0, padx=10, pady=20)

save_file_path = tk.Button(screen, text="Path", font=("Montserrat", 18), highlightbackground="#185ADB", fg="#fff",
                           width=10, command=lambda: file_save_path_opener())
save_file_path.grid(sticky="W", row=10, column=1, pady=10)

save_file_default = tk.Label(screen, text="or Default(Desktop)", font=("Montserrat", 14), bg="#0A1931", fg='#fceac2')
save_file_default.grid(row=10, column=1, padx=80)

submit = tk.Button(screen, text="Submit", font=("Montserrat", 18), highlightbackground="#185ADB", fg="#fff",
                   width=10, command=process)
submit.grid(row=11, column=0, pady=30)

cancel = tk.Button(screen, text="Cancel", font=("Montserrat", 18), highlightbackground="red", fg="#fff",
                   width=10, command=reset)
cancel.grid(row=11, column=1, pady=30)

screen.mainloop()
