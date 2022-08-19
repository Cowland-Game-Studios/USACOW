import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os

window = tk.Tk()
window.geometry("200x300")
window.configure(background="black")
window.resizable(False, False)
window.title("USACODE V1")

options = [
    "Cpp",
    "Java",
    "Py",
]

selLangVal = tk.StringVar()
selLangVal.set("Cpp")

projectNameVal = tk.StringVar()
projectNameVal.set("Project_Name")

selPathVal = "/".join(os.path.dirname(os.path.realpath(__file__)).replace("\\", "/").split("/"))

a = tk.Label(text="Project Generator", bg="black", fg="white", font=("Helvetica", 16))
a.pack()

langSel = tk.OptionMenu(window, selLangVal, *options)
langSel.pack()

# pack last
pathSel = tk.Text(background="black", fg="white")
pathSel.insert('1.0', selPathVal)
pathSel.configure(state='disabled')

nameSel = tk.Entry(textvariable=projectNameVal, background="black", fg="white")
nameSel.pack(fill="x", pady=(5, 0))

def open_file_explorer():
    global selPathVal
    newPath = filedialog.askdirectory(initialdir=selPathVal)

    if (newPath == ""): return

    pathSel.configure(state='normal')
    pathSel.delete("1.0", tk.END)
    pathSel.insert('1.0', newPath)
    pathSel.configure(state='disabled')
    selPathVal = newPath

selPathButton = tk.Button(text="Browse Folder", command=open_file_explorer, bg="#262626", fg="white")
selPathButton.pack(pady=5)
pathSel.pack(fill="x")

def create_project():
    path = selPathVal + "/" + projectNameVal.get().capitalize()
    if os.path.isdir(path):
        messagebox.showinfo(title="Project Directory Exists!", message=f"Failed to create project: directory already in use. \nDirectory: {path}")
        return
    
    os.mkdir(path)

    with open(path + "/" + projectNameVal.get() + "." + selLangVal.get(), "w+") as f:
        with open("/".join(os.path.dirname(os.path.realpath(__file__)).replace("\\", "/").split("/")) + "/Templates/" + selLangVal.get() + "." + selLangVal.get(), "r") as template:
            f.writelines([x.replace("Project_Name", projectNameVal.get()) for x in template.readlines()])

    with open(path + "/" + projectNameVal.get() + ".in", "w+") as f:
        pass
    with open(path + "/" + projectNameVal.get() + ".out", "w+") as f:
        pass

    messagebox.showinfo(title="Project Created!", message=f"Created \"{projectNameVal.get()}\" project \nLanguage: {selLangVal.get()}\nAt: {path}")

createButton = tk.Button(text="Create USACO Project", command=create_project, bg="#91FFE0", bd=0, highlightthickness=0)
createButton.place(rely=1, anchor="sw", height=40, width=200)

window.mainloop()