Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/linkedList5/linkedList5.py
 - Test commands: ['python', '-m', 'pytest', '--tb=no', './MOSA']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: 2023

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 55
 - Location sample coverage: 18.18 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.421528
 - Clean trial 2 run time: 0:00:00.218453
 - Mutation trials total run time: 0:00:03.875487

Overall mutation trial summary
==============================
 - DETECTED: 11
 - SURVIVED: 6
 - TOTAL RUNS: 17
 - RUN DATETIME: 2023-07-14 00:14:03.431659


Mutations by result status
==========================


SURVIVED
--------
 - linkedList5.py: (l: 45, c: 19) - mutation from None to False
 - linkedList5.py: (l: 45, c: 19) - mutation from None to True
 - linkedList5.py: (l: 46, c: 19) - mutation from None to False
 - linkedList5.py: (l: 46, c: 19) - mutation from None to True
 - linkedList5.py: (l: 49, c: 12) - mutation from If_Statement to If_True
 - linkedList5.py: (l: 72, c: 8) - mutation from If_Statement to If_False


DETECTED
--------
 - linkedList5.py: (l: 25, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - linkedList5.py: (l: 49, c: 12) - mutation from If_Statement to If_False
 - linkedList5.py: (l: 55, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - linkedList5.py: (l: 64, c: 31) - mutation from None to False
 - linkedList5.py: (l: 64, c: 31) - mutation from None to True
 - linkedList5.py: (l: 72, c: 8) - mutation from If_Statement to If_True
 - linkedList5.py: (l: 72, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - linkedList5.py: (l: 74, c: 24) - mutation from None to True
 - linkedList5.py: (l: 74, c: 24) - mutation from None to False
 - linkedList5.py: (l: 95, c: 31) - mutation from None to False
 - linkedList5.py: (l: 95, c: 31) - mutation from None to True