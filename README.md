# Naming-Name-Models

This repository contains the updated scripts in Python 3.8 to simulate the Naming Game (NG) model and its many variants. During the last recent years while I was developing a new variant of NG based upon the Bayesian inference, I wrote many scripts for simulating the dynamics of its variants, including their time-evolution in different types of complex networks such as random graphs, graphs with small-world properties  and scale-free networks. However, the scripts were written in Python 2.7 as this version was required for running the scripts in parallel on computer clusters. However,  Python 2.7  reached the end of its life on January 1st, 2020, however until one year I had to make scripts in Python 2.7. For this reason, I am rewriting the previous scripts in Python 3.8, adding also some changes/improvement when required. It is worth noting that it is crucially required to have very good pseudo-random generators for simulating the dynamics. Luckily, Python provides very good algorithms for random number generators from its library numpy (https://numpy.org/). Note that in some scripts the agents are implemented as objects as in such a case, it is easier to simulate a real-life semiotic dynamics of consensus, or to embedded the agents on nodes of a specific complex networks by means of the Python library NetworkX (https://networkx.org/).


## Table of contents
- [Python](#Python)
- [Usage](#usage)
  - [Input Variables](#input-variables)
  - [Running Scripts](#Running-script)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [Citation](#citation)

## Python Versions and Required Packages  
The script has been tested  with Python 3.8.10. 3.8.16, 3.11.5

The following library is also required for running the scripts
 - [NumPy](https://numpy.org/)

## Usage
In the following we explain  how to use `ng2c.py`



