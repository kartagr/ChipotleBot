import requests

ZIPCODE = '11111'
FIRSTNAME = 'firstName'
LASTNAME = 'lastName'
PHONENUMBER = '5103040167'

headers = {
    'origin': 'https://savorwavs.com',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.8',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'content-type': 'application/json;charset=UTF-8',
    'accept': 'application/json',
    'referer': 'https://savorwavs.com/buy-one-get-one',
    'authority': 'savorwavs.com',
    'cookie': '_gat_UA-5654566-49=1; _ga=GA1.2.1733890314.1500482726; _gid=GA1.2.1123691020.1500482726',
}

data = '{"zip":"' + ZIPCODE + '","firstName":"' + FIRSTNAME + '","lastName":"' + LASTNAME + '","phoneNumber":"+1' + PHONENUMBER + '","optedIn":false}'

r = requests.post('https://savorwavs.com/api/offer/request', headers=headers, data=data, verify=False)
if r.status_code == 200:
	print 'Success, text message sent to ' + PHONENUMBER
else:
	print 'Failed, text message was not sent to ' + PHONENUMBER
