import pandas as pd
import matplotlib.pyplot as plt
from src.utils.model import get_unique_filename
import os


def save_plot(history, plot_name, plots_dir):
    pd.DataFrame(history.history).plot(figsize=(10, 7))
    plt.grid(True)
    unique_filename = get_unique_filename(plot_name)
    path_to_plot = os.path.join(plots_dir, unique_filename)
    plt.savefig(path_to_plot)