from ase.lattice.cubic import FaceCenteredCubic

xLength = 120
yLength = 120
zLength = 100

atoms = FaceCenteredCubic('Cu',
                          pbc=(True,True,False))


xLatticeParam = atoms.get_cell()[0,0]
yLatticeParam = atoms.get_cell()[1,1]
zLatticeParam = atoms.get_cell()[2,2]

xRepeat = round(xLength/xLatticeParam)
yRepeat = round(yLength/yLatticeParam)
zRepeat = round(zLength/zLatticeParam)

atoms = FaceCenteredCubic('Cu',
                          pbc=(True,True,False),
                          size=(xRepeat,yRepeat,zRepeat))

print(len(atoms))

# atoms = FaceCenteredCubic('Cu',
#                           pbc=(True,True,False)
#                           repeat=)  


###########################################################
## visulizstion
###########################################################


from ase.visualize import view

# view(atoms)