![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=python&logoColor=white)
![SymPy](https://img.shields.io/badge/SymPy-3B5526?style=for-the-badge&logo=python&logoColor=white)

> A collection of **computational** and **numerical analysis** problems I have personally solved using `Python`, `NumPy`, `SymPy` and scientific visualizations (**plots**) with `Matplotlib`. Each project includes: **comprehensive documentation (PDF document)**, an **interactive `Jupyter Notebook`**, a **clean `.py script`**, and **exported plots**.
---

## Table of Contents

| # | Topic / Project | Preview | Full Documentation | Notebook | Script |
| :-: | :--- | :--- | :---: | :---: | :---: |
| **01** | **Monte Carlo Integration Between the Graphs of two Parabolas** | <a href="./1. Monte Carlo integration method 1.0 (parabolas)/"><img src="./1. Monte Carlo integration method 1.0 (parabolas)/graph.png" width="520" alt="Monte Carlo 1.0"></a> | [`📄assignment.pdf`](<./1. Monte Carlo integration method 1.0 (parabolas)/assignment.pdf>) | [`Jupyter Notebook`](<./1. Monte Carlo integration method 1.0 (parabolas)/monte-carlo-integration-method.ipynb>) | [`Python Code`](<./1. Monte Carlo integration method 1.0 (parabolas)/monte-carlo-integration-method.py/>) |
| **02** | **Monte Carlo Numerical Integration of 𝒇(𝒙)=√𝒙** | <a href="./2. Monte Carlo integration method 2.0 (mygraph)/"><img src="./2. Monte Carlo integration method 2.0 (mygraph)/graph_2.png" width="520" width: auto alt="Monte Carlo 2.0"></a> | [`📄assignment.pdf`](<./2. Monte Carlo integration method 2.0 (mygraph)/assignment.pdf>) | [`Jupyter Notebook`](<./2. Monte Carlo integration method 2.0 (mygraph)/monte-carlo-integration-2.0-mygraph.ipynb>) | [`Python Code`](<./2. Monte Carlo integration method 2.0 (mygraph)/monte-carlo-integration-2.0-mygraph.py>) |
| **03** | **Fixed-Point Iteration Method implementation (General Iterative Method) with Consecutive Errors Plotting** | <a href="./3. fixed point iteration method 1.0 (errors plotting)/"><img src="./3. fixed point iteration method 1.0 (errors plotting)/graph.png" width="520" alt="Fixed Point 1.0"></a> | [`📄assignment.pdf`](<./3. fixed point iteration method 1.0 (errors plotting)/assignment.pdf>) | [`Jupyter Notebook`](<./3. fixed point iteration method 1.0 (errors plotting)/fixed-point-iteration-method.ipynb/>) | [`Python Code`](<./3. fixed point iteration method 1.0 (errors plotting)/fixed-point-iteration-method.py/>) |
| **04** | **Fixed-Point Iteration Method implementation (General Iterative Method) with Functions Graph Plotting (Curves Intersection)** | <a href="./4. fixed point iteration method 2.0 (functions graph plotting)/"><img src="./4. fixed point iteration method 2.0 (functions graph plotting)/graph.png" height = "580" width="520" alt="Fixed Point 2.0"></a> | [`📄assignment.pdf`](<./4. fixed point iteration method 2.0 (functions graph plotting)/assignment.pdf>) | [`Jupyter Notebook`](<./4. fixed point iteration method 2.0 (functions graph plotting)/fixed-point-iteration-method-2.0.ipynb/>) | [`Python Code`](<./4. fixed point iteration method 2.0 (functions graph plotting)/fixed-point-iteration-method-2.0.py/>) |
| **05** | **Newton-Raphson (N-R) Method implementation for Solving Non-Linear Equations, with Consecutive Errors Plotting (both Linear and Logarithmic scale)** | <a href="./5. Newton-Raphson (N-R) method/"><img src="./5. Newton-Raphson (N-R) method/graph_1.png" height="520" alt="Newton-Raphson"></a> | [`📄assignment.pdf`](<./5. Newton-Raphson (N-R) method/assignment.pdf>) | [`Jupyter Notebook`](<./5. Newton-Raphson (N-R) method/newton-raphson-method.ipynb>) | [`Python Code`](<./5. Newton-Raphson (N-R) method/newton-raphson-method.py/>) |
| **06** | **Secant Method implementation for Solving Non-Linear Equations, with Consecutive Errors Plotting (both Linear and Logarithmic scale)** | <a href="./6. Secant method/"><img src="./6. Secant method/graph_2.png" height =auto width="520" alt="Secant Method"></a> | [`📄assignment.pdf`](<./6. Secant method/assignment.pdf>) | [`Jupyter Notebook`](<./6. Secant method/secant-method.ipynb>) | [`Python Code`](<./6. Secant method/secant-method.py>) |
| **07** | ***`Bonus`*: Computational Cost Comparison experiment: Newton-Raphson Method vs. Secant Method for Solving Non-Linear Equations** | <a href="./7. BONUS computational cost comparison between N-R and Secant/"><img src="./7. BONUS computational cost comparison between N-R and Secant/graph_1.png" height=auto width="520" alt="Cost Comparison"></a> | [`📄assignment.pdf`](<./7. BONUS computational cost comparison between N-R and Secant/assignment.pdf>) | [`Jupyter Notebook`](<./7. BONUS computational cost comparison between N-R and Secant/computational-cost-comparison-NR-secant.ipynb>) | [`Python Code`](<./7. BONUS computational cost comparison between N-R and Secant/computational-cost-comparison-NR-secant.ipynb>) |
| **08** | **Cholesky Decomposition Example** | <a href="./8. Cholesky decomposition/"><img src="./8. Cholesky decomposition/graph.png" height="520" width="520" alt="Cholesky"></a> | [`📄assignment.pdf`](<./8. Cholesky decomposition/assignment.pdf>) | [`Jupyter Notebook`](<./8. Cholesky decomposition/cholesky-decomp.ipynb/>) | [`Python Code`](<./8. Cholesky decomposition/cholesky-decomp.py/>) |

---
## In-Depth Section Breakdown
### 📌 01 & 02: Monte Carlo Numerical Integration
* **Description:** Stochastic approximation of definite integrals and geometric areas using uniform random sampling within a defined bounding domain $[0, 1] \times [0, 1]$.
  * **Exercise 1 (Parabolas):** Evaluates the area between two intersecting parabolic curves, $P_1(x) = x^2 - x + 1/2$ and $P_2(x) = -x^2 + x + 1/2$, averaged across 10 independent trials of $n = 1000$ points each (Estimate $\approx 0.3266$, Exact $= 1/3$).
  * **Exercise 2 (function `mygraph()`):** Integrates $f(x) = \sqrt{x}$ over $[0, 1]$ across multiple sample sizes ($n = 1000, 4000, 16000$) using a modular plotting function `mygraph()` to demonstrate convergence and error behavior (Exact $= 2/3 \approx 0.6667$).
* **Tools & Libraries:** `numpy`, `matplotlib.pyplot`, `sympy`
* **Files & Documentation:**
  * **Exercise 1:** [`Notebook`](<./1. Monte Carlo integration method 1.0 (parabolas)/monte-carlo-integration-method.ipynb>), [`Script (.py)`](<./1. Monte Carlo integration method 1.0 (parabolas)/monte-carlo-integration-method.py>), [Documentation (PDF)](<./1. Monte Carlo integration method 1.0 (parabolas)/assignment.pdf>)
  * **Exercise 2:** [`Notebook`](<./2. Monte Carlo integration method 2.0 (mygraph)/monte-carlo-integration-2.0-mygraph.ipynb>), [`Script (.py)`](<./2. Monte Carlo integration method 2.0 (mygraph)/monte-carlo-integration-2.0-mygraph.py>), [Documentation (PDF)](<./2. Monte Carlo integration method 2.0 (mygraph)/assignment.pdf>)

#### 📊 Output Visualizations

##### Exercise 1: Enclosed Area Between Parabolas ($n = 1000$, 10 Trials)
<p align="left">
  <img src="./1. Monte Carlo integration method 1.0 (parabolas)/graph.png" width="450" alt="Monte Carlo Integration - Parabolas">
</p>

##### Exercise 2: Area Under $f(x) = \sqrt{x}$ for Varying Sample Sizes ($n = 1000, 4000, 16000$)
<p align="left">
  <img src="./2. Monte Carlo integration method 2.0 (mygraph)/graph_1.png" width="450" alt="Monte Carlo n=1000">
</p>
<p align="left">
  <img src="./2. Monte Carlo integration method 2.0 (mygraph)/graph_2.png" width="450" alt="Monte Carlo n=4000">
</p> 
<p align="left">
  <img src="./2. Monte Carlo integration method 2.0 (mygraph)/graph_3.png" width="450" alt="Monte Carlo n=16000">
</p>

---

### 📌 03 & 04: Fixed-Point Iteration (General Iterative Method) implementation
* **Description:** Numerical solution of non-linear equations by rearranging $f(x) = 0$ into the equivalent fixed-point form $x = g(x)$ and generating the iterative sequence $x_{k+1} = g(x_k)$. Both implementations verify convergence conditions under the Fixed-Point Theorem and numerically estimate the asymptotic convergence rate ($p \approx 1.0$) and error constant ($C$).
  * **Exercise 3 (Errors Plot):** Solves the cubic equation $f(x) = x^3 + x - 1 = 0$ using the rearrangement $g(x) = \sqrt[3]{1 - x}$ with $x_0 = 0$, tolerance $\text{tol} = 10^{-6}$, and max iterations $= 100$. Tracks and plots consecutive errors $e_k = \vert{}x_{k+1} - x_k\vert{}$ across iterations, verifying an asymptotic error constant $C \approx 0.7160$.
  * **Exercise 4 (Functions Plot):** Solves $f(x) = \cos(x) - x = 0$ via the rearrangement $g(x) = \cos(x)$ starting from $x_0 = 0$. Provides a comparative geometric visualization of $y = \cos(x)$ against the identity line $y = x$ on $[-5, 5]$ highlighting the unique real root $x^* \approx 0.739085$ ($C \approx 0.6736$).
* **Tools & Libraries:** `numpy`, `matplotlib.pyplot`
* **Files & Documentation:**
  * **Exercise 3:** [`Notebook`](<./3. fixed point iteration method 1.0 (errors plotting)/fixed-point-iteration-method.ipynb>), [`Script (.py)`](<./3. fixed point iteration method 1.0 (errors plotting)/fixed-point-iteration-method.py>), [Documentation (PDF)](<./3. fixed point iteration method 1.0 (errors plotting)/assignment.pdf>)
  * **Exercise 4:** [`Notebook`](<./4. fixed point iteration method 2.0 (functions graph plotting)/fixed-point-iteration-method-2.0.ipynb>), [`Script (.py)`](<./4. fixed point iteration method 2.0 (functions graph plotting)/fixed-point-iteration-method-2.0.py>), [Documentation (PDF)](<./4. fixed point iteration method 2.0 (functions graph plotting)/assignment.pdf>)

#### 📊 Output Visualizations

##### Exercise 3: Error Convergence vs. Iterations
<p align="left">
  <img src="./3. fixed point iteration method 1.0 (errors plotting)/graph.png" width="450" alt="Fixed-Point Iteration Error Convergence">
</p>

##### Exercise 4: Geometric Intersection $y = \cos(x)$ & $y = x$
<p align="left">
  <img src="./4. fixed point iteration method 2.0 (functions graph plotting)/graph.png" width="450" alt="Fixed-Point Iteration Curves Intersection">
</p>

---

### 📌 05: Newton-Raphson (N-R) Method implementation
* **Description:** Iterative root-finding algorithm using tangent line linearization to compute real roots of the non-linear polynomial $f(x) = x^4 + 2x^3 - 7x^2 + 3 = 0$ with derivative $f'(x) = 4x^3 + 6x^2 - 14x$.
  * **Automated Root Search:** Iterates through starting points $x_0 = i \cdot 0.1$ (avoiding division-by-zero when $f'(x_0) = 0$) with tolerance $\text{tol} = 10^{-4}$ and $\text{maxit} = 15$ to isolate both distinct positive real roots: $x_1^* \approx 1.6180$ and $x_2^* \approx 0.7913$.
  * **Convergence Analysis ($x_0 = 1.4$):** Evaluates error progression towards $x^* \approx 1.6180$ in 5 iterations. The asymptotic error ratio $e_5 / e_4^2 \approx 1.8504$ closely matches the theoretical constant C = |f''(x*)| / (2|f'(x*)|) ≈ 1.8416, verifying quadratic convergence ($p = 2$).
* **Tools & Libraries:** `numpy`, `matplotlib.pyplot`
* **Files & Documentation:** [`Notebook`](<./5. Newton-Raphson (N-R) method/newton-raphson-method.ipynb>), [`Script (.py)`](<./5. Newton-Raphson (N-R) method/newton-raphson-method.py>), [Documentation (PDF)](<./5. Newton-Raphson (N-R) method/assignment.pdf>)

#### 📊 Output Visualizations (Error Convergence for $x_0 = 1.4$)
<p align="left">
  <img src="./5. Newton-Raphson (N-R) method/graph_1.png" width="450" alt="Newton-Raphson Error - Linear Scale">
</p>
<p align="left">
  <img src="./5. Newton-Raphson (N-R) method/graph_2.png" width="450" alt="Newton-Raphson Error - Log Scale">
</p>

---

### 📌 06: Secant Method implementation
* **Description:** Numerical root-finding algorithm that approximates the tangent slope using a secant line between the two most recent iterates, avoiding the need for an analytical derivative:
  $$x_{n+1} = x_n - \frac{f(x_n)(x_n - x_{n-1})}{f(x_n) - f(x_{n-1})}$$
  * **Target Non-linear Equation:** Solves $f(x) = x^4 + 2x^3 - 7x^2 + 3 = 0$.
  * **Automated Search for Positive Roots:** Iterates through consecutive intervals $(x_0, x_1) = (i \cdot 0.1, (i + 1) \cdot 0.1)$ while bypassing division-by-zero intervals ($\text{tol} = 10^{-4}$, $\text{maxit} = 15$). Successfully locates both positive real roots: $x_1^* \approx 1.6180$ and $x_2^* \approx 0.7913$.
  * **Convergence Analysis ($x_0 = 1.4, x_1 = 1.5$):** Converges to $x^* \approx 1.6180$ in 6 iterations. The sequence of consecutive errors confirms the characteristic superlinear convergence order of the golden ratio ($p \approx 1.618$):
    $$p = \frac{1 + \sqrt{5}}{2} \approx 1.618$$
* **Tools & Libraries:** `numpy`, `matplotlib.pyplot`
* **Files & Documentation:** [`Notebook`](<./6. Secant method/secant-method.ipynb>), [`Script (.py)`](<./6. Secant method/secant-method.py>), [Documentation (PDF)](<./6. Secant method/assignment.pdf>)

#### 📊 Output Visualizations (Error Convergence for $x_0 = 1.4, x_1 = 1.5$)
<p align="left">
  <img src="./6. Secant method/graph_1.png" width="450" alt="Secant Method Error - Linear Scale">
</p>
<p align="left">
  <img src="./6. Secant method/graph_2.png" width="450" alt="Secant Method Error - Log Scale">
</p>

---

### 📌 07: Bonus Experiment : Computational Cost Comparison Between the Newton-Raphson method and the Secant method
* **Description:** In-depth computational efficiency and cost benchmark between the Newton-Raphson method ($p = 2$, cost of $2k\text{ FLOPs/step}$) and the Secant method ($p \approx 1.618$, cost of $1k\text{ FLOPs/step}$) for finding the common positive root $x^* \approx 1.6180$ of $f(x) = x^4 + 2x^3 - 7x^2 + 3 = 0$ ($\text{tol} = 10^{-4}$, $\text{maxit} = 15$).
  * **Theoretical Background:** Because $2^2 = 4 \approx 4.23 = 1.618^3$, 3 iterations of the Secant method reduce the error as much as 2 iterations of Newton-Raphson. Evaluating the derivative cost equality yields $4k > 3k$, theoretically establishing that the Secant method requires less computational effort overall despite needing more steps.
  * **Empirical Validation:** Even though Newton-Raphson converges in fewer iterations (5 vs. 6), the Secant method achieves convergence with significantly fewer total function evaluations (7 vs. 10), resulting in lower measured CPU execution time ($18.84\ \mu\text{s} < 20.83\ \mu\text{s}$ over 20,000 runs) and confirming $7k < 10k$ and $3k < 4k$.
* **Tools & Libraries:** `numpy`, `matplotlib.pyplot`, `timeit`
* **Files & Documentation:** [`Notebook`](<./7. BONUS computational cost comparison between N-R and Secant/computational-cost-comparison-NR-secant.ipynb>), [Documentation (PDF)](<./7. BONUS computational cost comparison between N-R and Secant/assignment.pdf>)

#### Summary Table of Results

| Metric | Newton-Raphson (N-R) | Secant Method |
| :--- | :--- | :--- |
| **Initial Estimate(s)** | $x_0 = 1.4$ | $x_0 = 1.4, x_1 = 1.5$ |
| **Computed Root ($x^*$)** | 1.6180 | 1.6180 |
| **Iterations to Converge** | 5 | 6 |
| **Function Evaluations ($f + f'$)** | 10 | 7 |
| **Theoretical FLOPs Cost** | $10k$ | $7k$ |
| **Final Error ($e_{\text{last}}$)** | $5.1418 \times 10^{-5}$ (0.00005) | $6.2415 \times 10^{-7}$ (0.0000006) |
| **Execution Time (`timeit`)** | 20.83 $\mu\text{s}$ | 18.84 $\mu\text{s}$ |

#### 📊 Output Visualizations

#### Error vs. Iteration Count (Linear & Log Scale)
<p align="left">
  <img src="./7. BONUS computational cost comparison between N-R and Secant/graph_1.png" width="450" alt="Error vs. Iterations - Linear Scale">
</p>
<p align="left">
  <img src="./7. BONUS computational cost comparison between N-R and Secant/graph_3.png" width="450" alt="Error vs. Iterations - Log Scale">
</p>

#### Error vs. Total Function Evaluations / FLOPs Cost (Linear & Log Scale)
<p align="left">
  <img src="./7. BONUS computational cost comparison between N-R and Secant/graph_2.png" width="450" alt="Error vs. Evaluations - Linear Scale">
</p>
<p align="left">
  <img src="./7. BONUS computational cost comparison between N-R and Secant/graph_4.png" width="450" alt="Error vs. Evaluations - Log Scale">
</p>

---

### 📌 08: Cholesky Matrix Decomposition Example
* **Description:** Implementation of the direct, column-oriented Cholesky factorization method in numerical linear algebra. Any real, symmetric, and positive-definite (SPD) matrix $S$ is uniquely decomposed into the product of a lower triangular matrix $L$ (with strictly positive diagonal elements) and its transpose:
  $$S = L \cdot L^T$$
  * **Computational Advantages:** Highly stable numerically for SPD matrices without requiring row or column pivoting (unlike Gaussian elimination or general LU decomposition). It requires approximately half the arithmetic operations ($\approx n^3/3\text{ FLOPs}$) of LU factorization ($2n^3/3\text{ FLOPs}$), running more than twice as fast in practice.
  * **Algorithm Implementation:** Implemented from scratch via a custom `cholesky(a)` function using NumPy arrays and native math functions (`math.sqrt`) without relying on black-box solvers like `scipy.linalg.cholesky` or `np.linalg.cholesky`. It updates column by column, eliminates previous column contributions, computes square-root pivots on the diagonal, scales subdiagonal elements, and isolates $L$ using `np.tril()`.
  * **Test Matrix Construction & Verification:** Built an auxiliary $5 \times 5$ lower triangular matrix $A$ with full column rank to construct the guaranteed symmetric positive-definite matrix $S = A^T \cdot A$. The decomposition is verified by computing $L \cdot L^T$ (`np.dot(L, L.T)`), exactly reconstructing the original matrix $S$ within numerical precision.
* **Tools & Libraries:** `numpy`, `math.sqrt`
* **Files & Documentation:** [`Notebook`](<./8. Cholesky decomposition/cholesky-decomp.ipynb>), [`Script (.py)`](<./8. Cholesky decomposition/cholesky-decomp.py>), [Documentation (PDF)](<./8. Cholesky decomposition/assignment.pdf>)

#### Numerical Results & Matrix Reconstruction

```text
Matrix A (5x5 Lower Triangular, Full Rank):
[[1. 0. 0. 0. 0.]
 [1. 2. 0. 0. 0.]
 [1. 2. 3. 0. 0.]
 [1. 2. 3. 4. 0.]
 [1. 2. 3. 4. 5.]]

Symmetric Positive-Definite Matrix S = A^T * A:
[[ 5.  8.  9.  8.  5.]
 [ 8. 16. 18. 16. 10.]
 [ 9. 18. 27. 24. 15.]
 [ 8. 16. 24. 32. 20.]
 [ 5. 10. 15. 20. 25.]]

Computed Lower Triangular Factor L:
[[2.23606798 0.         0.         0.         0.        ]
 [3.57770876 1.78885438 0.         0.         0.        ]
 [4.02492236 2.01246118 2.59807621 0.         0.        ]
 [3.57770876 1.78885438 2.30940108 3.26598632 0.        ]
 [2.23606798 1.11803399 1.44337567 2.04124145 3.53553391]]

Verification Check: L * L^T (Matches S):
[[ 5.  8.  9.  8.  5.]
 [ 8. 16. 18. 16. 10.]
 [ 9. 18. 27. 24. 15.]
 [ 8. 16. 24. 32. 20.]
 [ 5. 10. 15. 20. 25.]]
```
---

## Repo Structure

```text
.
├── 1. Monte Carlo integration method 1.0 (parabolas)/
│   ├── assignment.pdf
│   ├── graph.png
│   ├── monte-carlo-integration-method.ipynb
│   └── monte-carlo-integration-method.py
│
├── 2. Monte Carlo integration method 2.0 (mygraph)/
│   ├── assignment.pdf
│   ├── graph_1.png
│   ├── graph_2.png
│   ├── graph_3.png
│   ├── monte-carlo-integration-2.0-mygraph.ipynb
│   └── monte-carlo-integration-2.0-mygraph.py
│
├── 3. fixed point iteration method 1.0 (errors plot)/
│   ├── assignment.pdf
│   ├── graph.png
│   ├── fixed-point-iteration-method.ipynb
│   └── fixed-point-iteration-method.py
│
├── 4. fixed point iteration method 2.0 (functions plot)/
│   ├── assignment.pdf
│   ├── graph.png
│   ├── fixed-point-iteration-method-2.0.ipynb
│   └── fixed-point-iteration-method-2.0.py
│
├── 5. Newton-Raphson (N-R) method/
│   ├── assignment.pdf
│   ├── graph_1.png
│   ├── graph_2.png
│   ├── newton-raphson-method.ipynb
│   └── newton-raphson-method.py
│
├── 6. Secant method/
│   ├── assignment.pdf
│   ├── graph_1.png
│   ├── graph_2.png
│   ├── secant-method.ipynb
│   └── secant-method.py
│
├── 7. BONUS computational cost comparison (N-R vs secant)/
│   ├── assignment.pdf
│   ├── graph_1.png
│   ├── graph_2.png
│   ├── graph_3.png
│   ├── graph_4.png
│   └── computational-cost-comparison-NR-secant.ipynb
│
├── 8. Cholesky decomposition/
│   ├── assignment.pdf
│   ├── cholesky-decomp.ipynb
│   └── cholesky-decomp.py
│
└── README.md
```

---

# 👤 Author
## Athanasios Gourdomichalis - https://github.com/AthanasiosGourdomichalis

---
