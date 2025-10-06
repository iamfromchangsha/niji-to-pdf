import requests
import json
import time
from docx import Document
from docx.oxml.ns import qn
from docx.shared import Pt

def login(email, password):
    session = requests.Session()
    
    url = 'https://nideriji.cn/api/login/'
    data = {
        'email': email,
        'password': password,
        'csrfmiddlewaretoken': ''  # 尝试空字符串
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0',
        'Referer': 'https://nideriji.cn/w/login'
    }

    resp = session.post(url, data=data, headers=headers)
    return resp.json()

def script(token):
    session = requests.Session()
    url = 'https://nideriji.cn/api/v2/sync/'
    headers = {
        'Auth': 'token ' + token,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0'
    }
    data = {
        'user_config_ts': '0',
        'diaries_ts': '0',
        'readmark_ts': '0',
        'images_ts': '0'
    }
    resp = session.post(url, data=data, headers=headers)
    return resp.json()

def pin(userid, token, id):
    session = requests.Session()
    url = f'https://nideriji.cn/api/diary/all_by_ids/{userid}/'
    headers = {
        'Auth': 'token ' + token,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0'
    }
    data = {
        'diary_ids': id
    }
    resp = session.post(url, data=data, headers=headers)
    return resp.json()

def set_chinese_font(doc, font_name='微软雅黑'):
    """设置默认中文字体"""
    style = doc.styles['Normal']
    style.font.name = font_name
    style._element.rPr.rFonts.set(qn('w:eastAsia'), font_name)
    style.font.size = Pt(12)

def main():
    logins = login('2212831947@qq.com', '89937.7374')
    token = logins.get('token')
    userid = logins.get('user_config').get('userid')
    print(userid)
    
    shujv = script(token).get('diaries')
    print(len(shujv))

    # 创建 Word 文档
    doc = Document()
    set_chinese_font(doc)  # 设置中文字体

    for i in shujv:
        diary = pin(userid, token, i.get('id'))
        content = diary.get('diaries')[0].get('content')
        timets = diary.get('diaries')[0].get('ts')
        l_time = time.localtime(timets)
        formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', l_time)

        # 添加标题（一级标题）
        doc.add_heading(formatted_time, level=1)
        # 添加正文
        doc.add_paragraph(content)

        print(formatted_time)
        print(content)

    # 保存文档
    doc.save('nideriji_diaries.docx')
    print('✅ Word 文档已保存为 nideriji_diaries.docx')

if __name__ == '__main__':
    main()