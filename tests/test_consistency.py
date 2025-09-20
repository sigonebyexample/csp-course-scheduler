import unittest
from src.models import CSPProblem, CSPSolution

class TestConsistency(unittest.TestCase):
    def test_valid_solution(self):
        variables = ["A", "B", "C"]
        constraints = [("A", "B"), ("B", "C")]
        problem = CSPProblem(variables, constraints)
        
        # Valid solution
        assignment = {"A": "Monday", "B": "Tuesday", "C": "Monday"}
        solution = CSPSolution(problem, assignment, True)
        self.assertTrue(solution.is_valid())
    
    def test_invalid_solution(self):
        variables = ["A", "B", "C"]
        constraints = [("A", "B"), ("B", "C")]
        problem = CSPProblem(variables, constraints)
        
        # Invalid solution (A and B have same value)
        assignment = {"A": "Monday", "B": "Monday", "C": "Tuesday"}
        solution = CSPSolution(problem, assignment, True)
        self.assertFalse(solution.is_valid())
    
    def test_partial_assignment_validity(self):
        variables = ["A", "B", "C"]
        constraints = [("A", "B"), ("B", "C")]
        problem = CSPProblem(variables, constraints)
        
        # Partial assignment that's valid
        assignment = {"A": "Monday", "B": "Tuesday"}
        solution = CSPSolution(problem, assignment, False)
        # Should still be valid for the assigned variables
        for (A, B) in constraints:
            if A in assignment and B in assignment:
                self.assertNotEqual(assignment[A], assignment[B])

if __name__ == "__main__":
    unittest.main()
