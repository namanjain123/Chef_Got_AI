from flask import Flask, request
app = Flask(__name__)


@app.route('/api2', methods=['POST'])  
def api2():
   data = request.get_json()
   # process data
   return "OK"
@app.route('/api1', methods=['POST'])
def api1():
   data = request.get_json()
   # process data
   return "OK"
