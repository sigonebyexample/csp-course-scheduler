
import unittest
from src.models import CSPProblem
from src.csp_solver import CSPSolver

class TestCSPSolver(unittest.TestCase):
    def setUp(self):
        self.variables = ["A", "B", "C"]
        self.constraints = [("A", "B"), ("B", "C")]
        self.problem = CSPProblem(self.variables, self.constraints)
        self.solver = CSPSolver(self.problem)
    
    def test_initialization(self):
        self.assertEqual(self.solver.problem.variables, self.variables)
        self.assertEqual(self.solver.problem.constraints, self.constraints)
    
    def test_constraint_graph(self):
        expected_graph = {
            "A": {"B"},
            "B": {"A", "C"},
            "C": {"B"}
        }
        self.assertEqual(self.solver.graph, expected_graph)
    
    def test_is_consistent(self):
        consistent_assignment = {"A": "Monday", "B": "Tuesday"}
        self.assertTrue(self.solver.is_consistent(consistent_assignment))
        
        inconsistent_assignment = {"A": "Monday", "B": "Monday"}
        self.assertFalse(self.solver.is_consistent(inconsistent_assignment))
    
    def test_solution_exists(self):
        solution = self.solver.solve()
        self.assertTrue(solution.is_solved)
        self.assertEqual(len(solution.assignment), len(self.variables))
        
        # Verify all constraints are satisfied
        for A, B in self.constraints:
            self.assertNotEqual(solution.assignment[A], solution.assignment[B])
    
    def test_unsolvable_problem(self):
        # Create an unsolvable problem (3 variables that all must be different with only 2 values)
        variables = ["A", "B", "C"]
        constraints = [("A", "B"), ("B", "C"), ("A", "C")]
        domains = {"A": ["Monday"], "B": ["Monday"], "C": ["Monday"]}  # All must be Monday but can't be same
        problem = CSPProblem(variables, constraints, domains)
        solver = CSPSolver(problem)
        
        solution = solver.solve()
        self.assertFalse(solution.is_solved)
        self.assertIsNone(solution.assignment)

if __name__ == "__main__":
    unittest.main()
