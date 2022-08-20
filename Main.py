import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
from PIL import ImageTk, Image  

CurrentPath = "/".join(os.path.dirname(os.path.realpath(__file__)).replace("\\", "/").split("/"))

window = tk.Tk()
window.geometry("400x300")
window.configure(background="#262626")
window.resizable(False, False)
window.title("USACODE Project Creator")
window.tk.call('wm', 'iconphoto', window._w, tk.PhotoImage(file=CurrentPath + "/Images/TopIcon.png"))

#images
print(CurrentPath)
LogoImage = ImageTk.PhotoImage(image=Image.open(CurrentPath + "/Images/Logo.png").resize((125, 125)))
GenerateButtonImage = ImageTk.PhotoImage(image=Image.open(CurrentPath + "/Images/Buttons/Gen.png").resize((260, 50)))

options = [
    "Cpp",
    "Java",
    "Py",
]

selLangVal = tk.StringVar()
selLangVal.set("Cpp")

projectNameVal = tk.StringVar()
projectNameVal.set("Project_Name")

selPathVal = CurrentPath #set default dir

leftPanel = tk.Frame(window, bg="#262626")

tk.Label(leftPanel, image=LogoImage).place(x=0, y=150, anchor="nw", width=125, height=125)

rightPanel = tk.Frame(window, bg="#262626")

a = tk.Label(rightPanel, text="USACO Generator", bg="#262626", fg="white", font=("Helvetica", 12))
a.pack()

langSel = tk.OptionMenu(rightPanel, selLangVal, *options)
langSel.config(bg="#A9D6FF", bd=0, highlightthickness=0)
langSel.pack()

#if download sample data use url
#http://www.usaco.org/index.php?page=viewproblem2&cpid=
#cpid

# pack last
pathSel = tk.Text(rightPanel, background="#2d2d2d", fg="white", borderwidth=0, font=("Helvetica", 10))
pathSel.insert('1.0', selPathVal)
pathSel.configure(state='disabled')

nameSel = tk.Entry(rightPanel, textvariable=projectNameVal, background="#2d2d2d", borderwidth=0, fg="white", font=("Helvetica", 10))
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

selPathButton = tk.Button(rightPanel, text="Browse Folder", command=open_file_explorer, bg="#A9D6FF", font=("Helvetica", 10), bd=0, highlightthickness=0)
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

createButton = tk.Button(rightPanel, text="Create USACO Project", command=create_project, bg="#A9D6FF", bd=0, highlightthickness=0)
createButton.place(relx=1, rely=1, anchor="se", width=250, height=50)

leftPanel.place(x=0, y=0, width=125, height=300, anchor="w")
rightPanel.place(x=140, rely=0.5, anchor="w", height=280, width=240)

window.mainloop()