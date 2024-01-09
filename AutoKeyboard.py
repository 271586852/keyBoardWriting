# 写一段python代码，自动利用键盘输入内容

import pyautogui
import time

import win32gui
import win32con
import win32api

# 设置输入内容content
import pypinyin

# ret = win32api.ShellExecute(1, 'open', 'D:\\test.txt', '', '', 1)
print('正在打开软件...')
# time.sleep(2)
handle = win32gui.GetForegroundWindow()
handleEdit = win32gui.FindWindowEx(handle, None, 'EDIT', None)

# menu = win32gui.GetMenu(handle)
# subMenu = win32gui.GetSubMenu(menu, 0)


mystring=['北国风光，千里冰封，万里雪飘。',
'望长城内外，惟余莽莽；大河上下，顿失滔滔。',
'山舞银蛇，原驰蜡象，欲与天公试比高。',
'须晴日，看红装素裹，分外妖娆。',
'江山如此多娇，引无数英雄竞折腰。',
'惜秦皇汉武，略输文采；唐宗宋祖，稍逊风骚。',
'一代天骄，成吉思汗，只识弯弓射大雕。',
'俱往矣，数风流人物，还看今朝。','《沁园春·雪》']


# content1 = 'The Belt and Road initiative has presented unprecedented opportunities for China development. However, it is imperative for us to be well-prepared for the potential challenges it may bring. As college students in this new era, our role is crucial.Firstly, we must actively engage with the initiative, understanding its goals and implications. This involves acquiring knowledge about diverse cultures and economies, fostering a global perspective. Additionally, language skills become invaluable assets in facilitating international collaborations.Secondly, cultivating adaptability is essential. The initiative introduces a dynamic landscape, and being flexible in our approach will enable us to navigate the uncertainties that may arise. This includes developing skills in problem-solving, critical thinking, and cross-cultural communication.Moreover, embracing sustainability is pivotal. As future leaders, we should advocate for environmentally responsible practices within the initiative, ensuring long-term benefits without compromising the well-being of our planet.In conclusion, the "Belt and Road" initiative is a transformative force, and as proactive university students, we must equip ourselves with knowledge, adaptability, and a commitment to sustainability to effectively contribute to and navigate the opportunities and challenges it presents.'

# time.sleep(2)  # Wait for 2 seconds
# position = pyautogui.position()  # Get the current mouse position
# pyautogui.click(position.x, position.y, button='left')  # Click the mouse at the current position

for index, i in enumerate(mystring):
        for ch in i:
                print(ch)
                win32gui.SendMessage(handleEdit, win32con.WM_CHAR, ord(ch), 0)
                time.sleep(0.01)

            # Simulate pressing the Enter key
        win32api.keybd_event(13, 0, 0, 0)
        time.sleep(0.05)
        win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)

# Replace Chinese comma and period with newline character



# Print the Pinyin content
# print(pinyin_content)



# # 1.获取1秒钟后鼠标的位置
# time.sleep(2)
# position = pyautogui.position()
# print(pyautogui.position())

# # 2.将鼠标移动到指定位置 unp
# pyautogui.moveTo(position.x, position.y, duration=1)

# # 3.点击鼠标左键
# pyautogui.click(position.x, position.y, button='left')

# # 4.自动利用键盘输入内容
# pyautogui.typewrite(content1, interval=0.1)  # 设置输入间隔为0.1秒，以便输入汉字

# # 完成键入后打印完成
# print('Done')
