import tkinter as tk
import ttkbootstrap as ttk
import customtkinter as ctk

# Main window
window = ttk.Window(themename='darkly')
window.attributes('-topmost', True)
window.title("Auto Clicker")
window_width = 500
window_height = 600
comp_width = window.winfo_screenwidth()
comp_height = window.winfo_screenheight()

left = int(comp_width / 2 - window_width / 2)
top = int(comp_height / 2 - window_height / 2)

window.geometry(f'{window_width}x{window_height}+{left}+{top}')

# Click interval FRAME
click_int = ttk.Labelframe(window, text='Click interval')
click_int.pack(pady=(10, 5), fill="x")

hours_entry = ttk.Entry(click_int, width=7, justify='right')
hours_entry.grid(column=0, row=0, padx=4, pady=4)
hours_label = ttk.Label(click_int, text='hours')
hours_label.grid(column=1, row=0, padx=4, pady=4)

mins_entry = ttk.Entry(click_int, width=7, justify='right')
mins_entry.grid(column=2, row=0, padx=4, pady=4)
mins_label = ttk.Label(click_int, text='mins')
mins_label.grid(column=3, row=0, padx=4, pady=4)

secs_entry = ttk.Entry(click_int, width=7, justify='right')
secs_entry.grid(column=4, row=0, padx=4, pady=4)
secs_label = ttk.Label(click_int, text='secs')
secs_label.grid(column=5, row=0, padx=4, pady=4)

miliseconds_entry = ttk.Entry(click_int, width=7, justify='right')
miliseconds_entry.grid(column=6, row=0, padx=4, pady=4)
miliseconds_label = ttk.Label(click_int, text='milliseconds')
miliseconds_label.grid(column=7, row=0, padx=4, pady=4)

# Frame for options and repeat
opt_rep = ttk.Frame(window)
opt_rep.pack(pady=(10, 5), fill="x")

# Click options FRAME
click_opt = ttk.Labelframe(opt_rep, text='Click options')
click_opt.grid(column=1, row=0, padx=5, sticky='ew')
ttk.Button(click_opt, text='button').pack(fill="x", padx=10, pady=5)

# Click repeat FRAME
click_rep = ttk.Labelframe(opt_rep, text='Click repeat')
click_rep.grid(column=0, row=0, padx=5, sticky='ew')
ttk.Button(click_rep, text='button').pack(fill="x", padx=10, pady=5)

# Cursor position FRAME
cursor_pos = ttk.Labelframe(window, text='Cursor position')
cursor_pos.pack(pady=(10, 5), fill="x")
ttk.Button(cursor_pos, text='button').pack(fill="x", padx=10, pady=5)

# Start/Stop | HotKey setting | Record & Playback
start_frame = ttk.Frame(window)
start_frame.pack(pady=(10, 5), fill="x")
# Example buttons, expand as needed
ttk.Button(start_frame, text="Start").pack(side="left", expand=True, padx=10)
ttk.Button(start_frame, text="Stop").pack(side="left", expand=True, padx=10)
ttk.Button(start_frame, text="Set Hotkey").pack(side="left", expand=True, padx=10)
ttk.Button(start_frame, text="Record").pack(side="left", expand=True, padx=10)
ttk.Button(start_frame, text="Playback").pack(side="left", expand=True, padx=10)

# run
window.mainloop()