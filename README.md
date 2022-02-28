# Tabu-Search 

Program for applying a tabu search algorithm on N-Queens Problem.

![8-Queens]

### Description

Taboo Search is a local search algorithm that uses a tabו list to prevent the development of previously developed steps.
This program tests the efficiency of the algorithm in terms of time and quality of solution against common local search algorithms
such as Hill Climbing, Random Restart and Simulated Annealing.
The test applyed on the problem of arranging N-Queens, but the algorithm can work on many other problems from the field of optimization.

### Installation

Install plotly: `pip install plotly`


### Usage

To run the program, please open the application and follow the steps below:
1. Through your terminal, run the main class: `python main.py <is_run_local_search> <number of queens> <number_of_iterations> <is_print_all_boards>`
2. <is_run_local_search> If you want to run local search for all the algorithms and print the board with the results. If you desire for graph put '0'. otherwise '1'.
3. <number of queens> The number of queues affects the different algorithms both in terms of runtime and in terms of space usage.
  Select the amount of queens you want to run in this argument. Remember, for N=1 there is a naive solution.
  For N=2 or N=3 there is no solution. Therefore select N>=4.
4. <number_of_iterations> Select a sufficient amount of iterations for the algorithm to get more accurate results and more reliable statistics.
5. <is_print_all_boards> Whether to print all the boards of all the iterations for each algorithm - 1 or 0. If 0 - will choose one random solution for printing.

 
### Dictionary
 
* Tabu Search
* Hill Climbing
* Hill Climbing Random Restart  
* Simulated Annealing  
* N-Queens  
* Mmain
* Run_algorithm
* Stats_and_plots

### Credits
  
In this project we examined the efficiency of the tabu search algorithm for the problem of N-Queens.
The Tabu Search code was written by Amit Twito and Itamar Laredo.
In purpose of comparing the algorithm to the different algorithms mentioned in the course, we used code from the following GitHub:
https://github.com/vitorverasm/ai-nqueens
The project was written as part of a project in Introduction to Optimization course, Bar-Ilan University.
