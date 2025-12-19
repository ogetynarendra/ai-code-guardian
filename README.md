# 🛡️ AI Code Guardian

> AI-powered code review system with ML-based vulnerability detection, bug pattern recognition, and automated security analysis.

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## 🚀 Features

- **🔍 Multi-Language Code Analysis**: Supports Python, JavaScript, TypeScript, Java, and C++
- **🛡️ Security Vulnerability Detection**: Identifies SQL injection, XSS, code injection, and hardcoded secrets
- **🐛 Bug Pattern Recognition**: Detects common code smells and anti-patterns
- **📊 Complexity Analysis**: Calculates cyclomatic complexity and provides metrics
- **🤖 ML-Powered Insights**: Uses machine learning for intelligent code review suggestions
- **📈 Comprehensive Reporting**: Generates detailed analysis reports with visualizations
- **⚡ Fast & Efficient**: Optimized for performance on large codebases

## 📋 Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage](#usage)
- [Architecture](#architecture)
- [API Reference](#api-reference)
- [Contributing](#contributing)
- [License](#license)

## 🔧 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Install from source

```bash
git clone https://github.com/ogetynarendra/ai-code-guardian.git
cd ai-code-guardian
pip install -r requirements.txt
```

### Development Installation

```bash
pip install -r requirements.txt
pip install -e .
```

## ⚡ Quick Start

### Basic Analysis

```python
from code_guardian import CodeAnalyzer

# Initialize the analyzer
analyzer = CodeAnalyzer()

# Analyze a single file
result = analyzer.analyze_file('path/to/your/code.py')
print(result)

# Analyze entire directory
results = analyzer.analyze_directory('path/to/project', extensions=['.py', '.js'])

# Generate report
report = analyzer.generate_report(results)
print(report)
```

### Vulnerability Detection

```python
from code_guardian import VulnerabilityDetector

detector = VulnerabilityDetector()

with open('mycode.py', 'r') as f:
    code = f.read()
    
vulnerabilities = detector.detect(code, file_type='.py')

for vuln in vulnerabilities:
    print(f"{vuln['severity']}: {vuln['type']} - {vuln['description']}")
```

## 📖 Usage

### CLI Usage

```bash
# Analyze a single file
python -m code_guardian analyze myfile.py

# Analyze directory
python -m code_guardian analyze ./src --recursive

# Generate HTML report
python -m code_guardian analyze ./src --output report.html

# Check specific vulnerability types
python -m code_guardian check-security ./src
```

### Advanced Examples

#### Custom Configuration

```python
from code_guardian import CodeAnalyzer, VulnerabilityDetector

analyzer = CodeAnalyzer()
detector = VulnerabilityDetector()

# Analyze with custom settings
results = analyzer.analyze_directory(
    'src/',
    extensions=['.py', '.js', '.ts'],
    exclude_patterns=['test_', '*_test.py']
)

# Filter by severity
critical_vulns = [
    v for v in detector.vulnerabilities 
    if v['severity'] == 'CRITICAL'
]
```

## 🏗️ Architecture

```
ai-code-guardian/
├── src/
│   └── code_guardian/
│       ├── __init__.py
│       ├── analyzer.py              # Main code analyzer
│       ├── vulnerability_detector.py # Security vulnerability detection
│       ├── bug_pattern_detector.py  # Bug pattern recognition
│       └── ml_model.py              # ML-based code review
├── tests/
│   ├── test_analyzer.py
│   ├── test_vulnerability.py
│   └── test_integration.py
├── examples/
│   ├── basic_usage.py
│   └── advanced_usage.py
├── docs/
│   ├── API.md
│   └── CONTRIBUTING.md
├── requirements.txt
├── setup.py
├── LICENSE
└── README.md
```

## 🔬 Core Components

### CodeAnalyzer

Main analysis engine that:
- Parses code using AST
- Calculates complexity metrics
- Identifies code structure
- Generates comprehensive reports

### VulnerabilityDetector

Security-focused component that:
- Detects SQL injection vulnerabilities
- Identifies XSS risks
- Finds hardcoded secrets
- Checks for weak cryptography
- Detects unsafe deserialization

### BugPatternDetector

Pattern recognition system for:
- Code smells
- Anti-patterns
- Performance issues
- Best practice violations

### MLCodeReviewer

Machine learning component that:
- Learns from code review history
- Suggests improvements
- Predicts potential issues
- Provides intelligent recommendations

## 📊 Metrics & Reports

AI Code Guardian provides:

- **Lines of Code (LOC)** analysis
- **Cyclomatic Complexity** calculations
- **Maintainability Index**
- **Security Score**
- **Code Quality Grade**

## 🧪 Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=code_guardian --cov-report=html

# Run specific test file
pytest tests/test_analyzer.py
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with passion for code quality and security
- Inspired by industry-leading static analysis tools
- Powered by modern ML techniques

## 📬 Contact

**Author**: ogetynarendra

**Project Link**: [https://github.com/ogetynarendra/ai-code-guardian](https://github.com/ogetynarendra/ai-code-guardian)

---

⭐ Star this repository if you find it helpful!
