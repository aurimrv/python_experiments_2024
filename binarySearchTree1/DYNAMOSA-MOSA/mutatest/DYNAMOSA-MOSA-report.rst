Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/binarySearchTree1/binarySearchTree1.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MOSA']
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
 - Clean trial 1 run time: 0:00:01.681979
 - Clean trial 2 run time: 0:00:01.674921
 - Mutation trials total run time: 0:01:35.664775

Overall mutation trial summary
==============================
 - SURVIVED: 7
 - DETECTED: 27
 - TOTAL RUNS: 34
 - RUN DATETIME: 2023-03-05 18:40:29.819307


Mutations by result status
==========================


SURVIVED
--------
 - binarySearchTree1.py: (l: 124, c: 17) - mutation from <class 'ast.Gt'> to <class 'ast.NotEq'>
 - binarySearchTree1.py: (l: 140, c: 23) - mutation from <class 'ast.Sub'> to <class 'ast.Add'>
 - binarySearchTree1.py: (l: 140, c: 23) - mutation from <class 'ast.Sub'> to <class 'ast.Mult'>
 - binarySearchTree1.py: (l: 143, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.Pow'>
 - binarySearchTree1.py: (l: 143, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.Add'>
 - binarySearchTree1.py: (l: 143, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.Mult'>
 - binarySearchTree1.py: (l: 147, c: 12) - mutation from If_Statement to If_True


DETECTED
--------
 - binarySearchTree1.py: (l: 18, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree1.py: (l: 18, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree1.py: (l: 37, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree1.py: (l: 37, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree1.py: (l: 68, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Div'>
 - binarySearchTree1.py: (l: 68, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Sub'>
 - binarySearchTree1.py: (l: 68, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.FloorDiv'>
 - binarySearchTree1.py: (l: 68, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Mult'>
 - binarySearchTree1.py: (l: 68, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Pow'>
 - binarySearchTree1.py: (l: 68, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Mod'>
 - binarySearchTree1.py: (l: 102, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - binarySearchTree1.py: (l: 114, c: 25) - mutation from None to False
 - binarySearchTree1.py: (l: 114, c: 25) - mutation from None to True
 - binarySearchTree1.py: (l: 124, c: 12) - mutation from If_Statement to If_False
 - binarySearchTree1.py: (l: 124, c: 12) - mutation from If_Statement to If_True
 - binarySearchTree1.py: (l: 124, c: 17) - mutation from <class 'ast.Gt'> to <class 'ast.GtE'>
 - binarySearchTree1.py: (l: 124, c: 17) - mutation from <class 'ast.Gt'> to <class 'ast.Lt'>
 - binarySearchTree1.py: (l: 124, c: 17) - mutation from <class 'ast.Gt'> to <class 'ast.LtE'>
 - binarySearchTree1.py: (l: 124, c: 17) - mutation from <class 'ast.Gt'> to <class 'ast.Eq'>
 - binarySearchTree1.py: (l: 140, c: 23) - mutation from <class 'ast.Sub'> to <class 'ast.Div'>
 - binarySearchTree1.py: (l: 140, c: 23) - mutation from <class 'ast.Sub'> to <class 'ast.Mod'>
 - binarySearchTree1.py: (l: 140, c: 23) - mutation from <class 'ast.Sub'> to <class 'ast.FloorDiv'>
 - binarySearchTree1.py: (l: 140, c: 23) - mutation from <class 'ast.Sub'> to <class 'ast.Pow'>
 - binarySearchTree1.py: (l: 143, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.Div'>
 - binarySearchTree1.py: (l: 143, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.Mod'>
 - binarySearchTree1.py: (l: 143, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.FloorDiv'>
 - binarySearchTree1.py: (l: 147, c: 12) - mutation from If_Statement to If_False