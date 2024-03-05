Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/stack3/stack3.py
 - Test commands: ['python', '-m', 'pytest', './MOSA-WHOLE_SUITE']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 24
 - Location sample coverage: 41.67 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.247681
 - Clean trial 2 run time: 0:00:00.211712
 - Mutation trials total run time: 0:00:08.407695

Overall mutation trial summary
==============================
 - DETECTED: 19
 - SURVIVED: 10
 - TIMEOUT: 1
 - TOTAL RUNS: 30
 - RUN DATETIME: 2023-03-06 14:09:30.601703


Mutations by result status
==========================


SURVIVED
--------
 - stack3.py: (l: 24, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - stack3.py: (l: 38, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - stack3.py: (l: 40, c: 8) - mutation from If_Statement to If_True
 - stack3.py: (l: 40, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.LtE'>
 - stack3.py: (l: 40, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.Eq'>
 - stack3.py: (l: 50, c: 12) - mutation from AugAssign_Sub to AugAssign_Div
 - stack3.py: (l: 50, c: 12) - mutation from AugAssign_Sub to AugAssign_Mult
 - stack3.py: (l: 50, c: 12) - mutation from AugAssign_Sub to AugAssign_Add
 - stack3.py: (l: 140, c: 0) - mutation from If_Statement to If_False
 - stack3.py: (l: 140, c: 0) - mutation from If_Statement to If_True


TIMEOUT
-------
 - stack3.py: (l: 24, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>


DETECTED
--------
 - stack3.py: (l: 27, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - stack3.py: (l: 27, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - stack3.py: (l: 27, c: 12) - mutation from AugAssign_Add to AugAssign_Sub
 - stack3.py: (l: 32, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - stack3.py: (l: 32, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - stack3.py: (l: 32, c: 12) - mutation from AugAssign_Add to AugAssign_Sub
 - stack3.py: (l: 38, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - stack3.py: (l: 38, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - stack3.py: (l: 38, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - stack3.py: (l: 38, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - stack3.py: (l: 39, c: 19) - mutation from None to True
 - stack3.py: (l: 39, c: 19) - mutation from None to False
 - stack3.py: (l: 40, c: 8) - mutation from If_Statement to If_False
 - stack3.py: (l: 40, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.Lt'>
 - stack3.py: (l: 40, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.Gt'>
 - stack3.py: (l: 40, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.NotEq'>
 - stack3.py: (l: 44, c: 12) - mutation from AugAssign_Sub to AugAssign_Add
 - stack3.py: (l: 44, c: 12) - mutation from AugAssign_Sub to AugAssign_Mult
 - stack3.py: (l: 44, c: 12) - mutation from AugAssign_Sub to AugAssign_Div