from genie.testbed import load
from pprint import pprint

#loading testbed
testbed = load('testbed/ewing.yml')
#calling out device
device = testbed.devices['alp-sw2']
#call device
device.connect()

response = device.parse('show version')
pprint(response)

#breaking dict down so I can call key:value pairs
#d just gets me too device statistics by calling the 'version' key
d = response['version'] #returns 28 key:value pairs!
pprint(d)
#calling the 'switch_num' key, which is a child of 'version'
model = ((d['switch_num'])['1'])['model_num']
ios_version = ((d['switch_num'])['1'])['sw_ver']

#creating tuple (model, ios_version) to check if up-to-date
dmx = (model, ios_version)
