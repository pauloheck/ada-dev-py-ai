import ast
from typing import List, Dict

class CodeAnalyzer:
    def __init__(self, source_code: str):
        self.source_code = source_code
        self.tree = ast.parse(source_code)

    def extract_functions(self) -> List[Dict[str, str]]:
        functions = []
        for node in ast.walk(self.tree):
            if isinstance(node, ast.FunctionDef):
                functions.append({
                    "name": node.name,
                    "docstring": ast.get_docstring(node),
                    "args": [arg.arg for arg in node.args.args]
                })
        return functions

    def extract_classes(self) -> List[Dict[str, str]]:
        classes = []
        for node in ast.walk(self.tree):
            if isinstance(node, ast.ClassDef):
                classes.append({
                    "name": node.name,
                    "docstring": ast.get_docstring(node),
                    "methods": [n.name for n in node.body if isinstance(n, ast.FunctionDef)]
                })
        return classes

def map_requirements_from_code(source_code: str) -> Dict[str, List[Dict[str, str]]]:
    analyzer = CodeAnalyzer(source_code)
    return {
        "functions": analyzer.extract_functions(),
        "classes": analyzer.extract_classes()
    }
