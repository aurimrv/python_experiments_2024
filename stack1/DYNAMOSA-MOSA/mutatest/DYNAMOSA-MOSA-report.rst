Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/stack1/stack1.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MOSA']
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
 - Clean trial 1 run time: 0:00:01.221640
 - Clean trial 2 run time: 0:00:01.806377
 - Mutation trials total run time: 0:01:00.264862

Overall mutation trial summary
==============================
 - DETECTED: 17
 - SURVIVED: 16
 - TOTAL RUNS: 33
 - RUN DATETIME: 2023-03-05 18:57:54.555351


Mutations by result status
==========================


SURVIVED
--------
 - stack1.py: (l: 66, c: 19) - mutation from <class 'ast.NotEq'> to <class 'ast.Lt'>
 - stack1.py: (l: 66, c: 19) - mutation from <class 'ast.NotEq'> to <class 'ast.Gt'>
 - stack1.py: (l: 95, c: 29) - mutation from <class 'ast.Sub'> to <class 'ast.Div'>
 - stack1.py: (l: 95, c: 29) - mutation from <class 'ast.Sub'> to <class 'ast.FloorDiv'>
 - stack1.py: (l: 95, c: 29) - mutation from <class 'ast.Sub'> to <class 'ast.Mod'>
 - stack1.py: (l: 95, c: 29) - mutation from <class 'ast.Sub'> to <class 'ast.Add'>
 - stack1.py: (l: 95, c: 29) - mutation from <class 'ast.Sub'> to <class 'ast.Mult'>
 - stack1.py: (l: 95, c: 29) - mutation from <class 'ast.Sub'> to <class 'ast.Pow'>
 - stack1.py: (l: 98, c: 29) - mutation from <class 'ast.Mod'> to <class 'ast.Mult'>
 - stack1.py: (l: 98, c: 29) - mutation from <class 'ast.Mod'> to <class 'ast.FloorDiv'>
 - stack1.py: (l: 98, c: 29) - mutation from <class 'ast.Mod'> to <class 'ast.Pow'>
 - stack1.py: (l: 98, c: 29) - mutation from <class 'ast.Mod'> to <class 'ast.Div'>
 - stack1.py: (l: 98, c: 29) - mutation from <class 'ast.Mod'> to <class 'ast.Add'>
 - stack1.py: (l: 98, c: 29) - mutation from <class 'ast.Mod'> to <class 'ast.Sub'>
 - stack1.py: (l: 130, c: 7) - mutation from <class 'ast.Gt'> to <class 'ast.NotEq'>
 - stack1.py: (l: 130, c: 7) - mutation from <class 'ast.Gt'> to <class 'ast.Lt'>


DETECTED
--------
 - stack1.py: (l: 29, c: 8) - mutation from If_Statement to If_False
 - stack1.py: (l: 29, c: 8) - mutation from If_Statement to If_True
 - stack1.py: (l: 29, c: 23) - mutation from None to True
 - stack1.py: (l: 29, c: 23) - mutation from None to False
 - stack1.py: (l: 39, c: 23) - mutation from None to False
 - stack1.py: (l: 39, c: 23) - mutation from None to True
 - stack1.py: (l: 61, c: 11) - mutation from <class 'ast.In'> to <class 'ast.NotIn'>
 - stack1.py: (l: 66, c: 19) - mutation from <class 'ast.NotEq'> to <class 'ast.LtE'>
 - stack1.py: (l: 66, c: 19) - mutation from <class 'ast.NotEq'> to <class 'ast.Eq'>
 - stack1.py: (l: 66, c: 19) - mutation from <class 'ast.NotEq'> to <class 'ast.GtE'>
 - stack1.py: (l: 67, c: 27) - mutation from False to None
 - stack1.py: (l: 67, c: 27) - mutation from False to True
 - stack1.py: (l: 72, c: 4) - mutation from If_Statement to If_True
 - stack1.py: (l: 72, c: 4) - mutation from If_Statement to If_False
 - stack1.py: (l: 130, c: 7) - mutation from <class 'ast.Gt'> to <class 'ast.Eq'>
 - stack1.py: (l: 130, c: 7) - mutation from <class 'ast.Gt'> to <class 'ast.LtE'>
 - stack1.py: (l: 130, c: 7) - mutation from <class 'ast.Gt'> to <class 'ast.GtE'>