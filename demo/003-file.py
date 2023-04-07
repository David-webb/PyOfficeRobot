# import office

# office.wechat.send_file(who='文件传输助手', file=r'C:\Users\tengwei0809\Videos\Iron-man-desktop.jpg')
# office.wechat.send_file(who='文件传输助手', file=r'C:\Users\tengwei0809\Documents\tmp_buffer.json')


from PyOfficeRobot.core.WeChatType import WeChat
wx = WeChat()
wx.ChatWith("文件传输助手")
# wx.SendFiles(r'C:\Users\tengwei0809\Documents\tmp_buffer.json')
wx.SendFiles(r'C:\Users\tengwei0809\Videos\Iron-man-desktop.jpg')