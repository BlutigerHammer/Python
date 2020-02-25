import numpy as np
import matplotlib.pyplot as plt
import math
from scipy. special import factorial


def monte_carlo(number_of_questions, number_of_responses, accuracy=1000):
    probability = np.zeros(number_of_questions + 1)
    points = 0
    for j in range(accuracy):
        for i in range(number_of_questions):
            if np.random.randint(0, number_of_responses) == 1:
                points += 1
        probability[points] += 1
        points = 0
    probability = 100 * probability / accuracy

    distribution = np.zeros(number_of_questions + 1)
    for i in range(1,len(probability)):
        distribution[i] = distribution[i-1] + probability[i]              
    
    return probability, distribution


def poisson(number_of_questions, number_of_responses):
    # f(k,u) = (u**k * exp(-u)) / k!
    # k - number of successes, u - expected value
    u = number_of_questions / number_of_responses
    probability = np.linspace(0, number_of_questions, number_of_questions+1)
    probability = np.power(u,probability) * np.exp(-u) / factorial(probability)

    distribution = np.zeros(number_of_questions + 1)
    for i in range(1,len(probability)):
        distribution[i] = distribution[i-1] + probability[i]
        
    return probability, distribution


def plot(prob_poisson, distr_poisson, prob_mc, distr_mc):
    x = range(len(prob_poisson))

    plt.subplot(2,2,1)
    plt.bar(x, prob_poisson)
    plt.title('Probability Poisson')

    plt.subplot(2,2,2)
    plt.bar(x, distr_poisson)
    plt.title('Distribution Poisson')
    
    plt.subplot(2,2,3)
    plt.bar(x, prob_mc)
    plt.title('Probability Monte Carlo')

    plt.subplot(2,2,4)
    plt.bar(x, distr_mc)
    plt.title('Distribution Monte Carlo')
    
    
    plt.show()

    
mc1, mc2 = monte_carlo(30, 4, 10000)
p1, p2 = poisson(30,4)
plot(p1,p2,mc1,mc2)
