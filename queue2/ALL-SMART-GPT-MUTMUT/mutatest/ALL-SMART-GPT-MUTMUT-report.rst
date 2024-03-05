Mutatest diagnostic summary
===========================
 - Source location: /home/lucca/desktop/ic/experimento/testes/python_experiments/queue2/queue2.py
 - Test commands: ['python', '-m', 'pytest', '--tb=no', './ALL-SMART-GPT-MUTMUT']
 - Mode: f
 - Excluded files: []
 - N locations input: 10000
 - Random seed: 2023

Random sample details
---------------------
 - Total locations mutated: 59
 - Total locations identified: 59
 - Location sample coverage: 100.00 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.829058
 - Clean trial 2 run time: 0:00:00.499593
 - Mutation trials total run time: 0:01:26.308203

Overall mutation trial summary
==============================
 - DETECTED: 140
 - SURVIVED: 8
 - TIMEOUT: 1
 - TOTAL RUNS: 149
 - RUN DATETIME: 2024-03-03 14:57:39.348530


Mutations by result status
==========================


SURVIVED
--------
 - queue2.py: (l: 15, c: 20) - mutation from None to True
 - queue2.py: (l: 15, c: 20) - mutation from None to False
 - queue2.py: (l: 67, c: 8) - mutation from If_Statement to If_False
 - queue2.py: (l: 67, c: 24) - mutation from None to True
 - queue2.py: (l: 67, c: 24) - mutation from None to False
 - queue2.py: (l: 121, c: 8) - mutation from If_Statement to If_False
 - queue2.py: (l: 121, c: 24) - mutation from None to True
 - queue2.py: (l: 121, c: 24) - mutation from None to False


TIMEOUT
-------
 - queue2.py: (l: 21, c: 12) - mutation from If_Statement to If_False


DETECTED
--------
 - queue2.py: (l: 7, c: 37) - mutation from None to True
 - queue2.py: (l: 7, c: 37) - mutation from None to False
 - queue2.py: (l: 15, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.GtE'>
 - queue2.py: (l: 15, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Eq'>
 - queue2.py: (l: 15, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Gt'>
 - queue2.py: (l: 15, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Lt'>
 - queue2.py: (l: 15, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.LtE'>
 - queue2.py: (l: 15, c: 14) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - queue2.py: (l: 15, c: 29) - mutation from <class 'ast.NotEq'> to <class 'ast.Lt'>
 - queue2.py: (l: 15, c: 29) - mutation from <class 'ast.NotEq'> to <class 'ast.Eq'>
 - queue2.py: (l: 15, c: 29) - mutation from <class 'ast.NotEq'> to <class 'ast.LtE'>
 - queue2.py: (l: 15, c: 29) - mutation from <class 'ast.NotEq'> to <class 'ast.GtE'>
 - queue2.py: (l: 15, c: 29) - mutation from <class 'ast.NotEq'> to <class 'ast.Gt'>
 - queue2.py: (l: 15, c: 35) - mutation from None to True
 - queue2.py: (l: 15, c: 35) - mutation from None to False
 - queue2.py: (l: 16, c: 12) - mutation from If_Statement to If_True
 - queue2.py: (l: 16, c: 12) - mutation from If_Statement to If_False
 - queue2.py: (l: 16, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - queue2.py: (l: 16, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue2.py: (l: 16, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue2.py: (l: 16, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue2.py: (l: 16, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue2.py: (l: 16, c: 26) - mutation from None to False
 - queue2.py: (l: 16, c: 26) - mutation from None to True
 - queue2.py: (l: 16, c: 39) - mutation from False to None
 - queue2.py: (l: 16, c: 39) - mutation from False to True
 - queue2.py: (l: 21, c: 12) - mutation from If_Statement to If_True
 - queue2.py: (l: 21, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue2.py: (l: 21, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - queue2.py: (l: 21, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue2.py: (l: 21, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue2.py: (l: 21, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue2.py: (l: 21, c: 32) - mutation from True to False
 - queue2.py: (l: 21, c: 32) - mutation from True to None
 - queue2.py: (l: 22, c: 15) - mutation from False to None
 - queue2.py: (l: 22, c: 15) - mutation from False to True
 - queue2.py: (l: 27, c: 21) - mutation from None to False
 - queue2.py: (l: 27, c: 21) - mutation from None to True
 - queue2.py: (l: 37, c: 8) - mutation from If_Statement to If_True
 - queue2.py: (l: 37, c: 8) - mutation from If_Statement to If_False
 - queue2.py: (l: 37, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - queue2.py: (l: 37, c: 24) - mutation from None to False
 - queue2.py: (l: 37, c: 24) - mutation from None to True
 - queue2.py: (l: 46, c: 15) - mutation from None to True
 - queue2.py: (l: 46, c: 15) - mutation from None to False
 - queue2.py: (l: 47, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Lt'>
 - queue2.py: (l: 47, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.GtE'>
 - queue2.py: (l: 47, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.LtE'>
 - queue2.py: (l: 47, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Gt'>
 - queue2.py: (l: 47, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Eq'>
 - queue2.py: (l: 47, c: 19) - mutation from None to True
 - queue2.py: (l: 47, c: 19) - mutation from None to False
 - queue2.py: (l: 48, c: 12) - mutation from If_Statement to If_False
 - queue2.py: (l: 48, c: 12) - mutation from If_Statement to If_True
 - queue2.py: (l: 48, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - queue2.py: (l: 48, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue2.py: (l: 48, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue2.py: (l: 48, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue2.py: (l: 48, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue2.py: (l: 49, c: 16) - mutation from If_Statement to If_True
 - queue2.py: (l: 49, c: 16) - mutation from If_Statement to If_False
 - queue2.py: (l: 49, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue2.py: (l: 49, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue2.py: (l: 49, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - queue2.py: (l: 49, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue2.py: (l: 49, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue2.py: (l: 49, c: 27) - mutation from None to False
 - queue2.py: (l: 49, c: 27) - mutation from None to True
 - queue2.py: (l: 53, c: 23) - mutation from True to False
 - queue2.py: (l: 53, c: 23) - mutation from True to None
 - queue2.py: (l: 56, c: 15) - mutation from False to True
 - queue2.py: (l: 56, c: 15) - mutation from False to None
 - queue2.py: (l: 61, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.GtE'>
 - queue2.py: (l: 61, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.LtE'>
 - queue2.py: (l: 61, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Eq'>
 - queue2.py: (l: 61, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Gt'>
 - queue2.py: (l: 61, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Lt'>
 - queue2.py: (l: 61, c: 19) - mutation from None to False
 - queue2.py: (l: 61, c: 19) - mutation from None to True
 - queue2.py: (l: 67, c: 8) - mutation from If_Statement to If_True
 - queue2.py: (l: 67, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - queue2.py: (l: 76, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.GtE'>
 - queue2.py: (l: 76, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.LtE'>
 - queue2.py: (l: 76, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Gt'>
 - queue2.py: (l: 76, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Eq'>
 - queue2.py: (l: 76, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Lt'>
 - queue2.py: (l: 76, c: 19) - mutation from None to False
 - queue2.py: (l: 76, c: 19) - mutation from None to True
 - queue2.py: (l: 77, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - queue2.py: (l: 77, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - queue2.py: (l: 77, c: 12) - mutation from AugAssign_Add to AugAssign_Sub
 - queue2.py: (l: 84, c: 20) - mutation from None to False
 - queue2.py: (l: 84, c: 20) - mutation from None to True
 - queue2.py: (l: 85, c: 20) - mutation from None to False
 - queue2.py: (l: 85, c: 20) - mutation from None to True
 - queue2.py: (l: 91, c: 36) - mutation from None to True
 - queue2.py: (l: 91, c: 36) - mutation from None to False
 - queue2.py: (l: 92, c: 8) - mutation from If_Statement to If_False
 - queue2.py: (l: 92, c: 8) - mutation from If_Statement to If_True
 - queue2.py: (l: 92, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - queue2.py: (l: 92, c: 24) - mutation from None to True
 - queue2.py: (l: 92, c: 24) - mutation from None to False
 - queue2.py: (l: 100, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue2.py: (l: 100, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue2.py: (l: 100, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - queue2.py: (l: 100, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue2.py: (l: 100, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue2.py: (l: 100, c: 28) - mutation from None to True
 - queue2.py: (l: 100, c: 28) - mutation from None to False
 - queue2.py: (l: 104, c: 8) - mutation from If_Statement to If_False
 - queue2.py: (l: 104, c: 8) - mutation from If_Statement to If_True
 - queue2.py: (l: 104, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - queue2.py: (l: 104, c: 24) - mutation from None to True
 - queue2.py: (l: 104, c: 24) - mutation from None to False
 - queue2.py: (l: 108, c: 8) - mutation from If_Statement to If_True
 - queue2.py: (l: 108, c: 8) - mutation from If_Statement to If_False
 - queue2.py: (l: 108, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - queue2.py: (l: 108, c: 24) - mutation from None to True
 - queue2.py: (l: 108, c: 24) - mutation from None to False
 - queue2.py: (l: 109, c: 24) - mutation from None to False
 - queue2.py: (l: 109, c: 24) - mutation from None to True
 - queue2.py: (l: 115, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.LtE'>
 - queue2.py: (l: 115, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Eq'>
 - queue2.py: (l: 115, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Lt'>
 - queue2.py: (l: 115, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.GtE'>
 - queue2.py: (l: 115, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Gt'>
 - queue2.py: (l: 115, c: 19) - mutation from None to True
 - queue2.py: (l: 115, c: 19) - mutation from None to False
 - queue2.py: (l: 121, c: 8) - mutation from If_Statement to If_True
 - queue2.py: (l: 121, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - queue2.py: (l: 130, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Eq'>
 - queue2.py: (l: 130, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Gt'>
 - queue2.py: (l: 130, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.LtE'>
 - queue2.py: (l: 130, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Lt'>
 - queue2.py: (l: 130, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.GtE'>
 - queue2.py: (l: 130, c: 19) - mutation from None to True
 - queue2.py: (l: 130, c: 19) - mutation from None to False
 - queue2.py: (l: 131, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - queue2.py: (l: 131, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - queue2.py: (l: 131, c: 12) - mutation from AugAssign_Add to AugAssign_Sub