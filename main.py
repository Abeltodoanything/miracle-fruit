import tkinter as tk
import ttkbootstrap as ttk
import customtkinter as ctk

# Main window
window = ttk.Window(themename='flatly')
window.attributes('-topmost', True)
window.title("Auto Clicker")
window.resizable(False,False)
window_width = 565
window_height = 350
comp_width = window.winfo_screenwidth()
comp_height = window.winfo_screenheight()

left = int(comp_width / 2 - window_width / 2)
top = int(comp_height / 2 - window_height / 2)

window.geometry(f'{window_width}x{window_height}+{left}+{top}')

# Click interval FRAME

hours_var = ttk.IntVar(value=0)
mins_var = ttk.IntVar(value=0)
secs_var = ttk.IntVar(value=0)
miliseconds_var = ttk.IntVar(value=100)

click_rep_var = ttk.IntVar(value=0)

click_int = ttk.Labelframe(window, text='Click interval')
click_int.pack(pady=(10, 5), fill="x", padx=5)


hours_entry = ttk.Entry(click_int, width=7, justify='right', textvariable=hours_var)
hours_entry.grid(column=0, row=0, padx=4, pady=4)
hours_label = ttk.Label(click_int, text='hours')
hours_label.grid(column=1, row=0, padx=4, pady=4)

mins_entry = ttk.Entry(click_int, width=7, justify='right', textvariable=mins_var)
mins_entry.grid(column=2, row=0, padx=4, pady=4)
mins_label = ttk.Label(click_int, text='mins')
mins_label.grid(column=3, row=0, padx=4, pady=4)

secs_entry = ttk.Entry(click_int, width=7, justify='right', textvariable=secs_var)
secs_entry.grid(column=4, row=0, padx=4, pady=4)
secs_label = ttk.Label(click_int, text='secs')
secs_label.grid(column=5, row=0, padx=4, pady=4)

miliseconds_entry = ttk.Entry(click_int, width=7, justify='right', textvariable=miliseconds_var)
miliseconds_entry.grid(column=6, row=0, padx=4, pady=4)
miliseconds_label = ttk.Label(click_int, text='milliseconds')
miliseconds_label.grid(column=7, row=0, padx=4, pady=4,)

# Frame for options and repeat
opt_rep = ttk.Frame(window)
opt_rep.pack(pady=(10, 5), fill="x")
opt_rep.columnconfigure(0)
opt_rep.columnconfigure(1)
opt_rep.rowconfigure(0)


# Click options FRAME
click_opt = ttk.Labelframe(opt_rep, text='Click options')
click_opt.grid(column=0, row=0, padx=5, sticky='nsew')
click_opt.columnconfigure(0, weight=1)
click_opt.columnconfigure(1, weight=1)
click_opt.rowconfigure(0, weight=1)
click_opt.rowconfigure(1, weight=1)

opts = ['Left', 'Right', 'Middle']
clicktype = ['Single', 'Double']

mouse_button_label = ttk.Label(click_opt, text='Mouse button: ')
mouse_button_label.grid(column=0, row=0, padx=10, pady=5)

mouse_button_cb = ttk.Combobox(click_opt, values=opts, state='readonly')
mouse_button_cb.grid(column=1, row=0, padx=10, pady=5)
mouse_button_cb.current(0)


click_type_label = ttk.Label(click_opt, text='Mouse button: ')
click_type_label.grid(column=0, row=1, padx=10, pady=5)

click_type_cb = ttk.Combobox(click_opt, values=clicktype, state='readonly')
click_type_cb.grid(column=1, row=1, padx=10, pady=5)
click_type_cb.current(0)

# Click repeat FRAME
cr_rb = ttk.StringVar(value='repeat00')

click_rep = ttk.Labelframe(opt_rep, text='Click repeat')
click_rep.grid(column=1, row=0, padx=5, sticky='nsew')
click_rep.columnconfigure(0, weight=1)
click_rep.columnconfigure(1, weight=1)
click_rep.columnconfigure(2, weight=1)
click_rep.rowconfigure(0, weight=1)
click_rep.rowconfigure(1, weight=1)

repeat_rb = ttk.Radiobutton(click_rep, text='Repeat', variable=cr_rb, value='repeat')
repeat_rb.grid(column=0, row=0, padx=10, pady=5, sticky='w')

repeat_sb = ttk.Spinbox(click_rep, justify='center', width=5, textvariable=click_rep_var)
repeat_sb.grid(column=1, row=0, padx=5, pady=5, sticky='w')

repeat_label = ttk.Label(click_rep, text='times')
repeat_label.grid(column=2, row=0, padx=5, pady=5, sticky='w')

repeat_until = ttk.Radiobutton(click_rep, text='Repeat until stopped', variable=cr_rb, value='repeat00')
repeat_until.grid(column=0, row=1, padx=10, pady=5)


# Cursor position FRAME
cp_rb = ttk.StringVar(value='current')

cursor_pos = ttk.Labelframe(window, text='Cursor position')
cursor_pos.pack(pady=10,padx=5, fill='x')


current_location_rb = ttk.Radiobutton(cursor_pos, text='Current Location', variable=cp_rb, value='current')
current_location_rb.pack(side='left', padx=(5, 80), pady=5)


picklocation_rb = ttk.Radiobutton(cursor_pos, variable=cp_rb, value='pick')
picklocation_rb.pack(side='left', padx=5, pady=5)
pickloc_button = ttk.Button(cursor_pos, text='Pick location')
pickloc_button.pack(side='left', padx=5, pady=5)

x_pos = ttk.Label(cursor_pos, text='X').pack(side='left', padx=5, pady=5)
x_entry = ttk.Entry(cursor_pos, width=6)
x_entry.pack(side='left', padx=5, pady=5)
y_pos = ttk.Label(cursor_pos, text='Y').pack(side='left', padx=5, pady=5)
y_entry = ttk.Entry(cursor_pos, width=6)
y_entry.pack(side='left', padx=5, pady=5)

# Start/Stop | HotKey setting | Record & Playback
start_frame = ttk.Frame(window)
start_frame.pack(pady=(10, 5), fill="x")
start_frame.columnconfigure(0, weight=1)
start_frame.columnconfigure(1, weight=1)
start_frame.rowconfigure(0, weight=1)
start_frame.rowconfigure(1, weight=1)
# Example buttons, expand as needed
start = ttk.Button(start_frame, text="Start (PGDN)", width=50, )
start.grid(column=0, row=0, pady=7, padx=10)
stop = ttk.Button(start_frame, text="Stop (PGDN)", width=50, )
stop.grid(column=1, row=0, pady=7, padx=10)
set_hotkey = ttk.Button(start_frame, text="Set Hotkey", width=50, )
set_hotkey.grid(column=0, row=1, pady=7, padx=10)
record_playblack = ttk.Button(start_frame, text="Record & Playback", width=50, )
record_playblack.grid(column=1, row=1, pady=7, padx=10)


# run
window.mainloop()