import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTK

def dispPhoto(path):

    newImage = PIL.Image.open(path).resize((300,300))
    imageData = PIL.ImageTK.PhotoImage(newImage)
    imageLabel.configure(image = imageData)
    imageLabel.image = imageData

def openFile():
    fpath = fd.askopenfilename()

    if fpath:
        dispPhoto(fpath)

root = tk.Tk()
root.geometry("400*350")

btn = tk.Button(text="フアイルを開く", command = openFile)
imageLabel = tk.Label()
btn.pack()
imageLabel.pack()
tk.mainloop()

