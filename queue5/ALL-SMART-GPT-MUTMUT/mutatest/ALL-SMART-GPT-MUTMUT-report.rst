Mutatest diagnostic summary
===========================
 - Source location: /home/lucca/desktop/ic/experimento/testes/python_experiments/queue5/queue5.py
 - Test commands: ['python', '-m', 'pytest', '--tb=no', './ALL-SMART-GPT-MUTMUT']
 - Mode: f
 - Excluded files: []
 - N locations input: 10000
 - Random seed: 2023

Random sample details
---------------------
 - Total locations mutated: 20
 - Total locations identified: 20
 - Location sample coverage: 100.00 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.769082
 - Clean trial 2 run time: 0:00:00.710429
 - Mutation trials total run time: 0:00:25.838227

Overall mutation trial summary
==============================
 - DETECTED: 33
 - SURVIVED: 4
 - TOTAL RUNS: 37
 - RUN DATETIME: 2024-02-23 21:10:31.632193


Mutations by result status
==========================


SURVIVED
--------
 - queue5.py: (l: 17, c: 11) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - queue5.py: (l: 26, c: 11) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - queue5.py: (l: 27, c: 19) - mutation from None to False
 - queue5.py: (l: 27, c: 19) - mutation from None to True


DETECTED
--------
 - queue5.py: (l: 5, c: 20) - mutation from None to True
 - queue5.py: (l: 5, c: 20) - mutation from None to False
 - queue5.py: (l: 11, c: 20) - mutation from None to True
 - queue5.py: (l: 11, c: 20) - mutation from None to False
 - queue5.py: (l: 12, c: 20) - mutation from None to True
 - queue5.py: (l: 12, c: 20) - mutation from None to False
 - queue5.py: (l: 17, c: 8) - mutation from If_Statement to If_True
 - queue5.py: (l: 17, c: 8) - mutation from If_Statement to If_False
 - queue5.py: (l: 17, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - queue5.py: (l: 17, c: 24) - mutation from None to False
 - queue5.py: (l: 17, c: 24) - mutation from None to True
 - queue5.py: (l: 17, c: 33) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - queue5.py: (l: 17, c: 46) - mutation from None to False
 - queue5.py: (l: 17, c: 46) - mutation from None to True
 - queue5.py: (l: 26, c: 8) - mutation from If_Statement to If_True
 - queue5.py: (l: 26, c: 8) - mutation from If_Statement to If_False
 - queue5.py: (l: 26, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - queue5.py: (l: 26, c: 24) - mutation from None to False
 - queue5.py: (l: 26, c: 24) - mutation from None to True
 - queue5.py: (l: 26, c: 33) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - queue5.py: (l: 26, c: 46) - mutation from None to True
 - queue5.py: (l: 26, c: 46) - mutation from None to False
 - queue5.py: (l: 30, c: 8) - mutation from If_Statement to If_False
 - queue5.py: (l: 30, c: 8) - mutation from If_Statement to If_True
 - queue5.py: (l: 30, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue5.py: (l: 30, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue5.py: (l: 30, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue5.py: (l: 30, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - queue5.py: (l: 30, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue5.py: (l: 31, c: 24) - mutation from None to False
 - queue5.py: (l: 31, c: 24) - mutation from None to True
 - queue5.py: (l: 32, c: 24) - mutation from None to True
 - queue5.py: (l: 32, c: 24) - mutation from None to False