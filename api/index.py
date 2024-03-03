from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy storage for JSON data
stored_data = {}

@app.route('/webhook/github', methods=['POST'])
def github_webhook():
    event_type = request.headers.get('X-GitHub-Event')

    if event_type == 'ping':
        return jsonify({'msg': 'Ping received'})

    if event_type == 'push':
        payload = request.json
        handle_push_event(payload)
        return jsonify({'msg': 'Push event received'})

    return jsonify({'msg': 'Unhandled event'}), 400

def handle_push_event(payload):
    # Extract relevant data from the payload
    repository_name = payload['repository']['full_name']
    commits = payload['commits']

    # Fetch JSON files from commits and store them
    for commit in commits:
        for file in commit['added']:
            if file.endswith('.json'):
                # Example: Storing JSON data with commit ID as key
                commit_id = commit['id']
                stored_data[commit_id] = fetch_json_data(file, commit['url'])

def fetch_json_data(file_path, commit_url):
    # Implement fetching JSON file content from GitHub using commit URL or other means
    # This is a simplified example; you may need to use GitHub API or other methods
    # For demonstration, we simply assume it's fetched from a URL
    # In real-world, you may need to authenticate with GitHub API
    json_data = {"example": "data"}
    return json_data

@app.route('/api/json/<commit_id>', methods=['GET'])
def get_json_data(commit_id):
    if commit_id in stored_data:
        return jsonify(stored_data[commit_id])
    else:
        return jsonify({'error': 'Data not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
