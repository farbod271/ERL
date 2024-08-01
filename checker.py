import json
from urllib.request import urlopen
# from telegram.ext import CallbackContext

# class check_class:
#         def __init__(self, id, status, counter):
#                 self.id = id
#                 id = CallbackContext._chat_id
#                 self.status = status
#                 self.counter = counter
counter = 0
def thejob():
                global counter
                global status
                url  = "https://www.erl.de/wp-json/kundenportal/v1/onoffice/get-stammobjekt-free-apartments?id=573"

                response = urlopen(url)
                data_json = json.loads(response.read())

                try:
                        if (data_json["success"] == True) and data_json["apartmentsAvailable"]["0"] == 0 and (data_json["apartmentsAvailable"]["1"] == 0) and (data_json["apartmentsAvailable"]["2"] == 0) and (data_json["apartmentsAvailable"]["3"] ==219) and (data_json["apartmentsAvailable"]["4"] == 0):
                                status = "No apartments available"
                                counter += 1
                                print(counter)
                                # return(status, counter)
                                # print("checking apartment availbility", counter)
                                # some changes
                                
                                        
                        else:
                                status = "apartments available"
                                return (status, counter)
                except:
                        print("we have an error")
                        # active = True


def notjob():
                global status
                url  = "https://www.erl.de/wp-json/kundenportal/v1/onoffice/get-stammobjekt-free-apartments?id=573"

                response = urlopen(url)
                data_json = json.loads(response.read())

                try:
                        if (data_json["success"] == True) and data_json["apartmentsAvailable"]["0"] == 0 and (data_json["apartmentsAvailable"]["1"] == 0) and (data_json["apartmentsAvailable"]["2"] == 0) and (data_json["apartmentsAvailable"]["3"] ==280):
                                status = "No apartments available"
                                # return(status, counter)
                                # print("checking apartment availbility", counter)
                                
                                        
                        else:
                                status = "apartments available"
                                return (status)
                except:
                        print("we have an error")
                        # active = True
