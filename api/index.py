from flask import Flask, request, jsonify
from urllib.parse import quote
import urllib, json
import re

app = Flask(__name__)

# Dummy storage for JSON data

    

@app.route('/api/<city>', methods=['GET'])
def get_json_data_city(city):

    recentsLink = "https://raw.githubusercontent.com/Leosly7663/Weather-Data-Analysis/main/Assets/Recent.json"

    response = urllib.request.urlopen(recentsLink, timeout=1)  # Set timeout to 1 second
    stored_data = json.loads(response.read())

    return(stored_data)

    for elem in stored_data:
        if (elem[-5:] == ".json"):
            assetName = elem[12:]
            assetName = re.match(r"^\w+", assetName).group()
            if(assetName == city):
                # Encode the URL with UTF-8
                urlBase = "https://raw.githubusercontent.com/Leosly7663/Weather-Data-Analysis/main/"

                encoded_url = quote(urlBase + elem, safe=':/')

                response = urllib.request.urlopen(encoded_url, timeout=1)  # Set timeout to 1 second
                return jsonify({[assetName] : json.loads(response.read())})

                    # 404 ERROR: https://raw.githubusercontent.com/Leosly7663/Weather-Data-Analysis/main/Assets/Data/Ottawa%20(Kanata%20-%20Orléans)/Main_2024-03-05_Queried_at_17h36m.json 
                    # I FOUND THE STUPID UNICODE CHARACTER THAT HAS BEEN TORMENTING ME FOR HOURS
    return jsonify({"error": "City data not found " + city})

@app.route('/', methods=['GET'])
def get_json_data():
    return ("No data selected")

if __name__ == '__main__':
    app.run(debug=True)
