class Tuple:
    elements: list
    def __init__(self, elements: list) -> None:
        self.elements = elements

    def __eq__(self, value: object) -> bool:
        return isinstance(value, Tuple) and self.elements == value.elements

    def __str__(self) -> str:
        return '(' + ', '.join(map(str, self.elements)) + ')'