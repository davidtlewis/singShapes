import urllib.parse
import requests

stop_code = "47591"
api = "http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2?BusStopCode=" + stop_code

r=requests.get(api, headers={"AccountKey":"aqQltF5FR+iUcFVdYDQxxA=="}).json()

#print (r)

for bus_service in r['Services']:
    for which_bus in ['NextBus','NextBus2','NextBus3',]:
        if ((bus_service[which_bus]['Latitude'] != "0") and (bus_service[which_bus]['Longitude'] != "0") and bus_service[which_bus]['EstimatedArrival'] != ""):
            print (bus_service['ServiceNo'],",",bus_service[which_bus]['EstimatedArrival'],",",bus_service[which_bus]['Latitude'],",",bus_service[which_bus]['Longitude'])   

