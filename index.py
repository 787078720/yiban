####代码仅供学习参考，by 月初
import requests
import time
from datetime import datetime
import hashlib
import urllib3
#-------------------------------------------------------变量信息----------------------------------------------------------------#
zhh={
    1:"2021",###第一个账号
}
mmm={
    1: "",###第一个账号密码
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
    n=n+1
    # -------------------------------------------------登录提取cookie--------------------------------------------------------------#
    headersq = {}
    urlq = "http://xggl.hnqczy.com/website/login"
    dataq = [
        ("uname", zh),
        ("pd_mm", kk)
    ]
    def post():
        r = requests.post(urlq, data=dataq, headers=headersq).headers['Set-Cookie']
        print(r)
        return r
    cooick = (post()[:43])
    cooick1 = (cooick[11:])
    # ---------------- ---------------------------------获取上次打卡记录josn--------------------------------------------------------------#
def get_xxx():
    url="http://xggl.hnqczy.com/content/student/temp/zzdk/lastone?_t_s_=1661221850154"
    headers = {}
    cookies = {
        'JSESSIONID':cooick1,
    }
    rsp =requests.get(url, headers,cookies=cookies).json()
    return rsp
hqjl=get_xxx()
dkd=hqjl['dkd']
jzdDz2=hqjl['jzdDz2']
lxdh = hqjl["lxdh"]
# ----------------------------------------------------------校验加密--------------------------------------------------------------#
def jm():
    http = urllib3.PoolManager()
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
        'Cookie':'JSESSIONID='+cooick1}
    resp = http.request('GET', 'http://xggl.hnqczy.com/wap/menu/student/temp/zzdk/_child_/edit?_t_s_=1661742092205',
                        headers=headers, )
    sj = (resp.data.decode())
    zzdk_token = (sj[sj.index('zzdk_token" value=\"') + 19:])
    zzdk_token = (zzdk_token[:zzdk_token.index('"/>')])
    return str(zzdk_token)
print(jm())
# ----------------------------------------------------------打卡--------------------------------------------------------------#
def post_xxx():
    url="http://xggl.hnqczy.com/content/student/temp/zzdk?_t_s_=1661311939332"
    headers = {}
    cookies = {
        'JSESSIONID':cooick1,
    }
    post_data = str("dkdz="+dkd+
                    "&dkdzZb=111.795074%2C28.592226"
                    "&dkly=yiban"
                    "&zzdk_token="+str(jm())+
                    "&dkd="+dkd+
                    "&jzdValue=430000%2C430200%2C430202"
                    "&jzdSheng.dm=430000"
                    "&jzdShi.dm=430200"
                    "&jzdXian.dm=430202"
                    "&jzdDz=湖南汽车工程职业学院"
                    "&jzdDz2="+jzdDz2+
                    "&lxdh="+lxdh+
                    "&sfzx=1&sfzx1=%E5%9C%A8%E6%A0%A1"
                    "&twM.dm=01"
                    "&tw1=%5B35.0~37.2%5D%E6%AD%A3%E5%B8%B8"
                    "&tw1M.dm="
                    "&tw11="
                    "&tw2M.dm="
                    "&tw12="
                    "&tw3M.dm="
                    "&tw13="
                    "&yczk.dm=01"
                    "&yczk1=无症状"
                    "&fbrq="
                    "&jzInd=0"
                    "&jzYy="
                    "&zdjg="
                    "&fxrq="
                    "&brStzk.dm=01"
                    "&brStzk1=身体健康、无异常"
                    "&brJccry.dm=01"
                    "&brJccry1=未接触传染源"
                    "&jrStzk.dm=01"
                    "&jrStzk1=身体健康、无异常"
                    "&jrJccry.dm=01"
                    "&jrJccry1=未接触传染源"
                    "&jkm=1"
                    "&jkm1=绿色"
                    "&xcm=1"
                    "&xcm1=绿色"
                    "&xgym="
                    "&xgym1="
                    "&hsjc=1"
                    "&hsjc1="
                    "&bz="
                    "&operationType=Create"
                    "&dm=")
    post_data=post_data.encode('utf-8')
    rsp = requests.post(url,headers=headers, data=post_data,cookies=cookies).json()
    return rsp
if post_xxx()['result']=='true':
    tt="打卡成功"
else:
    tt="打卡失败"
# ----------------------------------------------------------推送--------------------------------------------------------------#
def ts():
    key = ""  # 微信推送key这里    链接获取#https://sct.ftqq.com/sendkey
    api = "https://sc.ftqq.com/" + key + ".send"
    data = {
        "title": str(tt),
        "desp":str(post_xxx())
    }
    reqq = requests.post(api, data=data).json()
    return reqq
print(ts())
def main_handler(event, context):
    print(post_xxx())
if __name__ == '__main__':
    print(post_xxx())

