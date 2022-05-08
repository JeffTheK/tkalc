import tkinter as tk
from tkinter import ttk

class ButtonArea(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.button1 = tk.Button(self, text="1", command=lambda: add_to_entry("1"))
        self.button1.grid(row=2, column=0, sticky="nswe")
        self.button2 = tk.Button(self, text="2", command=lambda: add_to_entry("2"))
        self.button2.grid(row=2, column=1, sticky="nswe")
        self.button3 = tk.Button(self, text="3", command=lambda: add_to_entry("3"))
        self.button3.grid(row=2, column=2, sticky="nswe")

        self.button4 = tk.Button(self, text="4", command=lambda: add_to_entry("4"))
        self.button4.grid(row=1, column=0, sticky="nswe")
        self.button5 = tk.Button(self, text="5", command=lambda: add_to_entry("5"))
        self.button5.grid(row=1, column=1, sticky="nswe")
        self.button6 = tk.Button(self, text="6", command=lambda: add_to_entry("6"))
        self.button6.grid(row=1, column=2, sticky="nswe")

        self.button7 = tk.Button(self, text="7", command=lambda: add_to_entry("7"))
        self.button7.grid(row=0, column=0, sticky="nswe")
        self.button8 = tk.Button(self, text="8", command=lambda: add_to_entry("8"))
        self.button8.grid(row=0, column=1, sticky="nswe")
        self.button9 = tk.Button(self, text="9", command=lambda: add_to_entry("9"))
        self.button9.grid(row=0, column=2, sticky="nswe")

        self.button0 = tk.Button(self, text="0", command=lambda: add_to_entry("0"))
        self.button0.grid(row=3, column=0, sticky="nswe")

        self.separator1 = ttk.Separator(self, orient="vertical")
        self.separator1.grid(row=0, column=3, columnspan=5, sticky="ns", padx=5)

        self.button_plus = tk.Button(self, text="+", command=lambda: add_to_entry("+"))
        self.button_plus.grid(row=0, column=4, sticky="nswe")
        self.button_minus = tk.Button(self, text="-", command=lambda: add_to_entry("-"))
        self.button_minus.grid(row=0, column=5, sticky="nswe")

        self.button_multiply = tk.Button(self, text="*", command=lambda: add_to_entry("*"))
        self.button_multiply.grid(row=1, column=4, sticky="nswe")
        self.button_divide = tk.Button(self, text="-", command=lambda: add_to_entry("/"))
        self.button_divide.grid(row=1, column=5, sticky="nswe")

        self.button_equals = tk.Button(self, text="=", command=lambda: evaluate_entry(), bg="navajo white")
        self.button_equals.grid(row=2, column=4, columnspan=2, sticky="nswe")

        self.clear_button = tk.Button(self, text="C", command=lambda: entry.delete(0, "end"), fg="red")
        self.clear_button.grid(row=0, column=6, sticky="nswe")

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=1)
        self.columnconfigure(5, weight=1)
        self.columnconfigure(6, weight=1)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
    

def add_to_entry(string):
    global entry
    if string in ["+", "-", "/", "*"] and entry.get().endswith(("+", "-", "/", "*")):
        return
    entry.insert("end", string)

def evaluate_entry():
    text = entry.get()

    if text == "":
        return

    if text.endswith(("+", "-", "/", "*")):
        text = text[:-1]

    result = eval(text)
    entry.delete(0, "end")
    entry.insert(0, result)

    global previous_evaluations_area
    previous_evaluations_area.insert("end", f"{text} = {result}")
    previous_evaluations_area.yview("end")

root = tk.Tk()
root.title("TKalc")
root.geometry("400x350")

previous_evaluations_area = tk.Listbox(root, height=5, font="Arial 12")
previous_evaluations_area.pack_propagate(False)
previous_evaluations_area.grid(row=0, column=0, padx=5, pady=5, sticky="we")
scrollbar = tk.Scrollbar(previous_evaluations_area)
scrollbar.pack(side="right", fill="y")
previous_evaluations_area.config(yscrollcommand = scrollbar.set)

button_area = ButtonArea(root)
button_area.grid(row=2, column=0, sticky="nwes")
root.rowconfigure(2, weight=1)

entry = tk.Entry(root, font="Helvetica 18")
entry.grid(row=1, column=0, sticky="we")
root.columnconfigure(0, weight=1)

root.mainloop()