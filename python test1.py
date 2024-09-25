class Solution:
    def isValid(self, s: str) -> bool:
        
        bracket_map = {')': '(', '}': '{', ']': '['}
    
        stack = []
        
        for char in s:
            if char in bracket_map.values(): 
                stack.append(char)
            elif char in bracket_map: 
                if stack and stack[-1] == bracket_map[char]:
                    stack.pop() 
                else:
                    return False 
        return not stack  


import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_valid_parentheses(self):
        self.assertTrue(self.solution.isValid("()"))
        self.assertTrue(self.solution.isValid("()[]{}"))
        self.assertTrue(self.solution.isValid("{[()]}"))

    def test_invalid_parentheses(self):
        self.assertFalse(self.solution.isValid("(]"))
        self.assertFalse(self.solution.isValid("([)]"))

    def test_empty_string(self):
        self.assertTrue(self.solution.isValid(""))

    def test_mixed_parentheses(self):
        self.assertFalse(self.solution.isValid("(){"))

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
