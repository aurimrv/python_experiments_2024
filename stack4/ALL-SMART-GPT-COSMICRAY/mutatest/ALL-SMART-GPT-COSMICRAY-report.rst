Mutatest diagnostic summary
===========================
 - Source location: /home/lucca/desktop/ic/experimento/testes/python_experiments/stack4/stack4.py
 - Test commands: ['python', '-m', 'pytest', '--tb=no', './ALL-SMART-GPT-COSMICRAY']
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
 - Clean trial 1 run time: 0:00:00.554580
 - Clean trial 2 run time: 0:00:00.460738
 - Mutation trials total run time: 0:00:29.678429

Overall mutation trial summary
==============================
 - SURVIVED: 6
 - DETECTED: 54
 - TOTAL RUNS: 60
 - RUN DATETIME: 2024-02-25 13:28:20.372880


Mutations by result status
==========================


SURVIVED
--------
 - stack4.py: (l: 9, c: 39) - mutation from None to True
 - stack4.py: (l: 9, c: 39) - mutation from None to False
 - stack4.py: (l: 29, c: 28) - mutation from None to False
 - stack4.py: (l: 63, c: 12) - mutation from If_Statement to If_True
 - stack4.py: (l: 101, c: 28) - mutation from None to True
 - stack4.py: (l: 101, c: 28) - mutation from None to False


DETECTED
--------
 - stack4.py: (l: 29, c: 28) - mutation from None to True
 - stack4.py: (l: 32, c: 20) - mutation from None to True
 - stack4.py: (l: 32, c: 20) - mutation from None to False
 - stack4.py: (l: 37, c: 12) - mutation from If_Statement to If_False
 - stack4.py: (l: 37, c: 12) - mutation from If_Statement to If_True
 - stack4.py: (l: 44, c: 8) - mutation from AugAssign_Add to AugAssign_Div
 - stack4.py: (l: 44, c: 8) - mutation from AugAssign_Add to AugAssign_Mult
 - stack4.py: (l: 44, c: 8) - mutation from AugAssign_Add to AugAssign_Sub
 - stack4.py: (l: 48, c: 8) - mutation from If_Statement to If_False
 - stack4.py: (l: 48, c: 8) - mutation from If_Statement to If_True
 - stack4.py: (l: 52, c: 8) - mutation from AugAssign_Sub to AugAssign_Add
 - stack4.py: (l: 52, c: 8) - mutation from AugAssign_Sub to AugAssign_Mult
 - stack4.py: (l: 52, c: 8) - mutation from AugAssign_Sub to AugAssign_Div
 - stack4.py: (l: 63, c: 12) - mutation from If_Statement to If_False
 - stack4.py: (l: 63, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - stack4.py: (l: 63, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - stack4.py: (l: 63, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - stack4.py: (l: 63, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - stack4.py: (l: 63, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - stack4.py: (l: 70, c: 8) - mutation from If_Statement to If_False
 - stack4.py: (l: 70, c: 8) - mutation from If_Statement to If_True
 - stack4.py: (l: 70, c: 11) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - stack4.py: (l: 70, c: 20) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - stack4.py: (l: 72, c: 12) - mutation from AugAssign_Sub to AugAssign_Add
 - stack4.py: (l: 72, c: 12) - mutation from AugAssign_Sub to AugAssign_Mult
 - stack4.py: (l: 72, c: 12) - mutation from AugAssign_Sub to AugAssign_Div
 - stack4.py: (l: 74, c: 12) - mutation from If_Statement to If_True
 - stack4.py: (l: 74, c: 12) - mutation from If_Statement to If_False
 - stack4.py: (l: 74, c: 16) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - stack4.py: (l: 74, c: 30) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - stack4.py: (l: 74, c: 30) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - stack4.py: (l: 74, c: 30) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - stack4.py: (l: 74, c: 30) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - stack4.py: (l: 74, c: 30) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - stack4.py: (l: 76, c: 16) - mutation from AugAssign_Sub to AugAssign_Mult
 - stack4.py: (l: 76, c: 16) - mutation from AugAssign_Sub to AugAssign_Div
 - stack4.py: (l: 76, c: 16) - mutation from AugAssign_Sub to AugAssign_Add
 - stack4.py: (l: 84, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - stack4.py: (l: 84, c: 12) - mutation from AugAssign_Add to AugAssign_Sub
 - stack4.py: (l: 84, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - stack4.py: (l: 84, c: 23) - mutation from <class 'ast.Add'> to <class 'ast.FloorDiv'>
 - stack4.py: (l: 84, c: 23) - mutation from <class 'ast.Add'> to <class 'ast.Pow'>
 - stack4.py: (l: 84, c: 23) - mutation from <class 'ast.Add'> to <class 'ast.Div'>
 - stack4.py: (l: 84, c: 23) - mutation from <class 'ast.Add'> to <class 'ast.Mod'>
 - stack4.py: (l: 84, c: 23) - mutation from <class 'ast.Add'> to <class 'ast.Sub'>
 - stack4.py: (l: 84, c: 23) - mutation from <class 'ast.Add'> to <class 'ast.Mult'>
 - stack4.py: (l: 86, c: 15) - mutation from Slice_UnboundLower to Slice_UnboundUpper
 - stack4.py: (l: 86, c: 15) - mutation from Slice_UnboundLower to Slice_Unbounded
 - stack4.py: (l: 86, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Pow'>
 - stack4.py: (l: 86, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Div'>
 - stack4.py: (l: 86, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Sub'>
 - stack4.py: (l: 86, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Mult'>
 - stack4.py: (l: 86, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.FloorDiv'>
 - stack4.py: (l: 86, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Mod'>