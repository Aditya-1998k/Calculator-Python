from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        expression = request.json['expression']
        result = str(eval(expression))
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": 'invalid expression'})
    

if __name__=='__main__':
    app.run(debug=True)
