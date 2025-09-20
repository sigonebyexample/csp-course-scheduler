
from typing import List, Tuple, Dict, Optional, Set
from .models import CSPProblem, CSPSolution

class CSPSolver:
    """A Constraint Satisfaction Problem solver for course scheduling."""
    
    def __init__(self, problem: CSPProblem):
        """
        Initialize the CSP solver.
        
        Args:
            problem: A CSPProblem instance containing variables, constraints, and domains
        """
        self.problem = problem
        
        # Build constraint graph for efficiency
        self.graph = self._build_constraint_graph()
    
    def _build_constraint_graph(self) -> Dict[str, Set[str]]:
        """Build a graph representation of constraints."""
        graph = {var: set() for var in self.problem.variables}
        for (A, B) in self.problem.constraints:
            graph[A].add(B)
            graph[B].add(A)
        return graph
    
    def select_unassigned_variable(self, assignment: Dict[str, str]) -> str:
        """Select the next unassigned variable using Minimum Remaining Values heuristic."""
        unassigned = [var for var in self.problem.variables if var not in assignment]
        
        # MRV heuristic: choose variable with fewest legal values
        if not unassigned:
            raise ValueError("All variables are already assigned")
            
        # For simplicity, return first unassigned (can be enhanced with MRV)
        return unassigned[0]
    
    def is_consistent(self, assignment: Dict[str, str]) -> bool:
        """Check if the current assignment is consistent with all constraints."""
        for (A, B) in self.problem.constraints:
            if A in assignment and B in assignment and assignment[A] == assignment[B]:
                return False
        return True
    
    def backtrack(self, assignment: Optional[Dict[str, str]] = None) -> Optional[Dict[str, str]]:
        """
        Solve the CSP using backtracking search.
        
        Args:
            assignment: Current partial assignment
            
        Returns:
            Complete assignment if solution exists, None otherwise
        """
        if assignment is None:
            assignment = {}
            
        if len(assignment) == len(self.problem.variables):
            return assignment
            
        var = self.select_unassigned_variable(assignment)
        
        for value in self.problem.domains[var]:
            new_assignment = assignment.copy()
            new_assignment[var] = value
            
            if self.is_consistent(new_assignment):
                result = self.backtrack(new_assignment)
                if result is not None:
                    return result
                    
        return None
    
    def solve(self) -> CSPSolution:
        """Public method to solve the CSP."""
        assignment = self.backtrack()
        return CSPSolution(
            problem=self.problem,
            assignment=assignment,
            is_solved=assignment is not None
        )
