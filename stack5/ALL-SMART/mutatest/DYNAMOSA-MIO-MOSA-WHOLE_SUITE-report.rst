Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/stack5/stack5.py
 - Test commands: ['python', '-m', 'pytest', '--tb=no', './DYNAMOSA-MIO-MOSA-WHOLE_SUITE']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: 2023

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 11
 - Location sample coverage: 90.91 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.219068
 - Clean trial 2 run time: 0:00:00.210738
 - Mutation trials total run time: 0:00:03.629627

Overall mutation trial summary
==============================
 - DETECTED: 10
 - SURVIVED: 7
 - TOTAL RUNS: 17
 - RUN DATETIME: 2023-07-14 00:20:10.495851


Mutations by result status
==========================


SURVIVED
--------
 - stack5.py: (l: 11, c: 19) - mutation from None to False
 - stack5.py: (l: 11, c: 19) - mutation from None to True
 - stack5.py: (l: 17, c: 58) - mutation from None to False
 - stack5.py: (l: 17, c: 58) - mutation from None to True
 - stack5.py: (l: 20, c: 15) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - stack5.py: (l: 24, c: 34) - mutation from None to False
 - stack5.py: (l: 24, c: 34) - mutation from None to True


DETECTED
--------
 - stack5.py: (l: 3, c: 27) - mutation from None to False
 - stack5.py: (l: 3, c: 27) - mutation from None to True
 - stack5.py: (l: 10, c: 8) - mutation from If_Statement to If_True
 - stack5.py: (l: 10, c: 8) - mutation from If_Statement to If_False
 - stack5.py: (l: 10, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - stack5.py: (l: 10, c: 23) - mutation from None to True
 - stack5.py: (l: 10, c: 23) - mutation from None to False
 - stack5.py: (l: 17, c: 32) - mutation from <class 'ast.IsNot'> to <class 'ast.Is'>
 - stack5.py: (l: 17, c: 48) - mutation from None to True
 - stack5.py: (l: 17, c: 48) - mutation from None to False