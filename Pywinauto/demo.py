import pyautogui
import time
from pynput.keyboard import Controller
import pyperclip  # 用于操作剪贴板

# 打开应用程序（例如：通过 Spotlight 搜索）
# 在mac os中，实际上你需要在任何快捷键之前先按下command键，所以你需要在它们之间添加间隔。
pyautogui.hotkey('command', 'space', interval=0.25)  # 打开 Spotlight,
# 输入中文
# # 方法1：使用 pynput 库
# keyboard = Controller()
# keyboard.type('QQ音乐.app')

# 方法2：使用 pyperclip 将文本复制到剪贴板
pyperclip.copy('QQ音乐.app')
time.sleep(1)
# 输入英文
# pyautogui.write('QQ.app')  # 输入应用程序名称

# 粘贴剪贴板内容
pyautogui.hotkey('command', 'v', interval=0.25)
pyautogui.press('enter')  # 按下回车打开应用程序
time.sleep(5)

# 点击搜索框
region = (0, 0, 300, 400)
print(region)
search_position = pyautogui.locateOnScreen('./photos/iShot_2025-03-21_15.14.03.png', grayscale=True)  # 需要提前截取按钮图片
print(f"找到输入框，位置: {search_position}")
input_box_center = pyautogui.center(search_position)
pyautogui.click(input_box_center)

