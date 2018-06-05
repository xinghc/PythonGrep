import csv
import urllib.request

url = 'http://www.twse.com.tw/fund/TWT38U?response=csv&date=20180605'
response = urllib.request.urlopen(url)
data = csv.reader(response.read().decode('Big5','replace'))

for row in data:
    print(', '.join(row))
