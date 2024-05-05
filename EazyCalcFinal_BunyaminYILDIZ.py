
"Bunyamin Fuat Yildiz Final Code."
import tkinter as tk
from tkinter import messagebox

class EazyCalc:
    def __init__(self, master):
        self.master = master
        self.master.title("EazyCalc")
        self.button_size = 2

        self.entry = tk.Entry(master, width=20, font=('Arial', 14))
        self.entry.grid(row=0, column=0, columnspan=4)

        # Buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', 'C', '=',
            '+', 'Settings'
        ]
        row = 1
        col = 0
        for button in buttons:
            if button == 'Settings':
                tk.Button(master, text=button, width=10, height=2, command=self.open_settings).grid(row=row, column=col, columnspan=2)
            else:
                tk.Button(master, text=button, width=5*self.button_size, height=2*self.button_size, command=lambda b=button: self.button_click(b)).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def button_click(self, value):
        current = self.entry.get()
        if value == 'C':
            self.entry.delete(0, tk.END)
        elif value == '=':
            try:
                result = eval(current)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            self.entry.insert(tk.END, value)
    
    def open_settings(self):
        settings_window = tk.Toplevel(self.master)
        settings_window.title("Settings")

        tk.Label(settings_window, text="Button Size Adjustment", font=('Arial', 12, 'bold')).pack(pady=10)

        # Button Size Scale
        tk.Scale(settings_window, from_=1, to=3, orient=tk.HORIZONTAL, label="Button Size", command=self.change_button_size).pack()

    def change_button_size(self, value):
        self.button_size = int(value)
        for widget in self.master.winfo_children():
            if isinstance(widget, tk.Button):
                widget.config(width=5*self.button_size, height=2*self.button_size)

def main():
    root = tk.Tk()
    app = EazyCalc(root)
    root.mainloop()

if __name__ == "__main__":
    main()
