import requests
import json
def get_html_text1(url,args):
    try:
        h={'user-agent':'Mozilla/5.0(Windows NT 6.1;WOW64)'
                        'AppleWebKit/537.36(KHTML, like Gecko)'
                        'Chrome/68.0.3440.106 Safari/537.36'
        }
        r=requests.get(url,headers=h,timeout=3000,params=args)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except BaseException as e:
        print("出现异常:",e)
        return str(e)