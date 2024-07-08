#########################################################
# Script for collecting static metrics for a set of 
# Python files
# Requires radon (https://pypi.org/project/radon/) 
#########################################################

import sys
import os
from bs4 import BeautifulSoup as bs
import re
import json

def main():
	if len(sys.argv) < 3:
		print("error: 00metricsCalculation.py <project root dir>  <test-set-file>")
		print("Example: python 00metricsCalculation.py /path files.txt")
		sys.exit(1)

	baseDir = sys.argv[1]
	testSetFile =  sys.argv[2]

	prjList = baseDir+"/"+testSetFile
	prjReport = baseDir+"/report-radon-metrics.csv"

	dados = open(prjList, 'r')
	output = open(prjReport, 'w') 

	output.write("prj;classes;methods;cc;rank_cc;lloc;sloc;mi;rank_mi;h1;h2;N1;N2;vocabulary;length;calculated_length;volume;difficulty;effort;time;bugs\n")

	for x in dados:
		x = x.strip()
		info = x.split(':')
		prj = info[0]
		clazz = info[1]

		# Entering a particular project
		cmd = "cd " + prj
		
		prjDir = baseDir + "/" + prj
		metricsDir = prjDir + "/metrics"
		
		isExist = os.path.exists(metricsDir)
		if (not isExist):
			cmd = "mkdir " + metricsDir
			os.system(cmd)
		
		# Executing the metric collection tool
		cmd = "cd " +  prjDir + ";radon cc " + clazz + " -j -O " + metricsDir + "/radon-cc.json;" +	"radon raw " + clazz + " -j -O " + metricsDir + "/radon-raw.json;" + 	"radon mi " + clazz + " -j -O " + metricsDir + "/radon-mi.json;" +	"radon hal " + clazz + " -j -O " + metricsDir + "/radon-hal.json;"
		print(cmd)
		os.system(cmd)

		processingCCMetrics(clazz, metricsDir, output)
		processingRawMetrics(clazz, metricsDir, output)
		processingMIMetrics(clazz, metricsDir, output)
		processingHalsteadMetrics(clazz, metricsDir, output)
		
		output.write("\n")

	dados.close()
	output.close()

# Function for processing data on Complexity
def processingCCMetrics(clazz, metricsDir, output):
	print("Processing CC")
	with open(metricsDir+"/radon-cc.json", 'r') as json_file:
		cc_dict = json.load(json_file)

	# Iterates over the list of dictionaries looking for class and methods
	nClazz = 0
	nMethods = 0
	ccMax = 0
	rankCC = 'A'
	for data in cc_dict[clazz]:
		if (data['type'] == 'class'):
			nClazz = nClazz + 1
			nMethods = nMethods + len(data['methods'])
			if (ccMax < data['complexity']):
				ccMax = data['complexity']
			if (rankCC < data['rank']):
				rankCC = data['rank']
	
	output.write("%s;%s;%s;%s;%s" % (clazz,nClazz,nMethods,ccMax,rankCC))

# Function for processing data on Size
def processingRawMetrics(clazz, metricsDir, output):
	print("Processing RAW")
	with open(metricsDir+"/radon-raw.json", 'r') as json_file:
		cc_dict = json.load(json_file)

	# Data related to a python module
	data = cc_dict[clazz]
	output.write(";%s;%s" % (data['lloc'],data['sloc']))

# Function for processing data on Maintainability Index
def processingMIMetrics(clazz, metricsDir, output):
	print("Processing MI")
	with open(metricsDir+"/radon-mi.json", 'r') as json_file:
		cc_dict = json.load(json_file)
	
	# Data related to a python module
	data = cc_dict[clazz]
	output.write(";%s;%s" % (data['mi'],data['rank']))

# Function for processing data on Maintainability Index
def processingHalsteadMetrics(clazz, metricsDir, output):
	print("Processing Hal")
	with open(metricsDir+"/radon-hal.json", 'r') as json_file):
		cc_dict = json.load(json_file)
		print(cc_dict)

	# Data related to a python module
	data = cc_dict[clazz]['total']
	for value in data:
		output.write(";%s" % (value))

if __name__ == "__main__":
    main()
