import matplotlib.pyplot as plt

def residual_plot(y_true, y_pred):

    residuals = y_true - y_pred

    plt.scatter(y_pred, residuals)

    plt.axhline(0, linestyle="--")

    plt.xlabel("Fitted Values")
    plt.ylabel("Residuals")

    plt.title("Residuals vs Fitted")

    plt.savefig("../results/residual_plot.png")

    plt.close()
