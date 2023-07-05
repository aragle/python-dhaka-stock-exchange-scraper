import datetime
import requests
from bs4 import BeautifulSoup
import json

# write a json file append with [
# and name of the file is date_time.json
time = datetime.datetime.now()
filename = time.strftime("%Y%m%d_%H%M%S") + '.json'
with open(filename, 'a') as outfile:
    outfile.write('[')

# fetch data from dse website
url = "https://www.dsebd.org/latest_share_price_scroll_l.php"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# parse data
table = soup.find_all('table', class_='fixedHeader')
tr = table[0].find_all('tr')

# make json keys from table header
keys = tr[0].find_all('th')

# count number of rows
total_rows = len(tr)

for i in range(1, total_rows):
    values = tr[i].find_all('td')
    total_columns = len(values)

    data = {}
    for j in range(0, total_columns):
        key = keys[j].text.lower().replace('*', '').replace(" ", "_").replace("#", "id").replace("(", "").replace(")", "")
        value = values[j].text.strip()

        if key == 'trading_code':
            data[key] = str(value)
        elif value == '--':
            data[key]  = str("N/A")
        elif key == 'ltp' or key == 'high' or key == 'low' or key == 'closep' or key == 'ycp' or key == 'change' or key == 'value_mn':
            data[key]  = float(value.replace(',', ''))
        elif key == 'trade' or key == 'volume':
            data[key]  = int(value.replace(',', ''))
        else:
            data[key]  = str(value)

    # convert to json
    json_string = json.dumps(data, indent=4)

    # write to file append but not add last comma
    with open(filename, 'a') as outfile:
        if i == total_rows - 1:
            outfile.write(json_string)
        else:
            outfile.write(json_string + ',')

# write to file append with []
with open(filename, 'a') as outfile:
    outfile.write(']')

