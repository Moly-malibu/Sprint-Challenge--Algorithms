#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)Exponential O(n^3) time complexity -> the number of operations will increase n **3 or n*n*n times as the data set increases.

<!-- a)  a = 0
          while (a < n * n * n):
            a = a + n * n -->

b) Exponential O(n^2)  the number of operations will increase n^2 times as the data set increases, it has a nested while loop inside of a for loop.

 <!-- sum = 0
      for i in range(n):
        j = 1
        while j < n:
          j *= 2
          sum += 1 --> -->

c) Linear time: O(n) the number of operations is linear irrespective of the data size, call recursively.

<!-- c)  def bunnyEars(bunnies):
          if bunnies == 0:
            return 0

          return 2 + bunnyEars(bunnies-1 -->

## Exercise II n-story building and plenty of eggs

n is the number of floors of the building 
e is the number of eggs that we have to drop 
f is the breaking point 

(f = e + broken eggs)

Binary Search: 
O(log n) -> on each pass:  ruling out half the floors. 
            middle_floor = (highest_floor + lowest_floor) // 2 
                            Drop an egg on the middle floor. 
    If egg breaks, go to the midpoint floor between: 
                                the bottom floor.
                                and the current floor. 
    If an egg does not break on the middle floor, go to the midpoint floor between: 
                                the top floor and the current floor. 
--> this process until the correct floor is found.)