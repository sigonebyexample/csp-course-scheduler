
from src.models import CSPProblem
from src.csp_solver import CSPSolver
from src.utils import print_solution

def create_custom_problem():
    """Create a custom CSP problem."""
    # Variables represent different events
    variables = ["Meeting", "Class", "Lunch", "Study", "Exercise"]
    
    # Constraints: events that cannot happen at the same time
    constraints = [
        ("Meeting", "Class"),
        ("Class", "Lunch"),
        ("Meeting", "Lunch"),
        ("Study", "Exercise")  # Can't study and exercise at same time
    ]
    
    # Different domains for some variables
    domains = {
        "Meeting": ["Monday", "Tuesday"],
        "Class": ["Monday", "Wednesday"],
        "Lunch": ["Tuesday", "Wednesday"],
        "Study": ["Monday", "Tuesday", "Wednesday"],
        "Exercise": ["Monday", "Tuesday", "Wednesday"]
    }
    
    return CSPProblem(variables, constraints, domains)

def main():
    """Solve a custom scheduling problem."""
    print("Solving custom scheduling problem...")
    
    # Create the custom problem
    problem = create_custom_problem()
    print(f"Problem: {problem}")
    
    # Solve it
    solver = CSPSolver(problem)
    solution = solver.solve()
    
    # Print results
    print_solution(solution)
    
    if solution.is_solved:
        print(f"\nSolution is valid: {solution.is_valid()}")
    else:
        print("No solution could be found for this problem.")

if __name__ == "__main__":
    main()
