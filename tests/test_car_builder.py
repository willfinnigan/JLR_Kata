import pytest
from src.car import Car
from src.car_builder import CarBuilderService


def test_selecting_jaguar_updates_the_car():
    car = Car()
    car_builder = CarBuilderService()
    car = car_builder.select_brand(car, 'Jaguar')
    assert car.brand == 'Jaguar'

def test_selecting_hyundi_raises_an_exception():
    car = Car()
    car_builder = CarBuilderService()
    with pytest.raises(Exception):
        car = car_builder.select_brand(car, 'Hyundi')

def test_selecting_F_type_jaguar_updates_the_car():
    car = Car()
    car_builder = CarBuilderService()
    car = car_builder.select_brand(car, 'Jaguar')
    car = car_builder.select_model(car, 'F-Type')
    assert car.model == 'F-Type'

def test_selecting_F_type_land_rover_raises_an_exception():
    car = Car()
    car_builder = CarBuilderService()
    car = car_builder.select_brand(car, 'Land Rover')
    with pytest.raises(Exception):
        car = car_builder.select_model(car, 'F-Type')

def test_selecting_V8_4_0L_updates_the_car():
    car = Car()
    car_builder = CarBuilderService()
    car = car_builder.select_brand(car, 'Jaguar')
    car = car_builder.select_model(car, 'F-Type')
    car = car_builder.select_engine(car, 'V8 4.0L')
    assert car.engine == 'V8 4.0L'

def test_selecting_V8_5_0L_for_jaguar_raises_an_exception():
    car = Car()
    car_builder = CarBuilderService()
    car = car_builder.select_brand(car, 'Jaguar')
    car = car_builder.select_model(car, 'F-Type')
    with pytest.raises(Exception):
        car = car_builder.select_engine(car, 'V8 5.0L')

def test_selecting_British_Racing_Green_updates_the_car():
    car = Car()
    car_builder = CarBuilderService()
    car = car_builder.select_brand(car, 'Jaguar')
    car = car_builder.select_model(car, 'F-Type')
    car = car_builder.select_engine(car, 'V8 4.0L')
    car = car_builder.select_colour(car, 'British Racing Green')
    assert car.colour == 'British Racing Green'

def test_selecting_bright_pink_for_colour_raises_an_exception():
    car = Car()
    car_builder = CarBuilderService()
    car = car_builder.select_brand(car, 'Jaguar')
    car = car_builder.select_model(car, 'F-Type')
    car = car_builder.select_engine(car, 'V8 4.0L')
    with pytest.raises(Exception):
        car = car_builder.select_colour(car, 'Bright Pink')

def test_get_summary_returns_a_string():
    car = Car()
    car_builder = CarBuilderService()
    car = car_builder.select_brand(car, 'Jaguar')
    car = car_builder.select_model(car, 'F-Type')
    car = car_builder.select_engine(car, 'V8 4.0L')
    car = car_builder.select_colour(car, 'British Racing Green')
    summary = car.get_summary()
    assert isinstance(summary, str)
