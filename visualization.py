import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def visualize_data(file_path):
    df = pd.read_csv(file_path)
    
    # Histogram
    df.hist()
    plt.show()

    # Density plots
    plt.subplots(3, 3, figsize=(15, 15))
    for idx, col in enumerate(df.columns):
        ax = plt.subplot(3, 3, idx + 1)
        ax.yaxis.set_ticklabels([])
        sns.distplot(df.loc[df.Outcome == 0][col], hist=False, axlabel=False, kde_kws={'linestyle': '-', 'color': 'black', 'label': "No Diabetes"})
        sns.distplot(df.loc[df.Outcome == 1][col], hist=False, axlabel=False, kde_kws={'linestyle': '--', 'color': 'black', 'label': "Diabetes"})
        ax.set_title(col)
    plt.subplot(3, 3, 9).set_visible(False)
    plt.show()
