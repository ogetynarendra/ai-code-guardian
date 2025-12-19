"""Main code analyzer module for AI Code Guardian."""

import ast
import re
from typing import Dict, List, Any, Optional
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class CodeAnalyzer:
    """Main analyzer class for code review and analysis."""
    
    def __init__(self):
        self.results = []
        self.metrics = {}
        
    def analyze_file(self, file_path: str) -> Dict[str, Any]:
        """Analyze a single code file.
        
        Args:
            file_path: Path to the code file
            
        Returns:
            Dictionary containing analysis results
        """
        try:
            path = Path(file_path)
            if not path.exists():
                raise FileNotFoundError(f"File not found: {file_path}")
                
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            return self._analyze_code(content, path.suffix)
            
        except Exception as e:
            logger.error(f"Error analyzing file {file_path}: {e}")
            return {"error": str(e)}
    
    def _analyze_code(self, code: str, file_extension: str) -> Dict[str, Any]:
        """Perform detailed code analysis."""
        results = {
            "lines_of_code": len(code.split('\n')),
            "file_type": file_extension,
            "issues": [],
            "metrics": {}
        }
        
        if file_extension == '.py':
            results.update(self._analyze_python(code))
        elif file_extension in ['.js', '.ts']:
            results.update(self._analyze_javascript(code))
            
        return results
    
    def _analyze_python(self, code: str) -> Dict[str, Any]:
        """Analyze Python code using AST."""
        try:
            tree = ast.parse(code)
            
            analysis = {
                "complexity": self._calculate_complexity(tree),
                "functions": self._count_functions(tree),
                "classes": self._count_classes(tree),
                "imports": self._extract_imports(tree),
            }
            
            return analysis
            
        except SyntaxError as e:
            return {"syntax_error": str(e)}
    
    def _calculate_complexity(self, tree: ast.AST) -> int:
        """Calculate cyclomatic complexity."""
        complexity = 1
        
        for node in ast.walk(tree):
            if isinstance(node, (ast.If, ast.While, ast.For, ast.ExceptHandler)):
                complexity += 1
            elif isinstance(node, ast.BoolOp):
                complexity += len(node.values) - 1
                
        return complexity
    
    def _count_functions(self, tree: ast.AST) -> int:
        """Count number of functions in the code."""
        return sum(1 for node in ast.walk(tree) if isinstance(node, ast.FunctionDef))
    
    def _count_classes(self, tree: ast.AST) -> int:
        """Count number of classes in the code."""
        return sum(1 for node in ast.walk(tree) if isinstance(node, ast.ClassDef))
    
    def _extract_imports(self, tree: ast.AST) -> List[str]:
        """Extract all import statements."""
        imports = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for name in node.names:
                    imports.append(name.name)
            elif isinstance(node, ast.ImportFrom):
                module = node.module or ''
                for name in node.names:
                    imports.append(f"{module}.{name.name}")
        return imports
    
    def _analyze_javascript(self, code: str) -> Dict[str, Any]:
        """Basic JavaScript code analysis."""
        analysis = {
            "functions": len(re.findall(r'function\s+\w+', code)),
            "arrow_functions": len(re.findall(r'=>', code)),
            "classes": len(re.findall(r'class\s+\w+', code)),
        }
        return analysis
    
    def analyze_directory(self, dir_path: str, extensions: List[str] = None) -> List[Dict[str, Any]]:
        """Analyze all code files in a directory.
        
        Args:
            dir_path: Path to directory
            extensions: List of file extensions to analyze (e.g., ['.py', '.js'])
            
        Returns:
            List of analysis results for each file
        """
        if extensions is None:
            extensions = ['.py', '.js', '.ts', '.java', '.cpp']
            
        results = []
        path = Path(dir_path)
        
        for ext in extensions:
            for file_path in path.rglob(f'*{ext}'):
                logger.info(f"Analyzing: {file_path}")
                result = self.analyze_file(str(file_path))
                result['file_path'] = str(file_path)
                results.append(result)
                
        return results
    
    def generate_report(self, results: List[Dict[str, Any]]) -> str:
        """Generate a comprehensive analysis report."""
        report = "# Code Analysis Report\n\n"
        report += f"Total files analyzed: {len(results)}\n\n"
        
        total_loc = sum(r.get('lines_of_code', 0) for r in results)
        report += f"Total lines of code: {total_loc}\n\n"
        
        for result in results:
            report += f"## {result.get('file_path', 'Unknown')}\n"
            report += f"- Lines: {result.get('lines_of_code', 0)}\n"
            report += f"- Complexity: {result.get('complexity', 'N/A')}\n"
            if 'issues' in result and result['issues']:
                report += "- Issues found:\n"
                for issue in result['issues']:
                    report += f"  - {issue}\n"
            report += "\n"
            
        return report
