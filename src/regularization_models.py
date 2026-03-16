from sklearn.linear_model import LassoCV, RidgeCV

def run_lasso(X, y):
    model = LassoCV(cv=5)
    model.fit(X, y)
    return model


def run_ridge(X, y):
    alphas = [0.001, 0.01, 0.1, 1, 10, 100]
    model = RidgeCV(alphas=alphas, cv=5)
    model.fit(X, y)
    return model
