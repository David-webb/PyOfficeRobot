"""
接收多人微信消息指获取多人指定日期之后给你发送的消息（文字、文件等）
------------------------------------------------
下面是参考你的代码写的调用例子
office.wechat.receive_message(who = '',date = 1)
who是指接收谁的消息
date是接收近几天的消息

返回结果
先返回一行分隔线，（这个分隔线很重要）
之后再返回和用户的沟通信息
"""

import office
#
office.wechat.receive_message(who='DW', date=1)


import openai

openai.api_key = "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"

prompt = """对以下这段话中进行实体提取：‘设计一个高质感得眼镜盒，要求现代简约风格，使用褐色亚克力材质，尺寸为长20厘米，宽5厘米，高5厘米的长方体；希望盒盖可以群殴咪咕视频每个打开，盒子内部有绒布衬里，以保护眼镜，希望盒子表面有集合图案，可以通过
触摸感受到。此眼镜面向商务人士，用于存放正式场合需要佩戴的眼镜，设计师可以提出自己的创意和建议，但必须确保眼镜盒具有高质感和艺术品感。'"""
prompt2 = "将下面的句子翻译成中文.直接给出答案，不要任何提示:'Mi amigo, esa es la foto del artículo: 48609-Bz020'"

# GPT-3.5-turbo模型测试
res = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        # {"role": "system", "content":"You are a translator assistant."},
        {"role": "system", "content": "You are a great assistant."},
        {"role": "user", "content": prompt2},
    ]
)
print(res["choices"][0]["message"]["content"])
