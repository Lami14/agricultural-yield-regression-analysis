import statsmodels.api as sm

def build_regression_model(X, y):
    """
    Fit ordinary least squares regression model
    """
    X = sm.add_constant(X)
    model = sm.OLS(y, X).fit()
    return model
