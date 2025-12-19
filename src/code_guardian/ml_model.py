"""Machine learning model for intelligent code review."""

import numpy as np
from typing import Dict, List, Any
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer


class MLCodeReviewer:
    """ML-based code reviewer for intelligent suggestions."""
    
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.vectorizer = TfidfVectorizer(max_features=1000)
        self.trained = False
        
    def train(self, code_samples: List[str], labels: List[int]):
        """Train the model on code samples."""
        X = self.vectorizer.fit_transform(code_samples)
        self.model.fit(X, labels)
        self.trained = True
        
    def predict_quality(self, code: str) -> Dict[str, Any]:
        """Predict code quality."""
        if not self.trained:
            return {"score": 0.5, "confidence": 0.0, "trained": False}
            
        X = self.vectorizer.transform([code])
        probability = self.model.predict_proba(X)[0]
        
        return {
            "score": probability[1],
            "confidence": max(probability),
            "trained": True,
            "recommendation": "Good" if probability[1] > 0.5 else "Needs Improvement"
        }
        
    def suggest_improvements(self, code: str) -> List[str]:
        """Suggest code improvements based on ML analysis."""
        suggestions = []
        
        quality = self.predict_quality(code)
        if quality["score"] < 0.5:
            suggestions.append("Consider refactoring for better readability")
            suggestions.append("Add more comments and documentation")
            
        return suggestions
