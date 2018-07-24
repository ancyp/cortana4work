import requests
# from flask import Flask, Response, request, json

# app = Flask(__name__)

headers = {
    'Ocp-Apim-Subscription-Key': '1f1a322001154e3fb21d99b4622934d8',
}


# @app.route('/', methods = ['POST'])
# takes in json body {'command': <value>}
def get_intent(command):
    global headers
    # post_data #= request.json
    params = {
    'q': command,
    # Optional request parameters, set to default values
    'timezoneOffset': '0',
    'verbose': 'false',
    'spellCheck': 'false',
    'staging': 'false',
    }
    result = requests.get('https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/0a56a648-9802-4774-8986-5a7603228448', headers=headers, params=params)
    result_json = result.json()
    print('entities:', result_json['entities'])
    entities = [{e['type']: e['entity']} for e in result_json['entities']]
    intent = {"intent": result_json['topScoringIntent']['intent'], "entities": entities}
    # dict = json.dumps(dict)
    # resp = Response(dict, status=200, mimetype='application/json')
    return intent

# if __name__ == '__main__':
    # app.run()