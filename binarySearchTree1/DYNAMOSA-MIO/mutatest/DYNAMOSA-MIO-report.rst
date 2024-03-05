Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/binarySearchTree1/binarySearchTree1.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MIO']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 67
 - Location sample coverage: 14.93 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:01.738128
 - Clean trial 2 run time: 0:00:01.294085
 - Mutation trials total run time: 0:00:52.263887

Overall mutation trial summary
==============================
 - DETECTED: 22
 - SURVIVED: 2
 - TOTAL RUNS: 24
 - RUN DATETIME: 2023-03-05 12:16:05.526433


Mutations by result status
==========================


SURVIVED
--------
 - binarySearchTree1.py: (l: 122, c: 12) - mutation from If_Statement to If_False
 - binarySearchTree1.py: (l: 145, c: 15) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>


DETECTED
--------
 - binarySearchTree1.py: (l: 25, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree1.py: (l: 25, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree1.py: (l: 25, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - binarySearchTree1.py: (l: 40, c: 28) - mutation from None to True
 - binarySearchTree1.py: (l: 40, c: 28) - mutation from None to False
 - binarySearchTree1.py: (l: 68, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.FloorDiv'>
 - binarySearchTree1.py: (l: 68, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Div'>
 - binarySearchTree1.py: (l: 68, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Pow'>
 - binarySearchTree1.py: (l: 68, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Mult'>
 - binarySearchTree1.py: (l: 68, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Mod'>
 - binarySearchTree1.py: (l: 68, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Sub'>
 - binarySearchTree1.py: (l: 90, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - binarySearchTree1.py: (l: 111, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - binarySearchTree1.py: (l: 122, c: 12) - mutation from If_Statement to If_True
 - binarySearchTree1.py: (l: 129, c: 15) - mutation from False to True
 - binarySearchTree1.py: (l: 129, c: 15) - mutation from False to None
 - binarySearchTree1.py: (l: 145, c: 12) - mutation from If_Statement to If_True
 - binarySearchTree1.py: (l: 145, c: 12) - mutation from If_Statement to If_False
 - binarySearchTree1.py: (l: 145, c: 15) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - binarySearchTree1.py: (l: 145, c: 15) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - binarySearchTree1.py: (l: 145, c: 15) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - binarySearchTree1.py: (l: 145, c: 15) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>