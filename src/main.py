import customtkinter as ctk
from ctypes import windll, byref, sizeof, c_int
import pywinstyles

# ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")
#202020
#272727
app = ctk.CTk()
pywinstyles.apply_style(app, style="acrylic")
app.geometry("450x500")

# # title bar color
# HWND = windll.user32.GetParent(app.winfo_id())
# title_bar_color = 0x000000ff
# windll.dwmapi.DwmSetWindowAttribute(
#     HWND,
#     35,
#     byref(c_int(title_bar_color)),
#     sizeof(c_int)
# )


# dark_title_bar(app)

# def move_window(event):
#     app.geometry(f'+{event.x_root}+{event.y_root}')

# app.overrideredirect(True) # turns off title bar, geometry
# app.geometry('400x100+200+200') # set new geometry

# # make a frame for the title bar
# title_bar = ctk.CTkFrame(app)

# # put a close button on the title bar
# close_button = ctk.CTkButton(title_bar, text='X', width=50, command=app.destroy)

# # a canvas for the main area of the window
# window = ctk.CTkCanvas(app)

# # pack the widgets
# title_bar.pack(expand=1, fill="x")
# close_button.pack(side="right")
# window.pack(expand=1, fill="both")

# # bind title bar motion to the move window function
# title_bar.bind('<B1-Motion>', move_window)


# app.title("Login Interface")

# def login():
#     print("Testing login")

# frame = ctk.CTkFrame(master=app)
# frame.pack(pady=20, padx=60, fill="both", expand=True)

# label = ctk.CTkLabel(master=frame, text="Login System", font=("Roboto", 24))
# label.pack(pady=20, padx=10)

# entry1 = ctk.CTkEntry(master=frame, placeholder_text="Username")
# entry1.pack(pady=12, padx=10)

# entry2 = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*")
# entry2.pack(pady=12, padx=10)

# button = ctk.CTkButton(master=frame, text="Login", command=login)
# button.pack(pady=12, padx=10)

# checkbox = ctk.CTkCheckBox(master=frame, text="Remember me")
# checkbox.pack(pady=12, padx=10)

app.mainloop()