Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/linkedList3/linkedList3.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MOSA']
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
 - Clean trial 1 run time: 0:00:00.663142
 - Clean trial 2 run time: 0:00:01.291285
 - Mutation trials total run time: 0:00:52.896828

Overall mutation trial summary
==============================
 - DETECTED: 18
 - SURVIVED: 14
 - TIMEOUT: 1
 - TOTAL RUNS: 33
 - RUN DATETIME: 2023-03-05 18:47:30.664526


Mutations by result status
==========================


SURVIVED
--------
 - linkedList3.py: (l: 26, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - linkedList3.py: (l: 40, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - linkedList3.py: (l: 42, c: 8) - mutation from If_Statement to If_True
 - linkedList3.py: (l: 42, c: 8) - mutation from If_Statement to If_False
 - linkedList3.py: (l: 44, c: 35) - mutation from None to False
 - linkedList3.py: (l: 44, c: 35) - mutation from None to True
 - linkedList3.py: (l: 77, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - linkedList3.py: (l: 102, c: 0) - mutation from If_Statement to If_False
 - linkedList3.py: (l: 102, c: 0) - mutation from If_Statement to If_True
 - linkedList3.py: (l: 102, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - linkedList3.py: (l: 102, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - linkedList3.py: (l: 102, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - linkedList3.py: (l: 102, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - linkedList3.py: (l: 102, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>


TIMEOUT
-------
 - linkedList3.py: (l: 26, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>


DETECTED
--------
 - linkedList3.py: (l: 26, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - linkedList3.py: (l: 26, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - linkedList3.py: (l: 26, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - linkedList3.py: (l: 29, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - linkedList3.py: (l: 29, c: 12) - mutation from AugAssign_Add to AugAssign_Sub
 - linkedList3.py: (l: 29, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - linkedList3.py: (l: 40, c: 8) - mutation from If_Statement to If_False
 - linkedList3.py: (l: 40, c: 8) - mutation from If_Statement to If_True
 - linkedList3.py: (l: 40, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - linkedList3.py: (l: 40, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - linkedList3.py: (l: 40, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - linkedList3.py: (l: 40, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - linkedList3.py: (l: 77, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - linkedList3.py: (l: 77, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - linkedList3.py: (l: 77, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - linkedList3.py: (l: 77, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - linkedList3.py: (l: 77, c: 45) - mutation from False to None
 - linkedList3.py: (l: 77, c: 45) - mutation from False to True