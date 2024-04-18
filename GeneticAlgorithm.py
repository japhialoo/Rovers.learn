import pygad
import numpy as np
import Functions as fun
import morphing_udp as m
import Optimisation as opt
import matplotlib.pyplot as plt

############################################################################################################################################
##### Genetic Algorithm Implementation
############################################################################################################################################

udp = m.morphing_rover_UDP()
i = 0
j = 1
best_score= 100.00
scores = []
best_solution = []

def run():
    '''
    Runs Genetic Algorithm on specified range and parameters for optimisation.
    Returns best solution found along with it's fitness value
    
    Returns:
        best_solution: Best solution found
        best_fitness: Fitness value of best solution found
    '''
    
    print("Running Optimisation with Genetic Algorithm.......")
    ga = pygad.GA(num_generations=40, sol_per_pop=250, num_parents_mating=4, fitness_func=fitness, num_genes=m.NUM_NN_PARAMS, init_range_low=-100, 
                  init_range_high=100, parent_selection_type="tournament", K_tournament=3, crossover_type="two_points", crossover_probability=0.6, mutation_type="random", 
                  mutation_probability=0.4, save_best_solutions=True)

    ga.run()
    ga.plot_fitness()
    global scores, best_score, best_solution
    plt.plot(scores)
    
    return best_solution, best_score


def fitness(ga_instance, solution, solution_idx):
    '''
    Custom fitness function for genetic algorithm formatting
    '''
    
    global i, j, best_score, scores, best_solution
    i += 1
    
    scenarios = [1, 0, 2, 2, 4, 4]
    example = udp.example()
    mask_params = example[:m.NUM_MODE_PARAMETERS]
    pooling = example[m.NUM_NN_PARAMS:]
    complete = np.concatenate([mask_params, solution, pooling])
    
    score = opt.fitness(complete, scenarios, max=True, details=False)
    
    if score*-1 < best_score:
        best_score = score*-1
        best_solution = complete

    print(f"Score is {score*-1:.6f} for run ", i, " in generation ", j, end='\r')
    
    if i == 250:
        i = 0
        j += 1
    
    print(f"\n Best score in generation {j}: {best_score:.6f}", end='\r')
    
    scores.append(best_score)

    return score

best_params, best_score = run()

# Saving results and solutions locally
filename = "Genetic_Algorithm.txt"
fun.update_results_file(filename, best_params, best_score)
fun.create_submission("spoc-2-morphing-rovers","morphing-rovers", best_params, "Genetic_Algorithm.json","Japhia Loo","Testing out optimsation methods for this challenge.")

print(udp.pretty(best_params))
udp.plot(best_params)
plt.show()