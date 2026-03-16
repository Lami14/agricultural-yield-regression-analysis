import seaborn as sns
import matplotlib.pyplot as plt

def correlation_heatmap(df):

    corr = df.corr()

    plt.figure(figsize=(10,8))
    sns.heatmap(corr, cmap="coolwarm")

    plt.title("Correlation Matrix")
    plt.savefig("../results/correlation_heatmap.png")

    plt.close()
