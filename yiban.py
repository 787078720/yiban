##代码仅供学习参考，
####by 月初
import requests
import time
from datetime import datetime
import hashlib
dt01 = datetime.today()
xzrq=(dt01.date())
print(xzrq)
t = time.time()
rq=(str(int(t)))
print(rq)
zh = "20215321****"###########################你的学工账号学号
deomo_val = '******'#########################你的学工密码身份证后6
md5_val = hashlib.md5(deomo_val.encode('utf8')).hexdigest()
print(md5_val)
j =(md5_val[:30])
print(j)
k= (md5_val[:5])
print(k)
m=(j[9:])
l=(j[5:9])
kk = k + "a" + l + "b" + m
print(kk)
headersq = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46',
    'Host': 'xggl.hnqczy.com',
    'Connection': 'keep-alive',
    'Content-Length': '57',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'http://xggl.hnqczy.com',
    'Referer': 'http://xggl.hnqczy.com/index;jsessionid=E4C1D2DFA72761FF80084C3175023A8D',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'
}
urlq="http://xggl.hnqczy.com/website/login"
dataq = [
  ("uname", zh),
   ("pd_mm",kk)
]
def post():
   r = requests.post(urlq, data=dataq, headers=headersq).headers['Set-Cookie']
   return r
cooick = (post()[:43])
url = "http://xggl.hnqczy.com/content/student/temp/zzdk?_t_s_="+rq
print(url)
headers = {"Host": "xggl.hnqczy.com",
    "Connection": "keep-alive",
    "Content-Length": "1028",
    "Accept": "*/*",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Linux; Android 11; M2012K11AC Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36 yiban_android/5.0.8",
    "Content-Type": "application/x-www-form-urlencoded; charset\u003dUTF-8",
    "Origin": "http://xggl.hnqczy.com",
    "Referer": "http://xggl.hnqczy.com/wap/menu/student/temp/zzdk/_child_/edit?_t_s_\u003d1648091401446",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q\u003d0.9,en-US;q\u003d0.8,en;q\u003d0.7",
    "Cookie":cooick
  }
data = [
  ('dkdz', '湖南省株洲市天元区天台路60'),
  ('dkdzZb', '113.1404708,27.83356764'),
  ('dkly', 'baidu'),
  ('dkd', '湖南省株洲市'),
  ('jzdValue', '430000,430200,430202'),
  ('jzdSheng.dm', '430000'),
  ('jzdShi.dm', '430200'),
  ('jzdXian.dm', '430202'),
  ('jzdDz', '湖南汽车工程职业学院'),
  ('jzdDz2', ''),#寝室楼和寝室号
  ('lxdh', ''),#手机号
  ('sfzx', '1'),
  ('sfzx1', '在校'),
  ('twM.dm', '01'),
  ('tw1', '[35.0~37.2]正常'),
  ('yczk.dm', '01'),
  ('yczk1', '无症状'),
  ('fbrq', xzrq),
  ('jzInd', '0'),
  ('jzYy', ''),
  ('zdjg', ''),
  ('fxrq', xzrq),
  ('brStzk.dm', '01'),
  ('brStzk1', '身体健康、无异常'),
  ('brJccry.dm', '01'),
  ('brJccry1', '未接触传染源'),
  ('jrStzk.dm', '01'),
  ('jrStzk1', '身体健康、无异常'),
  ('jrJccry.dm', '01'),
  ('jrJccry1', '未接触传染源'),
  ('jkm', '1'),
  ('jkm1', '绿色'),
  ('xcm', '1'),
  ('xcm1', '绿色'),
  ('xgym', ''),
  ('xgym1', ''),
  ('hsjc', '1'),
  ('hsjc1', '是'),
  ('bz', ''),
  ('operationType', 'Create'),
  ('dm', ''),
]
def post():
    r = requests.post(url,data=data, headers=headers)
    return r.text
print(post())
u=(post())
def tuisong():
    key= ""#微信推送key这里    链接获取#https://sct.ftqq.com/sendkey
    api = "https://sc.ftqq.com/"+key+".send"
    data = {
        "title":"打卡成功",
        "desp": u
    }
    req = requests.post(api, data=data).json()
    print(req)
print(tuisong())



