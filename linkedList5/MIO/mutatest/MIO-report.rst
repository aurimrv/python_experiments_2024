Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/linkedList5/linkedList5.py
 - Test commands: ['python', '-m', 'pytest', '--tb=no', './MIO']
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
 - Clean trial 1 run time: 0:00:00.365581
 - Clean trial 2 run time: 0:00:00.225706
 - Mutation trials total run time: 0:00:03.953392

Overall mutation trial summary
==============================
 - DETECTED: 12
 - SURVIVED: 5
 - TOTAL RUNS: 17
 - RUN DATETIME: 2023-07-14 00:11:46.011850


Mutations by result status
==========================


SURVIVED
--------
 - linkedList5.py: (l: 45, c: 19) - mutation from None to False
 - linkedList5.py: (l: 45, c: 19) - mutation from None to True
 - linkedList5.py: (l: 46, c: 19) - mutation from None to False
 - linkedList5.py: (l: 46, c: 19) - mutation from None to True
 - linkedList5.py: (l: 72, c: 8) - mutation from If_Statement to If_False


DETECTED
--------
 - linkedList5.py: (l: 25, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - linkedList5.py: (l: 49, c: 12) - mutation from If_Statement to If_True
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