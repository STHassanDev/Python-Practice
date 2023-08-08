import tkinter as tk

class TempConverter:

    def __init__(self) -> None:
        
        self.wind = tk.Tk()

        self.wind.geometry("600x600")

        self.wind.config(bg='#E0FFFF')

        self.wind.title('Temperature Converter') 

        #Text Widget
        self.label = tk.Label(self.wind, text="Enter the temperature", font=('Arial', 16),bg='#E0FFFF')
        self.label.grid(row=0, column=1)
        
        #Temperature Input Widget
        self.ent = tk.Entry(self.wind, font=("Arial",16)) # User enters temperature here
        self.ent.bind("<KeyPress>", self.convert)
        self.ent.grid(row=1,column=1)

        #Convert Button Widget
        self.btn = tk.Button(self.wind, text="Convert", font=("Arial",18), command=self.convert) #Button for conversion
        self.btn.grid(row=2,column=1) 

        #Result Widget
        self.result = tk.Label(self.wind, text="", font=("Arial", 18, "bold"), bg='#E0FFFF')
        self.result.grid(row=3, column=1)

        """# Configure all rows to center
        for i in range(3):
            self.wind.grid_rowconfigure(i, weight=1)

        # Configure all columns to center
        for j in range(3):
            self.wind.grid_columnconfigure(j, weight=1)
        """

        self.wind.mainloop()

    def convert(self): #Need to add "Enter" as a shortcut
        try:
            self.result.config(text=f"{self.ent.get()}")

        except ValueError:
            self.result.config(text="Invalid Entry: Please Try again")
Go = TempConverter()
