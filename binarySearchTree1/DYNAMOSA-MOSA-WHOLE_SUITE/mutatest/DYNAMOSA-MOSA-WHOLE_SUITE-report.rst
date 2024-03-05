Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/binarySearchTree1/binarySearchTree1.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MOSA-WHOLE_SUITE']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 63
 - Location sample coverage: 15.87 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.424491
 - Clean trial 2 run time: 0:00:00.283846
 - Mutation trials total run time: 0:00:13.973291

Overall mutation trial summary
==============================
 - DETECTED: 28
 - SURVIVED: 3
 - TOTAL RUNS: 31
 - RUN DATETIME: 2023-03-12 12:46:18.088531


Mutations by result status
==========================


SURVIVED
--------
 - binarySearchTree1.py: (l: 140, c: 23) - mutation from <class 'ast.Sub'> to <class 'ast.Add'>
 - binarySearchTree1.py: (l: 140, c: 23) - mutation from <class 'ast.Sub'> to <class 'ast.Mult'>
 - binarySearchTree1.py: (l: 156, c: 8) - mutation from If_Statement to If_False


DETECTED
--------
 - binarySearchTree1.py: (l: 25, c: 21) - mutation from None to False
 - binarySearchTree1.py: (l: 25, c: 21) - mutation from None to True
 - binarySearchTree1.py: (l: 68, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Sub'>
 - binarySearchTree1.py: (l: 68, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Pow'>
 - binarySearchTree1.py: (l: 68, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.FloorDiv'>
 - binarySearchTree1.py: (l: 68, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Mult'>
 - binarySearchTree1.py: (l: 68, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Div'>
 - binarySearchTree1.py: (l: 68, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Mod'>
 - binarySearchTree1.py: (l: 97, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree1.py: (l: 97, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree1.py: (l: 102, c: 24) - mutation from None to True
 - binarySearchTree1.py: (l: 102, c: 24) - mutation from None to False
 - binarySearchTree1.py: (l: 122, c: 12) - mutation from If_Statement to If_False
 - binarySearchTree1.py: (l: 122, c: 12) - mutation from If_Statement to If_True
 - binarySearchTree1.py: (l: 122, c: 15) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - binarySearchTree1.py: (l: 122, c: 15) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - binarySearchTree1.py: (l: 122, c: 15) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - binarySearchTree1.py: (l: 122, c: 15) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - binarySearchTree1.py: (l: 122, c: 15) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - binarySearchTree1.py: (l: 127, c: 23) - mutation from True to None
 - binarySearchTree1.py: (l: 127, c: 23) - mutation from True to False
 - binarySearchTree1.py: (l: 140, c: 23) - mutation from <class 'ast.Sub'> to <class 'ast.FloorDiv'>
 - binarySearchTree1.py: (l: 140, c: 23) - mutation from <class 'ast.Sub'> to <class 'ast.Mod'>
 - binarySearchTree1.py: (l: 140, c: 23) - mutation from <class 'ast.Sub'> to <class 'ast.Div'>
 - binarySearchTree1.py: (l: 140, c: 23) - mutation from <class 'ast.Sub'> to <class 'ast.Pow'>
 - binarySearchTree1.py: (l: 145, c: 12) - mutation from If_Statement to If_True
 - binarySearchTree1.py: (l: 145, c: 12) - mutation from If_Statement to If_False
 - binarySearchTree1.py: (l: 156, c: 8) - mutation from If_Statement to If_True