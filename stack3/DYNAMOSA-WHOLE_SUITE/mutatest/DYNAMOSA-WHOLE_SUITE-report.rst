Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/stack3/stack3.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-WHOLE_SUITE']
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
 - Clean trial 1 run time: 0:00:00.273821
 - Clean trial 2 run time: 0:00:00.288969
 - Mutation trials total run time: 0:00:07.800472

Overall mutation trial summary
==============================
 - DETECTED: 22
 - SURVIVED: 7
 - TOTAL RUNS: 29
 - RUN DATETIME: 2023-03-05 22:22:10.449184


Mutations by result status
==========================


SURVIVED
--------
 - stack3.py: (l: 50, c: 12) - mutation from AugAssign_Sub to AugAssign_Add
 - stack3.py: (l: 50, c: 12) - mutation from AugAssign_Sub to AugAssign_Mult
 - stack3.py: (l: 50, c: 12) - mutation from AugAssign_Sub to AugAssign_Div
 - stack3.py: (l: 75, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - stack3.py: (l: 125, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - stack3.py: (l: 140, c: 0) - mutation from If_Statement to If_True
 - stack3.py: (l: 140, c: 0) - mutation from If_Statement to If_False


DETECTED
--------
 - stack3.py: (l: 27, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - stack3.py: (l: 27, c: 12) - mutation from AugAssign_Add to AugAssign_Sub
 - stack3.py: (l: 27, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - stack3.py: (l: 38, c: 8) - mutation from If_Statement to If_False
 - stack3.py: (l: 38, c: 8) - mutation from If_Statement to If_True
 - stack3.py: (l: 42, c: 35) - mutation from None to False
 - stack3.py: (l: 42, c: 35) - mutation from None to True
 - stack3.py: (l: 44, c: 12) - mutation from AugAssign_Sub to AugAssign_Add
 - stack3.py: (l: 44, c: 12) - mutation from AugAssign_Sub to AugAssign_Mult
 - stack3.py: (l: 44, c: 12) - mutation from AugAssign_Sub to AugAssign_Div
 - stack3.py: (l: 75, c: 15) - mutation from True to False
 - stack3.py: (l: 75, c: 15) - mutation from True to None
 - stack3.py: (l: 75, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - stack3.py: (l: 75, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - stack3.py: (l: 75, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - stack3.py: (l: 75, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - stack3.py: (l: 125, c: 15) - mutation from True to None
 - stack3.py: (l: 125, c: 15) - mutation from True to False
 - stack3.py: (l: 125, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - stack3.py: (l: 125, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - stack3.py: (l: 125, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - stack3.py: (l: 125, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>