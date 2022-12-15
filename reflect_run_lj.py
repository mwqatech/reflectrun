import requests
import json
import sys
import yaml
from yaml.loader import SafeLoader

data = {}
total_tcs = 0
passed_tcs = []
failed_tcs = []
for key, value in yaml.load(open('testdata.yml'), Loader=SafeLoader).items():
    if(str(key) == 'LJ_Testdata'):
        total_tcs = len(value)
        for tkey, tvalue in value.items():
            print("Testcase ID = ",tvalue)
            url = "https://api.reflect.run/v1/tests/" + str(tvalue) + "/executions"
            print(url)

            payload = ""
            headers = {"x-api-key": "j5rPTzYWK16hh7xyPRsnz1EYDIbyAcUE7sOKNp4U"}

            response = requests.request("POST", url, data=payload, headers=headers)
            if(response.status_code == 200):
                total_tcs -= 1
                json_data = json.loads(response.text)

                url2 = "https://api.reflect.run/v1/executions/" + str(json_data['executionId'])

                while True:
                    response2 = requests.request("GET", url2, data=payload, headers=headers)
                    data = json.loads(response2.text)
                    print(data['tests'][0]['status'])
                    if((data['tests'][0]['status'] != 'running') and (data['tests'][0]['status'] != 'queued')):
                        break

                if(data['tests'][0]['status'] == 'failed'):
                    print("Test Execution of TC ID "+ str(tvalue) +" is Failed\n")
                    failed_tcs.append(tvalue)
                    print("Total_TCs to be executed", total_tcs)

                if(len(failed_tcs) != 0 and total_tcs == 0):
                    print("Please check the failed/not triggered TCs:", failed_tcs)
                    sys.exit(-1)
            else:
                total_tcs -= 1
                print("Test Execution of TC ID "+ str(tvalue) +" is not triggered\n")
                failed_tcs.append(tvalue)
                print("Total_TCs to be executed", total_tcs)
          
                if(len(failed_tcs) != 0 and total_tcs == 0):
                    print("Please check the failed/not triggered TCs:", failed_tcs)
                    sys.exit(-1)
