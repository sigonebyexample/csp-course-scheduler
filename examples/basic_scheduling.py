
from src.utils import create_course_scheduling_problem, print_solution
from src.csp_solver import CSPSolver

def main():
    """Solve the basic course scheduling problem."""
    print("Solving course scheduling problem...")
    
    # Create the problem
    problem = create_course_scheduling_problem()
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
