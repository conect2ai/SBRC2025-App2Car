import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns


def plot_histogram_kde(
    data,
    variable,
    hist_color,
    kde_color,
    bins=80,
    show_median=True,
    median_color="red",
    xlabel="Tempo de Execução (µs)",
    ylabel="Frequência",
    xlim=None,
    figsize=(14, 5)
):
    plt.figure(figsize=figsize)

    hist = sns.histplot(
        x=data[variable],
        bins=bins,
        kde=True,
        alpha=0.7,
        color=hist_color,
        label="Distribuição"
    )

    kde_line = hist.get_lines()[0]
    kde_line.set_color(kde_color)
    kde_line.set_linewidth(3)

    if show_median:
        median_value = data[variable].median()
        plt.axvline(median_value, color=median_color, linestyle="--", linewidth=2, label=f"Mediana: {int(median_value)} µs")

    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)

    if xlim:
        plt.xlim(xlim)
    else:
        plt.xlim(0, min(5000, data[variable].max()))

    plt.legend(loc="upper right", frameon=False, fontsize=12)
    plt.grid(True, linestyle="--", alpha=0.3)
    plt.show()
