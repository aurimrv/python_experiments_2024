Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/queue2/queue2.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MIO-WHOLE_SUITE']
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
 - Clean trial 1 run time: 0:00:00.399548
 - Clean trial 2 run time: 0:00:00.257925
 - Mutation trials total run time: 0:00:07.149829

Overall mutation trial summary
==============================
 - DETECTED: 13
 - SURVIVED: 9
 - TOTAL RUNS: 22
 - RUN DATETIME: 2023-03-12 11:34:45.867966


Mutations by result status
==========================


SURVIVED
--------
 - queue2.py: (l: 66, c: 8) - mutation from If_Statement to If_False
 - queue2.py: (l: 84, c: 20) - mutation from None to True
 - queue2.py: (l: 84, c: 20) - mutation from None to False
 - queue2.py: (l: 103, c: 24) - mutation from None to True
 - queue2.py: (l: 103, c: 24) - mutation from None to False
 - queue2.py: (l: 107, c: 8) - mutation from If_Statement to If_False
 - queue2.py: (l: 107, c: 8) - mutation from If_Statement to If_True
 - queue2.py: (l: 108, c: 24) - mutation from None to True
 - queue2.py: (l: 108, c: 24) - mutation from None to False


DETECTED
--------
 - queue2.py: (l: 21, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue2.py: (l: 21, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue2.py: (l: 21, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue2.py: (l: 21, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - queue2.py: (l: 21, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue2.py: (l: 27, c: 21) - mutation from None to True
 - queue2.py: (l: 27, c: 21) - mutation from None to False
 - queue2.py: (l: 46, c: 15) - mutation from None to False
 - queue2.py: (l: 46, c: 15) - mutation from None to True
 - queue2.py: (l: 66, c: 8) - mutation from If_Statement to If_True
 - queue2.py: (l: 91, c: 8) - mutation from If_Statement to If_True
 - queue2.py: (l: 91, c: 8) - mutation from If_Statement to If_False
 - queue2.py: (l: 103, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>