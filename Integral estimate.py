import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

# Define the function to integrate
def g(x):
    return np.exp((-x**2)/2)

print("This program evaluates the integral 'exp((-x**2)/2)' from a to b using the Monte Carlo method.")
while True:
    # Get user inputs
    while True:
        try:
            N = int(input("Insert the number of trials: "))
            a = float(input("Assign a value for a: "))
            b = float(input("Assign a value for b: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer for N and valid floats for a and b.")

    # Generate random numbers and evaluate the integral
    x = np.random.uniform(low=a, high=b, size=N)
    y = np.random.uniform(low=0, high=1.1, size=N)
    fun = np.exp((-x**2)/2)
    m = np.mean(fun)
    print(m)
    integration = (b - a) * m
    print("The montecarlo value of the integral is: {}".format(integration))
    # Print the exact value of the integral
    exact = integrate.quad(g,a,b)
    print("The exact value of the integral is: {}".format(exact[0]))

    # Plot the results
    ins = y - np.exp((-x**2) / 2) < 0
    x_in = x[ins]
    y_in = y[ins]
    plt.figure(figsize=[10, 10])
    plt.scatter(x, y, s=1)
    plt.scatter(x_in, y_in, color='r', s=1)
    plt.text(1, 2.145, "Value of the integral:", fontsize=14)
    plt.text(4, 2.15, f"{integration:.4f}", bbox=dict(facecolor='red', alpha=0.5))
    plt.pause(0.01)
    plt.show()



    # Ask the user if they want to run the program again
    check = input("Do you want to quit or start again? Enter Y to restart or another key to end: ")
    if check.upper() == "Y":
        continue
    else:
        print("Bye...")
        break
