import matplotlib.pyplot as plt


input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
for i in plt.style.available:
    plt.style.use(i)
    fig, ax = plt.subplots()
    ax.plot(input_values, squares, linewidth=3)
    ax.set_title(f"Square Numbers ({i})", fontsize=24)
    ax.set_xlabel("Value", fontsize=14)
    ax.set_ylabel("Square of Value", fontsize=14)
    ax.tick_params(labelsize=14)
    plt.show()
