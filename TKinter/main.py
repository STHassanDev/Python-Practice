import tkinter as tk

wind = tk.Tk() #Intialize the GUI

wind.geometry("600x600") #Set the proportions of the window

wind.title("Siaka Traore is smart") #The name that shows up at the top of the window

label = tk.Label(wind, text="Hello World", font=('Times New Roman',18)) #The header for the gui
label.pack(padx=20,pady=20)

textbox = tk.Text(wind, height=5, font=("Arial",16)) # A text box that allows the user to type, 
textbox.pack(padx=10, pady=10)

button = tk.Button(wind, text="Convert", font=("Arial",18)) # A standard button. Does not have functionality 
button.pack()

buttonframe = tk.Frame(wind) # The framework for the way a series of buttons will be arranged in the gui. 
# FOllowed by the setup for 3 columns. 
buttonframe.columnconfigure(0, weight=1 )
buttonframe.columnconfigure(1, weight=1 )
buttonframe.columnconfigure(2, weight=1 )

#6 buttons total. 2 for each column
btn1 = tk.Button(buttonframe, text = '1', font=('Arial',18))
btn1.grid(row=0,column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(buttonframe, text = '2', font=('Arial',18))
btn2.grid(row=0,column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(buttonframe, text = '3', font=('Arial',18))
btn3.grid(row=0,column=2, sticky=tk.W+tk.E)

btn4 = tk.Button(buttonframe, text = '4', font=('Arial',18))
btn4.grid(row=1,column=0, sticky=tk.W+tk.E)

btn5 = tk.Button(buttonframe, text = '5', font=('Arial',18))
btn5.grid(row=1,column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonframe, text = '6', font=('Arial',18))
btn6.grid(row=1,column=2, sticky=tk.W+tk.E)

buttonframe.pack(fill='x')


wind.mainloop()

