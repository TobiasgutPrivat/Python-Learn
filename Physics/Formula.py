class Formula:
    #units multiplied give the value
    value: float 
    units: dict[str, int] #{unit: exponent}

    def __init__(self, value: float, units: dict[str, int]):
        self.value = value
        self.units = units

Formulas = [
    Formula(1000, {"kg": 1, "g": -1}), # 1kg / 1g = 1000
    Formula(100, {"m": 1, "cm": -1}), # 1m / 1cm = 100
    Formula(1, {"N": -1, "kg": 1, "m": 1, "s": -2}), # 1 = 1 kg*m/(s²*N)
    Formula(1, {"J": -1, "kg": 1, "m": 2, "s": -2}), # 1 = 1 kg*m²/(s²*J)
]