from flask import Flask, render_template, request, jsonify
import app
import json
app = Flask(__name__,template_folder=r'templates/')
from scrape import process_data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit-form', methods=['POST'])
def submit_form():
    data = json.loads(request.data)
    result = process_data(data)
    print(result)
    print("22222222222222")
    return jsonify(result)

if __name__ == '__main__':
    app.run( debug=True)
