Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/queue5/queue5.py
 - Test commands: ['python', '-m', 'pytest', './MIO-MOSA-WHOLE_SUITE']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 20
 - Location sample coverage: 50.00 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.224112
 - Clean trial 2 run time: 0:00:00.201192
 - Mutation trials total run time: 0:00:04.637187

Overall mutation trial summary
==============================
 - DETECTED: 14
 - SURVIVED: 6
 - TOTAL RUNS: 20
 - RUN DATETIME: 2023-03-06 09:34:37.716492


Mutations by result status
==========================


SURVIVED
--------
 - queue5.py: (l: 5, c: 20) - mutation from None to False
 - queue5.py: (l: 5, c: 20) - mutation from None to True
 - queue5.py: (l: 17, c: 11) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - queue5.py: (l: 26, c: 11) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - queue5.py: (l: 27, c: 19) - mutation from None to True
 - queue5.py: (l: 27, c: 19) - mutation from None to False


DETECTED
--------
 - queue5.py: (l: 11, c: 20) - mutation from None to False
 - queue5.py: (l: 11, c: 20) - mutation from None to True
 - queue5.py: (l: 12, c: 20) - mutation from None to True
 - queue5.py: (l: 12, c: 20) - mutation from None to False
 - queue5.py: (l: 17, c: 8) - mutation from If_Statement to If_True
 - queue5.py: (l: 17, c: 8) - mutation from If_Statement to If_False
 - queue5.py: (l: 17, c: 46) - mutation from None to True
 - queue5.py: (l: 17, c: 46) - mutation from None to False
 - queue5.py: (l: 26, c: 33) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - queue5.py: (l: 30, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue5.py: (l: 30, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue5.py: (l: 30, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue5.py: (l: 30, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue5.py: (l: 30, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>