import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os

window = tk.Tk()
window.geometry("200x300")
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

tk.Label(text="Project Generator").pack()

langSel = tk.OptionMenu(window, selLangVal, *options)
langSel.pack()

# pack last
pathSel = tk.Text()
pathSel.insert('1.0', selPathVal)
pathSel.configure(state='disabled')

nameSel = tk.Entry(textvariable=projectNameVal)
nameSel.pack()

def open_file_explorer():
    global selPathVal
    newPath = filedialog.askdirectory(initialdir=selPathVal)
    pathSel.configure(state='normal')
    pathSel.delete("1.0", tk.END)
    pathSel.insert('1.0', newPath)
    pathSel.configure(state='disabled')
    selPathVal = newPath

selPathButton = tk.Button(text="Browse Folder", command=open_file_explorer)
selPathButton.pack()
pathSel.pack()

def create_project():
    path = selPathVal + "/" + projectNameVal.get()
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

    messagebox.showinfo(title="Project Created!", message=f"Created \"{projectNameVal.get()}\" project \nLanguage: {selLangVal.get()}\nAt: {selPathVal}")

createButton = tk.Button(text="Create USACO Project", command=create_project)
createButton.place(rely=1, anchor="sw", height=40, width=200)

window.mainloop()