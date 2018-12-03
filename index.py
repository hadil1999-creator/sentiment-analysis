# -*- coding: utf-8 -*-

import sys
import six
import os

from flask import Flask, jsonify, request
from google.cloud import language_v1
from google.cloud.language_v1 import enums


app = Flask(__name__)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./credentials.json"


def analyze_sentiment(content):
    client = language_v1.LanguageServiceClient()

    if isinstance(content, six.binary_type):
        content = content.decode("utf-8")

    type_ = enums.Document.Type.PLAIN_TEXT
    document = {
        "language": "pt-BR",
        "type": enums.Document.Type.PLAIN_TEXT,
        "content": content,
    }

    response = client.analyze_sentiment(document)
    sentiment = response.document_sentiment

    return {
        "Score": sentiment.score,
        "Magnitude": sentiment.magnitude,
    }


@app.route("/", methods=["GET", "POST"])
def hello():
    if request.method == 'POST':
        json_data = request.get_json(force=True)
        return jsonify(analyze_sentiment(content=json_data['content']))
    else:
        return jsonify({"message": "POST at `/` with the following JSON object: `{content: string}`"})


def main():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "3000")), debug=False)


if __name__ == '__main__':
    main()
