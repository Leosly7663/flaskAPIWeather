from flask import Flask, request, jsonify
from urllib.parse import quote
import urllib, json
import re
from urllib.parse import unquote
from flask_cors import CORS

app = Flask(__name__)

# Dummy storage for JSON data


CORS(app)

@app.route('/api/<city>', methods=['GET'])
def get_json_data_city(city):

    city = unquote(city)
    
    recentsLink = "https://raw.githubusercontent.com/Leosly7663/Weather-Data-Analysis/main/Assets/Recent.json"
    urlBase = "https://raw.githubusercontent.com/Leosly7663/Weather-Data-Analysis/main/"

    responseRecent = urllib.request.urlopen(recentsLink, timeout=1)  # Set timeout to 1 second
    stored_data = json.loads(responseRecent.read())

    # Encode the URL with UTF-8
    

    encoded_url = quote(urlBase + stored_data[city], safe=':/')

    response = urllib.request.urlopen(encoded_url) 
    data = json.loads(response.read())


    return data

        # 404 ERROR: https://raw.githubusercontent.com/Leosly7663/Weather-Data-Analysis/main/Assets/Data/Ottawa%20(Kanata%20-%20Orléans)/Main_2024-03-05_Queried_at_17h36m.json 
        # I FOUND THE STUPID UNICODE CHARACTER THAT HAS BEEN TORMENTING ME FOR HOURS


@app.route('/', methods=['GET'])
def get_json_data():
    return ("No data selected")

if __name__ == '__main__':
    app.run(debug=True)
