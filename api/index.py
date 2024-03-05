from flask import Flask, request, jsonify
from urllib.parse import quote
import urllib, json
import re

app = Flask(__name__)

# Dummy storage for JSON data
stored_data = {"added":"none"}

@app.route('/webhook/github', methods=['POST'])
def github_webhook():
    global stored_data
    event_type = request.headers.get('X-GitHub-Event')

    if event_type == 'ping':
        return jsonify({'msg': 'Ping received'})

    if event_type == 'push':
        payload = request.json
        handle_push_event(payload)
        return jsonify({'msg': 'Push event received'})

    return jsonify({'msg': 'Unhandled event'}), 400

def handle_push_event(payload):
    global stored_data
    # Instead of taking info from the payload the push event will simply trigger the data to fill from github using the github timer to time json updates
    


    data = payload
    added_files = data['commits'][0]['added']
    stored_data['added'] = added_files
    
    # Assets/Data/Alexandria/Main_2024-03-05_Queried_at_13h59m.json

    

@app.route('/api/<city>', methods=['GET'])
def get_json_data_city(city):
    global stored_data

    for elem in stored_data:
        if elem[-5:] == ".json":
            assetName = elem[12:]
            assetName = re.match(r"^\w+", assetName).group()
            if assetName == city:
                # Encode the URL with UTF-8
                urlBase = "https://raw.githubusercontent.com/Leosly7663/Weather-Data-Analysis/main/"

                encoded_url = quote(urlBase + elem, safe=':/')

                response = urllib.request.urlopen(encoded_url, timeout=1)  # Set timeout to 1 second
                return({[assetName] : json.loads(response.read())})

                    # 404 ERROR: https://raw.githubusercontent.com/Leosly7663/Weather-Data-Analysis/main/Assets/Data/Ottawa%20(Kanata%20-%20Orléans)/Main_2024-03-05_Queried_at_17h36m.json 
                    # I FOUND THE STUPID UNICODE CHARACTER THAT HAS BEEN TORMENTING ME FOR HOURS



        else:
            continue
    return ()

@app.route('/', methods=['GET'])
def get_json_data():
    global stored_data
    return jsonify(stored_data)

if __name__ == '__main__':
    app.run(debug=True)
