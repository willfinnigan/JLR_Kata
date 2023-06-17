from dataclasses import dataclass


@dataclass
class Car():
    brand: str = None
    model: str = None
    engine: str = None
    colour: str = None

    def get_summary(self):
        return f'{self.brand} {self.model} {self.engine} {self.colour}'




