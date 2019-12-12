import configparser

cof = configparser.ConfigParser()
cof.read('settings.ini')

print(cof.get('DEFAULT', 'Directory'))