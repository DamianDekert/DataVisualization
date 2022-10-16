import matplotlib.pyplot as plt

#15.1
#x_values = [1, 2, 3, 4, 5]
#y_values = [1, 8, 27, 64, 100]

#15.2
x_values = range(5001)
y_values = [x**3 for x in x_values]

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10)

ax.set_title("Sześciany liczb", fontsize=24)
ax.set_xlabel("Wartości", fontsize=14)
ax.set_ylabel("Sześciany wartości", fontsize=14)

ax.tick_params(axis="both", labelsize=14)

ax.axis([0, 20, 0, 5100])

plt.show()
