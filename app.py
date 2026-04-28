from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    # Serves the calculator user interface
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        num1 = float(data.get('num1', 0))
        num2 = float(data.get('num2', 0))
        operation = data.get('operation')

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                return jsonify(error="Cannot divide by zero"), 400
            result = num1 / num2
        else:
            return jsonify(error="Invalid operation"), 400

        return jsonify(result=result)
    except Exception as e:
        return jsonify(error="Invalid input"), 400

if __name__ == '__main__':
    # The 0.0.0.0 is crucial for Docker networking!
    app.run(host='0.0.0.0', port=5000)
