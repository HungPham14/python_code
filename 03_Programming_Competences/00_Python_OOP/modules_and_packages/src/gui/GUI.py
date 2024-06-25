'''Python GUI version 1.0 Development by Hung Pham'''
import tkinter 
class textbox_window:
    '''Text widget which can display, write, save text as a notepad'''
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("800x600")
        self.root.title("Graphical User Interface v1.0")
        self.menubar = tkinter.Menu(master=self.root)
        self.root.config(menu=self.menubar)
        self.file_menu =  tkinter.Menu(master=self.menubar,tearoff=False)
        self.file_menu.add_command(label="Exit",command=self.root.destroy)
        self.menubar.add_cascade(label="File",menu=self.file_menu)
        self.textbox=tkinter.Text(master=self.root,font=("Arial",16),selectbackground="black").pack()
        self.root.mainloop()

if __name__ == "__main__":
    try:
        textbox_window()
    except:
        print("Error...")