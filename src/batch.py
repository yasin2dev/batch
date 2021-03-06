import tkinter as tk
from tkinter import filedialog

root = tk.Tk()

cl = tk.Text()
cl["height"] = 16
cl["font"] = "Consolas", 10
cl.pack(side="top")

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.wlcm = tk.Label(self)
        self.abt = tk.Label(self)
        self.create = tk.Button(self)
        self.open = tk.Button(self)
        #
        self.open["text"] = "Open Batch File"
        self.open["font"] = "Arial", 12
        self.open["highlightthickness"] = 10
        self.open["borderwidth"] = 0
        self.open["bg"] = "#101010"
        self.open["fg"] = "#ffffff"
        self.open["command"] = self.openBatchFile
        #
        self.create["text"] = "Create batch file"
        self.create["font"] = "Arial", 12
        self.create["highlightthickness"] = 10
        self.create["borderwidth"] = 0
        self.create["bg"] = "#505050"
        self.create["fg"] = "#ffffff"
        self.create["command"] = self.saveBatchFile
        #
        self.abt["text"] = 'You can create here batch files.\n Write batch code to textarea and click "Create batch file" button.'
        self.abt["font"] = "Arial", 10
        #
        self.wlcm["text"] = "Welcome to Batch"
        self.wlcm["font"] = "Arial", 16
        ##
        self.wlcm.pack(side="top", pady=15)
        self.abt.pack(side="top")
        self.open.pack(side="bottom")
        self.create.pack(side="bottom", pady=15)

    def saveBatchFile(self):
        self.filetypes = (('Batch files', '*.bat'),('All files', '*.*'))
        self.fd = filedialog.asksaveasfile(mode="w", title="Select save directory and filename", initialdir="/Desktop", filetypes=self.filetypes, defaultextension="*.bat")
        self.data = str(cl.get(1.0, tk.END))
        self.fd.write(self.data)
        self.fd.close()

    def openBatchFile(self):
        cl.delete(1.0, tk.END)
        self.filetypes = (('Batch files', '*.bat'),('All files', '*.*'))
        self.fd = filedialog.askopenfilename(title="Select file to open", initialdir="/Desktop", filetypes=self.filetypes)
        self.fd = open(self.fd)
        self.data = self.fd.read()
        str(cl.insert(tk.END, self.data))
        self.title = self.master.wm_title
        self.fd.close()
        self.insertTitle(self.fd.name)
    
    def insertTitle(self, title):
        self.master.wm_title(title + " - Batch")

root.geometry("480x480")
root.wm_title("Batch")
root.resizable(0,0),
root.iconbitmap("../res/batch.ico")
app = App(master=root)
app.mainloop()