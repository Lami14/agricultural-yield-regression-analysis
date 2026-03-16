import pandas as pd
from sklearn.metrics import mean_squared_error
import numpy as np

def evaluate_model(name, y_true, predictions):

    mse = mean_squared_error(y_true, predictions)

    rmse = np.sqrt(mse)

    return {
        "Model": name,
        "MSE": mse,
        "RMSE": rmse
    }
