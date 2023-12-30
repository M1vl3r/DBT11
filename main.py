from models.kepeeing import kepeeing
from models.materials import materials
from models.suppliers import suppliers

suppliers = suppliers()
materials = materials()
kepeeing = kepeeing()

for row, list in enumerate(suppliers.countAboutBanks()):
    print(row, ')', list)
