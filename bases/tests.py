from django.test import TestCase

# Create your tests here.
def dummy_function():
    return True

def test_dummy_function():
    assert dummy_function() == True

