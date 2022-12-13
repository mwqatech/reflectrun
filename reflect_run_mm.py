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
    if(str(key) == 'MM_Testdata'):
        for tkey, tvalue in value.items():
            total_tcs = len(value)
            print("Testcase ID = ",tvalue)
            url = "https://api.reflect.run/v1/tests/" + str(tvalue) + "/executions"
            print(url)

            payload = ""
            headers = {"x-api-key": "x1OBUoR7PY4qH4RyH199pwuN1a7ofw32BxmrfSxf"}

            response = requests.request("POST", url, data=payload, headers=headers)
            if(response.status_code == 200):
                json_data = json.loads(response.text)

                url2 = "https://api.reflect.run/v1/executions/" + str(json_data['executionId'])

                while True:
                    response2 = requests.request("GET", url2, data=payload, headers=headers)
                    data = json.loads(response2.text)
                    print(data['tests'][0]['status'])
                    if((data['tests'][0]['status'] != 'running') and (data['tests'][0]['status'] != 'queued')):
                        break

                if(data['tests'][0]['status'] == 'failed'):
                    print("Test Execution:"+ str(tvalue) +" is Failed\n")
                    failed_tcs.append(tvalue)
                    print("Please check the failed/not triggered TCs:", failed_tcs)
                    print("Total_TCs to be executed", total_tcs)

                if(len(failed_tcs) != 0 and total_tcs == 0):
                    print("Please check the failed/not triggered TCs:", failed_tcs)
                    system.exit(-1)
                total_tcs -= 1
            else:
                print("Test Execution for :"+ str(tvalue) +" is not triggered\n")
                failed_tcs.append(tvalue)
                print("Please check the failed/not triggered TCs:", failed_tcs)
                print("Total_TCs to be executed", total_tcs)

                if(len(failed_tcs) != 0 and total_tcs == 0):
                    print("Please check the failed/not triggered TCs:", failed_tcs)
                    system.exit(-1)
                total_tcs -= 1
