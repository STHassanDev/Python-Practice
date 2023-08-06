import tkinter as tk

class TempConverter:

    def __init__(self) -> None:
        
        self.wind = tk.Tk()

        self.wind.geometry("600x600")

        self.wind.config(bg='#800020')

        self.wind.title('Temperature Converter') 

        
        self.label = tk.Label(self.wind, text="Enter the temperature", font=('Arial', 16))
        self.label.grid(row=0, column=1)
        
        self.ent = tk.Entry(self.wind, font=("Arial",16)) # User enters temperature here
        self.ent.bind("<KeyPress>", self.convert)
        self.ent.grid(row=1,column=1)

        self.btn = tk.Button(self.wind, text="Convert", font=("Arial",18), command=self.convert) #Button for conversion
        self.btn.grid(row=2,column=1) 

        self.modes = ['Fahrenheit','Celsius','Kelvin']

        self.val = tk.StringVar(self.wind)

        self.modeMenu1 = tk.OptionMenu(self.wind,self.val,*self.modes)
        self.modeMenu1.grid(row=1, column=0)

        self.modeMenu2 = tk.OptionMenu(self.wind,self.val,*self.modes)
        self.modeMenu2.grid(row=1, column=2)

        # Configure all rows to center
        for i in range(3):
            self.wind.grid_rowconfigure(i, weight=1)

        # Configure all columns to center
        for j in range(3):
            self.wind.grid_columnconfigure(j, weight=1)


        self.wind.mainloop()

    def convert(self, event=None): #Need to add "Enter" as a shortcut
        """ 
        The plan is to have the function take two inputs, the 'number' that needs to be converted and the 'type' it is to 
        be converted to. It will only accept "Fahrenheit, Celsius and Kelvin" as valid arguements for the tpye parameter
        """
        
        if self.validate(self.ent.get()):
            print(self.ent.get())
        else:
            print("Your entry is not a number. Please Try Again")

    def validate(self,val): # This function will ensure the entry only accpets numbers and valid inputs
        if val=="": return True
        try:
            float(val)
            return True
        except ValueError:
            return False

Go = TempConverter()
