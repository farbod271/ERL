# read this json link
import json
url  = "https://www.erl.de/wp-json/kundenportal/v1/onoffice/get-stammobjekt-free-apartments?id=573"

from urllib.request import urlopen 
  
# store the response of URL 
response = urlopen(url) 
  
# storing the JSON response  
# from url in data 
data_json = json.loads(response.read()) 
  
# print the json response 
# if ((data_json["success"]) == True) and (data_json["apartmentsAvailable"]["0"] = 0) and (data_json["apartmentsAvailable"]["1"] = 0) and (data_json["apartmentsAvailable"]["2"] = 0) and (data_json["apartmentsAvailable"]["3"] = 280):
#     print("No apartments available")

if (data_json["success"] == True) and data_json["apartmentsAvailable"]["0"] == 0 and (data_json["apartmentsAvailable"]["1"] == 0) and (data_json["apartmentsAvailable"]["2"] == 0) and (data_json["apartmentsAvailable"]["3"] ==280):
        print("No apartments available")
else:
        print("apartments available")
