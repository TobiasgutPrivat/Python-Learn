from equations import equations, dependents

class PhysicalObject:
    name: str
    properties: dict[str, float]
    allowChanges: bool

    def __init__(self, name: str = "Object", allowChanges: bool = False):
        self.name = name
        self.allowChanges = allowChanges
        self.properties = {}

    def set_property(self, prop: str, value):
        """Sets a property. If already defined, it checks for conflicts."""
        if self.properties.get(prop) == value:
            return # no change
        
        if not self.allowChanges and self.properties.get(prop):
            print(f"Property {prop} can not be overwritten.")
            return

        self.properties[prop] = value
        self.update_dependents(prop)

    def update_dependents(self, prop: str):
        for dependency in dependents[prop]:
            self.compute_property(dependency)

    def compute_property(self, prop: str):
        """Computes a property using known values without modifying the object."""
        results = []
        for eq in equations[prop]:
            if all(var in self.properties for var in eq.vars):
                results.append(eq.calculate(self.properties))

        if not self.allowChanges and len(set(results)) != 1:
            print(f"Property {prop} has multiple possible values.")
            return
        
        self.set_property(eq.prop, results[0])

    def __str__(self):
        text = f"{self.name}:\n"
        for key, value in self.properties.items():
            text += f"  {key}: {value}\n"
        return text