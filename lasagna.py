# Define the expected bake time in minutes
EXPECTED_BAKE_TIME = 40

# Calculate remaining bake time
def bake_time_remaining(actual_minutes_in_oven):
    """Calculate the remaining bake time.

    :param actual_minutes_in_oven: int - minutes lasagna has been in the oven.
    :return: int - remaining minutes needed to bake the lasagna.

    Function uses a constant EXPECTED_BAKE_TIME to determine remaining time.
    """
    return EXPECTED_BAKE_TIME - actual_minutes_in_oven

# Calculate preparation time in minutes
def preparation_time_in_minutes(number_of_layers):
    """Calculate preparation time.

    :param number_of_layers: int - number of layers to prepare.
    :return: int - total preparation time (in minutes).

    Assumes each layer takes 2 minutes to prepare.
    """
    return number_of_layers * 2

# Calculate total elapsed cooking time (prep + bake) in minutes
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """
    prep_time = preparation_time_in_minutes(number_of_layers)
    return prep_time + elapsed_bake_time
