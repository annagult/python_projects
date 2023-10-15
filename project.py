import tkinter as tk

root = tk.Tk()
root.geometry("500x500")
root.title("My GUI")

label = tk.Label(root, text="Put classes here", font=('Arial', 18))
label.pack(padx=20, pady=20)

textBox= tk.Text(root, height=1, font=('Arial',18))
textBox.pack(padx=10, pady=10)



buttonFrame= tk.Frame(root)
buttonFrame.columnconfigure(0,weight=1)
buttonFrame.columnconfigure(1,weight=1)
buttonFrame.columnconfigure(2,weight=1)

btn1 = tk.Button(buttonFrame,text="Click me", font=('Arial',16))
btn1.grid(row=0, column=0,sticky=tk.W+tk.E)
btn2 = tk.Button(buttonFrame,text="Click me", font=('Arial',16))
btn2.grid(row=0, column=1,sticky=tk.W+tk.E)

btn3 = tk.Button(buttonFrame,text="Click me", font=('Arial',16))
btn3.grid(row=1, column=0,sticky=tk.W+tk.E)
btn4 = tk.Button(buttonFrame,text="Click me", font=('Arial',16))
btn4.grid(row=1, column=1,sticky=tk.W+tk.E)

buttonFrame.pack(fill="x")
root.mainloop()