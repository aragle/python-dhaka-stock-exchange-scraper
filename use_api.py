import json

filename = '20230706_025209.json'
with open(filename) as json_file:
    data = json.load(json_file)
    for p in data:
        print('Trading Code: ' + p['trading_code'])
        print('LTP: ' + str(p['ltp']))
        print('High: ' + str(p['high']))
        print('Low: ' + str(p['low']))
        print('Closep: ' + str(p['closep']))
        print('YCP: ' + str(p['ycp']))
        print('Change: ' + str(p['change']))
        print('Trade: ' + str(p['trade']))
        print('Volume: ' + str(p['volume']))
        print('Value (mn): ' + str(p['value_mn']))
        print('=====================================================')
