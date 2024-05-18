# Naming-Name-Models

This repository contains the updated scripts in Python 3.8 to simulate the Naming Game (NG) model and its many variants. During the last recent years while I was developing a new variant of NG based upon the Bayesian inference, I wrote many scripts for simulating the dynamics of its variants, including their time-evolution in different types of complex networks such as random graphs, graphs with small-world properties  and scale-free networks. However, the scripts were written in Python 2.7 as this version was required for running the scripts in parallel on computer clusters. However,  Python 2.7  reached the end of its life on January 1st, 2020, however until one year I had to make scripts in Python 2.7. For this reason, I am rewriting the previous scripts in Python 3.8, adding also some changes/improvement when required. It is worth noting that it is crucially required to have very good pseudo-random generators for simulating the dynamics. Luckily, Python provides very good algorithms for random number generators from its library  [numpy](https://numpy.org/). Note that in some scripts the agents are implemented as objects as in such a case, it is easier to simulate a real-life semiotic dynamics of consensus, or to embedded the agents on nodes of a specific complex networks by means of the Python library  [NetworkX](https://networkx.org/). For instance, in Figure below from my multi-agent simulations it is shown  the average memory per agent in the system (top panel), and the number of different words (bottom panel), as functions of the rescaled time, for the Erdos-Renyi network, the Barabasi-Albert network (both networks have average degree equal to four), and the complete graph. We refer the reader to G. Marchetti, at al., A bird's-eye view of naming game dynamics: From trait competition to Bayesian inference, Chaos: An Interdisciplinary Journal of Nonlinear Science, **30**, 6, 063119, 2020, and references therein for details. Please, if you find any mistake contact me via email at gionnimarchetti@gmail.com or
gionnimarchettiminstp@gmail.com. Thank you very much.

![Figura From Chaos](https://github.com/GionniMarchettiMInstP/Naming-Name-Models/blob/main/NGdynamics.png)

## Table of contents
- [Python](#Python)
- [Usage](#usage)
  - [Input](#input)
- [Citation](#citation)

## Python 
The script has been tested  with Python 3.8.10. 3.8.16, 3.11.5

The following library is also required for running the scripts
 - [NumPy](https://numpy.org/)

## Usage
The script `ng2c.py` simulate the semiotic dynamics of an ensemble of agents in number N restricted to two names A and B corresponding to
integers 0 and 1, respectively, starting from an initial configuration chosen by the user. Note that in such a model there will be always 
consensus at some time (the convergence time), that is, convergence to a state where all the agents have one name, either A or B, in their inventories. For such a simple model, except for the convergence time, there are two only observables: the total number of names and the success rate of the agents' pairwise interaction. The simulation outputs, including the convergence time and the maximum number of names are 
stored into file `results.text`.

## Input
Before to launch the script the user needs to input the following values in the input file `input.text`: number of agents N, initial number of agents with A, initial number of agents with B, number of steps for the simulation and the seed for the random number generator. The suitable choice of number of steps depends upon the system size N and can be inferred by the corresponding scaling law in Gionni Marchetti et al., Chaos: An Interdisciplinary Journal of Nonlinear Science, **30**, 6, 063119, 2020 and references therein. The seed is necessary for the reproducibility of the results. 

## Citation 
Gionni Marchetti, et al., A bird's-eye view of naming game dynamics: From trait competition to Bayesian inference, Chaos: An Interdisciplinary Journal of Nonlinear Science, **30**, 6, 063119, 2020
    





