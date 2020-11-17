import requests

AUTH_KEY = '4b7e6767b013f25d5486369c988219985b6b29cb'
args = {
    'bgn_de' :'20201001',
    'end_de':'20201101',
    'corp_cls':'K'
}
args_str =''
for k, v in args.items():
    args_str = '&%s=%s' %(k,v)

print(args_str)

res = requests.get('https://opendart.fss.or.kr/api/list.json?crtfc_key=%s%s' %(AUTH_KEY, args_str))

data = res.json()
print(data)
