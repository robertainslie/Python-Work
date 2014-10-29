import urllib
import urllib2

url='https://forms.hubspot.com/uploads/form/v2/203693/67e9b9ae-20b3-40ab-84fb-351c52aa9d20'

user_agent = 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36'
headers = {'Content-Type':'application/x-www-form-urlencoded','User-Agent':user_agent}
form_values = {'firstname':'API2 test','lastname': 'Python script','email':'pythontest2@test.com'}

data = urllib.urlencode(form_values)
req = urllib2.Request(url, data, headers)
actual_post = urllib2.urlopen(req)









#fo = open('response.txt',"w")
#fo.write(response.read())
#fo.close()