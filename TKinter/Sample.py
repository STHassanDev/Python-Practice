import tkinter as tk
from tkinter import messagebox

class GUI:
    def __init__(self) -> None:
        
        self.wind = tk.Tk()
        self.wind.title("Sample GUI")
        self.wind.geometry("600x600")

        self.menubar = tk.Menu(self.wind)

        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Close", command=self.onclosing)
        self.filemenu.add_command(label="Close without question", command=exit)

        self.actionmenu = tk.Menu(self.menubar, tearoff=0)
        self.actionmenu.add_command(label="Show Message             Control+Enter", command=self.show_message)
        self.actionmenu.add_command(label='Clear Textbox', command=self.clear)

        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.menubar.add_cascade(menu=self.actionmenu, label="Action")

        self.wind.config(menu=self.menubar)

        self.label= tk.Label(self.wind, text="Your Message", font=('Arial', 18))
        self.label.pack(padx=15, pady=15)

        self.textbox = tk.Text(self.wind, height=5, font=('Arial', 16))
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.bind("<KeyPress>", self.clear)
        self.textbox.pack(padx=10, pady=10)

        self.check_status = tk.IntVar()

        self.check = tk.Checkbutton(self.wind, text="Show Message Box", font=('Arial', 16), variable=self.check_status)
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.wind, text="Show Message", font=('Arial', 18), command=self.show_message)
        self.button.pack(padx=10, pady=10)

        self.clearbtn = tk.Button(self.wind, text="Clear", font=('Arial', 15), command=self.clear)
        self.clearbtn.pack(padx=10, pady=10)

        self.wind.protocol("WM_DELETE_WINDOW", self.onclosing)

        self.wind.mainloop()

    def show_message(self):
        if self.check_status.get()==0:
            print(self.textbox.get("1.0", tk.END))
        else:
            messagebox.showinfo(title="Message", message=self.textbox.get('1.0',tk.END ))

    def clear(self, event=None):
        if event==None:
            self.textbox.delete("1.0", tk.END)
        elif (event.state == 4 and event.keysym == 'BackSpace'):
            self.textbox.delete('1.0', tk.END)

    def shortcut(self, event):
        if event.state==4 and event.keysym=='Return':
            self.show_message()

    def onclosing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.wind.destroy()
      

ans = GUI()