Mutatest diagnostic summary
===========================
 - Source location: /home/lucca/desktop/ic/experimento/testes/python_experiments/linkedList1/ALL-SMART-GPT-MUTATEST/linkedList1.py
 - Test commands: ['python', '-m', 'pytest', '--tb=no']
 - Mode: f
 - Excluded files: []
 - N locations input: 10000
 - Random seed: 2023

Random sample details
---------------------
 - Total locations mutated: 51
 - Total locations identified: 51
 - Location sample coverage: 100.00 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.484322
 - Clean trial 2 run time: 0:00:00.425379
 - Mutation trials total run time: 0:00:54.070349

Overall mutation trial summary
==============================
 - DETECTED: 117
 - SURVIVED: 5
 - TOTAL RUNS: 122
 - RUN DATETIME: 2024-02-07 07:16:06.012019


Mutations by result status
==========================


SURVIVED
--------
 - linkedList1.py: (l: 21, c: 8) - mutation from If_Statement to If_True
 - linkedList1.py: (l: 21, c: 28) - mutation from None to True
 - linkedList1.py: (l: 21, c: 28) - mutation from None to False
 - linkedList1.py: (l: 130, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - linkedList1.py: (l: 134, c: 17) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>


DETECTED
--------
 - linkedList1.py: (l: 10, c: 20) - mutation from None to True
 - linkedList1.py: (l: 10, c: 20) - mutation from None to False
 - linkedList1.py: (l: 12, c: 22) - mutation from None to True
 - linkedList1.py: (l: 12, c: 22) - mutation from None to False
 - linkedList1.py: (l: 21, c: 8) - mutation from If_Statement to If_False
 - linkedList1.py: (l: 21, c: 11) - mutation from <class 'ast.IsNot'> to <class 'ast.Is'>
 - linkedList1.py: (l: 23, c: 18) - mutation from <class 'ast.IsNot'> to <class 'ast.Is'>
 - linkedList1.py: (l: 23, c: 29) - mutation from None to False
 - linkedList1.py: (l: 23, c: 29) - mutation from None to True
 - linkedList1.py: (l: 24, c: 16) - mutation from If_Statement to If_False
 - linkedList1.py: (l: 24, c: 16) - mutation from If_Statement to If_True
 - linkedList1.py: (l: 24, c: 19) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - linkedList1.py: (l: 25, c: 27) - mutation from True to False
 - linkedList1.py: (l: 25, c: 27) - mutation from True to None
 - linkedList1.py: (l: 27, c: 15) - mutation from False to True
 - linkedList1.py: (l: 27, c: 15) - mutation from False to None
 - linkedList1.py: (l: 35, c: 8) - mutation from If_Statement to If_False
 - linkedList1.py: (l: 35, c: 8) - mutation from If_Statement to If_True
 - linkedList1.py: (l: 35, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.LtE'>
 - linkedList1.py: (l: 35, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.Gt'>
 - linkedList1.py: (l: 35, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.Lt'>
 - linkedList1.py: (l: 35, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.NotEq'>
 - linkedList1.py: (l: 35, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.Eq'>
 - linkedList1.py: (l: 35, c: 11) - mutation from <class 'ast.Or'> to <class 'ast.And'>
 - linkedList1.py: (l: 35, c: 33) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - linkedList1.py: (l: 35, c: 33) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - linkedList1.py: (l: 35, c: 33) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - linkedList1.py: (l: 35, c: 33) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - linkedList1.py: (l: 35, c: 33) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - linkedList1.py: (l: 44, c: 8) - mutation from If_Statement to If_False
 - linkedList1.py: (l: 44, c: 8) - mutation from If_Statement to If_True
 - linkedList1.py: (l: 44, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.Eq'>
 - linkedList1.py: (l: 44, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.Lt'>
 - linkedList1.py: (l: 44, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.Gt'>
 - linkedList1.py: (l: 44, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.NotEq'>
 - linkedList1.py: (l: 44, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.LtE'>
 - linkedList1.py: (l: 44, c: 11) - mutation from <class 'ast.Or'> to <class 'ast.And'>
 - linkedList1.py: (l: 44, c: 33) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - linkedList1.py: (l: 44, c: 33) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - linkedList1.py: (l: 44, c: 33) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - linkedList1.py: (l: 44, c: 33) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - linkedList1.py: (l: 44, c: 33) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - linkedList1.py: (l: 53, c: 8) - mutation from If_Statement to If_True
 - linkedList1.py: (l: 53, c: 8) - mutation from If_Statement to If_False
 - linkedList1.py: (l: 53, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - linkedList1.py: (l: 53, c: 26) - mutation from None to True
 - linkedList1.py: (l: 53, c: 26) - mutation from None to False
 - linkedList1.py: (l: 65, c: 8) - mutation from If_Statement to If_True
 - linkedList1.py: (l: 65, c: 8) - mutation from If_Statement to If_False
 - linkedList1.py: (l: 65, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - linkedList1.py: (l: 65, c: 24) - mutation from None to True
 - linkedList1.py: (l: 65, c: 24) - mutation from None to False
 - linkedList1.py: (l: 71, c: 18) - mutation from <class 'ast.IsNot'> to <class 'ast.Is'>
 - linkedList1.py: (l: 71, c: 35) - mutation from None to False
 - linkedList1.py: (l: 71, c: 35) - mutation from None to True
 - linkedList1.py: (l: 80, c: 8) - mutation from AugAssign_Add to AugAssign_Div
 - linkedList1.py: (l: 80, c: 8) - mutation from AugAssign_Add to AugAssign_Mult
 - linkedList1.py: (l: 80, c: 8) - mutation from AugAssign_Add to AugAssign_Sub
 - linkedList1.py: (l: 86, c: 20) - mutation from None to False
 - linkedList1.py: (l: 86, c: 20) - mutation from None to True
 - linkedList1.py: (l: 95, c: 8) - mutation from If_Statement to If_False
 - linkedList1.py: (l: 95, c: 8) - mutation from If_Statement to If_True
 - linkedList1.py: (l: 95, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - linkedList1.py: (l: 95, c: 31) - mutation from None to False
 - linkedList1.py: (l: 95, c: 31) - mutation from None to True
 - linkedList1.py: (l: 107, c: 8) - mutation from If_Statement to If_True
 - linkedList1.py: (l: 107, c: 8) - mutation from If_Statement to If_False
 - linkedList1.py: (l: 107, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - linkedList1.py: (l: 107, c: 24) - mutation from None to False
 - linkedList1.py: (l: 107, c: 24) - mutation from None to True
 - linkedList1.py: (l: 113, c: 18) - mutation from <class 'ast.IsNot'> to <class 'ast.Is'>
 - linkedList1.py: (l: 113, c: 35) - mutation from None to False
 - linkedList1.py: (l: 113, c: 35) - mutation from None to True
 - linkedList1.py: (l: 120, c: 8) - mutation from AugAssign_Add to AugAssign_Mult
 - linkedList1.py: (l: 120, c: 8) - mutation from AugAssign_Add to AugAssign_Sub
 - linkedList1.py: (l: 120, c: 8) - mutation from AugAssign_Add to AugAssign_Div
 - linkedList1.py: (l: 123, c: 8) - mutation from If_Statement to If_False
 - linkedList1.py: (l: 123, c: 8) - mutation from If_Statement to If_True
 - linkedList1.py: (l: 123, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.Gt'>
 - linkedList1.py: (l: 123, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.NotEq'>
 - linkedList1.py: (l: 123, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.Eq'>
 - linkedList1.py: (l: 123, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.Lt'>
 - linkedList1.py: (l: 123, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.LtE'>
 - linkedList1.py: (l: 125, c: 8) - mutation from If_Statement to If_True
 - linkedList1.py: (l: 125, c: 8) - mutation from If_Statement to If_False
 - linkedList1.py: (l: 125, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - linkedList1.py: (l: 125, c: 24) - mutation from None to False
 - linkedList1.py: (l: 125, c: 24) - mutation from None to True
 - linkedList1.py: (l: 130, c: 12) - mutation from If_Statement to If_True
 - linkedList1.py: (l: 130, c: 12) - mutation from If_Statement to If_False
 - linkedList1.py: (l: 130, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - linkedList1.py: (l: 130, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - linkedList1.py: (l: 130, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - linkedList1.py: (l: 130, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - linkedList1.py: (l: 130, c: 24) - mutation from <class 'ast.Sub'> to <class 'ast.Div'>
 - linkedList1.py: (l: 130, c: 24) - mutation from <class 'ast.Sub'> to <class 'ast.Add'>
 - linkedList1.py: (l: 130, c: 24) - mutation from <class 'ast.Sub'> to <class 'ast.Mult'>
 - linkedList1.py: (l: 130, c: 24) - mutation from <class 'ast.Sub'> to <class 'ast.Pow'>
 - linkedList1.py: (l: 130, c: 24) - mutation from <class 'ast.Sub'> to <class 'ast.FloorDiv'>
 - linkedList1.py: (l: 130, c: 24) - mutation from <class 'ast.Sub'> to <class 'ast.Mod'>
 - linkedList1.py: (l: 134, c: 12) - mutation from If_Statement to If_True
 - linkedList1.py: (l: 134, c: 12) - mutation from If_Statement to If_False
 - linkedList1.py: (l: 134, c: 17) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - linkedList1.py: (l: 134, c: 17) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - linkedList1.py: (l: 134, c: 17) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - linkedList1.py: (l: 134, c: 17) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - linkedList1.py: (l: 151, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.Div'>
 - linkedList1.py: (l: 151, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.Add'>
 - linkedList1.py: (l: 151, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.FloorDiv'>
 - linkedList1.py: (l: 151, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.Mod'>
 - linkedList1.py: (l: 151, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.Pow'>
 - linkedList1.py: (l: 151, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.Mult'>
 - linkedList1.py: (l: 171, c: 8) - mutation from AugAssign_Add to AugAssign_Sub
 - linkedList1.py: (l: 171, c: 8) - mutation from AugAssign_Add to AugAssign_Mult
 - linkedList1.py: (l: 171, c: 8) - mutation from AugAssign_Add to AugAssign_Div
 - linkedList1.py: (l: 178, c: 20) - mutation from None to False
 - linkedList1.py: (l: 178, c: 20) - mutation from None to True