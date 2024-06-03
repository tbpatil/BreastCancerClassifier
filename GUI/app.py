from flask import Flask, request, jsonify, render_template
import model
import csv
import json
import ydf 
import pandas as pd

app = Flask(__name__)
model = ydf.load_model("GUI\model")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Check if a file was uploaded
    uploaded_file = request.files['file']
    if '.csv'     in uploaded_file.filename :
        # parse into dictionary if csv
        uploaded_file.save('GUI\static\data.csv')
        with open('GUI\static\data.csv', 'r' ) as file:
        
        
            csv_reader = csv.DictReader(file)
            data = [row for row in csv_reader]
        # convert into json file 
        with open('data.json', 'w' ) as file:
             json.dump(data,file,indent=4)
        
        # print(data.json)
                
        # extension = uploaded_file.filename.split('.')[1]
        # print(extension)
        newData=pd.DataFrame(data)
        predicition=model.predict(newData)
        print(predicition[0])
        if predicition[0]==1.0:
            return render_template('malignant.html')
        else:
            return render_template('benign.html')
        return int (predicition[0])
    # if 'file' in request.files:
    #     #uploaded_file = request.files['file']
    #     print(uploaded_file.filename )
    #     # Process the uploaded file using your model
    #     # For example:
    #     # prediction = model.predict_from_file(uploaded_file)
    #     # return jsonify({'prediction': prediction})
    #     return "File uploaded successfully. Prediction result will be shown here."

    else:
        # If no file was uploaded, handle form data as before
        print("BLAH")
        # data = request.form.to_dict()
        # feature_values = [float(data[key]) for key in data]
        # prediction = model.predict(feature_values)
        # return jsonify({'prediction': int(prediction)})
        return ("No file")

if __name__ == "__main__":
    app.run(debug=True)
