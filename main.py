import dearpygui.dearpygui as dpg
import pyperclip as clip
import pyautogui

cb = []

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

def topaste():
	cb.append('test')
	#print(cb)
	...

with dpg.window(tag="Primary Window"):
	modec = dpg.add_slider_int(label="粘贴模式",tag="cmode",width=150,min_value=0,max_value=2,default_value=0)
	pasteb = dpg.add_button(label="获取剪贴板",tag="pbutton",width=150,callback=topaste)
	dpg.add_text("记录：")
	with dpg.table(tag="listtable",header_row=True,resizable=True,borders_innerV=True,borders_innerH=True):
		dpg.add_table_column(label="删除")
		dpg.add_table_column(label="内容")
		
		'''
		print(cb)
		for i in range(len(cb)):
			with dpg.table_row():
				dpg.add_button(label="X",callback=lambda:cb.pop(i))
				dpg.add_button(label=cb[i])
		'''

		'''
		# 测试
		with dpg.table_row():
			dpg.add_button(label="X")
			dpg.add_button(label="texttext")
		# 测试
		with dpg.table_row():
			dpg.add_button(label="X")
			dpg.add_button(label="texttext")
		'''
	...
	dpg.bind_font(default_font)

with dpg.tooltip('cmode'):
	dpg.add_text("分别为：\n仅复制\n下次点击ctrl+v\nalt+tab并ctrl+v")



dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()