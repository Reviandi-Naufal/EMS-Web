# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 11:41:03 2022

@author: milth
"""

import requests
import pandas as pd

## Initialize All Urls
baseURL = "http://213.190.4.40/iems/iems-api/index.php/public/devices"
devicesToken = ["6cc5dc0059d39c5392784721c78d4bb3", "cea949ea3537bc59e96b3a8ce119dfc3", 
                "4438ca6fc2a575cfab4fa4f1d4569964", "5034e836792df04c0794f4c2a6beb6a7", "ed991a8d2fabbfc3067416caafdd52f8"] # Change this with what device token u need
device_id = []
device_name = []
device_status = []

for deviceToken in devicesToken:
  urls = {
      "info": baseURL + "/info?device_token=" + deviceToken,
      "pullByDate": baseURL + "/pullByDate?device_token=" + deviceToken + "&date=2021-09-20",
      "last": baseURL + "/last?device_token=" + deviceToken,
      "pull": baseURL + "/pull?device_token=" + deviceToken
  }

  ## Do request
  response = requests.get(urls["info"]) ## U will get response as a string
  result = response.json() ## We parse the string response to json

  dataset = pd.json_normalize(result["data"]) # Read data object from result
  device_id.append(dataset['id'][0])
  device_name.append(dataset['device_name'][0])
  device_status.append(dataset['device_status'][0])

df = pd.DataFrame({'id': device_id, 'device_name' : device_name, 'status' : device_status})
