import numpy as np
import Functions as fun
import morphing_udp as m
import Optimisation as opt
import matplotlib.pyplot as plt

############################################################################################################################################
##### Adaptive Random Search Implementation
############################################################################################################################################

udp = m.morphing_rover_UDP()
example = udp.example()
example = example.tolist()
lb, ub = udp.get_bounds()

def run(split, iter, scenarios, initial_range):
    '''
    Runs random search algorithm for parameter optimisation.
    Returns the best parameters found

    Args:
        lb: Lower bounds of the parameters
        ub: Upper bounds of the parameters
        split: range to split the parameters into 
        iter: total number of iterations
        scenarios: Hand picked scenarios to evaluate fitness on
        initial_range: Initial solution space

    Returns:
        best_params: Returns the best parameters obtain through hybrid random search
        best_score: Returns the best score obtained through hybrid random search
    '''

    print("Optimising.......")
    best_params = []
    best_score = 100.00
    scores = []
    param_values = initial_range
    temp = 0

    for i in range(iter):
        params = [np.random.choice(values) for values in param_values]
        score = opt.fitness(params=params, scenarios=scenarios, details=False)
        print(f"Fitness is {score:.6f} at iteration", i+1, end='\r')
        if score < best_score: 
            best_score = score
            best_params = params
            split -= 2
            if split <= 0:
                split = 2
            param_values = fun.CreateRange(best_params, 0.01, split)
            temp = i
            
        scores.append(best_score)
                 
        if i - temp == 2000:
            split += 2
            param_values = fun.CreateRange(best_params, 0.01, split)
        print(f"\nBest Fitness is {best_score:.6f}", end='\r')
        
    plt.plot(scores, '-g') 
    plt.xlabel('Iteration')
    plt.ylabel('Best Score')
    plt.title('Change in Best Score over Iterations')
    plt.grid(True)
    plt.show()
    
    return best_params, best_score

starting_range = fun.CreateRange(example, 0.01, 30)
scenarios = [1, 0, 2, 1, 4, 4]

best_params, best_score = run(split=20, iter=10000, scenarios=scenarios, initial_range=starting_range)

# Saving results and solutions locally
score = udp.fitness(best_params)
filename = f"ARS_2.txt"
fun.update_results_file(filename, best_params, score)
fun.create_submission("spoc-2-morphing-rovers","morphing-rovers", best_params, "ARS_2.json","Japhia Loo","Testing out optimsation methods for this challenge.")


print(udp.pretty(best_params))
udp.plot(best_params)
plt.show()