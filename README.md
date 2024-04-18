# Optimising Convolutional Neural Network Parameters for Morphing Rovers in GECCO 2023 Space Optimisation Challenge

## About the Project
This source code contains the implementations to solve the Morphing Rovers Challenge from GECCO 2023 SpOC 2: New Mars Settlement Program


## Installing Modules
```sh 
pip install cmaes scipy pygad matplotlib
```


## Obtaining Evaluation Code
1. Download Evaluation Code from [SpOC2-main](https://github.com/esa/SpOC2/archive/refs/heads/main.zip)
2. Unzip the folder and navigate to the Morphing Rovers directory which is shown in the path "SpOC2-main\Morphing Rovers" 
3. Copy both the "morphing_udp.py" file and the "data" folder and paste them into this directory.

## Source File Breakdown
1. The "Final_Results" folder contains the final results of each algorithm for the challenge along with their corresponding solutions in a .json file which is formatted for submission in the competition page and a .txt file which constains a list of the parameters. 
2. "AdaptiveRandomSearch.py" contains the implementation for adaptive random search 
3. "DualAnnealing.py" contains the implementation for dual annealing
4. "GeneticAlgorithm.py" contains the implementation for genetic algorithm
5. "CMAES.py" contains the implementation for covariance matrix adaptation evolution strategy
6. "Optimisation.py" contains the customised fitness function using handpicked scenarios
7. "Functions.py" contain miscellaneous functions used for creating arrays and saving solutions. 

## GitHub Repository
_Below is the code to clone the github repository for the implementations_

Clone the repo:
```sh
git clone https://github.com/japhialoo/SpOC2-Morphing-Rovers.git
```