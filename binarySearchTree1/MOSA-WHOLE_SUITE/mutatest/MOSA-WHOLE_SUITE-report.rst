Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/binarySearchTree1/binarySearchTree1.py
 - Test commands: ['python', '-m', 'pytest', './MOSA-WHOLE_SUITE']
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
 - Clean trial 1 run time: 0:00:00.349933
 - Clean trial 2 run time: 0:00:00.259016
 - Mutation trials total run time: 0:00:09.720977

Overall mutation trial summary
==============================
 - DETECTED: 24
 - SURVIVED: 2
 - TOTAL RUNS: 26
 - RUN DATETIME: 2023-03-06 14:07:20.995592


Mutations by result status
==========================


SURVIVED
--------
 - binarySearchTree1.py: (l: 37, c: 13) - mutation from <class 'ast.Gt'> to <class 'ast.NotEq'>
 - binarySearchTree1.py: (l: 124, c: 12) - mutation from If_Statement to If_False


DETECTED
--------
 - binarySearchTree1.py: (l: 11, c: 23) - mutation from None to False
 - binarySearchTree1.py: (l: 11, c: 23) - mutation from None to True
 - binarySearchTree1.py: (l: 37, c: 13) - mutation from <class 'ast.Gt'> to <class 'ast.Lt'>
 - binarySearchTree1.py: (l: 37, c: 13) - mutation from <class 'ast.Gt'> to <class 'ast.LtE'>
 - binarySearchTree1.py: (l: 37, c: 13) - mutation from <class 'ast.Gt'> to <class 'ast.Eq'>
 - binarySearchTree1.py: (l: 37, c: 13) - mutation from <class 'ast.Gt'> to <class 'ast.GtE'>
 - binarySearchTree1.py: (l: 56, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree1.py: (l: 56, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree1.py: (l: 68, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.FloorDiv'>
 - binarySearchTree1.py: (l: 68, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Div'>
 - binarySearchTree1.py: (l: 68, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Mult'>
 - binarySearchTree1.py: (l: 68, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Pow'>
 - binarySearchTree1.py: (l: 68, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Sub'>
 - binarySearchTree1.py: (l: 68, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Mod'>
 - binarySearchTree1.py: (l: 102, c: 24) - mutation from None to True
 - binarySearchTree1.py: (l: 102, c: 24) - mutation from None to False
 - binarySearchTree1.py: (l: 105, c: 24) - mutation from None to False
 - binarySearchTree1.py: (l: 105, c: 24) - mutation from None to True
 - binarySearchTree1.py: (l: 124, c: 12) - mutation from If_Statement to If_True
 - binarySearchTree1.py: (l: 127, c: 23) - mutation from True to None
 - binarySearchTree1.py: (l: 127, c: 23) - mutation from True to False
 - binarySearchTree1.py: (l: 161, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree1.py: (l: 161, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree1.py: (l: 161, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>