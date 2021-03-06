import tkinter as tk

def dispLabel():
    lbl.configure(text="こんにちは")

root = tk.TK()
root.geometry("200*100")

lbl = tk.Label(text="LABEL")
btn = tk.Button(text="PUSH", command = dispLabel)

lbl.pack()
btn.pack()
tk.mainloop()