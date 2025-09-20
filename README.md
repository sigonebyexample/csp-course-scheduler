# CSP Course Scheduler

A constraint satisfaction problem solver for course scheduling using backtracking search.

## Features

- Backtracking search algorithm
- Binary constraint handling
- Custom variable domains
- Constraint graph representation
- Solution validation

## Installation

1. Clone the repository:
```bash
git clone https://github.com/sigonebyexample/csp-course-scheduler
cd csp-course-scheduler
pip install -r requirements.txt
```
## Usage
# Basic Usage
```
from src.models import CSPProblem
from src.csp_solver import CSPSolver

# Define your problem
variables = ["CourseA", "CourseB", "CourseC"]
constraints = [("CourseA", "CourseB"), ("CourseB", "CourseC")]

# Create problem instance
problem = CSPProblem(variables, constraints)

# Solve it
solver = CSPSolver(problem)
solution = solver.solve()

if solution.is_solved:
    print("Solution found:", solution.assignment)
else:
    print("No solution exists")
```
# Using the Provided Example
```
python examples/basic_scheduling.py

```
# Creating Custom Problems
```
# See examples/custom_problem.py for detailed example
from src.models import CSPProblem
from src.csp_solver import CSPSolver

# Define custom domains
domains = {
    "Meeting": ["Monday", "Tuesday"],
    "Class": ["Monday", "Wednesday"],
    "Study": ["Monday", "Tuesday", "Wednesday"]
}

# Define constraints
constraints = [("Meeting", "Class"), ("Class", "Study")]

problem = CSPProblem(["Meeting", "Class", "Study"], constraints, domains)
solver = CSPSolver(problem)
solution = solver.solve()
```

## Algorithm Explanation

```markdown
# Algorithm Explanation

## Backtracking Search

The core algorithm used in this CSP solver is backtracking search, which is a depth-first search that tries assigning values to variables one at a time and backtracks when it determines that a partial assignment cannot be completed to a valid solution.

### Steps:

1. **Variable Selection**: Choose an unassigned variable. Currently uses a simple approach (first unassigned), but could be enhanced with heuristics like Minimum Remaining Values (MRV).

2. **Value Assignment**: Try each value in the variable's domain in order.

3. **Consistency Check**: After each assignment, check if the current partial assignment violates any constraints.

4. **Recursion**: If consistent, recursively continue with the next variable.

5. **Backtracking**: If no value leads to a solution, backtrack to the previous variable and try a different value.

### Complexity

The time complexity of backtracking is O(d^n) in the worst case, where:
- d is the size of the largest domain
- n is the number of variables

However, constraint checking prunes the search space significantly in practice.

## Constraint Graph

The solver builds a constraint graph where:
- Nodes represent variables
- Edges represent constraints between variables

This graph is used to efficiently check constraints during the search.

## Solution Validation

After finding a solution, the solver validates that all constraints are satisfied, providing confidence in the correctness of the solution.

## Potential Enhancements

1. **Heuristics**:
   - Minimum Remaining Values (MRV): Choose variable with fewest legal values
   - Degree Heuristic: Choose variable involved in most constraints
   - Least Constraining Value: Choose value that rules out fewest values for neighbors

2. **Inference**:
   - Forward Checking: Maintain arc consistency after each assignment
   - MAC (Maintaining Arc Consistency): Full arc consistency during search

3. **Local Search**: For large problems, consider algorithms like min-conflicts
