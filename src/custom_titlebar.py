import tkinter as tk

# --- constants --- (UPPER_CASE_NAMES)

# title bar colors
TITLE_FOREGROUND = "white"
TITLE_BACKGROUND = "#2c2c2c"
TITLE_BACKGROUND_HOVER = "green"

BUTTON_FOREGROUND = "white"
BUTTON_BACKGROUND = TITLE_BACKGROUND
BUTTON_FOREGROUND_HOVER = BUTTON_FOREGROUND
BUTTON_BACKGROUND_HOVER = 'red'

# window colors
WINDOW_BACKGROUND = "white"
WINDOW_FOREGROUND = "black"

# --- classes --- (CamelCaseNames)

class MyButton(tk.Button):

    def __init__(self, master, text='x', command=None, **kwargs):
        super().__init__(master, bd=0, font="bold", padx=5, pady=2, 
                         fg=BUTTON_FOREGROUND, 
                         bg=BUTTON_BACKGROUND,
                         activebackground=BUTTON_BACKGROUND_HOVER,
                         activeforeground=BUTTON_FOREGROUND_HOVER, 
                         highlightthickness=0, 
                         text=text,
                         command=command)

        self.bind('<Enter>', self.on_enter)
        self.bind('<Leave>', self.on_leave)

    def on_enter(self, event):
        self['bg'] = BUTTON_BACKGROUND_HOVER

    def on_leave(self, event):
        self['bg'] = BUTTON_BACKGROUND

class MyTitleBar(tk.Frame):

    def __init__(self, master, *args, **kwargs):
        super().__init__(master, relief='raised', bd=1, 
                         bg=TITLE_BACKGROUND,
                         highlightcolor=TITLE_BACKGROUND, 
                         highlightthickness=0)

        self.title_label = tk.Label(self, 
                                    bg=TITLE_BACKGROUND, 
                                    fg=TITLE_FOREGROUND)
                                    
        self.set_title("Title Name")

        self.close_button = MyButton(self, text='x', command=master.destroy)
        self.minimize_button = MyButton(self, text='-', command=self.on_minimize)
        self.other_button = MyButton(self, text='#', command=self.on_other)
                         
        self.pack(expand=True, fill='x')
        self.title_label.pack(side='left')
        self.close_button.pack(side='right')
        self.minimize_button.pack(side='right')
        self.other_button.pack(side='right')

        self.bind("<ButtonPress-1>", self.on_press)
        self.bind("<ButtonRelease-1>", self.on_release)
        self.bind("<B1-Motion>", self.on_move)
        
    def set_title(self, title):
        self.title = title
        self.title_label['text'] = title
        
    def on_press(self, event):
        self.xwin = event.x
        self.ywin = event.y
        self.set_title("Title Name - ... I'm moving! ...")
        self['bg'] = 'green'
        self.title_label['bg'] = TITLE_BACKGROUND_HOVER

    def on_release(self, event):
        self.set_title("Title Name")
        self['bg'] = TITLE_BACKGROUND
        self.title_label['bg'] = TITLE_BACKGROUND
        
    def on_move(self, event):
        x = event.x_root - self.xwin
        y = event.y_root - self.ywin
        self.master.geometry(f'+{x}+{y}')
        
    def on_minimize(self):
        print('TODO: minimize')
                
    def on_other(self):
        print('TODO: other')

# --- functions ---

# empty

# --- main ---

root = tk.Tk()
# turns off title bar, geometry
root.overrideredirect(True)

# set new geometry
root.geometry('400x100+200+200')

title_bar = MyTitleBar(root) 
#title_bar.pack()  # it is inside `TitleBar.__init__()`

# a canvas for the main area of the window
window = tk.Canvas(root, bg=WINDOW_BACKGROUND, highlightthickness=0)

# pack the widgets
window.pack(expand=True, fill='both')

root.mainloop()