Mutatest diagnostic summary
===========================
 - Source location: /home/lucca/desktop/ic/experimento/testes/python_experiments/linkedList2/linkedList2.py
 - Test commands: ['python', '-m', 'pytest', '--tb=no', './ALL-SMART-GPT-MUTMUT']
 - Mode: f
 - Excluded files: []
 - N locations input: 10000
 - Random seed: 2023

Random sample details
---------------------
 - Total locations mutated: 36
 - Total locations identified: 36
 - Location sample coverage: 100.00 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:01.012179
 - Clean trial 2 run time: 0:00:00.735183
 - Mutation trials total run time: 0:01:22.832765

Overall mutation trial summary
==============================
 - DETECTED: 86
 - SURVIVED: 5
 - TIMEOUT: 2
 - TOTAL RUNS: 93
 - RUN DATETIME: 2024-02-23 21:00:22.739664


Mutations by result status
==========================


SURVIVED
--------
 - linkedList2.py: (l: 15, c: 20) - mutation from None to True
 - linkedList2.py: (l: 15, c: 20) - mutation from None to False
 - linkedList2.py: (l: 67, c: 8) - mutation from If_Statement to If_False
 - linkedList2.py: (l: 67, c: 24) - mutation from None to True
 - linkedList2.py: (l: 67, c: 24) - mutation from None to False


TIMEOUT
-------
 - linkedList2.py: (l: 21, c: 12) - mutation from If_Statement to If_False
 - linkedList2.py: (l: 21, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>


DETECTED
--------
 - linkedList2.py: (l: 7, c: 37) - mutation from None to True
 - linkedList2.py: (l: 7, c: 37) - mutation from None to False
 - linkedList2.py: (l: 15, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Lt'>
 - linkedList2.py: (l: 15, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.LtE'>
 - linkedList2.py: (l: 15, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Eq'>
 - linkedList2.py: (l: 15, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Gt'>
 - linkedList2.py: (l: 15, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.GtE'>
 - linkedList2.py: (l: 15, c: 14) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - linkedList2.py: (l: 15, c: 29) - mutation from <class 'ast.NotEq'> to <class 'ast.Gt'>
 - linkedList2.py: (l: 15, c: 29) - mutation from <class 'ast.NotEq'> to <class 'ast.LtE'>
 - linkedList2.py: (l: 15, c: 29) - mutation from <class 'ast.NotEq'> to <class 'ast.GtE'>
 - linkedList2.py: (l: 15, c: 29) - mutation from <class 'ast.NotEq'> to <class 'ast.Lt'>
 - linkedList2.py: (l: 15, c: 29) - mutation from <class 'ast.NotEq'> to <class 'ast.Eq'>
 - linkedList2.py: (l: 15, c: 35) - mutation from None to True
 - linkedList2.py: (l: 15, c: 35) - mutation from None to False
 - linkedList2.py: (l: 16, c: 12) - mutation from If_Statement to If_True
 - linkedList2.py: (l: 16, c: 12) - mutation from If_Statement to If_False
 - linkedList2.py: (l: 16, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - linkedList2.py: (l: 16, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - linkedList2.py: (l: 16, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - linkedList2.py: (l: 16, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - linkedList2.py: (l: 16, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - linkedList2.py: (l: 16, c: 26) - mutation from None to False
 - linkedList2.py: (l: 16, c: 26) - mutation from None to True
 - linkedList2.py: (l: 16, c: 39) - mutation from False to None
 - linkedList2.py: (l: 16, c: 39) - mutation from False to True
 - linkedList2.py: (l: 21, c: 12) - mutation from If_Statement to If_True
 - linkedList2.py: (l: 21, c: 32) - mutation from True to False
 - linkedList2.py: (l: 21, c: 32) - mutation from True to None
 - linkedList2.py: (l: 22, c: 15) - mutation from False to True
 - linkedList2.py: (l: 22, c: 15) - mutation from False to None
 - linkedList2.py: (l: 27, c: 21) - mutation from None to False
 - linkedList2.py: (l: 27, c: 21) - mutation from None to True
 - linkedList2.py: (l: 37, c: 8) - mutation from If_Statement to If_False
 - linkedList2.py: (l: 37, c: 8) - mutation from If_Statement to If_True
 - linkedList2.py: (l: 37, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - linkedList2.py: (l: 37, c: 24) - mutation from None to False
 - linkedList2.py: (l: 37, c: 24) - mutation from None to True
 - linkedList2.py: (l: 46, c: 15) - mutation from None to True
 - linkedList2.py: (l: 46, c: 15) - mutation from None to False
 - linkedList2.py: (l: 47, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Eq'>
 - linkedList2.py: (l: 47, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.GtE'>
 - linkedList2.py: (l: 47, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.LtE'>
 - linkedList2.py: (l: 47, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Lt'>
 - linkedList2.py: (l: 47, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Gt'>
 - linkedList2.py: (l: 47, c: 19) - mutation from None to True
 - linkedList2.py: (l: 47, c: 19) - mutation from None to False
 - linkedList2.py: (l: 48, c: 12) - mutation from If_Statement to If_False
 - linkedList2.py: (l: 48, c: 12) - mutation from If_Statement to If_True
 - linkedList2.py: (l: 48, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - linkedList2.py: (l: 48, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - linkedList2.py: (l: 48, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - linkedList2.py: (l: 48, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - linkedList2.py: (l: 48, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - linkedList2.py: (l: 49, c: 16) - mutation from If_Statement to If_False
 - linkedList2.py: (l: 49, c: 16) - mutation from If_Statement to If_True
 - linkedList2.py: (l: 49, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - linkedList2.py: (l: 49, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - linkedList2.py: (l: 49, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - linkedList2.py: (l: 49, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - linkedList2.py: (l: 49, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - linkedList2.py: (l: 49, c: 27) - mutation from None to False
 - linkedList2.py: (l: 49, c: 27) - mutation from None to True
 - linkedList2.py: (l: 53, c: 23) - mutation from True to False
 - linkedList2.py: (l: 53, c: 23) - mutation from True to None
 - linkedList2.py: (l: 56, c: 15) - mutation from False to None
 - linkedList2.py: (l: 56, c: 15) - mutation from False to True
 - linkedList2.py: (l: 61, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Gt'>
 - linkedList2.py: (l: 61, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.LtE'>
 - linkedList2.py: (l: 61, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Eq'>
 - linkedList2.py: (l: 61, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Lt'>
 - linkedList2.py: (l: 61, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.GtE'>
 - linkedList2.py: (l: 61, c: 19) - mutation from None to False
 - linkedList2.py: (l: 61, c: 19) - mutation from None to True
 - linkedList2.py: (l: 67, c: 8) - mutation from If_Statement to If_True
 - linkedList2.py: (l: 67, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - linkedList2.py: (l: 76, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.GtE'>
 - linkedList2.py: (l: 76, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Gt'>
 - linkedList2.py: (l: 76, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Lt'>
 - linkedList2.py: (l: 76, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Eq'>
 - linkedList2.py: (l: 76, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.LtE'>
 - linkedList2.py: (l: 76, c: 19) - mutation from None to False
 - linkedList2.py: (l: 76, c: 19) - mutation from None to True
 - linkedList2.py: (l: 77, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - linkedList2.py: (l: 77, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - linkedList2.py: (l: 77, c: 12) - mutation from AugAssign_Add to AugAssign_Sub