from flask import Blueprint, request, jsonify, render_template
import os
import requests
import json
from .utils import create_tf_serving_json

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/gateway/chat/invocations', methods=['POST'])
def chat_invocations():
    try:
        dataset = request.get_json()
        chat_api_url = os.environ.get('ADB_SERVINGENDPOINT_URL')
        headers = {'Authorization': f"Bearer {os.environ.get('ADB_BEARER_TOKEN')}",
                   'Content-Type': 'application/json'}
        ds_dict = {
            "dataframe_split": {
                "columns": ["prompt"],
                "index": [0],
                "data": [[dataset]]
            }
        }
        data_json = json.dumps(ds_dict, allow_nan=True)
        response = requests.post(url=chat_api_url, headers=headers, data=data_json)

        if response.status_code != 200:
            raise Exception(f'Request failed with status {response.status_code}, {response.text}')
        response_data = response.json()

        return jsonify(response_data), response.status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500