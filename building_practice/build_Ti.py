from math import sqrt

from ase.lattice.hexagonal import HexagonalClosedPacked
from ase.build import cut
from ase.visualize import view

Lx = Ly = 120
Lz = 100

atoms = HexagonalClosedPacked('Ti',
                              pbc=(True,True,False),
                              size=(1,1,1))

aLatticeParam = atoms.get_cell()[0,0]
cLatticeParam = atoms.get_cell()[2,2]

aRepeat = round((sqrt(3)+1)/(sqrt(3)) * (Lx/aLatticeParam))
cRepeat = round(Lz/cLatticeParam)

atoms = HexagonalClosedPacked('Ti',
                              pbc=(True,True,False),
                              size=(aRepeat,aRepeat,cRepeat))

atoms_cut = cut(atoms, a=(sqrt(3)/(sqrt(3)+1),0,0), b = (1/(sqrt(3)+1), 2/(sqrt(3)+1), 0), c = (0,0,1))
view(atoms_cut)

print(atoms_cut.cell[:])
print(atoms_cut.pbc)
print(len(atoms_cut))



