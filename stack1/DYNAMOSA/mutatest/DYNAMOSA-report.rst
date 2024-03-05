Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/stack1/stack1.py
 - Test commands: ['python', '-m', 'pytest', '--tb=no', './DYNAMOSA']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: 2023

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 35
 - Location sample coverage: 28.57 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.212033
 - Clean trial 2 run time: 0:00:00.203318
 - Mutation trials total run time: 0:00:06.860081

Overall mutation trial summary
==============================
 - DETECTED: 14
 - SURVIVED: 19
 - TOTAL RUNS: 33
 - RUN DATETIME: 2023-07-14 00:10:15.771979


Mutations by result status
==========================


SURVIVED
--------
 - stack1.py: (l: 15, c: 23) - mutation from None to False
 - stack1.py: (l: 15, c: 23) - mutation from None to True
 - stack1.py: (l: 66, c: 19) - mutation from <class 'ast.NotEq'> to <class 'ast.Lt'>
 - stack1.py: (l: 66, c: 19) - mutation from <class 'ast.NotEq'> to <class 'ast.Gt'>
 - stack1.py: (l: 94, c: 29) - mutation from <class 'ast.Add'> to <class 'ast.Sub'>
 - stack1.py: (l: 94, c: 29) - mutation from <class 'ast.Add'> to <class 'ast.Mult'>
 - stack1.py: (l: 94, c: 29) - mutation from <class 'ast.Add'> to <class 'ast.Pow'>
 - stack1.py: (l: 94, c: 29) - mutation from <class 'ast.Add'> to <class 'ast.FloorDiv'>
 - stack1.py: (l: 94, c: 29) - mutation from <class 'ast.Add'> to <class 'ast.Mod'>
 - stack1.py: (l: 94, c: 29) - mutation from <class 'ast.Add'> to <class 'ast.Div'>
 - stack1.py: (l: 97, c: 29) - mutation from <class 'ast.Div'> to <class 'ast.Add'>
 - stack1.py: (l: 97, c: 29) - mutation from <class 'ast.Div'> to <class 'ast.Sub'>
 - stack1.py: (l: 97, c: 29) - mutation from <class 'ast.Div'> to <class 'ast.FloorDiv'>
 - stack1.py: (l: 97, c: 29) - mutation from <class 'ast.Div'> to <class 'ast.Pow'>
 - stack1.py: (l: 97, c: 29) - mutation from <class 'ast.Div'> to <class 'ast.Mod'>
 - stack1.py: (l: 97, c: 29) - mutation from <class 'ast.Div'> to <class 'ast.Mult'>
 - stack1.py: (l: 106, c: 8) - mutation from If_Statement to If_False
 - stack1.py: (l: 130, c: 7) - mutation from <class 'ast.Gt'> to <class 'ast.NotEq'>
 - stack1.py: (l: 130, c: 7) - mutation from <class 'ast.Gt'> to <class 'ast.Lt'>


DETECTED
--------
 - stack1.py: (l: 39, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - stack1.py: (l: 66, c: 19) - mutation from <class 'ast.NotEq'> to <class 'ast.Eq'>
 - stack1.py: (l: 66, c: 19) - mutation from <class 'ast.NotEq'> to <class 'ast.GtE'>
 - stack1.py: (l: 66, c: 19) - mutation from <class 'ast.NotEq'> to <class 'ast.LtE'>
 - stack1.py: (l: 67, c: 27) - mutation from False to True
 - stack1.py: (l: 67, c: 27) - mutation from False to None
 - stack1.py: (l: 70, c: 23) - mutation from False to True
 - stack1.py: (l: 70, c: 23) - mutation from False to None
 - stack1.py: (l: 76, c: 15) - mutation from True to False
 - stack1.py: (l: 76, c: 15) - mutation from True to None
 - stack1.py: (l: 106, c: 8) - mutation from If_Statement to If_True
 - stack1.py: (l: 130, c: 7) - mutation from <class 'ast.Gt'> to <class 'ast.LtE'>
 - stack1.py: (l: 130, c: 7) - mutation from <class 'ast.Gt'> to <class 'ast.Eq'>
 - stack1.py: (l: 130, c: 7) - mutation from <class 'ast.Gt'> to <class 'ast.GtE'>