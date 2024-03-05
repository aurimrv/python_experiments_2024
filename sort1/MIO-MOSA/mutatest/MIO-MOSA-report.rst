Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/sort1/sort1.py
 - Test commands: ['python', '-m', 'pytest', './MIO-MOSA']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 32
 - Location sample coverage: 31.25 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.206065
 - Clean trial 2 run time: 0:00:00.212212
 - Mutation trials total run time: 0:00:07.256350

Overall mutation trial summary
==============================
 - TIMEOUT: 1
 - DETECTED: 9
 - SURVIVED: 19
 - TOTAL RUNS: 29
 - RUN DATETIME: 2023-03-06 11:46:01.439565


Mutations by result status
==========================


SURVIVED
--------
 - sort1.py: (l: 17, c: 16) - mutation from If_Statement to If_True
 - sort1.py: (l: 17, c: 16) - mutation from If_Statement to If_False
 - sort1.py: (l: 17, c: 19) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - sort1.py: (l: 17, c: 19) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - sort1.py: (l: 17, c: 19) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - sort1.py: (l: 17, c: 19) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - sort1.py: (l: 17, c: 19) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - sort1.py: (l: 31, c: 18) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - sort1.py: (l: 31, c: 30) - mutation from <class 'ast.Gt'> to <class 'ast.Lt'>
 - sort1.py: (l: 31, c: 30) - mutation from <class 'ast.Gt'> to <class 'ast.GtE'>
 - sort1.py: (l: 31, c: 30) - mutation from <class 'ast.Gt'> to <class 'ast.Eq'>
 - sort1.py: (l: 31, c: 30) - mutation from <class 'ast.Gt'> to <class 'ast.LtE'>
 - sort1.py: (l: 31, c: 30) - mutation from <class 'ast.Gt'> to <class 'ast.NotEq'>
 - sort1.py: (l: 47, c: 8) - mutation from If_Statement to If_True
 - sort1.py: (l: 62, c: 14) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - sort1.py: (l: 62, c: 14) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - sort1.py: (l: 64, c: 12) - mutation from If_Statement to If_False
 - sort1.py: (l: 64, c: 12) - mutation from If_Statement to If_True
 - sort1.py: (l: 82, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>


TIMEOUT
-------
 - sort1.py: (l: 34, c: 22) - mutation from <class 'ast.Sub'> to <class 'ast.Pow'>


DETECTED
--------
 - sort1.py: (l: 47, c: 8) - mutation from If_Statement to If_False
 - sort1.py: (l: 62, c: 14) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - sort1.py: (l: 62, c: 14) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - sort1.py: (l: 62, c: 14) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - sort1.py: (l: 62, c: 14) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - sort1.py: (l: 82, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - sort1.py: (l: 82, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - sort1.py: (l: 82, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - sort1.py: (l: 82, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>