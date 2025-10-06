import requests
import json
import time
from fpdf import FPDF

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
        'Auth':'token '+token,
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0'
    }
    data = {
        'user_config_ts':'0',
        'diaries_ts':'0',
        'readmark_ts':'0',
        'images_ts':'0'
    }
    resp = session.post(url, data=data, headers=headers)
    return resp.json()

def pin(userid,token,id):
    session = requests.Session()
    url = 'https://nideriji.cn/api/diary/all_by_ids/' + str(userid)+'/'
    headers = {
        'Auth':'token '+token,
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0'
    }
    date = {
        'diary_ids':id
    }
    resp = session.post(url, data=date, headers=headers)
    return resp.json()

def pdf(content,formatted_time):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True,margin=15)
    

def main():
    logins= login('2212831947@qq.com', '89937.7374')
    token = logins.get('token')
    userid = logins.get('user_config').get('userid')
    print (userid)
    shujv = script(token).get('diaries')
    print (len(shujv))
    for i in shujv:
        diary = pin(userid,token,i.get('id'))
        print (diary)
        content = diary.get('diaries')[0].get('content')
        timets = diary.get('diaries')[0].get('ts')
        l_time = time.localtime(timets)
        formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', l_time)
        print (content)
        print (formatted_time)

main()