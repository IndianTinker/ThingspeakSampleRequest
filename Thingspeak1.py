import requests
API_KEY=raw_input('enter API key')
url="http://api.thingspeak.com/update?key="
url+=API_KEY
f1=raw_input('Sample Data for Field 1:')
f2=raw_input('Sample Data for Field 2:')
f3=raw_input('Sample Data for Field 3:')
url=url+"&field1="+f1+"&field2="+f2+"&field3="+f3
print url
response=requests.get(url)
if response.status_code==200:
    print "Data Plugged"+"\n"
