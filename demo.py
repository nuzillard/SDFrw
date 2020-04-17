"""
Demo for the sdfrw.py module.
Performs a few transformation on file "flavonoids.sdf"
and writes the result in "qualified_flavonoids.sdf",
then queries molecules for the value of the No_CE property
"""

import sdfrw
# for SDF file handling

data1 = """Name quercetine
No_CAS 117-39-5
No_ECHA 100.003.807
No_CE 204-187-1
DrugBank DB04216
PubChem 5280343
SMILES C1=CC(=C(C=C1C2=C(C(=O)C3=C(C=C(C=C3O2)O)O)O)O)O
InChI InChI=1/C15H10O7/c16-7-4-10(19)12-11(5-7)22-15(14(21)13(12)20)6-1-2-8(17)9(18)3-6/h1-5,16-19,21H"""
# wikipedia data for quercetine

data2 = """
Name kaempferol
No_CAS 520-18-3
No_ECHA 100.007.535
DrugBank DB01852
PubChem 5280863
SMILES c12c(oc(c3ccc(O)cc3)c(c1=O)O)cc(O)cc2O
InChI InChI=1/C15H10O6/c16-8-3-1-7(2-4-8)15-14(20)13(19)12-10(18)5-9(17)6-11(12)21-15/h1-6,16-18,20H"""
# wikipedia data for kaempferol

alldata = [data1, data2]
digest = [ [ line.strip().split(' ') for line in data.strip().split('\n')] for data in alldata]
# digest may be obtained from some file, is an array of arrays of arrays with
# first index is molecule index, second index is property index in molecule,
# third index is 0 for property name and 1 for property value

filenameIn = 'flavonoids.sdf'
# 2D MOL blocks from PubChem for quercetine and kaempferol
filenameOut = 'qualified_flavonoids.sdf'
# add properties and reset title in molecules from flavonoids.sdf
# and write result to qualified_flavonoids.sdf
print()
print("Reading molecules from "+filenameIn)

with open(filenameIn) as fhIn, open(filenameOut, "w") as fhOut:
# open files for reading and writing
	for molIndex, mol in enumerate(sdfrw.sdfReader(fhIn)):
# enumerate molecules from input file
		print()
		print("molecule "+str(molIndex+1))
		moldata = digest[molIndex]
# get properties and values for the current molecule
		for kv in moldata:
# loop over properties and values
			print("set property "+kv[0]+ " to value "+kv[1])
			changed, mol = sdfrw.sdfSetChangeProp(mol, kv[0], kv[1])
# update molecules with current property and value
		
		name = sdfrw.sdfGetProp(mol, 'Name')
# get name as value of property Name
		if not name: continue
# why not?
		oldtitle = sdfrw.sdfGetTitle(mol)
# get current, old, pubchem title
		mol = sdfrw.sdfChangeTitle(mol, name)
# change title for the value of the Name property
		if not mol: continue
# why not?
		newtitle = sdfrw.sdfGetTitle(mol)
# get newtitle again from the current molecule, just for checking
		print("Title "+oldtitle+ " --> "+newtitle)

		sdfrw.sdfWrite(fhOut, mol)
# write current molecule

print()
print("Writing modified molecules to "+filenameOut)


filenameIn = 'qualified_flavonoids.sdf'
# qualified_flavonoids.sdf for reading, now
look_for = 'No_CE'
# looking for the No_CE property, which is missing for kaempferol (was manually removed)
print()
print("Looking for property " + look_for+ " in "+filenameIn)

with open(filenameIn) as fhIn:
# open qualified_flavonoids.sdf for reading
	for mol in sdfrw.sdfReader(fhIn):
# get current molecule
		name = sdfrw.sdfGetProp(mol, 'Name')
# get name of current molecule
		if not name: continue
# why not ?
		noce = sdfrw.sdfGetProp(mol, look_for)
# try to get value of No_CE property
		value = noce if noce else "not found"
# value of No_CE property or substitution value if property is missing in the current molecule
		print(name+': '+value)
# print molecule name and No_CE, if possible.
