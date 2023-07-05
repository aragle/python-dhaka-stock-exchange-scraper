import json

filename = '20230706_030357.json'
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

# write all print output apend to a file
with open('output.txt', 'a') as outfile:
    for p in data:
        outfile.write('Trading Code: ' + p['trading_code'] + '\n')
        outfile.write('LTP: ' + str(p['ltp']) + '\n')
        outfile.write('High: ' + str(p['high']) + '\n')
        outfile.write('Low: ' + str(p['low']) + '\n')
        outfile.write('Closep: ' + str(p['closep']) + '\n')
        outfile.write('YCP: ' + str(p['ycp']) + '\n')
        outfile.write('Change: ' + str(p['change']) + '\n')
        outfile.write('Trade: ' + str(p['trade']) + '\n')
        outfile.write('Volume: ' + str(p['volume']) + '\n')
        outfile.write('Value (mn): ' + str(p['value_mn']) + '\n')
        outfile.write('=====================================================' + '\n')

