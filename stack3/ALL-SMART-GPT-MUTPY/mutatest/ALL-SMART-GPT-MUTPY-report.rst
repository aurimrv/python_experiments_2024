Mutatest diagnostic summary
===========================
 - Source location: /home/lucca/desktop/ic/experimento/testes/python_experiments/stack3/stack3.py
 - Test commands: ['python', '-m', 'pytest', '--tb=no', './ALL-SMART-GPT-MUTPY']
 - Mode: f
 - Excluded files: []
 - N locations input: 10000
 - Random seed: 2023

Random sample details
---------------------
 - Total locations mutated: 22
 - Total locations identified: 22
 - Location sample coverage: 100.00 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.936003
 - Clean trial 2 run time: 0:00:00.825621
 - Mutation trials total run time: 0:00:57.131889

Overall mutation trial summary
==============================
 - DETECTED: 49
 - SURVIVED: 8
 - TIMEOUT: 2
 - TOTAL RUNS: 59
 - RUN DATETIME: 2024-02-23 20:51:12.083810


Mutations by result status
==========================


SURVIVED
--------
 - stack3.py: (l: 19, c: 31) - mutation from None to True
 - stack3.py: (l: 19, c: 31) - mutation from None to False
 - stack3.py: (l: 38, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - stack3.py: (l: 40, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - stack3.py: (l: 75, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - stack3.py: (l: 103, c: 32) - mutation from None to False
 - stack3.py: (l: 103, c: 32) - mutation from None to True
 - stack3.py: (l: 125, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>


TIMEOUT
-------
 - stack3.py: (l: 24, c: 8) - mutation from If_Statement to If_False
 - stack3.py: (l: 24, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>


DETECTED
--------
 - stack3.py: (l: 10, c: 20) - mutation from None to True
 - stack3.py: (l: 10, c: 20) - mutation from None to False
 - stack3.py: (l: 15, c: 31) - mutation from None to True
 - stack3.py: (l: 15, c: 31) - mutation from None to False
 - stack3.py: (l: 24, c: 8) - mutation from If_Statement to If_True
 - stack3.py: (l: 27, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - stack3.py: (l: 27, c: 12) - mutation from AugAssign_Add to AugAssign_Sub
 - stack3.py: (l: 27, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - stack3.py: (l: 32, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - stack3.py: (l: 32, c: 12) - mutation from AugAssign_Add to AugAssign_Sub
 - stack3.py: (l: 32, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - stack3.py: (l: 38, c: 8) - mutation from If_Statement to If_True
 - stack3.py: (l: 38, c: 8) - mutation from If_Statement to If_False
 - stack3.py: (l: 38, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - stack3.py: (l: 38, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - stack3.py: (l: 38, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - stack3.py: (l: 38, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - stack3.py: (l: 39, c: 19) - mutation from None to False
 - stack3.py: (l: 39, c: 19) - mutation from None to True
 - stack3.py: (l: 40, c: 8) - mutation from If_Statement to If_False
 - stack3.py: (l: 40, c: 8) - mutation from If_Statement to If_True
 - stack3.py: (l: 40, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - stack3.py: (l: 40, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - stack3.py: (l: 40, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - stack3.py: (l: 40, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - stack3.py: (l: 42, c: 35) - mutation from None to False
 - stack3.py: (l: 42, c: 35) - mutation from None to True
 - stack3.py: (l: 44, c: 12) - mutation from AugAssign_Sub to AugAssign_Div
 - stack3.py: (l: 44, c: 12) - mutation from AugAssign_Sub to AugAssign_Mult
 - stack3.py: (l: 44, c: 12) - mutation from AugAssign_Sub to AugAssign_Add
 - stack3.py: (l: 50, c: 12) - mutation from AugAssign_Sub to AugAssign_Div
 - stack3.py: (l: 50, c: 12) - mutation from AugAssign_Sub to AugAssign_Mult
 - stack3.py: (l: 50, c: 12) - mutation from AugAssign_Sub to AugAssign_Add
 - stack3.py: (l: 75, c: 15) - mutation from True to False
 - stack3.py: (l: 75, c: 15) - mutation from True to None
 - stack3.py: (l: 75, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - stack3.py: (l: 75, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - stack3.py: (l: 75, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - stack3.py: (l: 75, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - stack3.py: (l: 75, c: 45) - mutation from False to None
 - stack3.py: (l: 75, c: 45) - mutation from False to True
 - stack3.py: (l: 125, c: 15) - mutation from True to None
 - stack3.py: (l: 125, c: 15) - mutation from True to False
 - stack3.py: (l: 125, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - stack3.py: (l: 125, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - stack3.py: (l: 125, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - stack3.py: (l: 125, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - stack3.py: (l: 125, c: 56) - mutation from False to None
 - stack3.py: (l: 125, c: 56) - mutation from False to True