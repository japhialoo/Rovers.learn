import os
import json
import datetime
import numpy as np
import morphing_udp as m

############################################################################################################################################
##### Miscellaneous Functions
############################################################################################################################################

def CreateInt(lb, ub, size):
    params = [[i for i in range(lb, ub)] for _ in range(size)] 

    return params

def CreateFloat(lb, ub, size, space):
    params = [[i for i in np.arange(lb, ub, space)] for _ in range(size)]

    return params

def CreateValues(lb, ub, split):
    params = []
    for i in range(len(lb)):
        row = []
        for j in np.arange(lb[i], ub[i], split):
            row.append(j)
        params.append(row)
    return params
            
            

def CreateMask(lb, mb, ub, size, space):
    centre_elements = [60, 181, 302, 423]
    params = [[j for j in np.arange(mb, ub, space)] if i in centre_elements else [j for j in np.arange(lb, ub, space)]  for i in range(size)]

    return params

def CreateRange(params, space, limits):
    example = params
    udp = m.morphing_rover_UDP()
    param_range = []
    lb, rb = udp.get_bounds()
    size = len(example)
    for i in range(size):
        row = []
        for j in np.arange(params[i] - limits, params[i] + limits, space):
            if j < lb[i]:
                row.append(lb[i])
            elif j > rb[i]:
                row.append(rb[i])
            else:
                row.append(j)
        param_range.append(row)
    
    return param_range

def create_submission(challenge_id, problem_id, x, fn_out = './submission.json', name = '', description= ''):
    """ The following parameters are mandatory to create a submission file:

        challenge_id: a string of the challenge identifier (found on the corresponding problem page)
        problem_id: a string of the problem identifier (found on the corresponding problem page)
        x: for single-objective problems: a list of numbers determining the decision vector
           for multi-objective problems: a list of list of numbers determining a population of decision vectors

        Optionally provide:
        fn_out: a string indicating the output path and filename
        name: a string that can be used to give your submission a title
        description: a string that can contain meta-information about your submission
    """
    assert type(challenge_id) == str
    assert type(problem_id) == str
    assert type(x) in [list, np.ndarray]
    assert type(fn_out) == str
    assert type(name) == str
    assert type(description) == str

    # converting numpy datatypes to python datatypes
    x = np.array(x).tolist()

    d = {'decisionVector':x,
         'problem':problem_id,
         'challenge':challenge_id,
         'name':name,
         'description':description }

    with open(fn_out, 'wt') as json_file:
        json.dump([d], json_file, indent = 6)
        
# Saving results locally
def update_results_file(filename, best_params, best_score):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    result_str = f"{best_params}\n"

    # Check if the file exists
    if os.path.exists(filename):
        # Append the result to the existing file
        with open(filename, 'a') as f:
            f.write(result_str)
    else:
        # Create a new file and write the result
        with open(filename, 'w') as f:
            f.write(result_str)