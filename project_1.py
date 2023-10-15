import tkinter as tk
from tkinter import messagebox

class MyGUI:
    def __init__(self):
        self.root=tk.Tk()



        self.label = tk.Label(self.root, text="Your message",font=('Arial',18))
        self.label.pack(padx=10,pady=10)

        self.TextBOx= tk.Text(self.root, height=1)
        self.TextBOx.bind("<KeyPress>", self.shortcut)
        self.TextBOx.pack(padx=10,pady=10)


        self.check_state= tk.IntVar()

        self.check = tk.Checkbutton(self.root, text="Show messagebox", font=('Arial',18), variable=self.check_state)
        self.check.pack(padx=10,pady=10)


        self.button = tk.Button(self.root,text="Show message",font=('Arial',18), command=self.show_message)
        self.button.pack(padx=10,pady=10)

        self.root.mainloop()
    
    def show_message(self):
        if self.check_state.get() == 0:
                print(self.TextBOx.get('1.0',tk.END))
        else:
             messagebox.showinfo(title="Message", message=self.TextBOx.get('1.0',tk.END))
    def shortcut(self,event):
         if event.state == 12 and event.keysym == "Return":
              self.show_message()
    
MyGUI()