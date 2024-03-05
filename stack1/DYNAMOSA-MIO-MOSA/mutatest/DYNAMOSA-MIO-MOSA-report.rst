Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/stack1/stack1.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MIO-MOSA']
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
 - Clean trial 1 run time: 0:00:00.263794
 - Clean trial 2 run time: 0:00:00.227421
 - Mutation trials total run time: 0:00:06.259239

Overall mutation trial summary
==============================
 - DETECTED: 14
 - SURVIVED: 10
 - TOTAL RUNS: 24
 - RUN DATETIME: 2023-03-06 00:07:21.527717


Mutations by result status
==========================


SURVIVED
--------
 - stack1.py: (l: 15, c: 8) - mutation from If_Statement to If_False
 - stack1.py: (l: 15, c: 8) - mutation from If_Statement to If_True
 - stack1.py: (l: 96, c: 29) - mutation from <class 'ast.Mult'> to <class 'ast.FloorDiv'>
 - stack1.py: (l: 96, c: 29) - mutation from <class 'ast.Mult'> to <class 'ast.Add'>
 - stack1.py: (l: 96, c: 29) - mutation from <class 'ast.Mult'> to <class 'ast.Mod'>
 - stack1.py: (l: 96, c: 29) - mutation from <class 'ast.Mult'> to <class 'ast.Pow'>
 - stack1.py: (l: 96, c: 29) - mutation from <class 'ast.Mult'> to <class 'ast.Sub'>
 - stack1.py: (l: 96, c: 29) - mutation from <class 'ast.Mult'> to <class 'ast.Div'>
 - stack1.py: (l: 130, c: 7) - mutation from <class 'ast.Gt'> to <class 'ast.Lt'>
 - stack1.py: (l: 130, c: 7) - mutation from <class 'ast.Gt'> to <class 'ast.NotEq'>


DETECTED
--------
 - stack1.py: (l: 29, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - stack1.py: (l: 57, c: 8) - mutation from If_Statement to If_False
 - stack1.py: (l: 57, c: 8) - mutation from If_Statement to If_True
 - stack1.py: (l: 61, c: 8) - mutation from If_Statement to If_False
 - stack1.py: (l: 61, c: 8) - mutation from If_Statement to If_True
 - stack1.py: (l: 61, c: 11) - mutation from <class 'ast.In'> to <class 'ast.NotIn'>
 - stack1.py: (l: 66, c: 16) - mutation from If_Statement to If_False
 - stack1.py: (l: 66, c: 16) - mutation from If_Statement to If_True
 - stack1.py: (l: 67, c: 27) - mutation from False to None
 - stack1.py: (l: 67, c: 27) - mutation from False to True
 - stack1.py: (l: 106, c: 11) - mutation from <class 'ast.In'> to <class 'ast.NotIn'>
 - stack1.py: (l: 130, c: 7) - mutation from <class 'ast.Gt'> to <class 'ast.GtE'>
 - stack1.py: (l: 130, c: 7) - mutation from <class 'ast.Gt'> to <class 'ast.Eq'>
 - stack1.py: (l: 130, c: 7) - mutation from <class 'ast.Gt'> to <class 'ast.LtE'>