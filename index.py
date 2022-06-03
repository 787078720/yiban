####代码仅供学习参考，
####by 月初
import requests
import time
from datetime import datetime
import hashlib
#-------------------------------------------------------变量信息----------------------------------------------------------------#

zhh={
    1:"2021532102",###第一个账号
    2:"0000000",#######第二个账号以此类推如果只有一个账号删除这行
}
mmm={
    1: "2551",###第一个账号密码
    2:"0000000",###第二个账号密码以此类推如果只有一个账号删除这行
}
n=0+1
zs = len(zhh)
while n<zs+1:
    zh = zhh[n]
    deomo_val = mmm[n]
    # ---------------------------------------------------------加密--------------------------------------------------------------#
    dt01 = datetime.today()
    xzrq = (dt01.date())
    t = time.time()
    rq = (str(int(t)))
    md5_val = hashlib.md5(deomo_val.encode('utf8')).hexdigest()
    j = (md5_val[:30])
    k = (md5_val[:5])
    m = (j[9:])
    l = (j[5:9])
    kk = k + "a" + l + "b" + m
    # -------------------------------------------------登录提取cookie--------------------------------------------------------------#
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
    urlq = "http://xggl.hnqczy.com/website/login"
    dataq = [
        ("uname", zh),
        ("pd_mm", kk)
    ]
    def post():
        r = requests.post(urlq, data=dataq, headers=headersq).headers['Set-Cookie']
        return r
    cooick = (post()[:43])
    cooick1 = (cooick[11:])
    # -------------------------------------------------获取上次打卡记录josn--------------------------------------------------------------#
    cookies = {
        'JSESSIONID': cooick1,
    }

    headers1 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46',
        'Host': 'xggl.hnqczy.com',
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'http://xggl.hnqczy.com/wap/menu/student/temp/zzdk/_child_/detail/16538745236399409694?_t_s_=1653919292775',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    }

    params1 = (
        ('_t_s_', '1653919293104'),
    )

    response = requests.get('http://xggl.hnqczy.com/content/student/temp/zzdk/16538745236399409694', headers=headers1,
                            params=params1, cookies=cookies)
    json = response.json()
    cjdz = json['jzdDz2']
    lxdh = json["lxdh"]
    xzrq = json["fxrq"]
    hs = "1"
    # ----------------------------------------------------------打卡--------------------------------------------------------------#
    url2 = "http://xggl.hnqczy.com/content/student/temp/zzdk?_t_s_=" + rq
    headers2 = {"Host": "xggl.hnqczy.com",
                "Connection": "keep-alive",
                "Content-Length": "1028",
                "Accept": "*/*",
                "X-Requested-With": "XMLHttpRequest",
                "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46',
                "Content-Type": "application/x-www-form-urlencoded; charset\u003dUTF-8",
                "Origin": "http://xggl.hnqczy.com",
                "Referer": "http://xggl.hnqczy.com/wap/menu/student/temp/zzdk/_child_/edit?_t_s_\u003d1648091401446",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "zh-CN,zh;q\u003d0.9,en-US;q\u003d0.8,en;q\u003d0.7",
                "Cookie": cooick
                }
    data2 = [
        ('dkdz', '湖南省株洲市天元区天台路60'),
        ('dkdzZb', '113.1404708,27.83356764'),
        ('dkly', 'baidu'),
        ('dkd', '湖南省株洲市'),
        ('jzdValue', '430000,430200,430202'),
        ('jzdSheng.dm', '430000'),
        ('jzdShi.dm', '430200'),
        ('jzdXian.dm', '430202'),
        ('jzdDz', '湖南汽车工程职业学院'),
        ('jzdDz2', cjdz),
        ('lxdh', lxdh),
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
        ('hsjc1', hs),
        ('bz', ''),
        ('operationType', 'Create'),
        ('dm', ''),
    ]
    def postt():
        r = requests.post(url2, data=data2, headers=headers2)
        u=r.json()
        return u
    print(postt())
    uuu=postt()
# --------------------------------------------------------信息推送-----------------------------------------------------------------#def tuisong():
    n=n+1
key= "SCT114092TdaLtRYOnxp0vLc0wwZAau4V6"#微信推送key这里    链接获取#https://sct.ftqq.com/sendkey
api = "https://sc.ftqq.com/"+key+".send"
data = {
    "title":"打卡成功",
     "desp": uuu
}
req = requests.post(api, data=data).json()
print(req)
print(tuisong())
def main_handler(event, context):
    r = "1"
    return r
if __name__ == '__main__':
    post()
