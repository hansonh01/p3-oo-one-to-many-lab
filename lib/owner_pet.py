class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []

    def __init__(self,name="",pet_type="", owner=None) -> None:
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        self.all.append(self)
    
    @property
    def pet_type(self):
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self, type):
        if type in self.PET_TYPES:
            self._pet_type = type
        else:
            raise Exception('Not a valid pet type.')
    
    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, owner):
        if (isinstance(owner, Owner) or not owner):
            self._owner = owner
        else:
            raise Exception("Object is not of type Owner")

class Owner:
    def __init__(self,name="") -> None:
        self.name = name
    
    def pets(self):
        result = []
        for pet in Pet.all:
            if pet.owner == self:
                result.append(pet)
        return result
    
    def add_pet(self,pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise Exception("Input object is not of type Pet")
    
    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)