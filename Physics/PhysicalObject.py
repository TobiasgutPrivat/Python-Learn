from equations import equations, dependents

class PhysicalObject:
    def __init__(self, name: str = "Object"):
        self.name = name
        self.user_properties = {}  # Properties explicitly set by the user
        self.derived_properties = {}  # Properties calculated by the system

    def set_property(self, prop: str, value):
        """
        Set a user-defined property. If already defined, it checks for conflicts.
        Derived properties cannot be set directly by the user.
        """
        if prop in self.derived_properties:
            raise ValueError(f"Cannot directly set derived property: {prop}")

        if self.user_properties.get(prop) == value:
            return  # No change

        self.user_properties[prop] = value
        self.update_dependents(prop)

    def update_dependents(self, prop: str):
        """
        Update all derived properties that depend on the given property.
        Avoids infinite recursion by tracking properties being calculated.
        """
        if prop not in dependents: return
        
        for dependency in dependents[prop]:
            if dependency not in self.user_properties:  # Only update derived properties
                self.compute_property(dependency)

    def compute_property(self, prop: str):
        """
        Compute a derived property using known values.
        Ensures that derived properties are not overwritten by user-defined values.
        """
        if prop in self.user_properties:
            return  # Do not overwrite user-defined properties

        results = []
        values = {**self.user_properties, **self.derived_properties}
        for eq in equations.get(prop, []):
            if all(var in self.user_properties or var in self.derived_properties for var in eq.vars):
                # Use both user-defined and derived properties for calculations
                results.append(eq.calculate(values))

        if len(set(results)) > 1:
            raise ValueError(f"Property {prop} has multiple possible values.")

        if results:
            self.derived_properties[prop] = results[0]
            self.update_dependents(prop)  # Update further dependencies

    def get_property(self, prop: str):
        """
        Get the value of a property, whether user-defined or derived.
        """
        if prop in self.user_properties:
            return self.user_properties[prop]
        elif prop in self.derived_properties:
            return self.derived_properties[prop]
        else:
            raise KeyError(f"Property {prop} not found.")

    def __str__(self):
        text = f"{self.name}:\n"
        values = {**self.user_properties, **self.derived_properties}
        for key, value in values.items():
            text += f"  {key}: {value}\n"
        return text