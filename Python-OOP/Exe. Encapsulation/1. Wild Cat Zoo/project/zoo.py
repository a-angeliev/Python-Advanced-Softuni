class Zoo:
    def __init__(self, name, budget, animal_capacity, worker_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = worker_capacity
        self.animals = []
        self.workers = []
        self.sum_salary = 0
        self.animal_cost = 0

    def add_animal(self, animal, price):
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.__budget -= price
            self.animals.append(animal)
            self.animal_cost += animal.money_for_care
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif self.__animal_capacity > len(self.animals):
            return f"Not enough budget"
        else:
            return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            self.sum_salary += worker.salary
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return f"Not enough space for worker"

    def fire_worker(self, worker_name):
        for el in self.workers:
            if el.name == worker_name:
                self.sum_salary -= el.salary
                self.workers.remove(el)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        if self.sum_salary <= self.__budget:
            self.__budget -= self.sum_salary
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        if self.__budget >= self.animal_cost:
            self.__budget -= self.animal_cost
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lion = []
        tiger = []
        cheetah = []
        for el in self.animals:
            if el.__class__.__name__ == "Tiger":
                tiger.append(el)
            elif el.__class__.__name__ == "Lion":
                lion.append(el)
            else:
                cheetah.append(el)

        returned_strign = f"You have {len(lion) + len(tiger) + len(cheetah)} animals\n"
        returned_strign += f"----- {len(lion)} Lions:\n"
        for el in lion:
            returned_strign += repr(el) + "\n"
        returned_strign += f"----- {len(tiger)} Tigers:\n"
        for el in tiger:
            returned_strign += repr(el) + "\n"
        returned_strign += f"----- {len(cheetah)} Cheetahs:\n"
        for el in cheetah:
            returned_strign += repr(el)
            if not el == cheetah[-1]:
                returned_strign += "\n"
        return returned_strign

    def workers_status(self):
        keepers = []
        caretakers = []
        vets = []
        for el in self.workers:
            if el.__class__.__name__ == "Keeper":
                keepers.append(el)
            elif el.__class__.__name__ == "Caretaker":
                caretakers.append(el)
            else:
                vets.append(el)

        returned_strign = f"You have {len(keepers) + len(vets) + len(caretakers)} workers\n"
        returned_strign += f"----- {len(keepers)} Keepers:\n"
        for el in keepers:
            returned_strign += repr(el) + "\n"
        returned_strign += f"----- {len(caretakers)} Caretakers:\n"
        for el in caretakers:
            returned_strign += repr(el) + "\n"
        returned_strign += f"----- {len(vets)} Vets:\n"
        for el in vets:
            returned_strign += repr(el)
            if not el == vets[-1]:
                returned_strign += "\n"
        return returned_strign
