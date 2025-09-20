
from typing import List, Tuple, Dict
from .models import CSPProblem

def create_course_scheduling_problem() -> CSPProblem:
    """Create the course scheduling problem with the provided data."""
    variables = ["A","B","c","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    constraints = [
        ("A","B"), ("A","c"), ("A","D"), ("B","E"), ("c","F"), ("D","E"),
        ("E","F"), ("F","G"), ("D","G"), ("H","I"), ("H","J"), ("I","K"),
        ("J","K"), ("K","L"), ("L","M"), ("M","N"), ("N","O"), ("O","P"),
        ("P","Q"), ("Q","R"), ("R","S"), ("S","T"), ("T","U"), ("U","V"),
        ("V","W"), ("W","X"), ("X","Y"), ("Y","Z")
    ]
    return CSPProblem(variables, constraints)

def print_solution(solution) -> None:
    """Print the solution in a readable format."""
    if not solution.is_solved:
        print("No solution found")
        return
        
    print("Solution found:")
    days = {}
    for var, day in solution.assignment.items():
        if day not in days:
            days[day] = []
        days[day].append(var)
    
    for day, courses in days.items():
        print(f"{day}: {', '.join(sorted(courses))}")
