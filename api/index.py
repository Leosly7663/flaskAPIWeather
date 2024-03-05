from flask import Flask, request, jsonify
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
    urlBase = "https://raw.githubusercontent.com/Leosly7663/Weather-Data-Analysis/main/"


    data = payload
    added_files = data['commits'][0]['added']

    
    # Assets/Data/Alexandria/Main_2024-03-05_Queried_at_13h59m.json

    for elem in data['commits'][0]['added']:
        if elem[-5:] == ".json":
            assetUniqueLink = elem
            assetName = elem[12:]
            assetName = re.match(r"^\w+", assetName).group()

            url = urlBase + assetUniqueLink
            url = url.replace(" ", "%20")

            try:
                response = urllib.request.urlopen(url)
                stored_data[assetName] = json.loads(response.read())
            except:
                print("404 ERROR: "+ url)


        else:
            continue
    


    



def fetch_json_data(file_path, commit_url):
    # Implement fetching JSON file content from GitHub using commit URL or other means
    # This is a simplified example; you may need to use GitHub API or other methods
    # For demonstration, we simply assume it's fetched from a URL
    # In real-world, you may need to authenticate with GitHub API
    json_data = {"example": "data"}
    return json_data

@app.route('/api/<city>', methods=['GET'])
def get_json_data_city():
    global stored_data
    return jsonify(stored_data[city])

@app.route('/', methods=['GET'])
def get_json_data():
    global stored_data
    return jsonify(stored_data)

if __name__ == '__main__':
    app.run(debug=False)
