Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/binarySearchTree2/binarySearchTree2.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MOSA-WHOLE_SUITE']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 69
 - Location sample coverage: 14.49 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.352958
 - Clean trial 2 run time: 0:00:00.249981
 - Mutation trials total run time: 0:00:11.205570

Overall mutation trial summary
==============================
 - DETECTED: 18
 - SURVIVED: 15
 - TOTAL RUNS: 33
 - RUN DATETIME: 2023-03-12 12:46:30.169457


Mutations by result status
==========================


SURVIVED
--------
 - binarySearchTree2.py: (l: 67, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - binarySearchTree2.py: (l: 67, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - binarySearchTree2.py: (l: 68, c: 28) - mutation from None to False
 - binarySearchTree2.py: (l: 89, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - binarySearchTree2.py: (l: 89, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - binarySearchTree2.py: (l: 89, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - binarySearchTree2.py: (l: 89, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - binarySearchTree2.py: (l: 89, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - binarySearchTree2.py: (l: 92, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree2.py: (l: 92, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree2.py: (l: 186, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - binarySearchTree2.py: (l: 186, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - binarySearchTree2.py: (l: 186, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - binarySearchTree2.py: (l: 186, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - binarySearchTree2.py: (l: 186, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>


DETECTED
--------
 - binarySearchTree2.py: (l: 10, c: 20) - mutation from None to True
 - binarySearchTree2.py: (l: 10, c: 20) - mutation from None to False
 - binarySearchTree2.py: (l: 20, c: 19) - mutation from False to None
 - binarySearchTree2.py: (l: 20, c: 19) - mutation from False to True
 - binarySearchTree2.py: (l: 47, c: 19) - mutation from False to True
 - binarySearchTree2.py: (l: 47, c: 19) - mutation from False to None
 - binarySearchTree2.py: (l: 67, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - binarySearchTree2.py: (l: 67, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - binarySearchTree2.py: (l: 67, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - binarySearchTree2.py: (l: 68, c: 28) - mutation from None to True
 - binarySearchTree2.py: (l: 120, c: 49) - mutation from <class 'ast.Sub'> to <class 'ast.Mod'>
 - binarySearchTree2.py: (l: 120, c: 49) - mutation from <class 'ast.Sub'> to <class 'ast.Add'>
 - binarySearchTree2.py: (l: 120, c: 49) - mutation from <class 'ast.Sub'> to <class 'ast.Mult'>
 - binarySearchTree2.py: (l: 120, c: 49) - mutation from <class 'ast.Sub'> to <class 'ast.Pow'>
 - binarySearchTree2.py: (l: 120, c: 49) - mutation from <class 'ast.Sub'> to <class 'ast.Div'>
 - binarySearchTree2.py: (l: 120, c: 49) - mutation from <class 'ast.Sub'> to <class 'ast.FloorDiv'>
 - binarySearchTree2.py: (l: 124, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree2.py: (l: 124, c: 8) - mutation from If_Statement to If_False