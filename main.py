import dearpygui.dearpygui as dpg
import pyperclip as clip
import pyautogui

dpg.create_context()
dpg.create_viewport(title='pincopy', width=300, height=600)
with dpg.font_registry():
	with dpg.font("./fonts/SourceHanSansSC-Normal.otf", 30) as default_font:
		dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
		dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Full)
		dpg.add_font_range_hint(dpg.mvFontRangeHint_Japanese)
		dpg.add_font_range_hint(dpg.mvFontRangeHint_Korean)
		dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)
		dpg.add_font_range_hint(dpg.mvFontRangeHint_Thai)
		dpg.add_font_range_hint(dpg.mvFontRangeHint_Vietnamese)



with dpg.window(tag="Primary Window"):
	modep = dpg.add_slider_int(label="粘贴模式",tag="pmode",width=150,min_value=0,max_value=2,default_value=0)
	copyb = dpg.add_button(label="获取剪贴板",tag="cbutton",width=150)
	dpg.add_text("记录：")
	with dpg.table(header_row=True,resizable=True,borders_innerV=True,borders_innerH=True):
		dpg.add_table_column(label="删除")
		dpg.add_table_column(label="内容")

		# 测试
		with dpg.table_row():
			dpg.add_button(label="X")
			dpg.add_text("texttext")
		# 测试
		with dpg.table_row():
			dpg.add_button(label="X")
			dpg.add_text("texttext")
	...
	dpg.bind_font(default_font)

with dpg.tooltip('pmode'):
	dpg.add_text("分别为：\n仅复制\n下次点击ctrl+v\nalt+tab并ctrl+v")



dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()