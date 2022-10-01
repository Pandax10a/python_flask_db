import json
from flask import Flask

import dbhelpers as dh
app = Flask(__name__)

@app.get('/cars')


def get_car():
    cursor=dh.just_connect()
    results = dh.cursor_result(cursor, 'CALL show_all_car()')
    if(type(results) == list):
        car_json = json.dumps(results, default=str)
        dh.the_closer(cursor)
        return car_json
    else:
        dh.the_closer(cursor)
        return "sorry, try again"

app.run(debug=True)    

aa = get_car()
print(aa)