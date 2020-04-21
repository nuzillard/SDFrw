"""
Demo for the sdfrw.py module.
Add property to molecules in an sdf file according to values stored in a text file

example: python updater.py Name flavonoid_names.txt < flavonoids.sdf > flavonoids_updated.sdf
result: Molecule property "Name", with values from file flavonoid_names.txt,
is set or reset for molecules in flavonoids.sdf to produce file flavonoids_updated.sdf.
"""

import sdfrw
import sys

fhIn = sys.stdin
fhOut = sys.stdout
# read/write from/to standard input/output

argc = len(sys.argv)
# get number of command line arguments
if argc != 3:
# in case 2 arguments are not present on command line
	print("Usage: python " + sys.argv[0] + " PropertyName ValuesFileName < sdfFileNameInput.sdf > sdfFileNameOutput.sdf")
	print("Example: python updater.py Name flavonoid_names.txt < flavonoids.sdf > flavonoids_updated.sdf")
	sys.exit()
# help message

propname = sys.argv[1]
# get new property name
txtfilename = sys.argv[2]
# get name of the file that contains the new values for the new property

with open(txtfilename) as fhTxt:
# open file with values for reading
	for mol in sdfrw.sdfReader(fhIn):
# loop through molecules from input sdf file
		propvalue = fhTxt.readline().strip()
# get property and values for the current molecule
		changed, mol = sdfrw.sdfSetChangeProp(mol, propname, propvalue)
# update current molecule with property and current value
		sdfrw.sdfWrite(fhOut, mol)
# write current molecule
