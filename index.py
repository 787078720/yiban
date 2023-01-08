####代码仅供学习参考，by 月初
import requests
import time
from datetime import datetime
import hashlib
import urllib3
from urllib import parse
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
print(hqjl)
dkd=str(hqjl['dkd'])
jzdDz=str(hqjl["jzdDz"])
jzdDz2=str(hqjl['jzdDz2'])
lxdh = str(hqjl["lxdh"])
dm=str(hqjl["jzdSheng"]["dm"])
dm1=str(hqjl["jzdShi"]["dm"])
dm2=str(hqjl["jzdXian"]["dm"])
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
jm=jm()
print(jm)
# ----------------------------------------------------------打卡--------------------------------------------------------------#
def post_xxx():
    sjc=str(time.time())
    url="http://xggl.hnqczy.com/content/student/temp/zzdk?_t_s_=1673140784571"
    headers = {'Host': 'xggl.hnqczy.com',
               'Connection': 'keep-alive',
               'Accept': '*/*',
               'X-Requested-With': 'XMLHttpRequest',
               'User-Agent': 'Mozilla/5.0 (Linux; Android 12; 22081212C Build/SKQ1.220303.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36;webank/h5face;webank/1.0 yiban_android/5.0.14',
               'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
               'Origin': 'http://xggl.hnqczy.com',
               'Referer': 'http://xggl.hnqczy.com/wap/menu/student/temp/zzdk/_child_/edit?_t_s_='+sjc,
               'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'}
    cookies = {
        'JSESSIONID':cooick1,
    }
    post_data = str("dkdz="+dkd+
                    "&dkdzZb=111.71111,28.589999"
                    "&dkly=yiban"
                    "&zzdk_token="+jm+
                    "&xcmTjd="
                    "&dkd="+dkd+
                    "&jzdValue="+dm+","+dm1+","+dm2+
                    "&jzdSheng.dm="+dm+
                    "&jzdShi.dm="+dm1+
                    "&jzdXian.dm="+dm2+
                    "&jzdDz="+jzdDz+
                    "&jzdDz2="+jzdDz2+
                    "&lxdh="+lxdh+
                    "&sfzx=1&sfzxText=不在校"
                    "&twM.dm=01&twMText=[35.0~37.2]正常&yczk.dm=01&yczkText=无症状&brStzk.dm=01&brStzkText=身体健康、无异常&brJccry.dm=01&brJccryText=未接触传染源&jrStzk.dm=01&jrStzkText=身体健康、无异常&jrJccry.dm=01&"
                    "jrJccryText=未接触传染源&xgym=2&xgymText=已接种已完成&hsjc=0&hsjcText=否&zdy1=0&zdy2=&operationType=Create&dm=&tw1M.dm=&tw2M.dm=&tw3M.dm=&jkm=1&xcm=1&jkmcl=&zdy3=&zdy4=&zdy5=&zdy6=&bz=")
    print(post_data)
    rsp = requests.post(url,headers=headers, data=post_data.encode('UTF-8'),cookies=cookies).json()
    return rsp
jg=post_xxx()
print(jg)
if jg['result']=='true':
    tt="打卡成功"
else:
    tt="打卡失败"
# ----------------------------------------------------------推送--------------------------------------------------------------#
def ts():
    key = ""  # 微信推送key这里    链接获取#https://sct.ftqq.com/sendkey
    api = "https://sc.ftqq.com/" + key + ".send"
    data = {
        "title": str(tt),
        "desp":str(jg)
    }
    reqq = requests.post(api, data=data).json()
    return reqq
print(ts())
def main_handler(event, context):
    1==1
if __name__ == '__main__':
    1==1
