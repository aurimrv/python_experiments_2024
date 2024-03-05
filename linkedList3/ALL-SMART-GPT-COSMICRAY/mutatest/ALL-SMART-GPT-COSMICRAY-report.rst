Mutatest diagnostic summary
===========================
 - Source location: /home/lucca/desktop/ic/experimento/testes/python_experiments/linkedList3/linkedList3.py
 - Test commands: ['python', '-m', 'pytest', '--tb=no', './ALL-SMART-GPT-COSMICRAY']
 - Mode: f
 - Excluded files: []
 - N locations input: 10000
 - Random seed: 2023

Random sample details
---------------------
 - Total locations mutated: 18
 - Total locations identified: 18
 - Location sample coverage: 100.00 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.873831
 - Clean trial 2 run time: 0:00:00.709278
 - Mutation trials total run time: 0:00:44.251704

Overall mutation trial summary
==============================
 - DETECTED: 40
 - SURVIVED: 5
 - TIMEOUT: 2
 - TOTAL RUNS: 47
 - RUN DATETIME: 2024-02-23 21:21:09.760166


Mutations by result status
==========================


SURVIVED
--------
 - linkedList3.py: (l: 21, c: 31) - mutation from None to True
 - linkedList3.py: (l: 21, c: 31) - mutation from None to False
 - linkedList3.py: (l: 40, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - linkedList3.py: (l: 42, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - linkedList3.py: (l: 77, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>


TIMEOUT
-------
 - linkedList3.py: (l: 26, c: 8) - mutation from If_Statement to If_False
 - linkedList3.py: (l: 26, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>


DETECTED
--------
 - linkedList3.py: (l: 12, c: 20) - mutation from None to True
 - linkedList3.py: (l: 12, c: 20) - mutation from None to False
 - linkedList3.py: (l: 17, c: 31) - mutation from None to True
 - linkedList3.py: (l: 17, c: 31) - mutation from None to False
 - linkedList3.py: (l: 29, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - linkedList3.py: (l: 29, c: 12) - mutation from AugAssign_Add to AugAssign_Sub
 - linkedList3.py: (l: 29, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - linkedList3.py: (l: 34, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - linkedList3.py: (l: 34, c: 12) - mutation from AugAssign_Add to AugAssign_Sub
 - linkedList3.py: (l: 34, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - linkedList3.py: (l: 40, c: 8) - mutation from If_Statement to If_False
 - linkedList3.py: (l: 40, c: 8) - mutation from If_Statement to If_True
 - linkedList3.py: (l: 40, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - linkedList3.py: (l: 40, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - linkedList3.py: (l: 40, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - linkedList3.py: (l: 40, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - linkedList3.py: (l: 41, c: 19) - mutation from None to False
 - linkedList3.py: (l: 41, c: 19) - mutation from None to True
 - linkedList3.py: (l: 42, c: 8) - mutation from If_Statement to If_True
 - linkedList3.py: (l: 42, c: 8) - mutation from If_Statement to If_False
 - linkedList3.py: (l: 42, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - linkedList3.py: (l: 42, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - linkedList3.py: (l: 42, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - linkedList3.py: (l: 42, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - linkedList3.py: (l: 44, c: 35) - mutation from None to False
 - linkedList3.py: (l: 44, c: 35) - mutation from None to True
 - linkedList3.py: (l: 46, c: 12) - mutation from AugAssign_Sub to AugAssign_Div
 - linkedList3.py: (l: 46, c: 12) - mutation from AugAssign_Sub to AugAssign_Mult
 - linkedList3.py: (l: 46, c: 12) - mutation from AugAssign_Sub to AugAssign_Add
 - linkedList3.py: (l: 52, c: 12) - mutation from AugAssign_Sub to AugAssign_Div
 - linkedList3.py: (l: 52, c: 12) - mutation from AugAssign_Sub to AugAssign_Mult
 - linkedList3.py: (l: 52, c: 12) - mutation from AugAssign_Sub to AugAssign_Add
 - linkedList3.py: (l: 77, c: 15) - mutation from True to False
 - linkedList3.py: (l: 77, c: 15) - mutation from True to None
 - linkedList3.py: (l: 77, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - linkedList3.py: (l: 77, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - linkedList3.py: (l: 77, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - linkedList3.py: (l: 77, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - linkedList3.py: (l: 77, c: 45) - mutation from False to None
 - linkedList3.py: (l: 77, c: 45) - mutation from False to True