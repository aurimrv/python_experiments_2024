Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/binarySearchTree3/binarySearchTree3.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MIO-WHOLE_SUITE']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 99
 - Location sample coverage: 10.10 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.595197
 - Clean trial 2 run time: 0:00:00.338080
 - Mutation trials total run time: 0:00:12.514340

Overall mutation trial summary
==============================
 - DETECTED: 20
 - SURVIVED: 7
 - TOTAL RUNS: 27
 - RUN DATETIME: 2023-03-12 11:33:24.783191


Mutations by result status
==========================


SURVIVED
--------
 - binarySearchTree3.py: (l: 61, c: 8) - mutation from AugAssign_Sub to AugAssign_Mult
 - binarySearchTree3.py: (l: 61, c: 8) - mutation from AugAssign_Sub to AugAssign_Add
 - binarySearchTree3.py: (l: 61, c: 8) - mutation from AugAssign_Sub to AugAssign_Div
 - binarySearchTree3.py: (l: 103, c: 59) - mutation from None to False
 - binarySearchTree3.py: (l: 103, c: 59) - mutation from None to True
 - binarySearchTree3.py: (l: 360, c: 12) - mutation from If_Statement to If_True
 - binarySearchTree3.py: (l: 360, c: 12) - mutation from If_Statement to If_False


DETECTED
--------
 - binarySearchTree3.py: (l: 98, c: 47) - mutation from <class 'ast.IsNot'> to <class 'ast.Is'>
 - binarySearchTree3.py: (l: 247, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree3.py: (l: 247, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree3.py: (l: 247, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - binarySearchTree3.py: (l: 247, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - binarySearchTree3.py: (l: 247, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - binarySearchTree3.py: (l: 247, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - binarySearchTree3.py: (l: 247, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - binarySearchTree3.py: (l: 306, c: 15) - mutation from <class 'ast.Sub'> to <class 'ast.FloorDiv'>
 - binarySearchTree3.py: (l: 306, c: 15) - mutation from <class 'ast.Sub'> to <class 'ast.Mult'>
 - binarySearchTree3.py: (l: 306, c: 15) - mutation from <class 'ast.Sub'> to <class 'ast.Add'>
 - binarySearchTree3.py: (l: 306, c: 15) - mutation from <class 'ast.Sub'> to <class 'ast.Div'>
 - binarySearchTree3.py: (l: 306, c: 15) - mutation from <class 'ast.Sub'> to <class 'ast.Pow'>
 - binarySearchTree3.py: (l: 306, c: 15) - mutation from <class 'ast.Sub'> to <class 'ast.Mod'>
 - binarySearchTree3.py: (l: 325, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree3.py: (l: 325, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree3.py: (l: 339, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree3.py: (l: 339, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree3.py: (l: 374, c: 28) - mutation from None to False
 - binarySearchTree3.py: (l: 374, c: 28) - mutation from None to True