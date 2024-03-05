Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/stack1/stack1.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MIO']
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
 - Clean trial 1 run time: 0:00:01.204213
 - Clean trial 2 run time: 0:00:01.155070
 - Mutation trials total run time: 0:00:29.442300

Overall mutation trial summary
==============================
 - DETECTED: 13
 - SURVIVED: 12
 - TOTAL RUNS: 25
 - RUN DATETIME: 2023-03-05 12:27:11.731870


Mutations by result status
==========================


SURVIVED
--------
 - stack1.py: (l: 15, c: 8) - mutation from If_Statement to If_False
 - stack1.py: (l: 15, c: 8) - mutation from If_Statement to If_True
 - stack1.py: (l: 15, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - stack1.py: (l: 98, c: 29) - mutation from <class 'ast.Mod'> to <class 'ast.FloorDiv'>
 - stack1.py: (l: 98, c: 29) - mutation from <class 'ast.Mod'> to <class 'ast.Sub'>
 - stack1.py: (l: 98, c: 29) - mutation from <class 'ast.Mod'> to <class 'ast.Pow'>
 - stack1.py: (l: 98, c: 29) - mutation from <class 'ast.Mod'> to <class 'ast.Mult'>
 - stack1.py: (l: 98, c: 29) - mutation from <class 'ast.Mod'> to <class 'ast.Div'>
 - stack1.py: (l: 98, c: 29) - mutation from <class 'ast.Mod'> to <class 'ast.Add'>
 - stack1.py: (l: 130, c: 4) - mutation from If_Statement to If_False
 - stack1.py: (l: 130, c: 7) - mutation from <class 'ast.Gt'> to <class 'ast.Lt'>
 - stack1.py: (l: 130, c: 7) - mutation from <class 'ast.Gt'> to <class 'ast.NotEq'>


DETECTED
--------
 - stack1.py: (l: 39, c: 8) - mutation from If_Statement to If_False
 - stack1.py: (l: 39, c: 8) - mutation from If_Statement to If_True
 - stack1.py: (l: 57, c: 8) - mutation from If_Statement to If_False
 - stack1.py: (l: 57, c: 8) - mutation from If_Statement to If_True
 - stack1.py: (l: 66, c: 16) - mutation from If_Statement to If_False
 - stack1.py: (l: 66, c: 16) - mutation from If_Statement to If_True
 - stack1.py: (l: 72, c: 4) - mutation from If_Statement to If_False
 - stack1.py: (l: 72, c: 4) - mutation from If_Statement to If_True
 - stack1.py: (l: 106, c: 11) - mutation from <class 'ast.In'> to <class 'ast.NotIn'>
 - stack1.py: (l: 130, c: 4) - mutation from If_Statement to If_True
 - stack1.py: (l: 130, c: 7) - mutation from <class 'ast.Gt'> to <class 'ast.Eq'>
 - stack1.py: (l: 130, c: 7) - mutation from <class 'ast.Gt'> to <class 'ast.GtE'>
 - stack1.py: (l: 130, c: 7) - mutation from <class 'ast.Gt'> to <class 'ast.LtE'>