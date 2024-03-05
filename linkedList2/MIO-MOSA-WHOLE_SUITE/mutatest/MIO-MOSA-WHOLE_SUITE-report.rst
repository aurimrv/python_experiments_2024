Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/linkedList2/linkedList2.py
 - Test commands: ['python', '-m', 'pytest', './MIO-MOSA-WHOLE_SUITE']
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
 - Clean trial 1 run time: 0:00:00.300362
 - Clean trial 2 run time: 0:00:00.224290
 - Mutation trials total run time: 0:00:09.067374

Overall mutation trial summary
==============================
 - DETECTED: 25
 - SURVIVED: 4
 - TOTAL RUNS: 29
 - RUN DATETIME: 2023-03-06 09:33:30.023199


Mutations by result status
==========================


SURVIVED
--------
 - linkedList2.py: (l: 15, c: 29) - mutation from <class 'ast.NotEq'> to <class 'ast.Eq'>
 - linkedList2.py: (l: 16, c: 12) - mutation from If_Statement to If_True
 - linkedList2.py: (l: 37, c: 24) - mutation from None to False
 - linkedList2.py: (l: 37, c: 24) - mutation from None to True


DETECTED
--------
 - linkedList2.py: (l: 7, c: 37) - mutation from None to True
 - linkedList2.py: (l: 7, c: 37) - mutation from None to False
 - linkedList2.py: (l: 15, c: 29) - mutation from <class 'ast.NotEq'> to <class 'ast.Lt'>
 - linkedList2.py: (l: 15, c: 29) - mutation from <class 'ast.NotEq'> to <class 'ast.LtE'>
 - linkedList2.py: (l: 15, c: 29) - mutation from <class 'ast.NotEq'> to <class 'ast.GtE'>
 - linkedList2.py: (l: 15, c: 29) - mutation from <class 'ast.NotEq'> to <class 'ast.Gt'>
 - linkedList2.py: (l: 15, c: 35) - mutation from None to False
 - linkedList2.py: (l: 15, c: 35) - mutation from None to True
 - linkedList2.py: (l: 16, c: 12) - mutation from If_Statement to If_False
 - linkedList2.py: (l: 21, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - linkedList2.py: (l: 21, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - linkedList2.py: (l: 21, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - linkedList2.py: (l: 21, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - linkedList2.py: (l: 21, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - linkedList2.py: (l: 66, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - linkedList2.py: (l: 75, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.GtE'>
 - linkedList2.py: (l: 75, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.LtE'>
 - linkedList2.py: (l: 75, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Gt'>
 - linkedList2.py: (l: 75, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Lt'>
 - linkedList2.py: (l: 75, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Eq'>
 - linkedList2.py: (l: 75, c: 19) - mutation from None to True
 - linkedList2.py: (l: 75, c: 19) - mutation from None to False
 - linkedList2.py: (l: 76, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - linkedList2.py: (l: 76, c: 12) - mutation from AugAssign_Add to AugAssign_Sub
 - linkedList2.py: (l: 76, c: 12) - mutation from AugAssign_Add to AugAssign_Mult