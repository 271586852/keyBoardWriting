# 写一段python代码，自动利用键盘输入内容

import pyautogui
import time

# 设置输入内容content
import pypinyin

content = '昨天我看了一个非常有趣的电视节目。它是关于一群朋友，他们住在一个没有太多方式来打发时间的小镇。所以他们决定建立一个社区组织，人们可以来这里看电影，做运动，交朋友，学习新事物。我住的小镇很安静，很无聊，所以这个节目启发了我。也许我可以做类似的事情。'  # Chinese characters

content1 = 'The Belt and Road initiative has presented unprecedented opportunities for China development. However, it is imperative for us to be well-prepared for the potential challenges it may bring. As college students in this new era, our role is crucial.Firstly, we must actively engage with the initiative, understanding its goals and implications. This involves acquiring knowledge about diverse cultures and economies, fostering a global perspective. Additionally, language skills become invaluable assets in facilitating international collaborations.Secondly, cultivating adaptability is essential. The initiative introduces a dynamic landscape, and being flexible in our approach will enable us to navigate the uncertainties that may arise. This includes developing skills in problem-solving, critical thinking, and cross-cultural communication.Moreover, embracing sustainability is pivotal. As future leaders, we should advocate for environmentally responsible practices within the initiative, ensuring long-term benefits without compromising the well-being of our planet.In conclusion, the "Belt and Road" initiative is a transformative force, and as proactive university students, we must equip ourselves with knowledge, adaptability, and a commitment to sustainability to effectively contribute to and navigate the opportunities and challenges it presents.'
# Convert Chinese characters to Pinyin
pinyin_content = pypinyin.lazy_pinyin(content)
pinyin_text = ''.join(pinyin_content)

# Replace Chinese comma and period with newline character
pinyin_text = pinyin_text.replace('，', '  ')
pinyin_text = pinyin_text.replace('。', '  ')

print(pinyin_text)


# Print the Pinyin content
# print(pinyin_content)



# 1.获取1秒钟后鼠标的位置
time.sleep(2)
position = pyautogui.position()
print(pyautogui.position())

# 2.将鼠标移动到指定位置 unp
pyautogui.moveTo(position.x, position.y, duration=1)

# 3.点击鼠标左键
pyautogui.click(position.x, position.y, button='left')

# 4.自动利用键盘输入内容
pyautogui.typewrite(content1, interval=0.1)  # 设置输入间隔为0.1秒，以便输入汉字

# 完成键入后打印完成
print('Done')