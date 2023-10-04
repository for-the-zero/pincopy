import dearpygui as dpg
import pyperclip as pc
import pyautogui

dpg.create_context()
with dpg.window(tag="Primary Window"):
	...
dpg.create_viewport(title='pincopy', width=400, height=400)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()