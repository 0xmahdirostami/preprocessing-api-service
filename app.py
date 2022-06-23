from flask import Flask, request
import os
from utils.common import response_message
from utils.interpolation_methods import linear_interpolation
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def isup():
    return response_message('API is active')

@app.route('/service1', methods=['GET', 'POST'])
def interpolation():
    req = request.get_json()
    data = req['data']
    config = req['config']
    result = linear_interpolation(data, config)
    return response_message(dict({"data": result}))

@app.route('/service2', methods=['GET', 'POST'])
def interpolation2():
    req = request.get_json()
    data = req['data']
    config = req['config']
    result = linear_interpolation(data, config)
    return response_message(dict({"data": result}))

@app.route('/service3', methods=['GET', 'POST'])
def interpolation3():
    req = request.get_json()
    data = req['data']
    config = req['config']
    result = linear_interpolation(data, config)
    return response_message(dict({"data": result}))

@app.route('/service4', methods=['GET', 'POST'])
def interpolation4():
    req = request.get_json()
    data = req['data']
    config = req['config']
    result = linear_interpolation(data, config)
    return response_message(dict({"data": result}))

port = os.environ.get("PORT", 5000)
if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=port)