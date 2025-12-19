"""Bug pattern detection module."""

import ast
import re
from typing import List, Dict, Any


class BugPatternDetector:
    """Detects common bug patterns and code smells."""
    
    def __init__(self):
        self.patterns = []
        
    def detect(self, code: str, file_type: str = '.py') -> List[Dict[str, Any]]:
        """Detect bug patterns in code."""
        self.patterns = []
        
        if file_type == '.py':
            self._detect_python_patterns(code)
            
        return self.patterns
    
    def _detect_python_patterns(self, code: str):
        """Detect Python-specific bug patterns."""
        try:
            tree = ast.parse(code)
            self._check_bare_except(tree)
            self._check_mutable_defaults(tree)
            self._check_unused_variables(tree)
        except SyntaxError:
            pass
    
    def _check_bare_except(self, tree: ast.AST):
        """Detect bare except clauses."""
        for node in ast.walk(tree):
            if isinstance(node, ast.ExceptHandler):
                if node.type is None:
                    self.patterns.append({
                        "type": "Bare Except Clause",
                        "severity": "MEDIUM",
                        "description": "Bare except catches all exceptions, including system exits"
                    })
    
    def _check_mutable_defaults(self, tree: ast.AST):
        """Detect mutable default arguments."""
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                for arg in node.args.defaults:
                    if isinstance(arg, (ast.List, ast.Dict, ast.Set)):
                        self.patterns.append({
                            "type": "Mutable Default Argument",
                            "severity": "HIGH",
                            "description": "Mutable default arguments can cause unexpected behavior",
                            "function": node.name
                        })
    
    def _check_unused_variables(self, tree: ast.AST):
        """Detect potentially unused variables."""
        pass  # Simplified for this implementation
