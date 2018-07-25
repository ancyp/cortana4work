import requests
from flask import Flask, Response, request, json
from twilio.rest import Client


app = Flask(__name__)

@app.route('/', methods = ['POST'])
def api_root():
    post_data = request.json
    if post_data['intent'] == 'notify':
        msg, target = None, None
        for e in post_data['entities']:
            if 'notification-msg' in e:
                msg = e['notification-msg']
            if 'notification-target' in e:
                target = e['notification-target']
        if msg:
            account_sid = 'AC2df2980c5ec1dbd6efd6441c5cbaa07e'
            auth_token = 'dc32d1267d6c0d843e89b85105eadec3'
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                                      body='This is Cortana on behalf of Shloak. He wanted to let you know: ' + msg,
                                      from_='+12065650895 ',
                                      to='+14084644203'
                                  )

            resp = Response(json.dumps({"txt-response": "Successfully notified {}!".format(target)}), status=200, mimetype='application/json')
            return resp
    resp = Response(json.dumps({"txt-response": "Unable to notify"}), status=200, mimetype='application/json')
    return resp

if __name__ == '__main__':
    app.run()