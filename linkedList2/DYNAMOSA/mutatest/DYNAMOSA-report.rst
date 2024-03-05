Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/linkedList2/linkedList2.py
 - Test commands: ['python', '-m', 'pytest', '--tb=no', './DYNAMOSA']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: 2023

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 36
 - Location sample coverage: 27.78 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.229974
 - Clean trial 2 run time: 0:00:00.198292
 - Mutation trials total run time: 0:00:05.524262

Overall mutation trial summary
==============================
 - DETECTED: 22
 - SURVIVED: 5
 - TOTAL RUNS: 27
 - RUN DATETIME: 2023-07-14 00:09:11.350388


Mutations by result status
==========================


SURVIVED
--------
 - linkedList2.py: (l: 15, c: 20) - mutation from None to True
 - linkedList2.py: (l: 15, c: 20) - mutation from None to False
 - linkedList2.py: (l: 66, c: 8) - mutation from If_Statement to If_False
 - linkedList2.py: (l: 66, c: 24) - mutation from None to False
 - linkedList2.py: (l: 66, c: 24) - mutation from None to True


DETECTED
--------
 - linkedList2.py: (l: 47, c: 19) - mutation from None to False
 - linkedList2.py: (l: 47, c: 19) - mutation from None to True
 - linkedList2.py: (l: 48, c: 12) - mutation from If_Statement to If_True
 - linkedList2.py: (l: 48, c: 12) - mutation from If_Statement to If_False
 - linkedList2.py: (l: 49, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - linkedList2.py: (l: 49, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - linkedList2.py: (l: 49, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - linkedList2.py: (l: 49, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - linkedList2.py: (l: 49, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - linkedList2.py: (l: 49, c: 27) - mutation from None to False
 - linkedList2.py: (l: 49, c: 27) - mutation from None to True
 - linkedList2.py: (l: 60, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Eq'>
 - linkedList2.py: (l: 60, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Gt'>
 - linkedList2.py: (l: 60, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.LtE'>
 - linkedList2.py: (l: 60, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.GtE'>
 - linkedList2.py: (l: 60, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Lt'>
 - linkedList2.py: (l: 60, c: 19) - mutation from None to False
 - linkedList2.py: (l: 60, c: 19) - mutation from None to True
 - linkedList2.py: (l: 66, c: 8) - mutation from If_Statement to If_True
 - linkedList2.py: (l: 76, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - linkedList2.py: (l: 76, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - linkedList2.py: (l: 76, c: 12) - mutation from AugAssign_Add to AugAssign_Sub