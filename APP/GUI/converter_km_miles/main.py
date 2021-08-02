import tkinter as tk


def calculate():
    miles_f = float(miles_input.get())
    km = round(miles_f * 1.609,2 )
    kilometer_convert.config(text=f"{km}")


window = tk.Tk()
window.title("Miles to Kilometer converter")
window.minsize(width=300, height=110)
window.config(padx=20, pady=20)


miles_input = tk.Entry(width=10)
miles_input.grid(row=0, column=1)

equal = tk.Label(text="is equal To", font=("Arial", 20))
equal.grid(row=1, column=0)

miles = tk.Label(text="Miles", font=("Arial", 18))
miles.grid(row=0, column=2)

kilometer_convert = tk.Label(text="0", font=("Arial", 20))
kilometer_convert.grid(row=1, column=1)

kilometer = tk.Label(text="km", font=("Arial", 18))
kilometer.grid(row=1, column=2)

button = tk.Button(text="calculate", command=calculate,highlightbackground="blue")
button.grid(row=2, column=1)

window.mainloop()
