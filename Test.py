class Employee:
    name: str
    age: int
    skills: str

    def add_skill(self, skill: str) -> None:
        self.skills.append(skill)


empl1: Employee = Employee("John", 30, ["Python", "Java"])
empl2: Employee = Employee("dan", 20, ["SQL", "Java"])

empl1.name = None

