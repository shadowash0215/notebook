# Homework

## Homework 11

1. To approximate a maximum spanning tree $T$ of an undirected graph $G = (V, E)$ with distinct edge weights $w(u, v)$ on each edge

## Homework 12

1. A bipartite graph $G$ is one whose vertex set can be partitioned into two sets $A$ and $B$, such that each edge in the graph goes between a vertex in $A$ and a vertex in $B$. Matching $M$ in $G$ is a set of edges that have no end points in common. *Maximum Bipartite Matching Problem* is to find a matching with the greatest number of edges(over all matching).  
Consider the following **Gradient Ascent Algorithm**:  
> As long as there is an edge whose endpoints are unmatched, add it to the current matching. When there is no such edge, terminate with a locally optimal matching.  

    Let $M_1$ and $M_2$ be matchings in a bipartite graph $G$. Which of the following statements is true?  
    A. The gradient ascent algorithm never returns the maximum matching.  
    B. Suppose that $\lvert M_1 \rvert > 2 \lvert M_2 \rvert$. Then there must be an edge $e \in M_1$ such that $M_2 \cup \{e\}$ is a matching in $G$.  
    C. Any locally optimal matching returned by the gradient ascent algorithm in a bipartite graph $G$ is at most half as large as a maximum matching in $G$.  
    D. All of the above.

    ??? note
        

2. **Spanning Tree Problem**:  Given an undirected graph $G = (V, E)$, where $\lvert V \rvert = n$ and $\lvert E \rvert = m$. Let $F$ be the set of all spanning tree of $G$. Define $d(u)$ to be the degree of a vertex $u \in V$. Define $w(e)$ to be the weight of an edge $e \in E$.  
We have tge following three variants of spanning tree problems:  
- Max Leaf Spanning Tree: find a spanning tree $T \in F$ with a maximum number of leaves.  
- Minimum Spanning Tree: find a spanning tree $T \in F$ with a minimum total weight of all the edges in $T$.  
- Minimum Degree Spanning Tree: find a spanning tree $T \in F$ such that its maximum degree of all the vertices is the smallest.  
For a pair of edges $(e, e')$ where $e \in T$ and $e' \in G \setminus T$ such that $e$ belongs to the unique cycle of $T \cup \{e'\}$, we define **edge-swapp** $(e, e')$ to be $T \setminus \{e\} \cup \{e'\}$.  
Here is a local search algorithm:  
```c
T = any spanning tree in F;  
while (there is an edge-swap(e1, e2) which reduces Cost(T)) {
    T = T - e1 + e2;
}
return T;
```  
Here ```Cost(T)``` is the number of leaves in $T$ in the Max Leaf Spanning Tree problem, the total weight of all the edges in $T$ in the Minimum Spanning Tree problem, and the maximum degree of all the vertices in $T$ in the Minimum Degree Spanning Tree problem.  
Which of the following statements is true?  
A. The local search always return an optimal solution for Max Leaf Spanning Tree  
B. The local search always return an optimal solution for Minimum Spanning Tree  
C. The local search always return an optimal solution for Minimum Degree Spanning Tree  
D. For none of the problems that this local search always return an optimal solution

    ??? note 
        !!! success "Lemma 1"
            If $T$ and $T'$ are two spanning trees of $G$, then $T$ can be transformed into $T'$ by a sequence of edge-swaps.

        !!! success "Lemma 2"
            Let $T$ be a minimum spanning tree of a graph $G$, and let $L$ be the sorted list of the edge weights of $T$. Then for any other minimum spanning tree $T'$ of $G$, the list $L$ is also the sorted list of edge weights of $T'$.
        
        Suppose that there are $n$ edges in $T$ and $T'$. $a_1, a_2, \cdots, a_n$ are the edge weights of $T$ in sorted order, and $b_1, b_2, \cdots, b_n$ are the edge weights of $T'$ in sorted order. Suppose that $i$ is the smallest index such that $a_i \neq b_i$. Without loss of generality, assume that $w(a_i) \geqslant w(b_i)$.   
        1. If $b_i \in T$, then there must be $j > i$ such that $b_i = a_j$ since $i$ is the smallest index that $a_i \neq b_i$. Then we have $w(b_i) = w(a_j) \geqslant w(a_i) \geqslant w(b_i)$, which means $w(b_i) = w(a_i) = w(a_j)$. Exchange $a_i$ and $a_j$ does not change the sorted list of edge weights of $T$.  
        2. If $b_i \notin T$, then $T \cup \{b_i\}$ has a unique cycle $C$. Since $T$ is a minimum spanning tree, $w(b_i) \geqslant w(e)$ for all $e \in C$. Also there exists $a_j \in C$ such that $a_j \notin T'$($T'$ is a tree). So we have $w(a_j) \leqslant w(b_i)$ and $j > i$. Thus, $w(b_i) \leqslant w(a_i) \leqslant w(a_j) \leqslant w(b_i)$, which means $w(b_i) = w(a_i) = w(a_j)$. Replace $a_j$ with $b_i$ does not change the sorted list of edge weights of $T$ and we go back to case 1.

        !!! success "Lemma 3"
            $T$ and $T'$ are two different minimum spanning trees of $G$. Then $T$ can be transformed into $T'$ by a sequence of edge-swaps and each immediate transformation holds the same cost.

        Case 2 of Lemma 2's proof shows that the choice of edge-swaps exists. 

        !!! success "Lemma 4"
            In a connected graph $G$, there does not exist a minimum spanning tree $T$ containing all the edges with the maximum weights in any cycle of $G$.

        !!! success "Lemma 5"
            Consider a spanning tree $T$ of a graph $G$. Then the dictionary order of the edge weights of the minimum spanning tree is the minimum among all the spanning trees of $G$.

        !!! success "Lemma 6"
            If $T$ is not a minimum spanning tree of $G$, then there exists an edge-swap that reduces the cost of $T$.

        !!! success "Lemma 7"
            If $T$ is not a minimum spanning tree of $G$, then there exists a sequence of edge-swaps that transforms $T$ into a minimum spanning tree of $G$ and each immediate transformation reduces the cost of $T$.

        !!! note "Theorem"
            The local search algorithm always returns an optimal solution for the Minimum Spanning Tree problem.

3. **Max-Cut Problem**: Given an undirected graph $G = (V, E)$ with positive integer edge weights $w_e$, find a node partition $(A, B)$ such that $w(A, B)$, the total weight of the edges crossing the cut $(A, B)$, is maximized. Let us define $S'$ be the neighbor of $S$ such that $S'$ can be obtained from $S$ by moving one vertex from $A$ to $B$ or vice versa. We only choose a node which, when flipped, increases the cut value by at least $w(A, B)/ \lvert V \rvert$. Then which of the following statements is true?  
A. Upon the termination of the algorithm, the algorithm returns a cut $(A, B)$ so that $2.5 \cdot w(A, B) \geqslant w(A^*, B^*)$, where $(A^*, B^*)$ is the optimal partition.  
B. The algorithm terminates after at most $O(\log \lvert V \rvert \log W)$ iterations, where $W$ is the total weight of all the edges in $G$.  
C. Upon the termination of the algorithm, the algorithm returns a cut $(A, B)$ so that $2 \cdot w(A, B) \geqslant w(A^*, B^*)$.  
D. The algorithm terminates after at most $O(\lvert V \rvert^2)$ flips.

    ??? note
        Recall that the "Big-improvement-flip" algorithm satisfies the following properties:  
        
        \begin{gather}
            (2 + \varepsilon) \cdot w(A, B) \geqslant w(A^*, B^*) \\
            \text{The algorithm terminates after at most } O(\dfrac{\lvert V \rvert}{\varepsilon}  \log W) \text{ iterations} \\
        \end{gather}

        Here $\varepsilon = 0.5$. So A is TRUE.

4. There are $n$ jobs, and each job $j$ has a processing time $t_j$. We will use a local search algorithm to partition the jobs into two groups $A$ and $B$, where set $A$ is assigned to machine $M_1$ and set $B$ is assigned to machine $M_2$. The time needed to process all of the jobs on the two machines is $T_1 = \sum_{j \in A} t_j$ and $T_2 = \sum_{j \in B} t_j$. The problem is to minimize the difference between the two processing times, i.e. $\lvert T_1 - T_2 \rvert$. Local search algorithm: Start by assigning jobs $1, 2, \cdots, n/2$ to machine $M_1$ and the remaining jobs to machine $M_2$. The local moves are to move a single job from one machine to the other, and we only move a job if the move reduces the difference between the two processing times. Which of the following statements is true?  
A. The problem is NP-hard and the local search algorithm will not terminate.  
B. When there are many candidate jobs that can be moved to reduce the absolute difference, if we always move the job $j$ with maximum $t_j$, then the local search algorithm will terminate in at most $n$ moves.  
C. The local search algorithm always returns an optimal solution.  
D. The local search algorithm always returns a local solution with $\frac{1}{2} T_1\leqslant T_2 \leqslant 2 T_1$.

    ??? note
        A. There are total $2^n$ possible partitions, so the problem is NP-hard. The local search algorithm will terminate since the number of possible moves is finite.  
        B. The local search algorithm will terminate in at most $n$ moves because the algorithm always moves the job that reduces the absolute difference the most which means if one job is moved, it will not be moved again.  
        C. Consider $\{10, 11, 12, 12, 13, 14\} = \{10, 11, 12\} + \{12, 13, 14\}$, but the optimal solution is $\{10, 12, 14\} + \{11, 12, 13\}$.  
        D. Consider $\{1, 2, 100\} = \{1, 2\} + \{100\}$.

## Homework 13

1. If we repeatedly perform independent trials of an experiment, each of which succeeds with probability $p > 0$, then the expected number of trials we need to perform until the first success is:  
A. $p/(1-p)$  
B. $1/(1-p)$  
C. $1/p$  
D. None of the above

    ??? note "Waiting Time Bound"
        Consider a series of independent trials where each trial succeeds with probability $p$ and fails with probability $1 − p$. Then, the expected number of trials until the first success is $1/p$.  
        Let $N$ be the number of trials until the first success. The probability that $j$ trials are needed is 

        \[
            \operatorname{Pr}[N = j] = (1-p)^{j-1} \cdot p.
        \]

        So the expected number of trials is

        \[
            E[N] = \sum_{j=1}^{\infty} j \cdot \operatorname{Pr}[N = j] = \sum_{j=1}^{\infty} j \cdot (1-p)^{j-1} \cdot p = \dfrac{1}{p}.
        \]

2. Given a *3-SAT* formula with $k$ clauses, in which each clause has three variables, the *MAX-3SAT* problem is to find a truth assignment that satisfies as many clauses as possible. A simple randomized algorithm is to flip a coin, and to set each variable true with probability 1/2, independently for each variable. Which of the following statements is FALSE?  
A. The expected number of clauses satisfied by this random assignment is $\frac{7}{8}k$.  
B. For every instance of *3-SAT*, there is a truth assignment that satisfies at least a $\frac{7}{8}$ fraction of all clauses.（至少有一种真值赋值使得其中 $\frac{7}{8}$ 的子句赋值为真）  
C. If we repeatedly generate random truth assignments until one of them satisfies $\geqslant \frac{7}{8}k$ clauses, then this algorithm is a $\frac{7}{8}$-approximation algorithm for *MAX-3SAT*.  
D. The probability that a random assignment satisfies at least $\frac{7}{8}k$ clauses is at most $\frac{1}{8k}$.  

    ??? note
        !!! success "Claim"
            Given a *3-SAT* formula with $k$ clauses, the expected number of clauses satisfied by a random assignment is $\frac{7}{8}k$.  

        Consider random variable $Z_j = \begin{cases} 1 & \text{if clause } C_j \text{ is satisfied} \\ 0 & \text{otherwise} \end{cases}$.  $Z$ is the sum of $Z_j$'s.  

        \begin{align}
            E[Z] &{} = \sum_{j = 1}^k E[Z_j] \\
            &{} = \sum_{j = 1}^k \operatorname{Pr}[C_j \text{ is satisfied}] \\
            &{} = \dfrac{7}{8} \cdot k
        \end{align}

        So A is TRUE.

        !!! success "Collary"
            For any instance of *3-SAT*, there is a truth assignment that satisfies at least a $\frac{7}{8}$ fraction of all clauses.

        So B is TRUE.

        !!! success "Lemma"
            The probability that a random assignment satisfies at least $\frac{7}{8}k$ clauses is at least $\frac{1}{8k}$.  
        Let $p_j$ be probability that exactly $j$ clauses are satisfied. Let $p$ be probability that $\geqslant \frac{7}{8}k$ clauses are satisfied.  

        \begin{align}
            \dfrac{7}{8}k = E[Z] &{} = \sum_{j = 0}^k j \cdot p_j \\
            &{} = \sum_{j < \frac{7}{8}k} j \cdot p_j + \sum_{j \geqslant \frac{7}{8}k} j \cdot p_j \\
            &{} \leqslant \dfrac{7k - 1}{8} \sum_{j < \frac{7}{8}k} p_j + k \sum_{j \geqslant \frac{7}{8}k} p_j \\
            &{} \leqslant (\dfrac{7}{8}k - \dfrac{1}{8}) \cdot 1 + k \cdot p \\ 
        \end{align}

        Thus, $p \geqslant \dfrac{1}{8k}$.

        So D is FALSE.

        !!! note "Johnson's Algorithm"
            If we repeatedly generate random truth assignments until one of them satisfies $\geqslant \frac{7}{8}k$ clauses, then this algorithm is a $\frac{7}{8}$-approximation algorithm for *MAX-3SAT*.  
        By previous lemma, each iteration succeeds with probability at least $\frac{1}{8k}$. By the waiting-time bound, the expected number of trials to find the satisfying assignment is at most $8k$, which means this algorithm will stop in polynomial time.
        
        So C is TRUE.