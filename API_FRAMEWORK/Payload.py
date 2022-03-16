from utilities.configurations import *


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
        "website": "http://google.com/user",
        "language": "RUSSIAN_UKRAINE_INDIA_PAK"
    }

    return body


def updatePlacePayload():
    body = {
        "place_id": "c1b3ce1b05562df6f8fb153e06fa2dad",
        "address": "70 summer talk, india",
        "key": "qaclick123"
    }
    return body


def deletePlacePayload():
    body = {
        "place_id": "c1b3ce1b05562df6f8fb153e06fa2dad"
    }
    return body


def buildPayloadDB(query):
    addBody = {}
    tp = getQuery(query)
    addBody['name'] = tp[0]
    addBody['isbn'] = tp[1]
    addBody['aisle'] = tp[2]
    addBody['author'] = tp[3]
    return addBody
