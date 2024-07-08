# Python Experiments

Repository to store data and scripts relate to Python programs experiments for ISSRE'2024 submission.

## Repository Content

This repository is organized as follows:

```
python_experiments_2024/
├── 00-Scripts                      => scripts utilized in the experiment
├── 01-CompliedReports              => organized general reports
├── 02-UncompiledReports            => general reports
├── 03-CrossExaminationData         => mutation score data
├── binarySearchTree1               => subject
├── binarySearchTree2               => subject
├── binarySearchTree3               => subject
├── binarySearchTree4               => subject
├── files-full.txt                  => defines the files under evaluation
├── files.txt                       => defines the files under evaluation
├── identifier1                     => subject
├── LICENSE                         => licensing iformation
├── linkedList1                     => subject
├── linkedList2                     => subject
├── linkedList3                     => subject
├── linkedList4                     => subject
├── linkedList5                     => subject
├── MapeamentoDosProjetos.txt       => source of subject programs
├── mutation-tools-full.txt         => defines the mutation tool under evaluation
├── mutation-tools.txt              => defines the mutation tool under evaluation
├── queue1                          => subject
├── queue2                          => subject
├── queue3                          => subject
├── queue4                          => subject
├── queue5                          => subject
├── random-test-set-size.txt        => Information about random test sizes
├── README.md                       => (this file)
├── requirements.txt                => Python packages required for running the experiment
├── sort1                           => subject
├── stack1                          => subject
├── stack2                          => subject
├── stack3                          => subject
├── stack4                          => subject
├── stack5                          => subject
├── test-set-cosmicray.txt          => defines the test-set under evaluation
├── test-set-mutatest.txt           => defines the test-set under evaluation
├── test-set-mutmut.txt             => defines the test-set under evaluation
├── test-set-mutpy.txt              => defines the test-set under evaluation
├── test-sets-full.txt              => defines the test-set under evaluation
├── test-sets.txt                   => defines the test-set under evaluation
```

The content of a given subject is as show below:

```
python_experiments_2024/binarySearchTree1/
├── ALL-SMART
├── ALL-SMART-GPT-COSMICRAY
├── ALL-SMART-GPT-MUTATEST
├── ALL-SMART-GPT-MUTMUT
├── ALL-SMART-GPT-MUTPY
├── binarySearchTree1.py
├── binarySearchTree1.toml
├── DYNAMOSA
├── DYNAMOSA-MIO
├── DYNAMOSA-MIO-MOSA
├── DYNAMOSA-MIO-WHOLE_SUITE
├── DYNAMOSA-MOSA
├── DYNAMOSA-MOSA-WHOLE_SUITE
├── DYNAMOSA-WHOLE_SUITE
├── metrics
├── MIO
├── MIO-MOSA
├── MIO-MOSA-WHOLE_SUITE
├── MIO-WHOLE_SUITE
├── MOSA
├── MOSA-WHOLE_SUITE
├── pynguin-report
├── RANDOM
├── test_binarySearchTree1.py
└── WHOLE_SUITE
```

## LLM Prompts for Test Generation

In order to achieve adequate test sets, the following prompts were used for chat-gpt 3.5 to generate tests:

Firstly, a general prompt to create initial tests:

```
Consider this code to create tests in the Pytest format, the tests must cover all methods {code}
```

After executing the initially generated tests, if an error occurs in Pytest, the following prompt is fed back to the LLM:
```
The test you have given me returned this error message {error message}, return me the corrected test sets
```

Finally, when executing the mutation tool, if there are still living mutants, the following prompt is fed back to the LLM:
```
I am trying to kill mutants in a specific method, give me a test that covers all lines of this method {method}
```

Therefore, if there are still living mutants, the next step is a manual analysis to identify equivalent mutants.

## Example of Commands to Run the Tools

Given examples for the module to be mutated = Identifier.py


### Pynguin 0.27.0

First, set the security variable
```
    export PYNGUIN_DANGER_AWARE=1
```
Generate tests, mutations, and reports
```
    pynguin --project-path ./ --output-path ./output --module name Identifier -v
extra parameters
    --create-coverage-report True --algorithm=DYNAMOSA --seed 1234
```

valid algorithms `DYNAMOSA(default)`, `MIO`, `MOSA`, `RANDOM`, `WHOLE_SUITE`


### Script to remove `xfail` marks

Parser tc_transformer.py

Function: remove xfail marks and the last line of marked codes

Run parser on code and generate output

```
    python3 tc_transformer.py test_Identifier.py > test_Identifier_parsed.py
```

For pytest

```
	python3 -m pytest test_Identifier_parsed.py
```

-------------------------------------------------------------------------------------

### Coverage.py 5.5

For tests in unittest format
```
		coverage run --source=Identifier --branch -m pytest test_Identifier_parsed.py
```

For generating reports
```
	coverage report
	coverage html -d coverage
```


### Mut.py 0.6.1

Run Mutpy and generate report

```
	time mut.py -t Identifier.py -u test_Identifier_parsed.py --runner pytest --report-html mutpy
```

<<<<<<< HEAD
### Mutmut 2.4.1

Run Mutmut

```
    time mutmut run --paths-to-mutate Identifier.py --tests-dir test_Identifier_parsed.py --runner 'python3 -m pytest test_validate.py'
```

For generating reports
```
    mutmut html
```


### Mutatest 3.1.0

Run Mutatest and generate report 
```
    time mutatest -s Identifier.py -t pytest -m f -o mutatest/name-report.rst
```    
(runs all files with test_ in the folder)


### Cosmic-ray 8.3.5

Create new config
```
    cosmic-ray new-config tests.toml
    
    [?] Top-level module path: Identifier.py
    [?] Test execution timeout (seconds): 20
    [?] Test command: python -m pytest test_Identifier_parsed.py
    -- MENU: Distributor --
      (0) http
      (1) local
    [?] Enter menu selection: 1
```

Initialize session

```
    cosmic-ray init tests.toml tests.sqlite
```
Run session
```
    cosmic-ray exec tests.toml tests.sqlite
```

Create report
```
    cr-report testes.sqlite > report.html
```
=======
for alg in $(cat test-sets.txt); do echo ${alg}; ./scripts/coverageReport.sh path-to-subjects files.txt ${alg};./scripts/coverageSummary.py path-to-subjects files.txt ${alg}; done
>>>>>>> 9c1fb8fc69cefba3ad6335a1fec1d03ead1d57a8
