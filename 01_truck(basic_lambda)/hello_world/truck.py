import json

def lambda_ticket(event,context):
    ticket = {
        "passenger": event["name"],
        "from": event["start"],
        "destination": event["end"],
        "data": "2021-12-02"
    }
    return ticket

def lat_long(event,context):
    location = {
        "latitude" : event["latitude"],
        "longitude" : event["longitude"]
    }
    return location