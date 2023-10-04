import dearpygui.dearpygui as dpg
import pyperclip as clip
import pyautogui

dpg.create_context()
dpg.create_viewport(title='pincopy', width=300, height=600)
with dpg.font_registry():
	with dpg.font("./fonts/SourceHanSansSC-Normal.otf", 30) as default_font:
		dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
		dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Full)



with dpg.window(tag="Primary Window"):
	modep = dpg.add_slider_int(label="粘贴模式",tag="pmode",width=150,min_value=0,max_value=3,default_value=0)
	copyb = dpg.add_button(label="获取剪贴板",tag="cbutton",width=150)
	dpg.add_text("记录：")
	...
	dpg.bind_font(default_font)

with dpg.tooltip('pmode'):
	dpg.add_text("分别为：\n仅复制\n下次点击ctrl+v\n下次点击paste()\n下次点击输入")



dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()