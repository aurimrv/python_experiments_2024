Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/linkedList3/linkedList3.py
 - Test commands: ['python', '-m', 'pytest', './MIO-MOSA-WHOLE_SUITE']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 20
 - Location sample coverage: 50.00 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.258105
 - Clean trial 2 run time: 0:00:00.213639
 - Mutation trials total run time: 0:00:08.738775

Overall mutation trial summary
==============================
 - DETECTED: 15
 - TIMEOUT: 2
 - SURVIVED: 10
 - TOTAL RUNS: 27
 - RUN DATETIME: 2023-03-06 09:33:39.502290


Mutations by result status
==========================


SURVIVED
--------
 - linkedList3.py: (l: 21, c: 31) - mutation from None to False
 - linkedList3.py: (l: 21, c: 31) - mutation from None to True
 - linkedList3.py: (l: 52, c: 12) - mutation from AugAssign_Sub to AugAssign_Mult
 - linkedList3.py: (l: 52, c: 12) - mutation from AugAssign_Sub to AugAssign_Add
 - linkedList3.py: (l: 52, c: 12) - mutation from AugAssign_Sub to AugAssign_Div
 - linkedList3.py: (l: 102, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - linkedList3.py: (l: 102, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - linkedList3.py: (l: 102, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - linkedList3.py: (l: 102, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - linkedList3.py: (l: 102, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>


TIMEOUT
-------
 - linkedList3.py: (l: 26, c: 8) - mutation from If_Statement to If_False
 - linkedList3.py: (l: 26, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>


DETECTED
--------
 - linkedList3.py: (l: 12, c: 20) - mutation from None to False
 - linkedList3.py: (l: 12, c: 20) - mutation from None to True
 - linkedList3.py: (l: 17, c: 31) - mutation from None to False
 - linkedList3.py: (l: 17, c: 31) - mutation from None to True
 - linkedList3.py: (l: 26, c: 8) - mutation from If_Statement to If_True
 - linkedList3.py: (l: 29, c: 12) - mutation from AugAssign_Add to AugAssign_Sub
 - linkedList3.py: (l: 29, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - linkedList3.py: (l: 29, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - linkedList3.py: (l: 40, c: 8) - mutation from If_Statement to If_False
 - linkedList3.py: (l: 40, c: 8) - mutation from If_Statement to If_True
 - linkedList3.py: (l: 42, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.NotEq'>
 - linkedList3.py: (l: 42, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.Gt'>
 - linkedList3.py: (l: 42, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.Lt'>
 - linkedList3.py: (l: 42, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.LtE'>
 - linkedList3.py: (l: 42, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.Eq'>