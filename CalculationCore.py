import math
import re

def evaluate_expression(expression: str) -> str:
    try:
        expression = expression.replace('^', '**')
        expression = expression.replace('π', str(math.pi))
        expression = expression.replace('e', str(math.e))
        expression = expression.replace('÷', '/')
        expression = expression.replace('x', '*')
        expression = expression.replace('log', 'math.log10')
        expression = expression.replace('ln', 'math.log')

        expression = re.sub(r'sin\((.*?)\)', r'math.sin(math.radians(\1))', expression)
        expression = re.sub(r'cos\((.*?)\)', r'math.cos(math.radians(\1))', expression)
        expression = re.sub(r'tan\((.*?)\)', r'math.tan(math.radians(\1))', expression)

        expression = re.sub(r'(\d+)!', r'math.factorial(\1)', expression)
        expression = re.sub(r'(\([^()]*\))!', r'math.factorial\1', expression)

        expression = re.sub(r'√(\d+(\.\d+)?)', r'math.sqrt(\1)', expression)
        expression = re.sub(r'√\((.*?)\)', r'math.sqrt(\1)', expression)

        result = eval(expression)
        return str(result)
        last_input = True
    except Exception:
        return "Error"
        last_input = True