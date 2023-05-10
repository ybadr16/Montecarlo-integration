# Monte Carlo Integration

This repository contains two Python scripts (`method1.py` and `method2.py`) that demonstrate the Monte Carlo integration method.

## Method 1

The file `method1.py` implements the Monte Carlo integration method to evaluate the integral of the function `exp((-x**2)/2)` from `a` to `b` where:
The mean value of a function $(f\)$ over the interval $\([a, b])\$ is given by:
$\[ \langle f \rangle = \frac{1}{b - a} \int_{a}^{b} f(x) \, dx \]$

It generates random numbers and estimates the integral using the mean value of the function. The script also plots the results, including the exact value of the integral.




## Method 2

The file `method2.py` uses the Monte Carlo integration method to estimate the value of the integral by approximating the area under a curve defined by a user-provided function where:


$$\\frac{{\text{{Area under integral}}}}{{\text{{Area of rectangle}}}} = \frac{{\text{{Random points in integral}}}}{{\text{{Total random points}}}}\$$



It generates random samples and checks if they fall within the curve. The script also creates an animation of the sampling process and saves it as a GIF file.





Make sure you have the necessary dependencies installed, such as NumPy, Matplotlib, and SciPy.

Feel free to explore and modify the scripts according to your needs!
