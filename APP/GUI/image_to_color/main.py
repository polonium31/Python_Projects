import extcolors
import tkinter as tk
from tkinter import filedialog, messagebox


def rgbtohex(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'


def file_opener():
    file_path_dic = filedialog.askopenfilename(
        filetypes=(("jpg file", "*.jpg"), ("png file", '*.png'), ("All files", "*.*"), ("jpeg file", "*.jpeg")))
    file_path.delete('1.0', tk.END)
    file_path.insert(tk.END, file_path_dic)


def process():
    file_name_ = file_path.get("1.0", tk.END)
    if file_path.compare("end-1c", "==", "1.0"):
        messagebox.showerror("show error", "Please select the file")
    else:
        file_name_ = file_name_.strip('\n')
        print(file_name_)
        colors = extcolors.extract_from_path(file_name_)
        list =[]
        print(colors)
        print()
        for i in range(0, len(colors[0])):
            x = str(colors[0][i][0])
            x = x.replace('(', '')
            x = x.replace(')', '')
            x = x.split(",")
            list.append(rgbtohex(r=int(x[0]), g=int(x[1]), b=int(x[2])))
        one.config(background=str(list[0]), highlightbackground="black")
        one_label.config(text=str(list[0]))

        two.config(background=str(list[1]), highlightbackground="black")
        two_label.config(text=str(list[1]))

        three.config(background=str(list[2]), highlightbackground="black")
        three_label.config(text=str(list[2]))

        four.config(background=str(list[3]), highlightbackground="black")
        four_label.config(text=str(list[3]))

        five.config(background=str(list[4]), highlightbackground="black")
        five_label.config(text=str(list[4]))

        six.config(background=str(list[5]), highlightbackground="black")
        six_label.config(text=str(list[5]))

screen = tk.Tk()
screen.title("Image to color palette Generator")
screen.minsize(width=800, height=400)
screen.config(padx=20, pady=20, bg='#faf7e3')

# file_path label
file_path_label = tk.Label(screen, text="Choose a file", font=("Montserrat", 18), bg="#faf7e3", fg='black')
file_path_label.grid(sticky="W", row=0, column=0, padx=10)

# file_path
file_path = tk.Text(screen, width=35, height=1, font=("Courier New", 20), background="#EFEFEF",
                    highlightbackground="black", highlightthickness=2, bd=0)
file_path.grid(sticky="W", row=0, column=1, pady=10)

# file_path Button
browse = tk.Button(screen, text="Browse", font=("Montserrat", 18), highlightbackground="#185ADB", fg="#fff", width=10,
                   command=lambda: file_opener())
browse.grid(sticky="W", row=0, column=3, pady=10, padx=10)

generate = tk.Button(screen, text="Generate", font=("Montserrat", 18), highlightbackground="red", fg="#fff", width=10,
                     command=process)
generate.grid(row=1, column=1, pady=10, padx=10)

one_label = tk.Label(screen, text=" ", font=("Montserrat", 20), bg="#faf7e3", fg='black')
one_label.grid(sticky="W", row=2, column=0, padx=10)

one = tk.Text(screen, width=20, height=1, font=("Courier New", 24), background="#faf7e3", highlightbackground="#faf7e3",
              highlightthickness=1, bd=0)
one.grid(row=2, column=1, pady=10)

two_label = tk.Label(screen, text=" ", font=("Montserrat", 20), bg="#faf7e3", fg='black')
two_label.grid(sticky="W", row=3, column=0, padx=10)

two = tk.Text(screen, width=20, height=1, font=("Courier New", 24), background="#faf7e3", highlightbackground="#faf7e3",
              highlightthickness=1, bd=0)
two.grid(row=3, column=1, pady=10)

three_label = tk.Label(screen, text=" ", font=("Montserrat", 20), bg="#faf7e3", fg='black')
three_label.grid(sticky="W", row=4, column=0, padx=10)

three = tk.Text(screen, width=20, height=1, font=("Courier New", 24), background="#faf7e3", highlightbackground="#faf7e3",
                highlightthickness=1, bd=0)
three.grid(row=4, column=1, pady=10)

four_label = tk.Label(screen, text=" ", font=("Montserrat", 20), bg="#faf7e3", fg='black')
four_label.grid(sticky="W", row=5, column=0, padx=10)

four = tk.Text(screen, width=20, height=1, font=("Courier New", 24), background="#faf7e3", highlightbackground="#faf7e3",
               highlightthickness=1, bd=0)
four.grid(row=5, column=1, pady=10)

five_label = tk.Label(screen, text=" ", font=("Montserrat", 20), bg="#faf7e3", fg='black')
five_label.grid(sticky="W", row=6, column=0, padx=10)

five = tk.Text(screen, width=20, height=1, font=("Courier New", 24), background="#faf7e3", highlightbackground="#faf7e3",
               highlightthickness=1, bd=0)
five.grid(row=6, column=1, pady=10)

six_label = tk.Label(screen, text=" ", font=("Montserrat", 20), bg="#faf7e3", fg='black')
six_label.grid(sticky="W", row=7, column=0, padx=10)


six = tk.Text(screen, width=20, height=1, font=("Courier New", 24), background="#faf7e3", highlightbackground="#faf7e3",
              highlightthickness=1, bd=0)
six.grid(row=7, column=1, pady=10)

screen.mainloop()
