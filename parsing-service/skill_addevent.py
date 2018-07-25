import requests
from datetime import datetime, timedelta
from flask import Flask, Response, request, json
import uuid
import json

token = 'eyJ0eXAiOiJKV1QiLCJub25jZSI6IkFRQUJBQUFBQUFEWHpaM2lmci1HUmJEVDQ1ek5TRUZFdlZBazRxUXlkVGE0SXd1VGIwVVVvVHVPemdfWDg0VDh4US1oTklHODNzQnZkZDN6cW9fN19kWGlFQ0Q0TVhwVHhySU93d1o1OC1UWFRTVE1BcU5xN1NBQSIsImFsZyI6IlJTMjU2IiwieDV0IjoiN19adWYxdHZrd0x4WWFIUzNxNmxValVZSUd3Iiwia2lkIjoiN19adWYxdHZrd0x4WWFIUzNxNmxValVZSUd3In0.eyJhdWQiOiJodHRwczovL2dyYXBoLm1pY3Jvc29mdC5jb20iLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC83MmY5ODhiZi04NmYxLTQxYWYtOTFhYi0yZDdjZDAxMWRiNDcvIiwiaWF0IjoxNTMyNDczOTA1LCJuYmYiOjE1MzI0NzM5MDUsImV4cCI6MTUzMjQ3NzgwNSwiYWNjdCI6MCwiYWNyIjoiMSIsImFpbyI6IkFVUUF1LzhJQUFBQUV2a0lDQ0orTVh0c2VzbWpNMGY2b29qZnRDcUw0cytLM2NNY2JHYWFsWXlCUGF5bFovSmlCelI3cHZaajdhQ1NWb1llZXRnNUJIQ2kwMDlZRVBtKzlBPT0iLCJhbXIiOlsid2lhIiwibWZhIl0sImFwcF9kaXNwbGF5bmFtZSI6IkdyYXBoIGV4cGxvcmVyIiwiYXBwaWQiOiJkZThiYzhiNS1kOWY5LTQ4YjEtYThhZC1iNzQ4ZGE3MjUwNjQiLCJhcHBpZGFjciI6IjAiLCJmYW1pbHlfbmFtZSI6IkphaW4iLCJnaXZlbl9uYW1lIjoiU2hsb2FrIiwiaW5fY29ycCI6InRydWUiLCJpcGFkZHIiOiIxNjcuMjIwLjEwMy40NyIsIm5hbWUiOiJTaGxvYWsgSmFpbiIsIm9pZCI6IjVlYTIwYzJhLTNhODctNDE5ZC1hOWRjLWY3MzlmMjZiMGRmNyIsIm9ucHJlbV9zaWQiOiJTLTEtNS0yMS0yMTI3NTIxMTg0LTE2MDQwMTI5MjAtMTg4NzkyNzUyNy0zMTY4MjEwOSIsInBsYXRmIjoiMyIsInB1aWQiOiIxMDAzMDAwMEFBQkZGRTE5Iiwic2NwIjoiQ2FsZW5kYXJzLlJlYWRXcml0ZSBDb250YWN0cy5SZWFkV3JpdGUgRGV2aWNlTWFuYWdlbWVudEFwcHMuUmVhZC5BbGwgRGV2aWNlTWFuYWdlbWVudEFwcHMuUmVhZFdyaXRlLkFsbCBEZXZpY2VNYW5hZ2VtZW50Q29uZmlndXJhdGlvbi5SZWFkLkFsbCBEZXZpY2VNYW5hZ2VtZW50Q29uZmlndXJhdGlvbi5SZWFkV3JpdGUuQWxsIERldmljZU1hbmFnZW1lbnRNYW5hZ2VkRGV2aWNlcy5Qcml2aWxlZ2VkT3BlcmF0aW9ucy5BbGwgRGV2aWNlTWFuYWdlbWVudE1hbmFnZWREZXZpY2VzLlJlYWQuQWxsIERldmljZU1hbmFnZW1lbnRNYW5hZ2VkRGV2aWNlcy5SZWFkV3JpdGUuQWxsIERldmljZU1hbmFnZW1lbnRSQkFDLlJlYWQuQWxsIERldmljZU1hbmFnZW1lbnRSQkFDLlJlYWRXcml0ZS5BbGwgRGV2aWNlTWFuYWdlbWVudFNlcnZpY2VDb25maWcuUmVhZC5BbGwgRGV2aWNlTWFuYWdlbWVudFNlcnZpY2VDb25maWcuUmVhZFdyaXRlLkFsbCBEaXJlY3RvcnkuQWNjZXNzQXNVc2VyLkFsbCBEaXJlY3RvcnkuUmVhZFdyaXRlLkFsbCBGaWxlcy5SZWFkV3JpdGUuQWxsIEdyb3VwLlJlYWRXcml0ZS5BbGwgSWRlbnRpdHlSaXNrRXZlbnQuUmVhZC5BbGwgTWFpbC5SZWFkV3JpdGUgTWFpbGJveFNldHRpbmdzLlJlYWRXcml0ZSBOb3Rlcy5SZWFkV3JpdGUuQWxsIG9wZW5pZCBQZW9wbGUuUmVhZCBwcm9maWxlIFJlcG9ydHMuUmVhZC5BbGwgU2l0ZXMuUmVhZFdyaXRlLkFsbCBUYXNrcy5SZWFkV3JpdGUgVXNlci5SZWFkQmFzaWMuQWxsIFVzZXIuUmVhZFdyaXRlIFVzZXIuUmVhZFdyaXRlLkFsbCBlbWFpbCIsInNpZ25pbl9zdGF0ZSI6WyJrbXNpIl0sInN1YiI6IlNyNm51V0N1T2NiQ3U3MnhYY2xfM051RlB4WFNhc05KZVFUd2hiNjZJdnMiLCJ0aWQiOiI3MmY5ODhiZi04NmYxLTQxYWYtOTFhYi0yZDdjZDAxMWRiNDciLCJ1bmlxdWVfbmFtZSI6InQtc2hqYUBtaWNyb3NvZnQuY29tIiwidXBuIjoidC1zaGphQG1pY3Jvc29mdC5jb20iLCJ1dGkiOiJBMUFQcldjcVlFQzRFWWI1a2pVREFBIiwidmVyIjoiMS4wIiwieG1zX3N0Ijp7InN1YiI6ImhTUk1Dd3NneGdJMVV4M0NNMC1HVnRIODlDX0FublhYdmcxUHExOGo3cjAifX0.UWh-EhI9NQ1QjgHsYgB3b1d6B5TGr3uNdLHjGnDNKEKpLESSkwQ9A29AQ058-F6Ve6sxwzOU2lNxrYiKoZu6AGlafqABRaJ6JbpD-KJfIVaZ1RLOcopshOC9SIdrIlvxNudUkKihvBF1cfCzK3RWJLAxB7j4MFlO4pS7mnligy6t8XyAqDCPcmW-QMHPkB_kpfmfw4mt6Wad6axgT4LlY1FD5pJdmj6OpbzF81FqLv_tmIwhTUDAdhuwUU1ga9NLYXSSNSPTX7K_IYRSOYTBA_glRO9hqy7bs16_uY3T1t53VDHoXadKcsGE1Ou7j4uIWD1wo701SAQ9mf40zZ57pg'
graph_endpoint = 'https://graph.microsoft.com/v1.0{0}'
app = Flask(__name__)
months = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12}

def make_api_call(method, url, token, payload = None, parameters = None):
  # Send these headers with all API calls
  headers = { 'Authorization' : 'Bearer {0}'.format(token),
              'Accept' : 'application/json',
              'Prefer': 'outlook.timezone="Pacific Standard Time"',
              'Prefer': 'outlook.body-content-type="Text"' }

  # Use these headers to instrument calls. Makes it easier
  # to correlate requests and responses in case of problems
  # and is a recommended best practice.
  request_id = str(uuid.uuid4())
  instrumentation = { 'client-request-id' : request_id,
                      'return-client-request-id' : 'true' }

  headers.update(instrumentation)

  response = None

  if (method.upper() == 'GET'):
      response = requests.get(url, headers = headers, params = parameters)
  elif (method.upper() == 'DELETE'):
      response = requests.delete(url, headers = headers, params = parameters)
  elif (method.upper() == 'PATCH'):
      headers.update({ 'Content-Type' : 'application/json' })
      response = requests.patch(url, headers = headers, data = json.dumps(payload), params = parameters)
  elif (method.upper() == 'POST'):
      headers.update({ 'Content-Type' : 'application/json' })
      response = requests.post(url, headers = headers, data = json.dumps(payload), params = parameters)

  return response

# takes in python datetime object, returns all events within param: days
# retuns json with subject, location, details, start, end, attendees fields if you have accepted the event
def get_events(date, num_days=1):
  get_messages_url = graph_endpoint.format('/me/calendarview')

  start_date = date.strftime('%Y-%m-%dT%H:%M:%SZ')
  end_date = (date + timedelta(days=num_days)).strftime('%Y-%m-%dT%H:%M:%SZ')
  query_parameters = {'startdatetime': start_date,
                      'enddatetime': end_date}

  r = make_api_call('GET', get_messages_url, token, parameters = query_parameters)
  accepted_response = {'accepted', 'organizer'}

  if (r.status_code == requests.codes.ok):
    json_response = r.json()["value"]
    events = [{'subject': e['subject'].encode('utf-8'), 'location': e['location']['displayName'].encode('utf-8'), 'details': e['bodyPreview'], \
    'start': (datetime.strptime(e['start']['dateTime'][:-8], '%Y-%m-%dT%H:%M:%S') + timedelta(hours=-7)).strftime("%Y-%m-%d %H:%M:%S"), \
    'end': (datetime.strptime(e['end']['dateTime'][:-8], '%Y-%m-%dT%H:%M:%S') + timedelta(hours=-7)).strftime("%Y-%m-%d %H:%M:%S"), \
    "attendees": [{'name': a['emailAddress']['name'].encode('utf-8')} for a in e['attendees']]} for e in json_response if e['responseStatus']['response'] in accepted_response]
    return events
  else:
    return "{0}: {1}".format(r.status_code, r.text)

@app.route('/', methods = ['POST'])
# takes in json body of intents
# add event to calendar when available during working hours
def api_root():
  post_data = request.json
  if post_data['intent'] == 'add-task':
      subject, deadline, duration = None, None, None
      for e in post_data['entities']:
        if 'Calendar.Subject' in e:
            subject = e['Calendar.Subject']
        if 'builtin.datetimeV2.duration' in e:
            duration = int(''.join(filter(str.isdigit, e["builtin.datetimeV2.duration"])))
        if "builtin.datetimeV2.date" in e:
            if 'min' in e["builtin.datetimeV2.date"]:
                duration = int(''.join(filter(str.isdigit, e["builtin.datetimeV2.date"])))
            else:
                for month in months:
                    if month in e["builtin.datetimeV2.date"]:
                        deadline = datetime(2018, months[month], int(''.join(filter(str.isdigit, e["builtin.datetimeV2.date"]))), 17, 00)
      if subject and deadline and duration:
          print(subject, deadline, deadline + timedelta(minutes=duration))
          get_messages_url = graph_endpoint.format('/me/events')
          time = find_open_time(deadline, duration)
          event = {"subject": subject, "start": {"dateTime": time.strftime('%Y-%m-%dT%H:%M:%S'), "timeZone": "Pacific Standard Time"}, "end": {
              "dateTime": (time + timedelta(minutes=duration)).strftime('%Y-%m-%dT%H:%M:%S'),
              "timeZone": "Pacific Standard Time"
          }}
          r = make_api_call('POST', get_messages_url, token, payload=event)
          if (r.status_code == requests.codes.ok or r.status_code == 201):
            resp = Response(json.dumps({"txt-response": "Task successfully added at {}".format(time)}), status=200, mimetype='application/json')
            return resp
          else:
            print("{0}: {1}".format(r.status_code, r.text))
  resp = Response(json.dumps({"txt-response": "Failed to add task."}), status=200, mimetype='application/json')
  return resp

def find_open_time(deadline, duration):
    date_now = (datetime.now() + timedelta(minutes=60)).replace(microsecond=0,second=0,minute=0)
    #print((deadline - date_now).days)
    all_events = get_events(date_now, (deadline - date_now).days)
    listings = [True] * (((deadline - date_now).days * 48) + (deadline - date_now).seconds // 60 // 30)
    #print('len: ', len(listings))
    for e in all_events:
        start = datetime.strptime(e['start'], "%Y-%m-%d %H:%M:%S")
        end = datetime.strptime(e['end'], "%Y-%m-%d %H:%M:%S")
        #print(e['subject'], start, e['start'])
        #print('start ind', (start - date_now).days * 48 + ((start - date_now).seconds // 60 // 30))
        #print('end ind', (end - date_now).days * 48 + ((end - date_now).seconds // 60 // 30) + 1)
        for i in range((start - date_now).days * 48 + ((start - date_now).seconds // 60 // 30), (end - date_now).days * 48 + ((end - date_now).seconds // 60 // 30) + 1):
            listings[i] = False
    for i in range(len(listings)):
        if is_valid(listings, i, duration, date_now):
            #print('ret ind', i)
            return date_now + timedelta(minutes=30*i)

def is_valid(listings, index, duration, date_now):
    return all([listings[i] for i in range(index, index + duration // 30 + 2)]) and (date_now + timedelta(minutes=30*index)).weekday() < 5 and (date_now + timedelta(minutes=30*index)).hour > 9 \
     and (date_now + timedelta(minutes=30*index)).hour < 17  



if __name__ == '__main__':
    app.run()

#date = datetime.now()
#print(get_events(date))