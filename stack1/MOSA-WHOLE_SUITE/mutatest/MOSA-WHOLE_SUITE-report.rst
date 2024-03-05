Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/stack1/stack1.py
 - Test commands: ['python', '-m', 'pytest', './MOSA-WHOLE_SUITE']
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
 - Clean trial 1 run time: 0:00:00.252524
 - Clean trial 2 run time: 0:00:00.216198
 - Mutation trials total run time: 0:00:05.440562

Overall mutation trial summary
==============================
 - DETECTED: 18
 - SURVIVED: 4
 - TOTAL RUNS: 22
 - RUN DATETIME: 2023-03-06 14:09:18.043162


Mutations by result status
==========================


SURVIVED
--------
 - stack1.py: (l: 15, c: 8) - mutation from If_Statement to If_False
 - stack1.py: (l: 15, c: 8) - mutation from If_Statement to If_True
 - stack1.py: (l: 66, c: 19) - mutation from <class 'ast.NotEq'> to <class 'ast.Gt'>
 - stack1.py: (l: 130, c: 4) - mutation from If_Statement to If_False


DETECTED
--------
 - stack1.py: (l: 29, c: 8) - mutation from If_Statement to If_False
 - stack1.py: (l: 29, c: 8) - mutation from If_Statement to If_True
 - stack1.py: (l: 29, c: 23) - mutation from None to True
 - stack1.py: (l: 29, c: 23) - mutation from None to False
 - stack1.py: (l: 39, c: 8) - mutation from If_Statement to If_False
 - stack1.py: (l: 39, c: 8) - mutation from If_Statement to If_True
 - stack1.py: (l: 48, c: 20) - mutation from None to True
 - stack1.py: (l: 48, c: 20) - mutation from None to False
 - stack1.py: (l: 61, c: 11) - mutation from <class 'ast.In'> to <class 'ast.NotIn'>
 - stack1.py: (l: 66, c: 19) - mutation from <class 'ast.NotEq'> to <class 'ast.Eq'>
 - stack1.py: (l: 66, c: 19) - mutation from <class 'ast.NotEq'> to <class 'ast.GtE'>
 - stack1.py: (l: 66, c: 19) - mutation from <class 'ast.NotEq'> to <class 'ast.Lt'>
 - stack1.py: (l: 66, c: 19) - mutation from <class 'ast.NotEq'> to <class 'ast.LtE'>
 - stack1.py: (l: 70, c: 23) - mutation from False to None
 - stack1.py: (l: 70, c: 23) - mutation from False to True
 - stack1.py: (l: 72, c: 4) - mutation from If_Statement to If_False
 - stack1.py: (l: 72, c: 4) - mutation from If_Statement to If_True
 - stack1.py: (l: 130, c: 4) - mutation from If_Statement to If_True