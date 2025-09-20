
from typing import List, Tuple, Dict, Optional

class CSPProblem:
    """Represents a CSP problem with variables, constraints, and domains."""
    
    def __init__(self, variables: List[str], constraints: List[Tuple[str, str]], 
                 domains: Optional[Dict[str, List[str]]] = None):
        """
        Initialize a CSP problem.
        
        Args:
            variables: List of variable names
            constraints: List of binary constraints as tuples (var1, var2)
            domains: Optional dictionary of domains for each variable
        """
        self.variables = variables
        self.constraints = constraints
        self.domains = domains or {var: ["Monday", "Tuesday", "Wednesday"] for var in variables}
    
    def __repr__(self):
        return f"CSPProblem(variables={len(self.variables)}, constraints={len(self.constraints)})"

class CSPSolution:
    """Represents a solution to a CSP problem."""
    
    def __init__(self, problem: CSPProblem, assignment: Optional[Dict[str, str]], is_solved: bool):
        """
        Initialize a CSP solution.
        
        Args:
            problem: The original CSP problem
            assignment: The variable assignment (None if no solution)
            is_solved: Whether the problem was solved
        """
        self.problem = problem
        self.assignment = assignment
        self.is_solved = is_solved
    
    def __repr__(self):
        status = "Solved" if self.is_solved else "Unsolved"
        return f"CSPSolution({status}, assignment={self.assignment})"
    
    def is_valid(self) -> bool:
        """Check if the solution is valid (satisfies all constraints)."""
        if not self.is_solved or not self.assignment:
            return False
            
        for (A, B) in self.problem.constraints:
            if self.assignment.get(A) == self.assignment.get(B):
                return False
        return True
