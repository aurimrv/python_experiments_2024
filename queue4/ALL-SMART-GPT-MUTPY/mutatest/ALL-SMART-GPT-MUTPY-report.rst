Mutatest diagnostic summary
===========================
 - Source location: /home/lucca/desktop/ic/experimento/testes/python_experiments/queue4/queue4.py
 - Test commands: ['python', '-m', 'pytest', '--tb=no', './ALL-SMART-GPT-MUTPY']
 - Mode: f
 - Excluded files: []
 - N locations input: 10000
 - Random seed: 2023

Random sample details
---------------------
 - Total locations mutated: 50
 - Total locations identified: 50
 - Location sample coverage: 100.00 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:01.427579
 - Clean trial 2 run time: 0:00:01.096688
 - Mutation trials total run time: 0:02:03.378282

Overall mutation trial summary
==============================
 - DETECTED: 106
 - SURVIVED: 11
 - TOTAL RUNS: 117
 - RUN DATETIME: 2024-02-25 21:25:58.044044


Mutations by result status
==========================


SURVIVED
--------
 - queue4.py: (l: 30, c: 28) - mutation from None to False
 - queue4.py: (l: 85, c: 28) - mutation from None to False
 - queue4.py: (l: 88, c: 8) - mutation from If_Statement to If_False
 - queue4.py: (l: 97, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue4.py: (l: 102, c: 59) - mutation from None to False
 - queue4.py: (l: 103, c: 16) - mutation from If_Statement to If_True
 - queue4.py: (l: 104, c: 59) - mutation from None to False
 - queue4.py: (l: 104, c: 59) - mutation from None to True
 - queue4.py: (l: 135, c: 28) - mutation from None to False
 - queue4.py: (l: 152, c: 19) - mutation from None to False
 - queue4.py: (l: 152, c: 19) - mutation from None to True


DETECTED
--------
 - queue4.py: (l: 7, c: 28) - mutation from None to True
 - queue4.py: (l: 7, c: 28) - mutation from None to False
 - queue4.py: (l: 7, c: 44) - mutation from None to True
 - queue4.py: (l: 7, c: 44) - mutation from None to False
 - queue4.py: (l: 7, c: 55) - mutation from None to True
 - queue4.py: (l: 7, c: 55) - mutation from None to False
 - queue4.py: (l: 30, c: 28) - mutation from None to True
 - queue4.py: (l: 32, c: 20) - mutation from None to True
 - queue4.py: (l: 32, c: 20) - mutation from None to False
 - queue4.py: (l: 33, c: 20) - mutation from None to False
 - queue4.py: (l: 33, c: 20) - mutation from None to True
 - queue4.py: (l: 39, c: 12) - mutation from If_Statement to If_False
 - queue4.py: (l: 39, c: 12) - mutation from If_Statement to If_True
 - queue4.py: (l: 46, c: 8) - mutation from If_Statement to If_True
 - queue4.py: (l: 46, c: 8) - mutation from If_Statement to If_False
 - queue4.py: (l: 48, c: 8) - mutation from If_Statement to If_False
 - queue4.py: (l: 48, c: 8) - mutation from If_Statement to If_True
 - queue4.py: (l: 50, c: 8) - mutation from AugAssign_Add to AugAssign_Div
 - queue4.py: (l: 50, c: 8) - mutation from AugAssign_Add to AugAssign_Sub
 - queue4.py: (l: 50, c: 8) - mutation from AugAssign_Add to AugAssign_Mult
 - queue4.py: (l: 55, c: 8) - mutation from If_Statement to If_True
 - queue4.py: (l: 55, c: 8) - mutation from If_Statement to If_False
 - queue4.py: (l: 55, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - queue4.py: (l: 55, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - queue4.py: (l: 55, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - queue4.py: (l: 55, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - queue4.py: (l: 55, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - queue4.py: (l: 59, c: 8) - mutation from If_Statement to If_False
 - queue4.py: (l: 59, c: 8) - mutation from If_Statement to If_True
 - queue4.py: (l: 60, c: 28) - mutation from None to False
 - queue4.py: (l: 60, c: 28) - mutation from None to True
 - queue4.py: (l: 62, c: 8) - mutation from AugAssign_Sub to AugAssign_Mult
 - queue4.py: (l: 62, c: 8) - mutation from AugAssign_Sub to AugAssign_Add
 - queue4.py: (l: 62, c: 8) - mutation from AugAssign_Sub to AugAssign_Div
 - queue4.py: (l: 63, c: 8) - mutation from If_Statement to If_False
 - queue4.py: (l: 63, c: 8) - mutation from If_Statement to If_True
 - queue4.py: (l: 63, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - queue4.py: (l: 63, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - queue4.py: (l: 63, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - queue4.py: (l: 63, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - queue4.py: (l: 63, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - queue4.py: (l: 64, c: 24) - mutation from None to True
 - queue4.py: (l: 64, c: 24) - mutation from None to False
 - queue4.py: (l: 71, c: 8) - mutation from If_Statement to If_False
 - queue4.py: (l: 71, c: 8) - mutation from If_Statement to If_True
 - queue4.py: (l: 73, c: 8) - mutation from If_Statement to If_True
 - queue4.py: (l: 73, c: 8) - mutation from If_Statement to If_False
 - queue4.py: (l: 73, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - queue4.py: (l: 73, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - queue4.py: (l: 73, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - queue4.py: (l: 73, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - queue4.py: (l: 73, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - queue4.py: (l: 75, c: 8) - mutation from AugAssign_Add to AugAssign_Sub
 - queue4.py: (l: 75, c: 8) - mutation from AugAssign_Add to AugAssign_Mult
 - queue4.py: (l: 75, c: 8) - mutation from AugAssign_Add to AugAssign_Div
 - queue4.py: (l: 80, c: 8) - mutation from If_Statement to If_False
 - queue4.py: (l: 80, c: 8) - mutation from If_Statement to If_True
 - queue4.py: (l: 80, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - queue4.py: (l: 80, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - queue4.py: (l: 80, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - queue4.py: (l: 80, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - queue4.py: (l: 80, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - queue4.py: (l: 84, c: 8) - mutation from If_Statement to If_False
 - queue4.py: (l: 84, c: 8) - mutation from If_Statement to If_True
 - queue4.py: (l: 85, c: 28) - mutation from None to True
 - queue4.py: (l: 87, c: 8) - mutation from AugAssign_Sub to AugAssign_Div
 - queue4.py: (l: 87, c: 8) - mutation from AugAssign_Sub to AugAssign_Add
 - queue4.py: (l: 87, c: 8) - mutation from AugAssign_Sub to AugAssign_Mult
 - queue4.py: (l: 88, c: 8) - mutation from If_Statement to If_True
 - queue4.py: (l: 88, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - queue4.py: (l: 88, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - queue4.py: (l: 88, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - queue4.py: (l: 88, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - queue4.py: (l: 88, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - queue4.py: (l: 89, c: 24) - mutation from None to False
 - queue4.py: (l: 89, c: 24) - mutation from None to True
 - queue4.py: (l: 96, c: 12) - mutation from If_Statement to If_True
 - queue4.py: (l: 96, c: 12) - mutation from If_Statement to If_False
 - queue4.py: (l: 96, c: 15) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - queue4.py: (l: 97, c: 16) - mutation from If_Statement to If_True
 - queue4.py: (l: 97, c: 16) - mutation from If_Statement to If_False
 - queue4.py: (l: 97, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - queue4.py: (l: 97, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue4.py: (l: 97, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue4.py: (l: 97, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue4.py: (l: 98, c: 43) - mutation from None to False
 - queue4.py: (l: 98, c: 43) - mutation from None to True
 - queue4.py: (l: 98, c: 49) - mutation from None to False
 - queue4.py: (l: 98, c: 49) - mutation from None to True
 - queue4.py: (l: 99, c: 16) - mutation from If_Statement to If_True
 - queue4.py: (l: 99, c: 16) - mutation from If_Statement to If_False
 - queue4.py: (l: 99, c: 21) - mutation from <class 'ast.IsNot'> to <class 'ast.Is'>
 - queue4.py: (l: 99, c: 21) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - queue4.py: (l: 99, c: 47) - mutation from <class 'ast.IsNot'> to <class 'ast.Is'>
 - queue4.py: (l: 101, c: 16) - mutation from If_Statement to If_False
 - queue4.py: (l: 101, c: 16) - mutation from If_Statement to If_True
 - queue4.py: (l: 101, c: 21) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - queue4.py: (l: 102, c: 59) - mutation from None to True
 - queue4.py: (l: 103, c: 16) - mutation from If_Statement to If_False
 - queue4.py: (l: 103, c: 21) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - queue4.py: (l: 105, c: 16) - mutation from AugAssign_Sub to AugAssign_Div
 - queue4.py: (l: 105, c: 16) - mutation from AugAssign_Sub to AugAssign_Mult
 - queue4.py: (l: 105, c: 16) - mutation from AugAssign_Sub to AugAssign_Add
 - queue4.py: (l: 114, c: 14) - mutation from True to None
 - queue4.py: (l: 114, c: 14) - mutation from True to False
 - queue4.py: (l: 135, c: 28) - mutation from None to True