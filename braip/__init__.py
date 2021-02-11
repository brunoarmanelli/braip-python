import requests

class Braip:
	def __init__(self, token):
		self.token = token
		
	def get_transactions(self, product_key=None, transaction_key=None, date_min=None, 
			date_max=None, last_update_min=None, last_update_max=None, status=None, 
			payment=None, page=None, participation=None):

		method_url = 'https://ev.braip.com/api/vendas'
		headers = {'Authorization': 'Bearer ' + self.token}
		payload = {}
		
		if product_key:
			payload['product_key'] = product_key
		if transaction_key:
			payload['transaction_key'] = transaction_key
		if date_min:
			payload['date_min'] = date_min
		if date_max:
			payload['date_max'] = date_max
		if last_update_min:
			payload['last_update_min'] = last_update_min
		if last_update_max:
			payload['last_update_max'] = last_update_max
		if status:
			payload['status'] = status
		if payment:
			payload['payment'] = payment
		if page:
			payload['page'] = page
		if participation:
			payload['participation'] = participation

		try:
			r = requests.get(url = method_url, headers = headers, params = payload)
			data = r.json()
			return data
		except: 
			return None