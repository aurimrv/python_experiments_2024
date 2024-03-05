Mutatest diagnostic summary
===========================
 - Source location: /home/lucca/desktop/ic/experimento/testes/python_experiments/stack2/ALL-SMART-GPT-MUTATEST/stack2.py
 - Test commands: ['python', '-m', 'pytest', '--tb=no']
 - Mode: f
 - Excluded files: []
 - N locations input: 10000
 - Random seed: 2023

Random sample details
---------------------
 - Total locations mutated: 3
 - Total locations identified: 3
 - Location sample coverage: 100.00 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.640995
 - Clean trial 2 run time: 0:00:00.656975
 - Mutation trials total run time: 0:00:08.063967

Overall mutation trial summary
==============================
 - DETECTED: 12
 - SURVIVED: 1
 - TOTAL RUNS: 13
 - RUN DATETIME: 2023-12-14 08:38:14.498382


Mutations by result status
==========================


SURVIVED
--------
 - stack2.py: (l: 13, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>


DETECTED
--------
 - stack2.py: (l: 13, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - stack2.py: (l: 13, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - stack2.py: (l: 13, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - stack2.py: (l: 13, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - stack2.py: (l: 21, c: 8) - mutation from If_Statement to If_False
 - stack2.py: (l: 21, c: 8) - mutation from If_Statement to If_True
 - stack2.py: (l: 27, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Mult'>
 - stack2.py: (l: 27, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Mod'>
 - stack2.py: (l: 27, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Div'>
 - stack2.py: (l: 27, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Sub'>
 - stack2.py: (l: 27, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Pow'>
 - stack2.py: (l: 27, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.FloorDiv'>