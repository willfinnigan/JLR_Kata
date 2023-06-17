from src.car import Car


class CarBuilderService:

    def __init__(self):
        self.brands = ['Jaguar', 'Land Rover']
        self.models = ['F-Type', 'XE', 'XF', 'XJ', 'Range Rover', 'Range Rover Sport', 'Range Rover Evoque']
        self.engines = ['V6 3.0L', 'V8 4.0L', 'V8 5.0L']
        self.colours = ['British Racing Green', 'Santorini Black', 'Fuji White', 'Firenze Red', 'Indus Silver']

        self.brand_model_combinations = {'Jaguar': ['F-Type', 'XE', 'XF', 'XJ'],
                                        'Land Rover': ['Range Rover', 'Range Rover Sport', 'Range Rover Evoque',
                                                       'Discovery', 'Discovery Sport', 'Defender']}

        self.brand_engine_combinations = {'Jaguar': ['V6 3.0L', 'V8 4.0L'],
                                          'Land Rover': ['V6 3.0L', 'V8 4.0L', 'V8 5.0L']}

    def select_brand(self, car: Car, brand_name: str) -> Car:
        if brand_name not in self.brands:
            raise Exception(f'Brand {brand_name} is not supported')
        car.brand = brand_name
        return car

    def select_model(self, car: Car, model_name: str) -> Car:
        if model_name not in self.models:
            raise Exception(f'Model {model_name} is not supported')
        if car.brand not in self.brand_model_combinations:
            raise Exception(f'Brand {car.brand} is not supported')
        if model_name not in self.brand_model_combinations[car.brand]:
            raise Exception(f'Model {model_name} is not supported for brand {car.brand}')
        car.model = model_name
        return car

    def select_engine(self, car: Car, engine: str) -> Car:
        if engine not in self.engines:
            raise Exception(f'Engine {engine} is not supported')
        if car.brand not in self.brand_engine_combinations:
            raise Exception(f'Brand {car.brand} is not supported')
        if engine not in self.brand_engine_combinations[car.brand]:
            raise Exception(f'Engine {engine} is not supported for brand {car.brand}')
        car.engine = engine
        return car

    def select_colour(self, car: Car, colour: str) -> Car:
        if colour not in self.colours:
            raise Exception(f'Colour {colour} is not supported')
        car.colour = colour
        return car