"""
copy.py copies an sdf file from standard input to standard output.
Side-effect: lignes such as  ">  <tag-name> (n)" are changed to ">  <tag-name>"

usage: python copy.py < fileIn.sdf > fileOut.sdf
"""

import sdfrw
import sys

fhIn = sys.stdin
fhOut = sys.stdout
# read/write from/to standard input/output


def transformation(mol):
# transormation return a copy a molecule with a fresh new tag line
	sdfprops = sdfrw.sdfGetPropList(mol)
# get the list of all tags
	for sdfprop in sdfprops:
# loop through tags
		sdfvalue = sdfrw.sdfGetProp(mol, sdfprop)
# get the value associated to the current tag
		sdfrw.sdfSetChangeProp(mol, sdfprop, sdfvalue)
# reset tag and value with a fresh new tag line
	return mol
# return the copied molecule

for molIn in sdfrw.sdfReader(fhIn):
# read input molecule
	molOut = transformation(molIn)
# transform input molecule to output molecule
	sdfrw.sdfWrite(fhOut, molOut)
# write output molecule
