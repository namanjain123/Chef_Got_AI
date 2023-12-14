from flask import Flask, jsonify, request
import LLM_Get_DishesName as ChefLLM;

# create a Flask 
app = Flask(__name__)

@app.route('/api/dishes', methods=['POST'])
def api1():
   try:
      data = request.get_json()
      ingrident = data['ingrident']
      details=data['details']
      pointers=data['pointers']
      list_dishes=ChefLLM.get_Dishes_option(ingrident,details,pointers)
      return jsonify(list_dishes)
   except Exception as e:
        return jsonify({"error": str(e)}), 400
