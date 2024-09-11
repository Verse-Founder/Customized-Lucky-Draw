import pandas as pd
import random
from PIL import Image, ImageTk
import PIL.Image
import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename

# Global variables
columns = ['Please upload a file...']
employeelist = None
data = []
global_image_path = None
is_run = False  # Define is_run as a global variable
going = False  # Define going as a global variable for lottery roll
lucky_draw_window_title = "Lucky Draw"  # Define a global variable to store the user-inputted title for the lucky draw window
ready_text = "Are You Ready?"
lucky_text = "Will You Be the Lucky One?"
congrats_text = "Congratulations!"

global photo  # Define a global variable to store the photo
photo = None
lucky_draw_window = None  # Declare lucky_draw_window as a global variable
title_entry = None  # Define title_entry as a global variable


# Function to update the dropdown menu with column names
def update_column_dropdown(column_names):
    menu = column_menu["menu"]
    menu.delete(0, "end")
    for name in column_names:
        menu.add_command(label=name, command=lambda value=name: column_var.set(value))
    column_var.set(column_names[0])  # Set the default value

# Function to update the names list based on the selected column
def update_names_list(*args):
    global data
    selected_column = column_var.get()
    if employeelist is not None and selected_column in employeelist.columns:
        data = employeelist[selected_column].dropna().tolist()

# Function to upload the Excel file and update the dropdown
def upload_file():
    file_path = askopenfilename(filetypes=[("Excel Files", "*.xlsx"), ("All Files", "*.*")])
    if file_path:
        global employeelist, columns
        employeelist = pd.read_excel(file_path)
        columns = employeelist.columns.tolist()
        update_column_dropdown(columns)
        update_names_list()  # Update names list for the default selected column

# Initialize the main window
root = tk.Tk()
root.withdraw()

def open_setting_window():
    global setting_window, bg_image, ready_entry, lucky_entry, congrats_entry
    # Declare setting_window as a global variable
    setting_window = tk.Toplevel(root) #创建了一个新的Tkinter窗口，作为主窗口root的子窗口（Toplevel表示顶级窗口）。这个新窗口被赋值给全局变量setting_window
    setting_window.title("Settings")
    setting_window.geometry("600x450")
    
    # Load the background image
    bg_image = PhotoImage(file="./xjtlu.png")

    # Create a Label with the background image
    bg_label = Label(setting_window, image=bg_image)
    bg_label.place(relwidth=1, relheight=1)

    # Frame to organize and group the text input fields
    text_frame = Frame(setting_window)
    text_frame.pack(pady=10)
    
    # Entry widgets for user input
    title_label = Label(text_frame, text="Title for Lucky Draw Window:")
    title_label.grid(row=0, column=0, pady=5, padx=5, sticky="w")
    title_entry = Entry(text_frame)
    title_entry.insert(0, lucky_draw_window_title)  # Default text
    title_entry.grid(row=0, column=1, pady=5, padx=5, sticky="w")                     
    
    ready_label = Label(text_frame, text="Are You Ready?")
    ready_label.grid(row=1, column=0, pady=5, padx=5, sticky="w")
    ready_entry = Entry(text_frame)
    ready_entry.insert(0, ready_text)  # Default text
    ready_entry.grid(row=1, column=1, pady=5, padx=5, sticky="w")

    lucky_label = Label(text_frame, text="Will You Be the Lucky One?")
    lucky_label.grid(row=2, column=0, pady=5, padx=5, sticky="w")
    lucky_entry = Entry(text_frame)
    lucky_entry.insert(0, lucky_text)  # Default text
    lucky_entry.grid(row=2, column=1, pady=5, padx=5, sticky="w")
    
    congrats_label = Label(text_frame, text="Congratulations!")
    congrats_label.grid(row=3, column=0, pady=5, padx=5, sticky="w")
    congrats_entry = Entry(text_frame)
    congrats_entry.insert(0, congrats_text)  # Default text
    congrats_entry.grid(row=3, column=1, pady=5, padx=5, sticky="w") 

    # Button to update the four variables
    update_title_and_text_button = tk.Button(setting_window, text="Update Lucky Draw Window Title", command=lambda: update_title_and_texts(title_entry.get(), ready_entry.get(), lucky_entry.get(), congrats_entry.get()))
    update_title_and_text_button.pack(pady=10)
    
    # Function to update the title for the lucky draw window
    def update_title_and_texts(new_title, new_ready_text, new_lucky_text, new_congrats_text):
        global lucky_draw_window_title, ready_text, lucky_text, congrats_text
        lucky_draw_window_title = new_title  # Get the inputted new title
        root.title(lucky_draw_window_title)  # Update the title of lucky_draw_window

        ready_text = new_ready_text
        lucky_text = new_lucky_text
        congrats_text = new_congrats_text
              
              
    file_button = tk.Button(setting_window, text="Select Excel File Contains Participants List", command=upload_file)
    file_button.pack(pady=10)
    
   
    global column_var, column_menu   # Global variables for column selection
    text_frame = Frame(setting_window)
    text_frame.pack(pady=10)
    column_label = Label(text_frame, text="Select Participants Column:") # Create a Label to display explanation text
    column_label.pack(side="left", pady=3, padx=3)  # Place the Label on the left side of the Frame with some padding
    column_var = StringVar(setting_window)   # Create a StringVar to store the selected column value
    column_var.trace("w", update_names_list)  # Add a trace to call the 'update_names_list' function whenever the selected column changes
    column_menu = OptionMenu(text_frame, column_var, *columns)  # Create an OptionMenu (dropdown menu) with the selected column variable and available columns
    column_menu.pack(side="left", pady=3, padx=3)  # Place the OptionMenu on the left side of the Frame with some padding
    
    
    # Create a button to allow users to select a background image
    image_button = tk.Button(setting_window, text="Select Background Image (1920*1080 is recommended)", command=upload_image)
    image_button.pack(pady=10)

    # Create a button to start the lucky draw
    start_button = tk.Button(setting_window, text="Start", command=start_lucky_draw)
    start_button.pack(pady=10)
    
    # Create an exit button
    end_button = tk.Button(setting_window, text="Exit", command=on_closing)
    end_button.pack(pady=10)

    # Function to upload the background image
def upload_image():
    global global_image_path
    image_path = askopenfilename(filetypes=(("Image files", "*.jpg;*.png"), ("All files", "*.*")))        
    global_image_path = image_path  # Update the global variable with the selected image path

# Function to start the lucky draw
def start_lucky_draw():
    global global_image_path, photo, title_entry, ready_entry, lucky_entry, congrats_entry, lucky_draw_window, ready_text, lucky_text, congrats_text, var1, var2

    def start_lottery():
        lottery_start(var1, var2)

    # Create a lucky draw window and set the window title with the previously stored lucky_draw_window_title
    lucky_draw_window = tk.Toplevel(root)
    lucky_draw_window.title(lucky_draw_window_title)  # Use the stored title
    lucky_draw_window.geometry('1920x1080')

    # Check if an image path is selected, otherwise use a default image
    if global_image_path:
        image_path = global_image_path
    else:
        image_path = "./Christmas_3.jpeg"  # Replace with the path to your default image

    image = PIL.Image.open(image_path)
    
    # Assuming 'image' is your PIL image object
    image = image.resize((1920, 1080), resample=PIL.Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(image)

    # Create a canvas to draw on
    canvas = Canvas(lucky_draw_window, width=1920, height=1080)
    canvas.pack(expand=True, fill=BOTH)
    canvas.create_image(0, 0, image=photo, anchor="nw")

    # Replace Labels with Text or Entry widgets for editable text
    var1 = StringVar(value=ready_entry.get())
    namelabel = Label(lucky_draw_window, textvariable=var1, anchor=CENTER, width=21, height=2, font='Arial -72 bold', foreground='black')
    namelabel.place(relx=.5, rely=.45, anchor="center")

    var2 = StringVar(value=lucky_entry.get())
    show_label2 = Label(lucky_draw_window, textvariable=var2, anchor=CENTER, width=25, height=2, font='Arial -60 bold', foreground='red')
    show_label2.place(relx=.5, rely=.65, anchor="center")
    
    # Add a 'End' button
    button_end = Button(lucky_draw_window, text='Stop', command=lambda: lottery_end(), width=12, height=2, bg='#A8A8A8', font='Arial -27 bold')
    button_end.place(relx=0.75, rely=0.8, anchor="center")

    # Add a 'Start' button
    start_button = Button(lucky_draw_window, text='Start', command=start_lottery, width=12, height=2, bg='#A8A8A8', font='Arial -27 bold')
    start_button.place(relx=0.25, rely=0.8, anchor="center")
    
    
    lucky_draw_window.state('zoomed')  # Set the window state to maximized

def on_closing():
    root.destroy()  # 关闭窗口
    # 这里可以执行一些清理工作
    exit()  # 结束程序

# Function to end the lottery
def lottery_end():
    global going, is_run
    going = False
    is_run = False

# Function to start the lottery
def lottery_start(var1, var2):
    global is_run, show_member, going
    if is_run:
        return
    is_run = True
    var2.set(lucky_entry.get())
    going = True
    lottery_roll(var1, var2)

# 修改 lottery_roll 函数以实现持续滚动名字
def lottery_roll(var1, var2):
    show_member = random.choice(data)
    var1.set(show_member)
    if going:
        root.after(50, lottery_roll, var1, var2)  # 使用 root.after 持续调用 lottery_roll
    else:
        var2.set(congrats_entry.get())
        choice = random.randrange(len(data))
        var1.set(data[choice])
        data.remove(data[choice])
        is_run = False
        return
    
if __name__ == '__main__':
    open_setting_window()
    root.mainloop()  # This starts the Tkinter event loop
