Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/stack3/stack3.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MOSA-WHOLE_SUITE']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 23
 - Location sample coverage: 43.48 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.290339
 - Clean trial 2 run time: 0:00:00.241762
 - Mutation trials total run time: 0:00:09.006849

Overall mutation trial summary
==============================
 - DETECTED: 23
 - TIMEOUT: 1
 - SURVIVED: 3
 - TOTAL RUNS: 27
 - RUN DATETIME: 2023-03-12 12:49:01.061287


Mutations by result status
==========================


SURVIVED
--------
 - stack3.py: (l: 40, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.Eq'>
 - stack3.py: (l: 40, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.LtE'>
 - stack3.py: (l: 75, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>


TIMEOUT
-------
 - stack3.py: (l: 24, c: 8) - mutation from If_Statement to If_False


DETECTED
--------
 - stack3.py: (l: 15, c: 31) - mutation from None to True
 - stack3.py: (l: 15, c: 31) - mutation from None to False
 - stack3.py: (l: 27, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - stack3.py: (l: 27, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - stack3.py: (l: 27, c: 12) - mutation from AugAssign_Add to AugAssign_Sub
 - stack3.py: (l: 39, c: 19) - mutation from None to False
 - stack3.py: (l: 39, c: 19) - mutation from None to True
 - stack3.py: (l: 40, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.Lt'>
 - stack3.py: (l: 40, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.Gt'>
 - stack3.py: (l: 40, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.NotEq'>
 - stack3.py: (l: 42, c: 35) - mutation from None to False
 - stack3.py: (l: 42, c: 35) - mutation from None to True
 - stack3.py: (l: 44, c: 12) - mutation from AugAssign_Sub to AugAssign_Div
 - stack3.py: (l: 44, c: 12) - mutation from AugAssign_Sub to AugAssign_Add
 - stack3.py: (l: 44, c: 12) - mutation from AugAssign_Sub to AugAssign_Mult
 - stack3.py: (l: 75, c: 15) - mutation from True to False
 - stack3.py: (l: 75, c: 15) - mutation from True to None
 - stack3.py: (l: 75, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - stack3.py: (l: 75, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - stack3.py: (l: 75, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - stack3.py: (l: 75, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - stack3.py: (l: 75, c: 45) - mutation from False to None
 - stack3.py: (l: 75, c: 45) - mutation from False to True