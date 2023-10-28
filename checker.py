import json
from urllib.request import urlopen
import time

counter= 0


def thejob():
    while True:
        global counter
        global status
        url  = "https://www.erl.de/wp-json/kundenportal/v1/onoffice/get-stammobjekt-free-apartments?id=573"

        response = urlopen(url)
        data_json = json.loads(response.read())

        try:
                if (data_json["success"] == True) and data_json["apartmentsAvailable"]["0"] == 0 and (data_json["apartmentsAvailable"]["1"] == 0) and (data_json["apartmentsAvailable"]["2"] == 0) and (data_json["apartmentsAvailable"]["3"] ==280):
                        status = "No apartments available"
                        counter += 1
                        return
                        # print("checking apartment availbility", counter)
                        if counter > 3:
                                return 
                else:
                        status = "apartments available"
                        return
        except:
                print("Error")
                # active = True
        print("Bot started")
        time.sleep(2)
        

# while True:
#     thejob()
#     time.sleep(2)
