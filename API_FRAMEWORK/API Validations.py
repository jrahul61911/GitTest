
import requests
class A:

    def getAPI(self):
        rq=requests.get('https://rahulshettyacademy.com/maps/api/place/get/json?key=qaclick123&place_id=1f3f536d81ae001def46f66fae3be1c2')
        print(rq.json())

a = A()
a.getAPI()





# time.sleep(3)
# rp = requests.post('http://127.0.0.1:5000/users', json={
#     "color": "#53B0AE",
#     "name": "llow_turquoise619",
#     "pantone_value": "0-5173",
#     "year": 20010
# }, )
# print(rp.json())
# print(rp.status_code)

# time.sleep(3)
# ru = requests.put('http://127.0.0.1:5000/users/2', json={
#     "color": "#7BC4C4",
#     "id": 2,
#     "name": "aqua sky_231",
#     "pantone_value": "14-4811122",
#     "year": 2001
# })
# print(ru.json())
#
# time.sleep(3)
# rd = requests.delete(' http://127.0.0.1:5000/users/1')
# print(rd.json())
# print(rd.status_code)
