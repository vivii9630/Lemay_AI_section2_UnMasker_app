
from flask import Flask, render_template, request, jsonify
from flask_restful import Resource, Api
import time
import threading
import torch

from transformers import pipeline
unmasker = pipeline('fill-mask', model='bert-base-uncased')
#unmasker("Hello I'm a [MASK] model.")
app = Flask(__name__)
api = Api(app)


#tokenizer = AutoTokenizer.from_pretrained(model_path, local_files_only=True)
#model = AutoModelForSequenceClassification.from_pretrained(model_path, local_files_only=True)
#pipe = TextClassificationPipeline(model=model, tokenizer=tokenizer)

tweets = [{'content': 'dont know what todo', 'date': '17-02-2021', 'id': '1', 'example': 'I am [MASK] driver'},
          {'content': 'doing flask and its pretty great', 'date': '18-02-2021', 'id': '2', 'example': 'I am [MASK] diver'}]

# print(keras.__version__)
# model = load_model('./tf_model.h5')


def task():
    #background process handling by threads
    print("Started Task ...")
    print(threading.current_thread().name)
    time.sleep(5)
    print("completed .....")

@app.route('/', methods=['GET'])
def test():
    #content = request.get_json('content')
    example = request.json['example']
    #hasil = pipe(content)
    fill_mask = unmasker(example)
    #print(hasil[0]['label'])
    return jsonify({'message': example, 'mask':fill_mask})


class lemay_mask(Resource):
    @app.route('/tweet', methods=['POST'])
    def createTweet():
        threading.Thread(target=task).start()
        example = request.json['example']
        fill_mask = unmasker(example)
        tweet = {'example' : example,
             'date': request.json['date'], 'id': request.json['id'], 'mask':fill_mask}

        tweets.append(tweet)
        return jsonify({'data': tweet})


api.add_resource(lemay_mask, '/tweet')

