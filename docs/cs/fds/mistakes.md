# Mistakes Collection

## Judgement

1. The Fibonacci number sequence $\{F_N\}$ is defined as: $F_0 = 0, F_1 = 1, F_N = F_{N−1}​ + F_{N−2}, N = 2, 3, \ldots$. The time complexity of the function which calculates $F_N$ recursively is $\Theta(N!)$.  

2. For the following piece of code  
```c 
if (A > B) {     
  for (i = 0; i < N*2; i++)         
    for (j = N*N; j > i; j--)             
      C += A; 
}
else {     
  for (i = 0; i < N * N / 100; i++)         
    for ( j = N; j > i; j--) 
      for (k = 0; k < N * 3; k++)
        C += B; 
} 
```
The lowest upper bound of the time complexity is $O(N^3)$. 

3. For a sequentially stored linear list of length $N$, the time complexities for deleting the first element and inserting the last element are $O(1)$ and $O(N)$, respectively.