Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/linkedList2/linkedList2.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MIO-MOSA']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 36
 - Location sample coverage: 27.78 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.311457
 - Clean trial 2 run time: 0:00:00.237903
 - Mutation trials total run time: 0:00:08.832228

Overall mutation trial summary
==============================
 - DETECTED: 23
 - SURVIVED: 6
 - TOTAL RUNS: 29
 - RUN DATETIME: 2023-03-06 00:05:45.897350


Mutations by result status
==========================


SURVIVED
--------
 - linkedList2.py: (l: 15, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Eq'>
 - linkedList2.py: (l: 21, c: 32) - mutation from True to None
 - linkedList2.py: (l: 21, c: 32) - mutation from True to False
 - linkedList2.py: (l: 37, c: 24) - mutation from None to False
 - linkedList2.py: (l: 37, c: 24) - mutation from None to True
 - linkedList2.py: (l: 49, c: 16) - mutation from If_Statement to If_True


DETECTED
--------
 - linkedList2.py: (l: 15, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.LtE'>
 - linkedList2.py: (l: 15, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Gt'>
 - linkedList2.py: (l: 15, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.GtE'>
 - linkedList2.py: (l: 15, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Lt'>
 - linkedList2.py: (l: 27, c: 21) - mutation from None to False
 - linkedList2.py: (l: 27, c: 21) - mutation from None to True
 - linkedList2.py: (l: 37, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - linkedList2.py: (l: 46, c: 15) - mutation from None to True
 - linkedList2.py: (l: 46, c: 15) - mutation from None to False
 - linkedList2.py: (l: 49, c: 16) - mutation from If_Statement to If_False
 - linkedList2.py: (l: 49, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - linkedList2.py: (l: 49, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - linkedList2.py: (l: 49, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - linkedList2.py: (l: 49, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - linkedList2.py: (l: 49, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - linkedList2.py: (l: 60, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Lt'>
 - linkedList2.py: (l: 60, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.GtE'>
 - linkedList2.py: (l: 60, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Eq'>
 - linkedList2.py: (l: 60, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.LtE'>
 - linkedList2.py: (l: 60, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Gt'>
 - linkedList2.py: (l: 76, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - linkedList2.py: (l: 76, c: 12) - mutation from AugAssign_Add to AugAssign_Sub
 - linkedList2.py: (l: 76, c: 12) - mutation from AugAssign_Add to AugAssign_Mult