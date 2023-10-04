import dearpygui.dearpygui as dpg
import pyperclip as clip
import pyautogui

dpg.create_context()
dpg.create_viewport(title='pincopy', width=600, height=300)
with dpg.font_registry():
	default_font = dpg.add_font("./fonts/SourceHanSansSC-Normal.otf", 35)

with dpg.window(tag="Primary Window"):
	dpg.add_text("Hello, world")
	...
	dpg.bind_font(default_font)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()