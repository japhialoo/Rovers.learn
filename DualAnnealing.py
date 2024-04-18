import numpy as np
import morphing_udp as m
import Optimisation as opt
import Functions as fun
import time
import matplotlib.pyplot as plt 
from scipy.optimize import dual_annealing

############################################################################################################################################
##### Dual Annealing Implementation
############################################################################################################################################

udp = m.morphing_rover_UDP()
example = udp.example()
mask_params = example[:m.NUM_MODE_PARAMETERS]
pooling = example[m.NUM_NN_PARAMS:]
scores = []
i = 0


def fitness(solution):
    '''
    Fitnesse function for dual annealing.
    
    Args:
        solution: Solution to be evaluated
    
    Returns:
        score: Fitness value of the solution being evaluated
    '''
    scenarios = [1, 0, 2, 2, 4, 4]
    global i
    i += 1
    score = opt.fitness(solution, scenarios, details=False)
    print(f"Score is {score:.6f} at iteration {i}")
    global scores
    scores.append(score)
    return score

start_time = time.time()

lb, ub = udp.get_bounds()
result = dual_annealing(func=fitness, bounds=list(zip(lb, ub)), maxfun=10000)

plt.plot(scores, '-g')

elapsed_time = time.time() - start_time
print(f"Elapsed time for Simulated Annealing to run {elapsed_time: .2f} seconds")
time.sleep(1)

best_score = result.fun
best_solution = result.x

# Output results
print("Best score found:", best_score)

# Saving results and solutions locally
filename = "DualAnnealing.txt"
fun.update_results_file(filename, best_solution, best_score)
fun.create_submission("spoc-2-morphing-rovers","morphing-rovers", best_solution, "DualAnnealing.json","Japhia Loo","Testing out optimsation methods for this challenge.")


print(udp.pretty(best_solution))
udp.plot(best_solution)
plt.show()