Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/binarySearchTree1/binarySearchTree1.py
 - Test commands: ['python', '-m', 'pytest', './MIO-WHOLE_SUITE']
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
 - Clean trial 1 run time: 0:00:00.286828
 - Clean trial 2 run time: 0:00:00.244372
 - Mutation trials total run time: 0:00:09.226064

Overall mutation trial summary
==============================
 - DETECTED: 25
 - SURVIVED: 5
 - TOTAL RUNS: 30
 - RUN DATETIME: 2023-03-09 23:54:44.343390


Mutations by result status
==========================


SURVIVED
--------
 - binarySearchTree1.py: (l: 20, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree1.py: (l: 122, c: 15) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - binarySearchTree1.py: (l: 147, c: 17) - mutation from <class 'ast.Gt'> to <class 'ast.GtE'>
 - binarySearchTree1.py: (l: 147, c: 17) - mutation from <class 'ast.Gt'> to <class 'ast.NotEq'>
 - binarySearchTree1.py: (l: 161, c: 8) - mutation from If_Statement to If_True


DETECTED
--------
 - binarySearchTree1.py: (l: 11, c: 23) - mutation from None to True
 - binarySearchTree1.py: (l: 11, c: 23) - mutation from None to False
 - binarySearchTree1.py: (l: 20, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree1.py: (l: 68, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Mod'>
 - binarySearchTree1.py: (l: 68, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Mult'>
 - binarySearchTree1.py: (l: 68, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Div'>
 - binarySearchTree1.py: (l: 68, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Sub'>
 - binarySearchTree1.py: (l: 68, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.FloorDiv'>
 - binarySearchTree1.py: (l: 68, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Pow'>
 - binarySearchTree1.py: (l: 90, c: 24) - mutation from None to False
 - binarySearchTree1.py: (l: 90, c: 24) - mutation from None to True
 - binarySearchTree1.py: (l: 114, c: 25) - mutation from None to True
 - binarySearchTree1.py: (l: 114, c: 25) - mutation from None to False
 - binarySearchTree1.py: (l: 122, c: 15) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - binarySearchTree1.py: (l: 122, c: 15) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - binarySearchTree1.py: (l: 122, c: 15) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - binarySearchTree1.py: (l: 122, c: 15) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - binarySearchTree1.py: (l: 127, c: 23) - mutation from True to None
 - binarySearchTree1.py: (l: 127, c: 23) - mutation from True to False
 - binarySearchTree1.py: (l: 136, c: 24) - mutation from None to True
 - binarySearchTree1.py: (l: 136, c: 24) - mutation from None to False
 - binarySearchTree1.py: (l: 147, c: 17) - mutation from <class 'ast.Gt'> to <class 'ast.LtE'>
 - binarySearchTree1.py: (l: 147, c: 17) - mutation from <class 'ast.Gt'> to <class 'ast.Eq'>
 - binarySearchTree1.py: (l: 147, c: 17) - mutation from <class 'ast.Gt'> to <class 'ast.Lt'>
 - binarySearchTree1.py: (l: 161, c: 8) - mutation from If_Statement to If_False