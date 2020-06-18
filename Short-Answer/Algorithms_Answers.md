#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)  O(n) - Linear - as input increases, the runtime will grow at the same rate
           Because the speed of the algorithm increases at the same rate as the input size.

b)  O(n^c) - Polynomial The run time will grow at a faster rate
    There is a nested loop, and that nested loop is multiplying the outer loop by 2 each iteration.  It will get larger each loop.

c)  O(n)  - Linear - as input increases, the runtime will grow at the same.  Will run n amount of times per bunny ..just adding 2 to show how many ears per bunny. 

## Exercise II


If egg != broken, go up one floor and throw again. 
Else: set n (number_floor) to current floor
Loop through floors until egg_broken is True. 
Return the current_floor - 1 to get the floor where eggs will not break. 

run time complexity O(n). No matter how many floors the number of computations within the function is the same.

