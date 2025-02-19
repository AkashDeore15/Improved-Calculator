import pytest
from decimal import Decimal
from faker import Faker
from calculator.operations import add, subtract, multiply, divide

fake = Faker()

def generate_test_data(num_records):
    operation_mappings = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }

    for _ in range(num_records):
        a = Decimal(fake.random_number(digits=2))
        b = Decimal(fake.random_number(digits=2))

        operation_name = fake.random_element(elements=list(operation_mappings.keys()))
        operation_func = operation_mappings[operation_name]

        # Ensure b is not zero for division
        if operation_func == divide and b == Decimal('0'):
            b = Decimal('1')

        try:
            expected = operation_func(a, b)
        except ZeroDivisionError:
            print(f"Error: Division by zero with {a} / {b}")
            expected = "ZeroDivisionError"

        yield a, b, operation_name, operation_func, expected

def pytest_addoption(parser):
    parser.addoption('--num-records', action="store", type=int, default=10, help='Number of test records to generate')

def pytest_generate_tests(metafunc):
    
    if {'a', 'b', 'expected'}.intersection(metafunc.fixturenames):
        num_records = metafunc.config.getoption('num_records')
        test_data = list(generate_test_data(num_records))
        modified_test_data = [(a,b,op_name if 'operation_name' in metafunc.fixturenames else op_func, op_func, expected) for a,b,op_name,op_func,expected in test_data]
        metafunc.parametrize('a, b, operation_name, operation_func, expected', modified_test_data)
