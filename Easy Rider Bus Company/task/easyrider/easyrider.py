import re
import json


checks = [
    {"field": "bus_id", "type": "Integer", "format": None, "required": True, "errors": 0},
    {"field": "stop_id", "type": "Integer", "format": None, "required": True, "errors": 0},
    {"field": "stop_name", "type": "String", "format": r"[A-Z].+ (Road|Avenue|Boulevard|Street)$", "required": True, "errors": 0},
    {"field": "next_stop", "type": "Integer", "format": None, "required": True, "errors": 0},
    {"field": "stop_type", "type": "String", "format": r"[SOF]?$", "required": False, "errors": 0},
    {"field": "a_time", "type": "String", "format": r"[0-2][0-9]:[0-5][0-9]$", "required": True, "errors": 0}
]

bus_line = []


db = json.loads(input())

for db_item in db:
    for check in checks:
        if check["type"] == "Integer":
            if not (isinstance(db_item[check["field"]], int) or (check["required"] is False and len(str(db_item[check["field"]])) == 0)):
                check["errors"] += 1

        elif check["type"] == "String":
            if not (isinstance(db_item[check["field"]], str) and re.match(check["format"], str(db_item[check["field"]]))):
                check["errors"] += 1

    if not any(d['bus_id'] == db_item['bus_id'] for d in bus_line):
        bus_line.append({'bus_id': db_item['bus_id'], 'stops': 0})
    for d in bus_line:
        if d['bus_id'] == db_item['bus_id']:
            d['stops'] += 1

# print(f"Format validation: {sum([check['errors'] for check in checks])} errors")
# for check in checks:
#     if check["field"] in ["stop_name", "stop_type", "a_time"]:
#         print(check["field"] + ":", check["errors"])

print("Line names and number of stops:")
for bus_lines in bus_line:
    print("bus_id: " + str(bus_lines['bus_id']) + ",", "stops: " + str(bus_lines['stops']))


