from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
# Enable CORS to allow requests from the future frontend
CORS(app)

@app.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint to verify the API is running.
    """
    return jsonify({"status": "API is running"}), 200

if __name__ == '__main__':
    # Run the app on host 0.0.0.0 to make it accessible if needed, default port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
