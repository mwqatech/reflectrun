import requests
import json
import sys
import yaml
import time
from yaml.loader import SafeLoader

data = {}
total_tss = 0
failed_tss = []

payload = json.dumps({"overrides": {"hostnames": [{"original": "ourlittlejoys.com", "replacement": "stg.ourlittlejoys.com"}]}})
apikey = "j5rPTzYWK16hh7xyPRsnz1EYDIbyAcUE7sOKNp4U"

for key, value in yaml.load(open('testdata_stg_ts.yml'), Loader=SafeLoader).items():
    if (str(key) == 'LJ'):
        total_tss = len(value)
        for tkey, tvalue in value.items():
            print("Test Suite ID = ", tvalue)
            url = "https://api.reflect.run/v1/suites/" + str(tvalue) + "/executions"
            print(url)

            headers = {"x-api-key": apikey}

            response = requests.request("POST", url, data=payload, headers=headers)
            if (response.status_code == 200):
                total_tss -= 1
                json_data = json.loads(response.text)

                url2 = "https://api.reflect.run/v1/suites/" + str(tvalue) + "/executions/" + str(json_data['executionId'])

                while True:
                    response2 = requests.request("GET", url2, headers=headers)
                    data = json.loads(response2.text)
                    time.sleep(5)
                    if ((data['status'] != 'pending') and (data['status'] != 'running') and (data['isFinished'] != False)):
                        print("Execution of Test Suite " + str(tvalue) + " is in Progress ...\n")
                        break
                        
                print("Execution of Test Suite " + str(tvalue) + " is Completed!!!\n")
                
                if (data['status'] == 'failed'):
                    print("Test Execution of Test Suite ID " + str(tvalue) + " is Failed\n")
                    failed_tss.append(tvalue)
                    print("Total Test Suites to be executed", total_tss)

                if (len(failed_tss) != 0 and total_tss == 0):
                    print("Please check the failed/not triggered Test Suites:", failed_tss)
                    sys.exit(-1)
            else:
                total_tss -= 1
                print("Test Execution of Test Suite ID " + str(tvalue) + " is not triggered\n")
                failed_tss.append(tvalue)
                print("Total Test Suites to be executed", total_tss)

                if (len(failed_tss) != 0 and total_tss == 0):
                    print("Please check the failed/not triggered Test Suites:", failed_tss)
                    sys.exit(-1)