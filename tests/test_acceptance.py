from src.car import Car
from src.car_builder import CarBuilderService




def test_car_builder_acceptance():

    car_builder = CarBuilderService()

    car = Car()
    car = car_builder.select_brand(car, 'Jaguar')
    car = car_builder.select_model(car, 'F-Type')
    car = car_builder.select_engine(car, 'V8 4.0L')
    car = car_builder.select_colour(car, 'British Racing Green')
    summary = car.get_summary()
    assert summary == 'Jaguar F-Type V8 4.0L British Racing Green'
