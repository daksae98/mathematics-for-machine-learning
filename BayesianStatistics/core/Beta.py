import math
import numpy as np
import sympy as sy
import matplotlib.pyplot as plt


def Beta(a, b):
    def BetaDistribution(theta):
        return math.gamma(a+b)/math.gamma(a)/math.gamma(b)*math.pow(theta, a-1)*math.pow(1-theta, b-1)

    return BetaDistribution


def BetaSy(a, b, theta):

    return sy.gamma(a+b)/sy.gamma(a)/sy.gamma(b)*theta**(a-1)*(1-theta)**(b-1)


def IntegralBetaSy(a, b):

    BetaDistribution = Beta(a, b)

    theta = np.linspace(0.01, 1, 101)

    points = np.array([[t, BetaDistribution(t)] for t in theta])

    plt.plot(points[:, 0], points[:, 1])

    theta = sy.symbols('theta')
    beta = BetaSy(a, b, theta)
    I = sy.Integral(beta, (theta, 0, 1))
    print(sy.pretty(I))
    print('\n값:', sy.integrate(beta, (theta, 0, 1)).evalf())
