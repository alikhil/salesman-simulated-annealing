# Assignment 2

Link to repository - [alikhil/salesman-simulated-annealing](https://github.com/alikhil/salesman-simulated-annealing)

## Motivation

In this assignment I implemented Simulated Annealing (SA) algorithm for solving Traveling Salesman problem and compared results of SA simulations with different cooling rates.

## Implementation

SA implemented according to algorithm described in the [assignment](https://hackmd.io/s/r1WGbzm6Q#). 

Implementation can be found in [the project repository](https://github.com/alikhil/salesman-simulated-annealing)

## Results

I have run SA with three different values of cooling rate:

- slow cooling - 0.995
- middle cooling - 0.99
- fast cooling - 0.97

The speed of convergence and value to which they converge we see in figure below:

![img2](https://user-images.githubusercontent.com/7482065/48836697-88bf9600-ed94-11e8-818c-40783c11c637.png)

As we see, slower the cooling rate better it converges.

In figure below we can see how path is changing for cooling rate = 0.995.

![anneal_animation](https://user-images.githubusercontent.com/7482065/48839813-bceb8480-ed9d-11e8-9e8c-b4f800eef46d.gif)
