Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/binarySearchTree2/binarySearchTree2.py
 - Test commands: ['python', '-m', 'pytest', './MIO-MOSA-WHOLE_SUITE']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 77
 - Location sample coverage: 12.99 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.331557
 - Clean trial 2 run time: 0:00:00.248708
 - Mutation trials total run time: 0:00:09.828863

Overall mutation trial summary
==============================
 - SURVIVED: 7
 - DETECTED: 22
 - TOTAL RUNS: 29
 - RUN DATETIME: 2023-03-06 09:32:45.530468


Mutations by result status
==========================


SURVIVED
--------
 - binarySearchTree2.py: (l: 92, c: 13) - mutation from <class 'ast.Gt'> to <class 'ast.Lt'>
 - binarySearchTree2.py: (l: 92, c: 13) - mutation from <class 'ast.Gt'> to <class 'ast.GtE'>
 - binarySearchTree2.py: (l: 92, c: 13) - mutation from <class 'ast.Gt'> to <class 'ast.Eq'>
 - binarySearchTree2.py: (l: 92, c: 13) - mutation from <class 'ast.Gt'> to <class 'ast.LtE'>
 - binarySearchTree2.py: (l: 92, c: 13) - mutation from <class 'ast.Gt'> to <class 'ast.NotEq'>
 - binarySearchTree2.py: (l: 102, c: 31) - mutation from None to False
 - binarySearchTree2.py: (l: 102, c: 31) - mutation from None to True


DETECTED
--------
 - binarySearchTree2.py: (l: 19, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree2.py: (l: 19, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree2.py: (l: 20, c: 19) - mutation from False to None
 - binarySearchTree2.py: (l: 20, c: 19) - mutation from False to True
 - binarySearchTree2.py: (l: 21, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - binarySearchTree2.py: (l: 21, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - binarySearchTree2.py: (l: 21, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - binarySearchTree2.py: (l: 21, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - binarySearchTree2.py: (l: 21, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - binarySearchTree2.py: (l: 46, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - binarySearchTree2.py: (l: 46, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - binarySearchTree2.py: (l: 46, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - binarySearchTree2.py: (l: 46, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - binarySearchTree2.py: (l: 46, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - binarySearchTree2.py: (l: 49, c: 19) - mutation from True to False
 - binarySearchTree2.py: (l: 49, c: 19) - mutation from True to None
 - binarySearchTree2.py: (l: 51, c: 12) - mutation from If_Statement to If_False
 - binarySearchTree2.py: (l: 51, c: 12) - mutation from If_Statement to If_True
 - binarySearchTree2.py: (l: 59, c: 34) - mutation from None to True
 - binarySearchTree2.py: (l: 59, c: 34) - mutation from None to False
 - binarySearchTree2.py: (l: 66, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree2.py: (l: 66, c: 8) - mutation from If_Statement to If_False