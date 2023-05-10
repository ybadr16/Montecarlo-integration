import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy import integrate, optimize

# Define parameters
num_samples = int(input('Number of samples you want: '))
a = int(input('Lower integral limit: '))
b = int(input('Upper integral limit: '))
f_str = input("Enter the function to be evaluated in python syntax: ")
f = eval(f"lambda x: {f_str}")

# Use scipy.optimize to find the maximum
result = optimize.minimize_scalar(lambda x: -f(x))
maximum_y = -result.fun

print("Maximum y value:", maximum_y)

maximum_y = maximum_y + 0.2 #this is less optimized but looks better

x = np.random.uniform(a, b, num_samples)
y = np.random.uniform(0, maximum_y, num_samples)

# Define the Monte Carlo calculation
def estimate_pi(num_samples):
    is_inside = y - f(x) < 0
    approx_pi = maximum_y * (b - a) * np.sum(is_inside) / num_samples
    return approx_pi, x[is_inside], y[is_inside]

# Estimate the value of pi using the Monte Carlo method
approx_pi, x_inside, y_inside = estimate_pi(num_samples)

# Print the estimated value of pi
exact = integrate.quad(f, a, b)[0]
print(f"Exact: {exact}, approximation: {approx_pi}")

# Create the plot and set the axes limits
fig, ax = plt.subplots(figsize=[10, 10])
ax.set_xlim(a, b)
ax.set_ylim(0, maximum_y)
ax.set_title("Monte Carlo Integration")
approx_text = ax.text(1, maximum_y + (maximum_y * 0.1), "", fontsize=14)

# Create the plot lines for the animation
line1, = ax.plot([], [], 'o')
line2, = ax.plot([], [], 'o', color='r')

# Initialize the text object with the approximation value
approx_text.set_text(f"Approximation: {approx_pi:.4f}")

# Define the animation update function
def animate(i):
    line1.set_data(x[:i], y[:i])
    if i < len(x_inside):
        line2.set_data(x_inside[:i], y_inside[:i])
    approx, _, _ = estimate_pi(i)
    approx_text.set_text(f"Approximation: {approx:.4f}")

# Create the animation
anim = FuncAnimation(fig, animate, frames=num_samples, interval=100, repeat=False)

plt.show()
anim.save("monte_carlo.gif", writer="pillow")
