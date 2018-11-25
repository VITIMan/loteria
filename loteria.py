
import json
import time
import datetime
import requests

numbers_2016 = {
    "MAILLO": 91473,
    "PABLO": 30807,
    "MARINA": 85766,
    "MAITE": 9358,
    "MMMERY": 42545,
    "RUF": 88119,
    "PAKO": 9520,
    "POETNXO": 18042,
    "POETNXO BONUS TRACK": 8851,
    "PAQUI": 99579,
    "VITI": 77944,
    "DANTE": 20914,
    "JORGE": 88669,
}

numbers = {
    "MAILLO": 96380,
    "IGNACIO": 6368,
    "PAKO": 72599,
    "P4BL0L": 30807,
    "PAQUI": 91217,
    "MARINA": 57746,
    "SARAY": 29282,
    "IVETTE": 50547,
    "SAMER": 76581,
    "MAITE": 51815,
    "YOLANDA": 99833,
    "MMMERY": 84832,
    "RUF": 61464,
    "PENTXO": 67497,
    "ISA": 62414,
    "DAAANTE": 7550,
    "JOROGE": 39684,
    "GABI": 93308,
    "LUISMI": 39969,
    "CHEX": 97283,
    "VIT SAN": 72686,
    "ZUR ZUR": 36678,
    "PEDROPA": 32084
}

API_LOTERIA = "http://api.elpais.com/ws/LoteriaNavidadPremiados"

now = datetime.datetime.now()

struct = {
    name: {
        "number": number,
        "premio": 0,
        "hora": now.strftime("%H:%M")} for name, number in numbers.iteritems()}


while True:
    with open("loteria.txt", "w") as f:
        results = []
        for name, number in numbers.iteritems():
            try:
                print("query {}".format(name))
                result = requests.get(API_LOTERIA, params={"n": number})
                results.append({"name": name, "number": number, "result": result, "premio": 0, "hora": ""})
            except Exception:
                pass

        for result in results:
            text = result["result"].content
            if "busqueda=" in text:
                text = text.replace("busqueda=", "")

            data = {}
            try:
                data = json.loads(text)
            except Exception:
                pass
            if "premio" in data:
                struct[result["name"]]["premio"] = data["premio"]
                struct[result["name"]]["hora"] = datetime.datetime.now().strftime("%H:%M")

        for name, v in struct.iteritems():
            f.write("{}: {}, premio:{} hora:{} \n".format(name, v["number"],
                                                          v["premio"], v["hora"]))
        total = sum([v["premio"] for v in struct.itervalues()])
        f.write("TOTAL:{}\n".format(total))

    time.sleep(30)

