Mutatest diagnostic summary
===========================
 - Source location: /home/lucca/desktop/ic/experimento/testes/python_experiments/linkedList5/ALL-SMART-GPT-MUTATEST/linkedList5.py
 - Test commands: ['python', '-m', 'pytest', '--tb=no']
 - Mode: f
 - Excluded files: []
 - N locations input: 10000
 - Random seed: 2023

Random sample details
---------------------
 - Total locations mutated: 55
 - Total locations identified: 55
 - Location sample coverage: 100.00 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.825587
 - Clean trial 2 run time: 0:00:00.755489
 - Mutation trials total run time: 0:01:25.186545

Overall mutation trial summary
==============================
 - DETECTED: 101
 - SURVIVED: 10
 - TOTAL RUNS: 111
 - RUN DATETIME: 2024-01-25 10:47:12.849987


Mutations by result status
==========================


SURVIVED
--------
 - linkedList5.py: (l: 45, c: 8) - mutation from If_Statement to If_False
 - linkedList5.py: (l: 45, c: 19) - mutation from None to True
 - linkedList5.py: (l: 45, c: 19) - mutation from None to False
 - linkedList5.py: (l: 55, c: 8) - mutation from If_Statement to If_False
 - linkedList5.py: (l: 55, c: 19) - mutation from None to False
 - linkedList5.py: (l: 55, c: 19) - mutation from None to True
 - linkedList5.py: (l: 72, c: 8) - mutation from If_Statement to If_False
 - linkedList5.py: (l: 72, c: 19) - mutation from None to False
 - linkedList5.py: (l: 72, c: 19) - mutation from None to True
 - linkedList5.py: (l: 77, c: 8) - mutation from If_Statement to If_False


DETECTED
--------
 - linkedList5.py: (l: 3, c: 34) - mutation from None to True
 - linkedList5.py: (l: 3, c: 34) - mutation from None to False
 - linkedList5.py: (l: 13, c: 28) - mutation from None to True
 - linkedList5.py: (l: 13, c: 28) - mutation from None to False
 - linkedList5.py: (l: 19, c: 14) - mutation from <class 'ast.IsNot'> to <class 'ast.Is'>
 - linkedList5.py: (l: 19, c: 26) - mutation from None to False
 - linkedList5.py: (l: 19, c: 26) - mutation from None to True
 - linkedList5.py: (l: 20, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - linkedList5.py: (l: 20, c: 12) - mutation from AugAssign_Add to AugAssign_Sub
 - linkedList5.py: (l: 20, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - linkedList5.py: (l: 25, c: 8) - mutation from If_Statement to If_True
 - linkedList5.py: (l: 25, c: 8) - mutation from If_Statement to If_False
 - linkedList5.py: (l: 25, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - linkedList5.py: (l: 25, c: 19) - mutation from None to False
 - linkedList5.py: (l: 25, c: 19) - mutation from None to True
 - linkedList5.py: (l: 26, c: 19) - mutation from None to True
 - linkedList5.py: (l: 26, c: 19) - mutation from None to False
 - linkedList5.py: (l: 32, c: 8) - mutation from If_Statement to If_True
 - linkedList5.py: (l: 32, c: 8) - mutation from If_Statement to If_False
 - linkedList5.py: (l: 32, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - linkedList5.py: (l: 32, c: 19) - mutation from None to False
 - linkedList5.py: (l: 32, c: 19) - mutation from None to True
 - linkedList5.py: (l: 33, c: 19) - mutation from None to True
 - linkedList5.py: (l: 33, c: 19) - mutation from None to False
 - linkedList5.py: (l: 35, c: 8) - mutation from If_Statement to If_True
 - linkedList5.py: (l: 35, c: 8) - mutation from If_Statement to If_False
 - linkedList5.py: (l: 35, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - linkedList5.py: (l: 35, c: 24) - mutation from None to True
 - linkedList5.py: (l: 35, c: 24) - mutation from None to False
 - linkedList5.py: (l: 39, c: 14) - mutation from <class 'ast.IsNot'> to <class 'ast.Is'>
 - linkedList5.py: (l: 39, c: 36) - mutation from None to False
 - linkedList5.py: (l: 39, c: 36) - mutation from None to True
 - linkedList5.py: (l: 45, c: 8) - mutation from If_Statement to If_True
 - linkedList5.py: (l: 45, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - linkedList5.py: (l: 46, c: 19) - mutation from None to False
 - linkedList5.py: (l: 46, c: 19) - mutation from None to True
 - linkedList5.py: (l: 48, c: 14) - mutation from <class 'ast.IsNot'> to <class 'ast.Is'>
 - linkedList5.py: (l: 48, c: 31) - mutation from None to True
 - linkedList5.py: (l: 48, c: 31) - mutation from None to False
 - linkedList5.py: (l: 49, c: 12) - mutation from If_Statement to If_True
 - linkedList5.py: (l: 49, c: 12) - mutation from If_Statement to If_False
 - linkedList5.py: (l: 49, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - linkedList5.py: (l: 49, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - linkedList5.py: (l: 49, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - linkedList5.py: (l: 49, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - linkedList5.py: (l: 49, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - linkedList5.py: (l: 52, c: 15) - mutation from None to True
 - linkedList5.py: (l: 52, c: 15) - mutation from None to False
 - linkedList5.py: (l: 55, c: 8) - mutation from If_Statement to If_True
 - linkedList5.py: (l: 55, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - linkedList5.py: (l: 57, c: 8) - mutation from If_Statement to If_False
 - linkedList5.py: (l: 57, c: 8) - mutation from If_Statement to If_True
 - linkedList5.py: (l: 57, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - linkedList5.py: (l: 57, c: 24) - mutation from None to False
 - linkedList5.py: (l: 57, c: 24) - mutation from None to True
 - linkedList5.py: (l: 59, c: 8) - mutation from If_Statement to If_False
 - linkedList5.py: (l: 59, c: 8) - mutation from If_Statement to If_True
 - linkedList5.py: (l: 59, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - linkedList5.py: (l: 59, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - linkedList5.py: (l: 59, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - linkedList5.py: (l: 59, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - linkedList5.py: (l: 59, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - linkedList5.py: (l: 64, c: 14) - mutation from <class 'ast.IsNot'> to <class 'ast.Is'>
 - linkedList5.py: (l: 64, c: 31) - mutation from None to False
 - linkedList5.py: (l: 64, c: 31) - mutation from None to True
 - linkedList5.py: (l: 65, c: 12) - mutation from If_Statement to If_False
 - linkedList5.py: (l: 65, c: 12) - mutation from If_Statement to If_True
 - linkedList5.py: (l: 65, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - linkedList5.py: (l: 65, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - linkedList5.py: (l: 65, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - linkedList5.py: (l: 65, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - linkedList5.py: (l: 65, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - linkedList5.py: (l: 72, c: 8) - mutation from If_Statement to If_True
 - linkedList5.py: (l: 72, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - linkedList5.py: (l: 74, c: 8) - mutation from If_Statement to If_False
 - linkedList5.py: (l: 74, c: 8) - mutation from If_Statement to If_True
 - linkedList5.py: (l: 74, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - linkedList5.py: (l: 74, c: 24) - mutation from None to False
 - linkedList5.py: (l: 74, c: 24) - mutation from None to True
 - linkedList5.py: (l: 77, c: 8) - mutation from If_Statement to If_True
 - linkedList5.py: (l: 77, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - linkedList5.py: (l: 77, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - linkedList5.py: (l: 77, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - linkedList5.py: (l: 77, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - linkedList5.py: (l: 77, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - linkedList5.py: (l: 80, c: 14) - mutation from <class 'ast.IsNot'> to <class 'ast.Is'>
 - linkedList5.py: (l: 80, c: 36) - mutation from None to False
 - linkedList5.py: (l: 80, c: 36) - mutation from None to True
 - linkedList5.py: (l: 81, c: 12) - mutation from If_Statement to If_True
 - linkedList5.py: (l: 81, c: 12) - mutation from If_Statement to If_False
 - linkedList5.py: (l: 81, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - linkedList5.py: (l: 81, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - linkedList5.py: (l: 81, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - linkedList5.py: (l: 81, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - linkedList5.py: (l: 81, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - linkedList5.py: (l: 88, c: 14) - mutation from <class 'ast.IsNot'> to <class 'ast.Is'>
 - linkedList5.py: (l: 88, c: 31) - mutation from None to True
 - linkedList5.py: (l: 88, c: 31) - mutation from None to False
 - linkedList5.py: (l: 95, c: 14) - mutation from <class 'ast.IsNot'> to <class 'ast.Is'>
 - linkedList5.py: (l: 95, c: 31) - mutation from None to True
 - linkedList5.py: (l: 95, c: 31) - mutation from None to False