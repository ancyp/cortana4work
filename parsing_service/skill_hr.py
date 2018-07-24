import requests
from flask import Flask, Response, request, json, Blueprint

skill_hr = Blueprint('skill_hr',__name__)

# todo: move this to a DB
all_records = []

@skill_hr.route('/report-time-off', methods = ['POST'])
# takes in json body {'command': <value>}
def api_root(post_data):
    print(post_data.keys(),"*******")
    global all_records
    # post_data = request.json
    if post_data['intent'] == 'get-time-off':
        txt_response = 'Here are your records: '
        for r in all_records:
            txt_response += r["start-date"] + ', ' + r["duration"] + '. '
        resp = Response(json.dumps({"records": all_records, "txt-response": txt_response}), status=200, mimetype='application/json')
        return resp
    # post_data = request.json
    if post_data['intent'] == 'add-time-off':
        start_date, duration = None, None
        for e in post_data['entities']:
            if "builtin.datetimeV2.duration" in e:
                duration = e["builtin.datetimeV2.duration"]
            if "builtin.datetimeV2.date" in e:
                start_date = e["builtin.datetimeV2.date"]
        if start_date and duration:
            all_records.append({"start-date": start_date, "duration": duration})
            return "hr_skill.html" , {}
            resp = Response(json.dumps({"txt-response": "Enjoy your time off"}), status=200, mimetype='application/json')
            return resp

    resp = Response(json.dumps({"txt-response": "Unable to add"}), status=200, mimetype='application/json')
    return resp

if __name__ == '__main__':
    app.run()