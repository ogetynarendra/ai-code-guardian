examples/basic_usage.py  #!/usr/bin/env python3
"""Example usage of AI Code Guardian."""

import sys
sys.path.insert(0, 'src')

from code_guardian import CodeAnalyzer, VulnerabilityDetector, BugPatternDetector


def main():
    print("=== AI Code Guardian Example ===")
    print()
    
    # Example code to analyze
    sample_code = '''
import pickle

def process_data(data):
    password = "hardcoded123"
    result = eval(data)
    return result

def load_from_file(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)
'''
    
    # 1. Code Analysis
    print("1. Running Code Analyzer...")
    analyzer = CodeAnalyzer()
    analysis = analyzer._analyze_python(sample_code)
    print(f"   Functions: {analysis['functions']}")
    print(f"   Complexity: {analysis['complexity']}")
    print()
    
    # 2. Vulnerability Detection
    print("2. Scanning for Vulnerabilities...")
    vuln_detector = VulnerabilityDetector()
    vulns = vuln_detector.detect(sample_code, file_type='.py')
    
    if vulns:
        for vuln in vulns:
            print(f"   [{vuln['severity']}] {vuln['type']}")
            print(f"   - {vuln['description']}")
    else:
        print("   No vulnerabilities found!")
    print()
    
    # 3. Bug Pattern Detection
    print("3. Detecting Bug Patterns...")
    bug_detector = BugPatternDetector()
    patterns = bug_detector.detect(sample_code, file_type='.py')
    
    if patterns:
        for pattern in patterns:
            print(f"   [{pattern['severity']}] {pattern['type']}")
            print(f"   - {pattern['description']}")
    else:
        print("   No bug patterns detected!")
    print()
    
    print("=== Analysis Complete ===")


if __name__ == "__main__":
    main()
