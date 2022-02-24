import requests
import configparser
from Payload import *
from utilities.resources import *
from utilities.configurations import *
class ApiFramework:
    url_get = getConfig()['API']['endpoint'] + APIResources.getmaps
    url_post = getConfig()['API']['endpoint'] + APIResources.addmaps
    url_put = getConfig()['API']['endpoint'] + APIResources.updatemaps
    url_del = getConfig()['API']['endpoint'] + APIResources.deletemaps

    def get_book(self, url_get):
        get_APIresponsE = requests.get(self.url_get, json=addBookPayload(),
                                       headers={"Content-Type": "application/json"})
        print(get_APIresponsE.json())


getAPI = ApiFramework()
getAPI.get_book(url_get=getConfig()['API']['endpoint'] + APIResources.getmaps)
# add_UserResponse = requests.post(url_post, json=addBookPayload()
#                                   , headers={"Content-Type": "application/json"})
# print(add_UserResponse.json())

# def get_API():
#     get_Userresponse = requests.get(url_get, timeout=0.001)
#     print(get_Userresponse.json())
#
# print(add_UserResponse.json())
#
# update_User = requests.put(url_post, timeout=0.001)
# print(update_User.json())

# if add_BookResponse.status_code == 404:
#     raise Exception("Please re enter name")
# else:
#     print(f"The status code after adding book is {add_BookResponse.status_code}")
# response = add_BookResponse.json()
# print(response)
# print(add_BookResponse.status_code)
