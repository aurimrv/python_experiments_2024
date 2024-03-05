Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/linkedList1/linkedList1.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MIO-WHOLE_SUITE']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 53
 - Location sample coverage: 18.87 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.549101
 - Clean trial 2 run time: 0:00:00.274230
 - Mutation trials total run time: 0:00:10.987270

Overall mutation trial summary
==============================
 - DETECTED: 20
 - SURVIVED: 4
 - ERROR: 1
 - TOTAL RUNS: 25
 - RUN DATETIME: 2023-03-12 11:33:52.072886


Mutations by result status
==========================


SURVIVED
--------
 - linkedList1.py: (l: 151, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.Mult'>
 - linkedList1.py: (l: 151, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.Mod'>
 - linkedList1.py: (l: 151, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.Pow'>
 - linkedList1.py: (l: 151, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.FloorDiv'>


DETECTED
--------
 - linkedList1.py: (l: 10, c: 20) - mutation from None to True
 - linkedList1.py: (l: 10, c: 20) - mutation from None to False
 - linkedList1.py: (l: 35, c: 11) - mutation from <class 'ast.Or'> to <class 'ast.And'>
 - linkedList1.py: (l: 53, c: 26) - mutation from None to True
 - linkedList1.py: (l: 53, c: 26) - mutation from None to False
 - linkedList1.py: (l: 65, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - linkedList1.py: (l: 113, c: 35) - mutation from None to True
 - linkedList1.py: (l: 113, c: 35) - mutation from None to False
 - linkedList1.py: (l: 125, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - linkedList1.py: (l: 130, c: 24) - mutation from <class 'ast.Sub'> to <class 'ast.FloorDiv'>
 - linkedList1.py: (l: 130, c: 24) - mutation from <class 'ast.Sub'> to <class 'ast.Pow'>
 - linkedList1.py: (l: 130, c: 24) - mutation from <class 'ast.Sub'> to <class 'ast.Add'>
 - linkedList1.py: (l: 130, c: 24) - mutation from <class 'ast.Sub'> to <class 'ast.Div'>
 - linkedList1.py: (l: 130, c: 24) - mutation from <class 'ast.Sub'> to <class 'ast.Mod'>
 - linkedList1.py: (l: 130, c: 24) - mutation from <class 'ast.Sub'> to <class 'ast.Mult'>
 - linkedList1.py: (l: 151, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.Add'>
 - linkedList1.py: (l: 151, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.Div'>
 - linkedList1.py: (l: 171, c: 8) - mutation from AugAssign_Add to AugAssign_Mult
 - linkedList1.py: (l: 171, c: 8) - mutation from AugAssign_Add to AugAssign_Sub
 - linkedList1.py: (l: 171, c: 8) - mutation from AugAssign_Add to AugAssign_Div


ERROR
-----
 - linkedList1.py: (l: 180, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>