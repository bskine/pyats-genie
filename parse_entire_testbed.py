from genie.testbed import load
from pprint import pprint

result_dict = {}

testbed = load('~/auto/genie/testbed/ewing.yml')
#suppress stdout on connection cause ain't nobody got time for that!
testbed.connect(log_stdout=False)

for i in testbed:
    rs = i.parse('show version')
    d = rs['version']
    hostname = d['hostname']
    sn = d['chassis_sn']
    #diving one layer deeper to retrieve model and version
    model = ((d['switch_num'])['1'])['model_num']
    ios_version = ((d['switch_num'])['1'])['sw_ver']
    dmx = {hostname: {'Model': model,
                      'IOS': ios_version,
                      'SN': sn}}                  
    result_dict.update(dmx)
    
print(result_dict)
print(result_dict.keys())
    