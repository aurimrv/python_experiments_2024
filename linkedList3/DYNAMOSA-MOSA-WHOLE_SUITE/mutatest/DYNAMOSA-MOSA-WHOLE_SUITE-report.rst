Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/linkedList3/linkedList3.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MOSA-WHOLE_SUITE']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 19
 - Location sample coverage: 52.63 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.272337
 - Clean trial 2 run time: 0:00:00.218208
 - Mutation trials total run time: 0:00:06.801275

Overall mutation trial summary
==============================
 - DETECTED: 21
 - SURVIVED: 4
 - TOTAL RUNS: 25
 - RUN DATETIME: 2023-03-12 12:47:24.689154


Mutations by result status
==========================


SURVIVED
--------
 - linkedList3.py: (l: 40, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - linkedList3.py: (l: 42, c: 8) - mutation from If_Statement to If_True
 - linkedList3.py: (l: 102, c: 0) - mutation from If_Statement to If_True
 - linkedList3.py: (l: 102, c: 0) - mutation from If_Statement to If_False


DETECTED
--------
 - linkedList3.py: (l: 12, c: 20) - mutation from None to False
 - linkedList3.py: (l: 12, c: 20) - mutation from None to True
 - linkedList3.py: (l: 29, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - linkedList3.py: (l: 29, c: 12) - mutation from AugAssign_Add to AugAssign_Sub
 - linkedList3.py: (l: 29, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - linkedList3.py: (l: 34, c: 12) - mutation from AugAssign_Add to AugAssign_Sub
 - linkedList3.py: (l: 34, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - linkedList3.py: (l: 34, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - linkedList3.py: (l: 40, c: 8) - mutation from If_Statement to If_True
 - linkedList3.py: (l: 40, c: 8) - mutation from If_Statement to If_False
 - linkedList3.py: (l: 40, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - linkedList3.py: (l: 40, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - linkedList3.py: (l: 40, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - linkedList3.py: (l: 40, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - linkedList3.py: (l: 41, c: 19) - mutation from None to True
 - linkedList3.py: (l: 41, c: 19) - mutation from None to False
 - linkedList3.py: (l: 42, c: 8) - mutation from If_Statement to If_False
 - linkedList3.py: (l: 44, c: 35) - mutation from None to True
 - linkedList3.py: (l: 44, c: 35) - mutation from None to False
 - linkedList3.py: (l: 77, c: 15) - mutation from True to None
 - linkedList3.py: (l: 77, c: 15) - mutation from True to False