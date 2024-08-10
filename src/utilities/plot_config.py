import matplotlib.pyplot as plt
from matplotlib import rc


def apply_style():
    plt.rcParams.update(
        {
            "font.size": 12,
            "axes.labelsize": 14,
            "axes.titlesize": 16,
            "xtick.labelsize": 12,
            "ytick.labelsize": 12,
            "legend.fontsize": 12,
            "figure.titlesize": 16,
            "text.usetex": True,
            "font.family": "serif",
            "font.serif": ["Computer Modern Roman"],
            "text.latex.preamble": r"\usepackage{amsmath,amssymb,amsfonts}",
        }
    )

    rc("lines", linewidth=2, markersize=6)
    rc("axes", grid=True)
    rc("grid", linestyle="--", color="gray", alpha=0.7)
    rc("legend", loc="best")
