def set_window_fullscreen(window):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    taskbar_height = get_taskbar_height()

    window.geometry(f"{screen_width}x{screen_height - taskbar_height}")

def get_taskbar_height():
    taskbar_height = 0

    if ctypes.windll.user32.GetSystemMetrics(0x02) != 0:  # 0x02 mengindikasikan taskbar di bawah
        taskbar_height = ctypes.windll.user32.GetSystemMetrics(0x02) 

    return taskbar_height