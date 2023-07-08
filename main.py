import mysql.connector
import requests
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Connect to the MySQL database
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='abuelkheir'
)


def wordSub(request_):
    input_ = request_.json.get('param')
    API_URL = "https://api-inference.huggingface.co/models/aubmindlab/bert-base-arabert"
    headers = {"Authorization": "Bearer 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"}

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()

    input_ = input_.replace('!', '[MASK]')
    outputs = query({
        "inputs": input_,
    })
    subWords = []
    for output in outputs:
        subWords.append(output.get('token_str'))
    return json.dumps(subWords)


def aautoComp(request_):
    print("he")
    param = request_.json.get('param')
    return json.dumps(param)


def spellChcker(request_):
    param2 = request_.json.get('param3')
    param3 = request_.json.get('param31')
    return json.dumps([param2, param3])


def plagiarism(request_):
    param3 = request_.json.get('param3')
    return json.dumps(param3)



@app.route("/", methods=['POST'])
def connect():
    if request.method == 'POST':
        serviceNo = request.json.get('serviceNo')
        if serviceNo == 1:
            return wordSub(request)
        elif serviceNo == 2:
          #return autocomplete_suggestions(request)
            return aautoComp(request)
        elif serviceNo == 3:
            return spellChcker(request)
        elif serviceNo == 4:
            return plagiarism(request)
        else:
            return json.dumps(['invalid service'])


if __name__ == "__main__":
    app.run(host="0.0.0.0")
