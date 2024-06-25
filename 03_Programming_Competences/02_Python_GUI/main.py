''' Python GUI Development ''' 

# 01. Import Libraries
import tkinter
# from tkinter import ttk

# 02. Import tkinter.Tk() Class which is a Toplevel widget of tkinter. it represents the window of the application. it has associated with Tcl interpreter
root = tkinter.Tk()

# 03. Configure the size of window
root.geometry("800x600") # width x height

# 04. Set title on the window
root.title("Graphical User Interface v1.0")

# 05. Create a menu bar: a child of root window
menubar = tkinter.Menu(master=root)
root.config(menu=menubar)

# 06. Create a menu: a child of menubar
file_menu = tkinter.Menu(
    master=menubar,
    tearoff=False # to remove the dashed line
)

# 07. Add a menu item to the file_menu | menu
file_menu.add_command(
    label="Exit",
    command=root.destroy
)

# 08. Add the File menu to the menu bar | Add a hierachical menu item to the menu bar
menubar.add_cascade(
    label="File",
    menu=file_menu
)

# 05. Import tkinter.Label() Class which is a label widget, it can display text and bitmaps
# label = tkinter.Label(
#     master=root, # the parent master | root window
#     font=("Arial",18), # style and size of the font
#     justify="center", # default: center, optional: left | right
#     # padx=20, # horizontal padding
#     # pady=20, # vertical padding
#     text="This Is Testing"
# )

# 06. Pack the Label into the window
# label.pack()

# 07. Import tkinter.Text() Class which is a text box widget, it can display text inside textbox with various settings
textbox = tkinter.Text(
    master=root,
    # bg="lightblue", # background color of the textbox
    font=("Arial",16),
    selectbackground="black"
)

# 08. Pack the child widget into the window
textbox.pack()

# Run the loop
root.mainloop()

######################################################################################################################

# ttk
# style = ttk.Style()
# style.configure(style="BW.TLabel")
