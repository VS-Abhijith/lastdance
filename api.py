from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

# Get the absolute path of the current file
dir_path = os.path.dirname(os.path.realpath(__file__))

# Load data from JSON file
try:
    with open(os.path.join(dir_path, 'q-vercel-python.json'), 'r') as file:
        data = json.load(file)
except Exception as e:
    data = []
    print(f"Error loading JSON file: {e}")

@app.route('/api', methods=['GET'])
def get_marks():
    try:
        names = request.args.getlist('name')
        marks = [student['marks'] for student in data if student['name'] in names]
        return jsonify({"marks": marks})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run()
