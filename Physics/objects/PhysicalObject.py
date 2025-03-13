from equations import equations, dependents

class PhysicalObject:
    name: str
    properties: dict[str, float]
    def __init__(self, name: str = "Object"):
        self.name = name
        self.properties = {}

    def set_property(self, prop: str, value):
        """Sets a property. If already defined, it checks for conflicts."""
        if self.properties.get(prop):
            print(f"Property {prop} is already defined.")
            return

        self.properties[prop] = value  # Overwrite value regardless
        self.update_dependents(prop)

    def update_dependents(self, prop: str):
        for dependency in dependents[prop]:
            self.compute_property(dependency)

    def compute_property(self, prop: str):
        """Computes a property using known values without modifying the object."""
        #1. get equations with available values
        #2. calculate all equations
        #3. check for conflicts //TODO this
        for eq in equations[prop]:
            if all(var in self.properties for var in eq.vars):
                value = eq.calculate(self.properties)
                self.set_property(eq.prop, value)

    def __str__(self):
        text = f"{self.name}:\n"
        for key, value in self.properties.items():
            text += f"  {key}: {value}\n"
        return text