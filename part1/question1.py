################################################################################
#     ____                          __     _                          ___
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          <  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \         / /
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        / /
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /_/
#
#  Question 1
################################################################################
#
# Instructions:
# The two functions below are used to tell the weather. They have some bugs that
# need to be fixed. The test suite in `question1_test.py` will verify the output.
# Read the test suite to know the values that these functions should return.

city_dict = {
    "Quito": {"temperature": 22, "sky_condition": "sunny"},
    "Sao Paulo": {"temperature": 17, "sky_condition": "cloudy"},
    "San Francisco": {"temperature": 16, "sky_condition": None},
    "New York": {"temperature": 14, "sky_condition": "rainy"},
}


def get_city_temperature(city):
    return city_dict[city]["temperature"] if city in city_dict else None


def get_city_sky_condition(city):
    return city_dict[city]["sky_condition"] if city in city_dict else None


def get_city_weather(city):
    return (
        str(get_city_temperature(city)) + " degrees and " + get_city_sky_condition(city)
    )
