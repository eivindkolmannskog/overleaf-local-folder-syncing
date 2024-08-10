from utilities.plot_config import apply_style
import matplotlib.pyplot as plt
import os
apply_style()


def main() -> None:
    plt.plot([1, 2, 3], [-1, -2, -3], label="Line 1")
    plt.plot([1, 2, 3], [-2, -3, -4], label="Line 2")
    plt.xlabel("X-axis label")
    plt.ylabel(r"$\frac{\eta E_{11}}{\nu}$")
    plt.title("Title")
    plt.legend()
    plt.savefig(os.path.join("results", "plot.png")) 
    plt.show()



if __name__ == "__main__":
    main()
