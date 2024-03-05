Mutatest diagnostic summary
===========================
 - Source location: /home/lucca/desktop/ic/experimento/testes/python_experiments/stack5/stack5.py
 - Test commands: ['python', '-m', 'pytest', '--tb=no', './ALL-SMART-GPT-MUTPY']
 - Mode: f
 - Excluded files: []
 - N locations input: 10000
 - Random seed: 2023

Random sample details
---------------------
 - Total locations mutated: 11
 - Total locations identified: 11
 - Location sample coverage: 100.00 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.733948
 - Clean trial 2 run time: 0:00:00.718595
 - Mutation trials total run time: 0:00:13.748120

Overall mutation trial summary
==============================
 - DETECTED: 15
 - SURVIVED: 4
 - TOTAL RUNS: 19
 - RUN DATETIME: 2024-02-23 20:51:27.733673


Mutations by result status
==========================


SURVIVED
--------
 - stack5.py: (l: 11, c: 19) - mutation from None to True
 - stack5.py: (l: 11, c: 19) - mutation from None to False
 - stack5.py: (l: 24, c: 34) - mutation from None to False
 - stack5.py: (l: 24, c: 34) - mutation from None to True


DETECTED
--------
 - stack5.py: (l: 3, c: 27) - mutation from None to True
 - stack5.py: (l: 3, c: 27) - mutation from None to False
 - stack5.py: (l: 10, c: 8) - mutation from If_Statement to If_False
 - stack5.py: (l: 10, c: 8) - mutation from If_Statement to If_True
 - stack5.py: (l: 10, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - stack5.py: (l: 10, c: 23) - mutation from None to False
 - stack5.py: (l: 10, c: 23) - mutation from None to True
 - stack5.py: (l: 17, c: 32) - mutation from <class 'ast.IsNot'> to <class 'ast.Is'>
 - stack5.py: (l: 17, c: 48) - mutation from None to False
 - stack5.py: (l: 17, c: 48) - mutation from None to True
 - stack5.py: (l: 17, c: 58) - mutation from None to False
 - stack5.py: (l: 17, c: 58) - mutation from None to True
 - stack5.py: (l: 20, c: 15) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - stack5.py: (l: 20, c: 30) - mutation from None to False
 - stack5.py: (l: 20, c: 30) - mutation from None to True