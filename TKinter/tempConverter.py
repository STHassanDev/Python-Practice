import tkinter as tk

class TempConverter:

    def __init__(self) -> None:
        
        self.wind = tk.Tk()

        self.wind.geometry("600x600")

        self.wind.title('Temperature Converter') 

        self.label = tk.Label(self.wind, text="Enter the temperature", font=('Arial', 16))
        self.label.pack(padx=10, pady=10)
        
        self.ent = tk.Entry(self.wind, font=("Arial",16), validate="key")
        self.ent.configure(validatecommand=self.wind.register(self.validate))
        self.ent.pack()

        self.btn = tk.Button(self.wind, text="Convert", font=("Arial",18), command=self.convert)
        self.btn.pack()

        self.wind.mainloop()

    def convert(self):
        if self.validate(self.ent.get()):
            print(self.ent.get())
        else:
            print("Your entry is not a number. Please Try Again")

    def validate(self,val):
        if val=="": return True
        try:
            float(val)
            return True
        except ValueError:
            return False

bop = TempConverter()
