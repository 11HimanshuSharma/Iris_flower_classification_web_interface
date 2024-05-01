from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)


model = joblib.load('iris_model.pkl')  

@app.route('/', methods=['GET', 'POST'])
def index():
    species_mapping = {
    "setosa": 0,
    "versicolor": 1,
    "virginica": 2
    }
    if request.method == 'POST':
        sepal_length = float(request.form['sepal_length'])
        sepal_width = float(request.form['sepal_width'])
        petal_length = float(request.form['petal_length'])
        petal_width = float(request.form['petal_width'])

        new_input = np.array([sepal_length, sepal_width, petal_length, petal_width]).reshape(1, -1)
        predicted_numerical_label = model.predict(new_input)
        predicted_species = list(species_mapping.keys())[list(species_mapping.values()).index(predicted_numerical_label)]

        return render_template('index.html', prediction_text=predicted_species)

    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True) 
