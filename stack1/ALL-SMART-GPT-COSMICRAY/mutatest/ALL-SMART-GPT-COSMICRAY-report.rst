Mutatest diagnostic summary
===========================
 - Source location: /home/lucca/desktop/ic/experimento/testes/python_experiments/stack1/stack1.py
 - Test commands: ['python', '-m', 'pytest', '--tb=no', './ALL-SMART-GPT-COSMICRAY']
 - Mode: f
 - Excluded files: []
 - N locations input: 10000
 - Random seed: 2023

Random sample details
---------------------
 - Total locations mutated: 35
 - Total locations identified: 35
 - Location sample coverage: 100.00 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:01.060983
 - Clean trial 2 run time: 0:00:00.812896
 - Mutation trials total run time: 0:01:23.600259

Overall mutation trial summary
==============================
 - DETECTED: 94
 - SURVIVED: 5
 - TOTAL RUNS: 99
 - RUN DATETIME: 2024-02-23 21:25:21.846448


Mutations by result status
==========================


SURVIVED
--------
 - stack1.py: (l: 15, c: 8) - mutation from If_Statement to If_False
 - stack1.py: (l: 15, c: 23) - mutation from None to False
 - stack1.py: (l: 15, c: 23) - mutation from None to True
 - stack1.py: (l: 72, c: 7) - mutation from <class 'ast.NotEq'> to <class 'ast.Gt'>
 - stack1.py: (l: 130, c: 7) - mutation from <class 'ast.Gt'> to <class 'ast.NotEq'>


DETECTED
--------
 - stack1.py: (l: 9, c: 20) - mutation from None to True
 - stack1.py: (l: 9, c: 20) - mutation from None to False
 - stack1.py: (l: 15, c: 8) - mutation from If_Statement to If_True
 - stack1.py: (l: 15, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - stack1.py: (l: 26, c: 8) - mutation from AugAssign_Add to AugAssign_Div
 - stack1.py: (l: 26, c: 8) - mutation from AugAssign_Add to AugAssign_Sub
 - stack1.py: (l: 26, c: 8) - mutation from AugAssign_Add to AugAssign_Mult
 - stack1.py: (l: 29, c: 8) - mutation from If_Statement to If_True
 - stack1.py: (l: 29, c: 8) - mutation from If_Statement to If_False
 - stack1.py: (l: 29, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - stack1.py: (l: 29, c: 23) - mutation from None to False
 - stack1.py: (l: 29, c: 23) - mutation from None to True
 - stack1.py: (l: 35, c: 12) - mutation from AugAssign_Sub to AugAssign_Add
 - stack1.py: (l: 35, c: 12) - mutation from AugAssign_Sub to AugAssign_Mult
 - stack1.py: (l: 35, c: 12) - mutation from AugAssign_Sub to AugAssign_Div
 - stack1.py: (l: 39, c: 8) - mutation from If_Statement to If_True
 - stack1.py: (l: 39, c: 8) - mutation from If_Statement to If_False
 - stack1.py: (l: 39, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - stack1.py: (l: 39, c: 23) - mutation from None to True
 - stack1.py: (l: 39, c: 23) - mutation from None to False
 - stack1.py: (l: 48, c: 20) - mutation from None to True
 - stack1.py: (l: 48, c: 20) - mutation from None to False
 - stack1.py: (l: 57, c: 8) - mutation from If_Statement to If_True
 - stack1.py: (l: 57, c: 8) - mutation from If_Statement to If_False
 - stack1.py: (l: 57, c: 11) - mutation from <class 'ast.In'> to <class 'ast.NotIn'>
 - stack1.py: (l: 61, c: 8) - mutation from If_Statement to If_True
 - stack1.py: (l: 61, c: 8) - mutation from If_Statement to If_False
 - stack1.py: (l: 61, c: 11) - mutation from <class 'ast.In'> to <class 'ast.NotIn'>
 - stack1.py: (l: 66, c: 16) - mutation from If_Statement to If_True
 - stack1.py: (l: 66, c: 16) - mutation from If_Statement to If_False
 - stack1.py: (l: 66, c: 19) - mutation from <class 'ast.NotEq'> to <class 'ast.GtE'>
 - stack1.py: (l: 66, c: 19) - mutation from <class 'ast.NotEq'> to <class 'ast.LtE'>
 - stack1.py: (l: 66, c: 19) - mutation from <class 'ast.NotEq'> to <class 'ast.Lt'>
 - stack1.py: (l: 66, c: 19) - mutation from <class 'ast.NotEq'> to <class 'ast.Eq'>
 - stack1.py: (l: 66, c: 19) - mutation from <class 'ast.NotEq'> to <class 'ast.Gt'>
 - stack1.py: (l: 67, c: 27) - mutation from False to True
 - stack1.py: (l: 67, c: 27) - mutation from False to None
 - stack1.py: (l: 70, c: 23) - mutation from False to None
 - stack1.py: (l: 70, c: 23) - mutation from False to True
 - stack1.py: (l: 72, c: 4) - mutation from If_Statement to If_True
 - stack1.py: (l: 72, c: 4) - mutation from If_Statement to If_False
 - stack1.py: (l: 72, c: 7) - mutation from <class 'ast.NotEq'> to <class 'ast.LtE'>
 - stack1.py: (l: 72, c: 7) - mutation from <class 'ast.NotEq'> to <class 'ast.Eq'>
 - stack1.py: (l: 72, c: 7) - mutation from <class 'ast.NotEq'> to <class 'ast.GtE'>
 - stack1.py: (l: 72, c: 7) - mutation from <class 'ast.NotEq'> to <class 'ast.Lt'>
 - stack1.py: (l: 73, c: 15) - mutation from False to None
 - stack1.py: (l: 73, c: 15) - mutation from False to True
 - stack1.py: (l: 76, c: 15) - mutation from True to None
 - stack1.py: (l: 76, c: 15) - mutation from True to False
 - stack1.py: (l: 94, c: 29) - mutation from <class 'ast.Add'> to <class 'ast.Mod'>
 - stack1.py: (l: 94, c: 29) - mutation from <class 'ast.Add'> to <class 'ast.Pow'>
 - stack1.py: (l: 94, c: 29) - mutation from <class 'ast.Add'> to <class 'ast.Div'>
 - stack1.py: (l: 94, c: 29) - mutation from <class 'ast.Add'> to <class 'ast.Mult'>
 - stack1.py: (l: 94, c: 29) - mutation from <class 'ast.Add'> to <class 'ast.FloorDiv'>
 - stack1.py: (l: 94, c: 29) - mutation from <class 'ast.Add'> to <class 'ast.Sub'>
 - stack1.py: (l: 95, c: 29) - mutation from <class 'ast.Sub'> to <class 'ast.Mult'>
 - stack1.py: (l: 95, c: 29) - mutation from <class 'ast.Sub'> to <class 'ast.Mod'>
 - stack1.py: (l: 95, c: 29) - mutation from <class 'ast.Sub'> to <class 'ast.Pow'>
 - stack1.py: (l: 95, c: 29) - mutation from <class 'ast.Sub'> to <class 'ast.Add'>
 - stack1.py: (l: 95, c: 29) - mutation from <class 'ast.Sub'> to <class 'ast.FloorDiv'>
 - stack1.py: (l: 95, c: 29) - mutation from <class 'ast.Sub'> to <class 'ast.Div'>
 - stack1.py: (l: 96, c: 29) - mutation from <class 'ast.Mult'> to <class 'ast.Sub'>
 - stack1.py: (l: 96, c: 29) - mutation from <class 'ast.Mult'> to <class 'ast.Mod'>
 - stack1.py: (l: 96, c: 29) - mutation from <class 'ast.Mult'> to <class 'ast.Pow'>
 - stack1.py: (l: 96, c: 29) - mutation from <class 'ast.Mult'> to <class 'ast.Add'>
 - stack1.py: (l: 96, c: 29) - mutation from <class 'ast.Mult'> to <class 'ast.FloorDiv'>
 - stack1.py: (l: 96, c: 29) - mutation from <class 'ast.Mult'> to <class 'ast.Div'>
 - stack1.py: (l: 97, c: 29) - mutation from <class 'ast.Div'> to <class 'ast.Mult'>
 - stack1.py: (l: 97, c: 29) - mutation from <class 'ast.Div'> to <class 'ast.Add'>
 - stack1.py: (l: 97, c: 29) - mutation from <class 'ast.Div'> to <class 'ast.Pow'>
 - stack1.py: (l: 97, c: 29) - mutation from <class 'ast.Div'> to <class 'ast.FloorDiv'>
 - stack1.py: (l: 97, c: 29) - mutation from <class 'ast.Div'> to <class 'ast.Mod'>
 - stack1.py: (l: 97, c: 29) - mutation from <class 'ast.Div'> to <class 'ast.Sub'>
 - stack1.py: (l: 98, c: 29) - mutation from <class 'ast.Mod'> to <class 'ast.FloorDiv'>
 - stack1.py: (l: 98, c: 29) - mutation from <class 'ast.Mod'> to <class 'ast.Sub'>
 - stack1.py: (l: 98, c: 29) - mutation from <class 'ast.Mod'> to <class 'ast.Mult'>
 - stack1.py: (l: 98, c: 29) - mutation from <class 'ast.Mod'> to <class 'ast.Div'>
 - stack1.py: (l: 98, c: 29) - mutation from <class 'ast.Mod'> to <class 'ast.Pow'>
 - stack1.py: (l: 98, c: 29) - mutation from <class 'ast.Mod'> to <class 'ast.Add'>
 - stack1.py: (l: 99, c: 29) - mutation from <class 'ast.Pow'> to <class 'ast.Sub'>
 - stack1.py: (l: 99, c: 29) - mutation from <class 'ast.Pow'> to <class 'ast.Div'>
 - stack1.py: (l: 99, c: 29) - mutation from <class 'ast.Pow'> to <class 'ast.FloorDiv'>
 - stack1.py: (l: 99, c: 29) - mutation from <class 'ast.Pow'> to <class 'ast.Add'>
 - stack1.py: (l: 99, c: 29) - mutation from <class 'ast.Pow'> to <class 'ast.Mod'>
 - stack1.py: (l: 99, c: 29) - mutation from <class 'ast.Pow'> to <class 'ast.Mult'>
 - stack1.py: (l: 106, c: 8) - mutation from If_Statement to If_False
 - stack1.py: (l: 106, c: 8) - mutation from If_Statement to If_True
 - stack1.py: (l: 106, c: 11) - mutation from <class 'ast.In'> to <class 'ast.NotIn'>
 - stack1.py: (l: 130, c: 4) - mutation from If_Statement to If_False
 - stack1.py: (l: 130, c: 4) - mutation from If_Statement to If_True
 - stack1.py: (l: 130, c: 7) - mutation from <class 'ast.Gt'> to <class 'ast.GtE'>
 - stack1.py: (l: 130, c: 7) - mutation from <class 'ast.Gt'> to <class 'ast.Eq'>
 - stack1.py: (l: 130, c: 7) - mutation from <class 'ast.Gt'> to <class 'ast.LtE'>
 - stack1.py: (l: 130, c: 7) - mutation from <class 'ast.Gt'> to <class 'ast.Lt'>