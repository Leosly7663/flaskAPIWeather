from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook/github', methods=['POST'])
def github_webhook():
    event_type = request.headers.get('X-GitHub-Event')

    if event_type == 'ping':
        return jsonify({'msg': 'Ping received'})

    if event_type == 'push':
        payload = request.json
        # Process the payload, update your React application accordingly
        handle_push_event(payload)
        return jsonify({'msg': 'Push event received'})

    return jsonify({'msg': 'Unhandled event'}), 400

def handle_push_event(payload):
    # Example function to handle push events
    repository_name = payload['repository']['full_name']
    commits = payload['commits']
    # Process commits and update React application
    return(commits)

if __name__ == '__main__':
    app.run(debug=True)