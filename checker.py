import json
from urllib.request import urlopen


counter = 0


def thejob():
        global counter
        global status
        url  = "https://www.erl.de/wp-json/kundenportal/v1/onoffice/get-stammobjekt-free-apartments?id=573"

        response = urlopen(url)
        data_json = json.loads(response.read())

        try:
                if (data_json["success"] == True) and data_json["apartmentsAvailable"]["0"] == 0 and (data_json["apartmentsAvailable"]["1"] == 0) and (data_json["apartmentsAvailable"]["2"] == 0) and (data_json["apartmentsAvailable"]["3"] ==280):
                        status = "No apartments available"
                        counter = counter + 1
                        print(counter)
                        # return(status, counter)
                        # print("checking apartment availbility", counter)
                        
                                
                else:
                        status = "apartments available"
                        return (status, counter)
        except:
                print("we have an error")
                # active = True
        

# while True:
#     thejob()
#     time.sleep(2)
