Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/stack1/stack1.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MIO-WHOLE_SUITE']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 35
 - Location sample coverage: 28.57 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.257304
 - Clean trial 2 run time: 0:00:00.226266
 - Mutation trials total run time: 0:00:06.704020

Overall mutation trial summary
==============================
 - SURVIVED: 12
 - DETECTED: 14
 - TOTAL RUNS: 26
 - RUN DATETIME: 2023-03-12 11:35:25.504772


Mutations by result status
==========================


SURVIVED
--------
 - stack1.py: (l: 15, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - stack1.py: (l: 15, c: 23) - mutation from None to False
 - stack1.py: (l: 15, c: 23) - mutation from None to True
 - stack1.py: (l: 48, c: 20) - mutation from None to True
 - stack1.py: (l: 48, c: 20) - mutation from None to False
 - stack1.py: (l: 72, c: 7) - mutation from <class 'ast.NotEq'> to <class 'ast.Gt'>
 - stack1.py: (l: 96, c: 29) - mutation from <class 'ast.Mult'> to <class 'ast.Mod'>
 - stack1.py: (l: 96, c: 29) - mutation from <class 'ast.Mult'> to <class 'ast.Pow'>
 - stack1.py: (l: 96, c: 29) - mutation from <class 'ast.Mult'> to <class 'ast.Add'>
 - stack1.py: (l: 96, c: 29) - mutation from <class 'ast.Mult'> to <class 'ast.Sub'>
 - stack1.py: (l: 96, c: 29) - mutation from <class 'ast.Mult'> to <class 'ast.Div'>
 - stack1.py: (l: 96, c: 29) - mutation from <class 'ast.Mult'> to <class 'ast.FloorDiv'>


DETECTED
--------
 - stack1.py: (l: 26, c: 8) - mutation from AugAssign_Add to AugAssign_Mult
 - stack1.py: (l: 26, c: 8) - mutation from AugAssign_Add to AugAssign_Sub
 - stack1.py: (l: 26, c: 8) - mutation from AugAssign_Add to AugAssign_Div
 - stack1.py: (l: 29, c: 23) - mutation from None to True
 - stack1.py: (l: 29, c: 23) - mutation from None to False
 - stack1.py: (l: 57, c: 8) - mutation from If_Statement to If_False
 - stack1.py: (l: 57, c: 8) - mutation from If_Statement to If_True
 - stack1.py: (l: 61, c: 11) - mutation from <class 'ast.In'> to <class 'ast.NotIn'>
 - stack1.py: (l: 72, c: 4) - mutation from If_Statement to If_False
 - stack1.py: (l: 72, c: 4) - mutation from If_Statement to If_True
 - stack1.py: (l: 72, c: 7) - mutation from <class 'ast.NotEq'> to <class 'ast.LtE'>
 - stack1.py: (l: 72, c: 7) - mutation from <class 'ast.NotEq'> to <class 'ast.Lt'>
 - stack1.py: (l: 72, c: 7) - mutation from <class 'ast.NotEq'> to <class 'ast.GtE'>
 - stack1.py: (l: 72, c: 7) - mutation from <class 'ast.NotEq'> to <class 'ast.Eq'>