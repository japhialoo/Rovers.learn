from cmaes import CMA
import Functions as fun
import numpy as np
import morphing_udp as m
import Optimisation as opt
import time
import matplotlib.pyplot as plt

############################################################################################################################################
##### Covariance Matrix Adaptation Evolution Strategy Implementation
############################################################################################################################################

# Getting mean and bounds for each parameter and variable initialisation
udp = m.morphing_rover_UDP()
lb, ub = udp.get_bounds()
bounds = []
mean = []
generation = 2500
scenarios = [1, 0, 2, 1, 4, 4]
best_params = []
best_score = 100
scores = []
hl, = plt.plot([],[])
iterations = []
scores = []


for i in range(len(lb)):
    bounds.append([lb[i], ub[i]])
    mean.append((ub[i]+lb[i])/2)

# Initialising CMA with means and bounds obtained from udp.get_bounds()
optimiser = CMA(mean=np.array(mean), bounds=np.array(bounds), sigma=1.3, n_max_resampling=100, population_size=4)


# Running CMA 
for j in range(generation):
    solutions = []
    for i in range(optimiser.population_size):
        start_time = time.time()
        point = optimiser.ask()
        elapsed_time = time.time() - start_time
        print(f"Elapsed time for ask to run is {elapsed_time: .2f} seconds")
        time.sleep(1)
        
        score = opt.fitness(point, scenarios, details=False)
        solutions.append((point, score))
        
        if score < best_score:
            best_score = score
            best_params = point
        
        scores.append(best_score)
    print(f"Best score in generation {j+1} is {best_score:.6f} ")
    optimiser.tell(solutions)

# Plotting best score through the iterations
plt.plot(scores, '-g')

# Saving solution locally
filename = "CMAES.txt"
fun.update_results_file(filename, best_params, best_score)
fun.create_submission("spoc-2-morphing-rovers","morphing-rovers", best_params, "Genetic_Algorithm.json","Japhia Loo","Testing out optimsation methods for this challenge.")

print(udp.pretty(best_params))
udp.plot(best_params)
plt.show()