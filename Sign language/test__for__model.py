import pickle

model_dict = {"example_key": "example_value"}  # Replace this with actual model data
with open("model.p", "wb") as f:
    pickle.dump(model_dict, f)  # Save the model
