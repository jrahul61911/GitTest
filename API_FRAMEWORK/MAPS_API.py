import requests
import configparser
from Payload import *
from utilities.resources import *
from utilities.configurations import *
import json


class ApiFramework:
    url_get = getConfig()['API']['endpoint'] + APIResources.getmaps
    url_post = getConfig()['API']['endpoint'] + APIResources.addmaps
    url_put = getConfig()['API']['endpoint'] + APIResources.updatemaps
    url_del = getConfig()['API']['endpoint'] + APIResources.deletemaps

    def add_maps(self, url_post):
        add_APIresponse = requests.post(self.url_post, json=addPlacePayload(),
                                        headers={"Content-Type": "application/json"})
        print(add_APIresponse.json())

    def update_maps(self, url_put):
        update_APIresponse = requests.put(self.url_put, json=updatePlacePayload(),
                                          headers={"Content-Type": "application/json"})
        print(update_APIresponse.json())

    def get_maps(self, url_get):
        get_APIresponsE = requests.get(self.url_get)
        print(get_APIresponsE.json())
        assert get_APIresponsE.status_code == 200

    def del_maps(self, url_del):
        del_APIresponse = requests.delete(self.url_del, json=deletePlacePayload(),
                                          headers={"Content-Type": "application/json"})
        print(del_APIresponse.json())


# if __name__ == "__main__":
#     getAPI = ApiFramework()
#     getAPI.add_maps('url_post')
#     getAPI.update_maps('url_put')
#     getAPI.get_maps('url_get')
#     getAPI.del_maps('url_del')
#     getAPI.maps_db_post()
