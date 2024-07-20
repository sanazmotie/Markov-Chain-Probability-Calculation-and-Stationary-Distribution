# Markov Chain Probability Calculation and Stationary Distribution

This project is part of a Linear Algebra course and provides a Python-based solution for analyzing Markov chains.

## Introduction
This project involves two main tasks:
1. Calculating the probability of a specific state after a given number of steps in a Markov chain.
2. Computing the stationary distribution of a Markov chain.


## Code Description

### Markov Chain Probability Calculation
The code computes the probability of being in a specific state after a certain number of steps. The process involves defining the states, transition names, and transition matrix. The probability calculation is repeated multiple times to get an accurate percentage.

Example states and transition matrix:

```python
states = ["Sleep", "Icecream", "Run"]
transitionName = [["SS", "SR", "SI"], ["RS", "RR", "RI"], ["IS", "IR", "II"]]
transitionMatrix = [[0.2, 0.6, 0.2], [0.1, 0.6, 0.3], [0.2, 0.7, 0.1]]
```

The code then checks if the sum of each row in the transition matrix equals one, indicating a valid transition matrix. The user is prompted to input the starting and last states, and the `activity_forecast` function is used to simulate the Markov process. The results are stored and the probability is calculated based on the simulations.

### Stationary Distribution Calculation
The stationary distribution is the distribution of states that remains unchanged as the Markov process progresses. The code takes a user-defined transition matrix and computes the left eigenvector corresponding to the eigenvalue of 1, which is then normalized to give the stationary distribution.

