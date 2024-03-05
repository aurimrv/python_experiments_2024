Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/binarySearchTree3/binarySearchTree3.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-WHOLE_SUITE']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 116
 - Location sample coverage: 8.62 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.477323
 - Clean trial 2 run time: 0:00:00.318929
 - Mutation trials total run time: 0:00:09.504307

Overall mutation trial summary
==============================
 - SURVIVED: 10
 - DETECTED: 14
 - TOTAL RUNS: 24
 - RUN DATETIME: 2023-03-05 22:19:52.112093


Mutations by result status
==========================


SURVIVED
--------
 - binarySearchTree3.py: (l: 84, c: 28) - mutation from None to False
 - binarySearchTree3.py: (l: 103, c: 59) - mutation from None to True
 - binarySearchTree3.py: (l: 103, c: 59) - mutation from None to False
 - binarySearchTree3.py: (l: 104, c: 16) - mutation from AugAssign_Sub to AugAssign_Div
 - binarySearchTree3.py: (l: 104, c: 16) - mutation from AugAssign_Sub to AugAssign_Add
 - binarySearchTree3.py: (l: 104, c: 16) - mutation from AugAssign_Sub to AugAssign_Mult
 - binarySearchTree3.py: (l: 159, c: 40) - mutation from None to False
 - binarySearchTree3.py: (l: 177, c: 11) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - binarySearchTree3.py: (l: 179, c: 11) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - binarySearchTree3.py: (l: 372, c: 51) - mutation from None to False


DETECTED
--------
 - binarySearchTree3.py: (l: 49, c: 8) - mutation from AugAssign_Add to AugAssign_Div
 - binarySearchTree3.py: (l: 49, c: 8) - mutation from AugAssign_Add to AugAssign_Sub
 - binarySearchTree3.py: (l: 49, c: 8) - mutation from AugAssign_Add to AugAssign_Mult
 - binarySearchTree3.py: (l: 79, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - binarySearchTree3.py: (l: 79, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - binarySearchTree3.py: (l: 79, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - binarySearchTree3.py: (l: 79, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - binarySearchTree3.py: (l: 79, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - binarySearchTree3.py: (l: 84, c: 28) - mutation from None to True
 - binarySearchTree3.py: (l: 159, c: 40) - mutation from None to True
 - binarySearchTree3.py: (l: 259, c: 16) - mutation from AugAssign_Add to AugAssign_Mult
 - binarySearchTree3.py: (l: 259, c: 16) - mutation from AugAssign_Add to AugAssign_Sub
 - binarySearchTree3.py: (l: 259, c: 16) - mutation from AugAssign_Add to AugAssign_Div
 - binarySearchTree3.py: (l: 372, c: 51) - mutation from None to True