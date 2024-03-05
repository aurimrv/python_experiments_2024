Mutatest diagnostic summary
===========================
 - Source location: /home/lucca/desktop/ic/experimento/testes/python_experiments/queue3/queue3.py
 - Test commands: ['python', '-m', 'pytest', '--tb=no', './ALL-SMART-GPT-MUTPY']
 - Mode: f
 - Excluded files: []
 - N locations input: 10000
 - Random seed: 2023

Random sample details
---------------------
 - Total locations mutated: 42
 - Total locations identified: 42
 - Location sample coverage: 100.00 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:01.192422
 - Clean trial 2 run time: 0:00:00.836189
 - Mutation trials total run time: 0:01:40.485900

Overall mutation trial summary
==============================
 - DETECTED: 90
 - SURVIVED: 26
 - TOTAL RUNS: 116
 - RUN DATETIME: 2024-02-23 20:46:19.023338


Mutations by result status
==========================


SURVIVED
--------
 - queue3.py: (l: 16, c: 31) - mutation from None to True
 - queue3.py: (l: 16, c: 31) - mutation from None to False
 - queue3.py: (l: 21, c: 37) - mutation from None to False
 - queue3.py: (l: 21, c: 37) - mutation from None to True
 - queue3.py: (l: 25, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue3.py: (l: 40, c: 37) - mutation from None to False
 - queue3.py: (l: 40, c: 37) - mutation from None to True
 - queue3.py: (l: 44, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue3.py: (l: 61, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue3.py: (l: 62, c: 19) - mutation from None to False
 - queue3.py: (l: 62, c: 19) - mutation from None to True
 - queue3.py: (l: 63, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue3.py: (l: 65, c: 35) - mutation from None to False
 - queue3.py: (l: 83, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue3.py: (l: 84, c: 19) - mutation from None to False
 - queue3.py: (l: 84, c: 19) - mutation from None to True
 - queue3.py: (l: 85, c: 8) - mutation from If_Statement to If_False
 - queue3.py: (l: 85, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - queue3.py: (l: 85, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue3.py: (l: 88, c: 35) - mutation from None to False
 - queue3.py: (l: 106, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue3.py: (l: 112, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue3.py: (l: 113, c: 19) - mutation from None to False
 - queue3.py: (l: 113, c: 19) - mutation from None to True
 - queue3.py: (l: 168, c: 35) - mutation from None to True
 - queue3.py: (l: 168, c: 35) - mutation from None to False


DETECTED
--------
 - queue3.py: (l: 10, c: 20) - mutation from None to True
 - queue3.py: (l: 10, c: 20) - mutation from None to False
 - queue3.py: (l: 11, c: 20) - mutation from None to True
 - queue3.py: (l: 11, c: 20) - mutation from None to False
 - queue3.py: (l: 25, c: 8) - mutation from If_Statement to If_False
 - queue3.py: (l: 25, c: 8) - mutation from If_Statement to If_True
 - queue3.py: (l: 25, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - queue3.py: (l: 25, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue3.py: (l: 25, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue3.py: (l: 25, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue3.py: (l: 30, c: 12) - mutation from AugAssign_Add to AugAssign_Sub
 - queue3.py: (l: 30, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - queue3.py: (l: 30, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - queue3.py: (l: 38, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - queue3.py: (l: 38, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - queue3.py: (l: 38, c: 12) - mutation from AugAssign_Add to AugAssign_Sub
 - queue3.py: (l: 44, c: 8) - mutation from If_Statement to If_False
 - queue3.py: (l: 44, c: 8) - mutation from If_Statement to If_True
 - queue3.py: (l: 44, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue3.py: (l: 44, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - queue3.py: (l: 44, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue3.py: (l: 44, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue3.py: (l: 49, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - queue3.py: (l: 49, c: 12) - mutation from AugAssign_Add to AugAssign_Sub
 - queue3.py: (l: 49, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - queue3.py: (l: 55, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - queue3.py: (l: 55, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - queue3.py: (l: 55, c: 12) - mutation from AugAssign_Add to AugAssign_Sub
 - queue3.py: (l: 61, c: 8) - mutation from If_Statement to If_True
 - queue3.py: (l: 61, c: 8) - mutation from If_Statement to If_False
 - queue3.py: (l: 61, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue3.py: (l: 61, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue3.py: (l: 61, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue3.py: (l: 61, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - queue3.py: (l: 63, c: 8) - mutation from If_Statement to If_False
 - queue3.py: (l: 63, c: 8) - mutation from If_Statement to If_True
 - queue3.py: (l: 63, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue3.py: (l: 63, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue3.py: (l: 63, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue3.py: (l: 63, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - queue3.py: (l: 65, c: 35) - mutation from None to True
 - queue3.py: (l: 66, c: 32) - mutation from None to True
 - queue3.py: (l: 66, c: 32) - mutation from None to False
 - queue3.py: (l: 67, c: 12) - mutation from AugAssign_Sub to AugAssign_Add
 - queue3.py: (l: 67, c: 12) - mutation from AugAssign_Sub to AugAssign_Mult
 - queue3.py: (l: 67, c: 12) - mutation from AugAssign_Sub to AugAssign_Div
 - queue3.py: (l: 74, c: 32) - mutation from None to False
 - queue3.py: (l: 74, c: 32) - mutation from None to True
 - queue3.py: (l: 75, c: 32) - mutation from None to True
 - queue3.py: (l: 75, c: 32) - mutation from None to False
 - queue3.py: (l: 76, c: 12) - mutation from AugAssign_Sub to AugAssign_Mult
 - queue3.py: (l: 76, c: 12) - mutation from AugAssign_Sub to AugAssign_Add
 - queue3.py: (l: 76, c: 12) - mutation from AugAssign_Sub to AugAssign_Div
 - queue3.py: (l: 83, c: 8) - mutation from If_Statement to If_True
 - queue3.py: (l: 83, c: 8) - mutation from If_Statement to If_False
 - queue3.py: (l: 83, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue3.py: (l: 83, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - queue3.py: (l: 83, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue3.py: (l: 83, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue3.py: (l: 85, c: 8) - mutation from If_Statement to If_True
 - queue3.py: (l: 85, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue3.py: (l: 85, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue3.py: (l: 85, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue3.py: (l: 87, c: 32) - mutation from None to True
 - queue3.py: (l: 87, c: 32) - mutation from None to False
 - queue3.py: (l: 88, c: 35) - mutation from None to True
 - queue3.py: (l: 91, c: 12) - mutation from AugAssign_Sub to AugAssign_Add
 - queue3.py: (l: 91, c: 12) - mutation from AugAssign_Sub to AugAssign_Div
 - queue3.py: (l: 91, c: 12) - mutation from AugAssign_Sub to AugAssign_Mult
 - queue3.py: (l: 96, c: 32) - mutation from None to True
 - queue3.py: (l: 96, c: 32) - mutation from None to False
 - queue3.py: (l: 97, c: 28) - mutation from None to True
 - queue3.py: (l: 97, c: 28) - mutation from None to False
 - queue3.py: (l: 99, c: 12) - mutation from AugAssign_Sub to AugAssign_Mult
 - queue3.py: (l: 99, c: 12) - mutation from AugAssign_Sub to AugAssign_Add
 - queue3.py: (l: 99, c: 12) - mutation from AugAssign_Sub to AugAssign_Div
 - queue3.py: (l: 106, c: 15) - mutation from True to False
 - queue3.py: (l: 106, c: 15) - mutation from True to None
 - queue3.py: (l: 106, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue3.py: (l: 106, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - queue3.py: (l: 106, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue3.py: (l: 106, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue3.py: (l: 106, c: 45) - mutation from False to True
 - queue3.py: (l: 106, c: 45) - mutation from False to None
 - queue3.py: (l: 112, c: 8) - mutation from If_Statement to If_False
 - queue3.py: (l: 112, c: 8) - mutation from If_Statement to If_True
 - queue3.py: (l: 112, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue3.py: (l: 112, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - queue3.py: (l: 112, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue3.py: (l: 112, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
