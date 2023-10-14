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

#reflash = 0
def delitem(sender,app_data,user_data):
	global cb
	del cb[user_data]
	reflash()

def copyit(sender,app_data,user_data):
	global cb
	thisdata = cb[user_data]
	#print(thisdata)
	if dpg.get_value(modec) == 0:
		clip.copy(thisdata)
	elif dpg.get_value(modec) == 1:
		pyautogui.hotkey('alt','tab')
		clip.copy(thisdata)
		pyautogui.hotkey('ctrl','v')
		pyautogui.hotkey('alt','tab')


def reflash():
	global cb
	dpg.delete_item("listtable", children_only=True)
	dpg.add_table_column(label="删除",parent="listtable")
	dpg.add_table_column(label="内容",parent="listtable")
	for i in range(len(cb)):
		with dpg.table_row(parent="listtable"):
			dpg.add_button(label="X",callback=delitem,user_data=i)
			dpg.add_button(label=cb[i],callback=copyit,user_data=i)

def getclip():
	if clip.paste() not in cb:
		cb.append(clip.paste())
		reflash()


with dpg.window(tag="Primary Window"):
	modec = dpg.add_slider_int(label="复制模式",tag="cmode",width=150,min_value=0,max_value=1,default_value=0)
	pasteb = dpg.add_button(label="获取剪贴板",tag="pbutton",width=150,callback=getclip)
	modep = dpg.add_checkbox(label="自动粘贴",tag="pmode")
	buttonr = dpg.add_button(label="手动刷新列表",tag="rbutton",width=150,callback=reflash)
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
	dpg.add_text("分别为：\n仅复制\nalt+tab并ctrl+v")



dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)

lastclip = 0

while dpg.is_dearpygui_running():
	if dpg.get_value(modep):
		#print('running')
		nowclip = clip.paste()
		if nowclip != lastclip and not nowclip in cb:
			cb.append(nowclip)
			lastclip = nowclip
		reflash()
	dpg.render_dearpygui_frame()


dpg.destroy_context()