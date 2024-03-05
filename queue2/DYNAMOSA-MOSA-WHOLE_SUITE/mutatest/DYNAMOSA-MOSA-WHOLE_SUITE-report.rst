Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/queue2/queue2.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MOSA-WHOLE_SUITE']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 59
 - Location sample coverage: 16.95 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.473055
 - Clean trial 2 run time: 0:00:00.274126
 - Mutation trials total run time: 0:00:11.190307

Overall mutation trial summary
==============================
 - DETECTED: 20
 - SURVIVED: 4
 - TOTAL RUNS: 24
 - RUN DATETIME: 2023-03-12 12:48:02.382216


Mutations by result status
==========================


SURVIVED
--------
 - queue2.py: (l: 15, c: 29) - mutation from <class 'ast.NotEq'> to <class 'ast.Eq'>
 - queue2.py: (l: 16, c: 12) - mutation from If_Statement to If_True
 - queue2.py: (l: 120, c: 24) - mutation from None to True
 - queue2.py: (l: 120, c: 24) - mutation from None to False


DETECTED
--------
 - queue2.py: (l: 15, c: 29) - mutation from <class 'ast.NotEq'> to <class 'ast.Gt'>
 - queue2.py: (l: 15, c: 29) - mutation from <class 'ast.NotEq'> to <class 'ast.LtE'>
 - queue2.py: (l: 15, c: 29) - mutation from <class 'ast.NotEq'> to <class 'ast.GtE'>
 - queue2.py: (l: 15, c: 29) - mutation from <class 'ast.NotEq'> to <class 'ast.Lt'>
 - queue2.py: (l: 16, c: 12) - mutation from If_Statement to If_False
 - queue2.py: (l: 49, c: 27) - mutation from None to False
 - queue2.py: (l: 49, c: 27) - mutation from None to True
 - queue2.py: (l: 55, c: 15) - mutation from False to True
 - queue2.py: (l: 55, c: 15) - mutation from False to None
 - queue2.py: (l: 66, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - queue2.py: (l: 75, c: 19) - mutation from None to False
 - queue2.py: (l: 75, c: 19) - mutation from None to True
 - queue2.py: (l: 99, c: 28) - mutation from None to True
 - queue2.py: (l: 99, c: 28) - mutation from None to False
 - queue2.py: (l: 120, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - queue2.py: (l: 129, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Eq'>
 - queue2.py: (l: 129, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.LtE'>
 - queue2.py: (l: 129, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Lt'>
 - queue2.py: (l: 129, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.GtE'>
 - queue2.py: (l: 129, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Gt'>