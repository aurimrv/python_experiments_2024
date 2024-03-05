Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/binarySearchTree3/binarySearchTree3.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MIO']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 116
 - Location sample coverage: 8.62 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:02.688050
 - Clean trial 2 run time: 0:00:01.685665
 - Mutation trials total run time: 0:01:02.198859

Overall mutation trial summary
==============================
 - DETECTED: 19
 - SURVIVED: 10
 - TOTAL RUNS: 29
 - RUN DATETIME: 2023-03-05 12:18:02.951347


Mutations by result status
==========================


SURVIVED
--------
 - binarySearchTree3.py: (l: 58, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree3.py: (l: 63, c: 24) - mutation from None to False
 - binarySearchTree3.py: (l: 63, c: 24) - mutation from None to True
 - binarySearchTree3.py: (l: 102, c: 16) - mutation from If_Statement to If_True
 - binarySearchTree3.py: (l: 102, c: 16) - mutation from If_Statement to If_False
 - binarySearchTree3.py: (l: 102, c: 21) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - binarySearchTree3.py: (l: 159, c: 40) - mutation from None to False
 - binarySearchTree3.py: (l: 263, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - binarySearchTree3.py: (l: 401, c: 40) - mutation from None to False
 - binarySearchTree3.py: (l: 401, c: 40) - mutation from None to True


DETECTED
--------
 - binarySearchTree3.py: (l: 58, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree3.py: (l: 159, c: 40) - mutation from None to True
 - binarySearchTree3.py: (l: 263, c: 12) - mutation from If_Statement to If_True
 - binarySearchTree3.py: (l: 263, c: 12) - mutation from If_Statement to If_False
 - binarySearchTree3.py: (l: 263, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - binarySearchTree3.py: (l: 263, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - binarySearchTree3.py: (l: 263, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - binarySearchTree3.py: (l: 263, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - binarySearchTree3.py: (l: 271, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - binarySearchTree3.py: (l: 271, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - binarySearchTree3.py: (l: 271, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - binarySearchTree3.py: (l: 271, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - binarySearchTree3.py: (l: 271, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - binarySearchTree3.py: (l: 306, c: 15) - mutation from <class 'ast.Sub'> to <class 'ast.Add'>
 - binarySearchTree3.py: (l: 306, c: 15) - mutation from <class 'ast.Sub'> to <class 'ast.FloorDiv'>
 - binarySearchTree3.py: (l: 306, c: 15) - mutation from <class 'ast.Sub'> to <class 'ast.Mod'>
 - binarySearchTree3.py: (l: 306, c: 15) - mutation from <class 'ast.Sub'> to <class 'ast.Mult'>
 - binarySearchTree3.py: (l: 306, c: 15) - mutation from <class 'ast.Sub'> to <class 'ast.Div'>
 - binarySearchTree3.py: (l: 306, c: 15) - mutation from <class 'ast.Sub'> to <class 'ast.Pow'>