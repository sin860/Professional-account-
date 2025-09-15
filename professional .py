import os
import sys
try:
	import requests
	import logging
except Exception:
	os.system('pip install requests  ')
class sin:
	def __init__(self):
		logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
	def __csrftoken__(self):
		api=requests.get('https://www.instagram.com').cookies.get('csrftoken','EROR')
		return api
	def __professional__(self,sis,crf):
		try:
			url = "https://www.instagram.com/api/v1/business/account/convert_account/"

			payload = {
  'category_id': "2700",
  'create_business_id': "true",
  'entry_point': "ig_web_settings",
  'set_public': "true",
  'should_bypass_contact_check': "true",
  'should_show_category': "0",
  'to_account_type': "3",
  'jazoest': "22671"
}

			headers = {
  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Mobile Safari/537.36",
  'sec-ch-ua-full-version-list': "\"Chromium\";v=\"140.0.7339.51\", \"Not=A?Brand\";v=\"24.0.0.0\", \"Google Chrome\";v=\"140.0.7339.51\"",
  'sec-ch-ua-platform': "\"Android\"",
  'sec-ch-ua': "\"Chromium\";v=\"140\", \"Not=A?Brand\";v=\"24\", \"Google Chrome\";v=\"140\"",
  'sec-ch-ua-model': "\"RMX2189\"",
  'sec-ch-ua-mobile': "?1",
  'x-ig-app-id': "1217981644879628",
  'x-requested-with': "XMLHttpRequest",
  'x-instagram-ajax': "1027111155",
  'x-csrftoken': f"{crf!r}",
  'x-web-session-id': "rm9z48:j4trgb:vpy96w",
  'x-asbd-id': "359341",
  'sec-ch-prefers-color-scheme': "dark",
  'sec-ch-ua-platform-version': "\"11.0.0\"",
  'origin': "https://www.instagram.com",
  'sec-fetch-site': "same-origin",
  'sec-fetch-mode': "cors",
  'sec-fetch-dest': "empty",
  'referer': "csrftoken/accounts/convert_to_professional_account/",
  'accept-language': "ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7",
  'priority': "u=1, i",
  'Cookie': f"csrftoken={crf!r}; sessionid={sis!s}"
}

			response = requests.post(url, data=payload, headers=headers)

			return response.text
		except Exception as e:
			logging.error('There is an error ')
			return e			
SIN=sin()

if __name__=='__main__':
			def main():
				list=[]
				try:
					print(str(__import__('pyfiglet').figlet_format('S I N')))
					print(sys.version)
					print()
					print('\n')
					sis=str(input('put your  sessionid '))
					with open('Sessionid.txt','a') as sinn:
						sinn.write(sis)
					list.append(sis)
					
					if not sis:
						raise Exception('Must not be empty sessionid ')
						
					crf=SIN.__csrftoken__()
					professional=SIN.__professional__(sis,crf)
					if 'status":"ok''' in professional:
						logging.info('تم تحويل الحساب الى احترافي')
						print('\n')
						size = sys.getsizeof(list)
						print(f"Memory size {size}")
					else:
						logging.info('فشل تحويل الحساب تاكد من سيشن')
				except Exception as e:
					logging.error('There is a problem ')
					print(e)
main()
del main
print('Memory deleted ')