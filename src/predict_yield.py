import pandas as pd

def predict(model, sample_data):

    prediction = model.predict(sample_data)

    return prediction
