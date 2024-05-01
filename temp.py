import joblib  # Or pickle, if you used that for saving

import pickle


model = joblib.load('ML_Model/iris_model.pkl')

# Use the model for predictions
new_data = [[9.0, 3.5, 1.4, 0.2]]
species_mapping = {
    "setosa": 0,
    "versicolor": 1,
    "virginica": 2
}

# ... Get user input (as a string)

predicted_numerical_label = model.predict(new_data)
predicted_species = list(species_mapping.keys())[list(species_mapping.values()).index(predicted_numerical_label)]

print(predicted_species)