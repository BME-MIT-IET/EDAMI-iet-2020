from behave import *


@given('I print {string:s}')
def i_have_cukes_in_my_belly(context, string):
	print(f"Cukes: {string}")
	assert
