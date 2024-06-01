from flask import Flask, request, jsonify, render_template
import model

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form.to_dict()
    feature_values = [float(data[key]) for key in data]
    prediction = model.predict(feature_values)
    
    return jsonify({'prediction': int(prediction)})

if __name__ == "__main__":
    app.run(debug=True)
