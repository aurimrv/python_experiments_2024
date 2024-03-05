Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/stack3/stack3.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MIO']
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
 - Clean trial 1 run time: 0:00:01.205537
 - Clean trial 2 run time: 0:00:01.097864
 - Mutation trials total run time: 0:00:40.535405

Overall mutation trial summary
==============================
 - DETECTED: 17
 - SURVIVED: 15
 - TOTAL RUNS: 32
 - RUN DATETIME: 2023-03-05 12:28:14.899106


Mutations by result status
==========================


SURVIVED
--------
 - stack3.py: (l: 38, c: 8) - mutation from If_Statement to If_False
 - stack3.py: (l: 40, c: 8) - mutation from If_Statement to If_True
 - stack3.py: (l: 40, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.Eq'>
 - stack3.py: (l: 40, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.LtE'>
 - stack3.py: (l: 75, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - stack3.py: (l: 103, c: 32) - mutation from None to True
 - stack3.py: (l: 103, c: 32) - mutation from None to False
 - stack3.py: (l: 125, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - stack3.py: (l: 140, c: 0) - mutation from If_Statement to If_False
 - stack3.py: (l: 140, c: 0) - mutation from If_Statement to If_True
 - stack3.py: (l: 140, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - stack3.py: (l: 140, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - stack3.py: (l: 140, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - stack3.py: (l: 140, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - stack3.py: (l: 140, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>


DETECTED
--------
 - stack3.py: (l: 38, c: 8) - mutation from If_Statement to If_True
 - stack3.py: (l: 40, c: 8) - mutation from If_Statement to If_False
 - stack3.py: (l: 40, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.Gt'>
 - stack3.py: (l: 40, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.NotEq'>
 - stack3.py: (l: 40, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.Lt'>
 - stack3.py: (l: 42, c: 35) - mutation from None to False
 - stack3.py: (l: 42, c: 35) - mutation from None to True
 - stack3.py: (l: 75, c: 15) - mutation from True to None
 - stack3.py: (l: 75, c: 15) - mutation from True to False
 - stack3.py: (l: 75, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - stack3.py: (l: 75, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - stack3.py: (l: 75, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - stack3.py: (l: 75, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - stack3.py: (l: 125, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - stack3.py: (l: 125, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - stack3.py: (l: 125, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - stack3.py: (l: 125, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>