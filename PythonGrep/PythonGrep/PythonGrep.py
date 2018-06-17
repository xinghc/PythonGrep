import csv
import urllib.request

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

url = 'http://www.twse.com.tw/fund/TWT38U?response=csv&date=20180605'
response = urllib.request.urlopen(url)
data = csv.reader(response.read().decode('Big5','replace').splitlines())
next(data)

for row in data:
    if RepresentsInt(row[1]): # Skip those we are not able recognized
        # ToDo: Handle those special code name (e.g., ="00637L")
        print(', '.join(row))

