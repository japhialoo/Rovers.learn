import morphing_udp as m

############################################################################################################################################
##### Optimised Fitness Function
############################################################################################################################################    
            
# Custom Fitness Function
def fitness(params, scenarios, max = False, details = False):
    '''
    Custom fitness function to evaluate fitness on handpicked scenarios instead of running the entire fitness function
    
    Args:
        params: Parameters to evaluate
        scenarios: Handpicked scenarios to evaluate the parameters on
        max: True if optimisation algorithm maximises the fitness score. Default value False
        details: If True, prints scores for each scenario and average score. Default value False
    
    Returns:
        avg: Final score accross handpicked scenarios
    '''
    maps = [0, 1, 2, 3, 4, 5]
    udp = m.morphing_rover_UDP()
    function = udp.run_single_scenario
    rover = m.Rover(params)
    fitness_scenario = []
    time_scenario = []
    scores = []
    score = 0
    total_time = 0
    
    for i in range(len(scenarios)):
        temp_fit, temp_time = function(rover, maps[i], scenarios[i])
        ind_score = (1+temp_fit) * temp_time
        scores.append(ind_score)
        fitness_scenario.append(float(temp_fit))
        time_scenario.append(float(temp_time))
        total_time += time_scenario[i]
        score += ind_score
    
    avg = float(score/len(scenarios))
    if details:
        print("Scoress across all scenarios: ", scores)
        print("Total time taken: ", float(total_time))
        print(f"Score: {avg:.4f}")
    
    if max:
        return avg*-1
    else:
        return avg