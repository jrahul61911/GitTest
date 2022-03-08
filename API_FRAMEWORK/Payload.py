from  utilities.configurations import *
def addPlacePayload():
    body = {
        "location": {
            "lat": -38.38342,
            "lng": 33.42722
        },
        "accuracy": 500,
        "name": "R",
        "phone_number": "(+92) 921 893 3937",
        "address": "292, side3 layoutd, cohend 09",
        "types": [
            "shoe park_01",
            "shop_near"
        ],
        "website": "http://google.com",
        "language": "RUSSIAN_UKRAINE_INDIA"
    }

    return body


def updatePlacePayload():
    body = {
        "place_id": "c7b4fb65ecce98390d57676f75b5c990",
        "address": "70 summer talk, india",
        "key": "qaclick123"
    }
    return body


def deletePlacePayload():
    body = {
        "place_id": "c7b4fb65ecce98390d57676f75b5c990"
    }
    return body


def buildPayloadDB(query):
    addBody = {}
    tp = getQuery(query)
    addBody['first_name'] = ''
    addBody['last_name'] = ''
    addBody['gender'] = ''
    addBody['hire_date'] = ''
    return addBody
