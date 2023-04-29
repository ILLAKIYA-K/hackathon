import http.client as ht

conn = ht.HTTPSConnection("api.msg91.com")

headers = {# Paste your MSG91 API Key
		'authkey' : "",
		'content-type': "application/json"}

payload = '''{"sender": "MSGAPI",
			"route": "4",
			"country": "91",
			"sms": [
				{
				"message": "Here we need help to dogs",
				"to": [
					"9090XX8921"
				]
				},
				{
				"message": "Here i need help",
				"to": [
					"901X83XX01"
				]
				}
			]
			}'''

# importing the module
import http.client as ht

# establishing connection
conn = ht.HTTPSConnection("api.msg91.com")

# determining the payload
payload = '''{"sender": "MSGAPI",
			"route": "4",
			"country": "91",
			"sms": [
				{
				"message": "here's help needed",
				"to": [
					"9090XX8921"
				]
				},
			]
			}'''

# creating the header
headers = {
	'authkey': "",
	'content-type': "application / json"
}

# sending the connection request
conn.request("POST", "/api / v2 / sendsms", payload, headers)

res = conn.getresponse()
data = res.read()

# printing the acknowledgement
print(data.decode("utf-8"))
