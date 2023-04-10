import tkinter as tk

class TempConverter:

    def __init__(self) -> None:
        
        self.wind = tk.Tk()

        self.wind.geometry("600x600")

        self.wind.title('Temperature Converter') 

        self.label = tk.Label(self.wind, text="Enter the temperature", font=('Arial', 16))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.wind, height=5, font=('Arial', 16))
        self.textbox.pack(padx=10, pady=10)

        

        self.wind.mainloop()

bop = TempConverter()
