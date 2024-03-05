Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/stack4/stack4.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MIO-WHOLE_SUITE']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 22
 - Location sample coverage: 45.45 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.282439
 - Clean trial 2 run time: 0:00:00.223006
 - Mutation trials total run time: 0:00:06.257889

Overall mutation trial summary
==============================
 - SURVIVED: 9
 - DETECTED: 14
 - TOTAL RUNS: 23
 - RUN DATETIME: 2023-03-12 11:35:47.156004


Mutations by result status
==========================


SURVIVED
--------
 - stack4.py: (l: 9, c: 39) - mutation from None to False
 - stack4.py: (l: 9, c: 39) - mutation from None to True
 - stack4.py: (l: 29, c: 28) - mutation from None to False
 - stack4.py: (l: 72, c: 12) - mutation from AugAssign_Sub to AugAssign_Mult
 - stack4.py: (l: 72, c: 12) - mutation from AugAssign_Sub to AugAssign_Div
 - stack4.py: (l: 72, c: 12) - mutation from AugAssign_Sub to AugAssign_Add
 - stack4.py: (l: 76, c: 16) - mutation from AugAssign_Sub to AugAssign_Div
 - stack4.py: (l: 76, c: 16) - mutation from AugAssign_Sub to AugAssign_Add
 - stack4.py: (l: 76, c: 16) - mutation from AugAssign_Sub to AugAssign_Mult


DETECTED
--------
 - stack4.py: (l: 29, c: 28) - mutation from None to True
 - stack4.py: (l: 32, c: 20) - mutation from None to True
 - stack4.py: (l: 32, c: 20) - mutation from None to False
 - stack4.py: (l: 48, c: 8) - mutation from If_Statement to If_False
 - stack4.py: (l: 48, c: 8) - mutation from If_Statement to If_True
 - stack4.py: (l: 63, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - stack4.py: (l: 63, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - stack4.py: (l: 63, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - stack4.py: (l: 63, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - stack4.py: (l: 63, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - stack4.py: (l: 70, c: 8) - mutation from If_Statement to If_True
 - stack4.py: (l: 70, c: 8) - mutation from If_Statement to If_False
 - stack4.py: (l: 70, c: 20) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - stack4.py: (l: 74, c: 16) - mutation from <class 'ast.And'> to <class 'ast.Or'>