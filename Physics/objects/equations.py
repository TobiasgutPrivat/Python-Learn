from typing import Callable

class Equation:
    prop: str
    vars: list[str]
    func: Callable

    def __init__(self, prop, vars, func):
        self.prop = prop
        self.vars = vars
        self.func = func

    def calculate(self, values):
        return self.func(values)
    
    def __str__(self):
        return f"{self.prop} from {self.vars}"
    
    def __repr__(self):
        return str(self)

EQUATIONS: list[Equation] = [
    Equation("F", ["m", "a"], lambda values: values["m"] * values["a"]),
    Equation("m", ["F", "a"], lambda values: values["F"] / values["a"] if values["a"] != 0 else None),
    Equation("a", ["F", "m"], lambda values: values["F"] / values["m"] if values["m"] != 0 else None),
    Equation("p", ["F", "A"], lambda values: values["F"] / values["A"] if values["A"] != 0 else None),
]

# equations to calculate a property
equations: dict[str, list[Equation]] =  {key: [eq for eq in EQUATIONS if key == eq.prop] for key in set(eq.prop for eq in EQUATIONS)}

# equations that depend on a property
dependents: dict[str, list[str]] = {key: [eq.prop for eq in EQUATIONS if key in eq.vars] for key in set.union(*[set(eq.vars) for eq in EQUATIONS])}

if __name__ == "__main__":
    print(equations)
    print(dependents)