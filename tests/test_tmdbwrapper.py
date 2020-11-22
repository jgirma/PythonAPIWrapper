# tests/test_tmdbwrapper.py

from tmdbwrapper import TV
from pytest import fixture
import vcr

@fixture
def tv_keys():
    # Will return the test data
    return ["id", "origin_country", "poster_path",
            "name", "overview", "popularity", "backdrop_path",
            "first_air_date", "vote_count", "vote_average"]

# The following code will pull the most popular tv shows from tmbd
# and test to make sure the first show meets the tv_keys requirements
@vcr.use_cassette('tests/vcr_cassettes/tv-popular.yml')
def test_tv_popular():
    """Tests an API call to get a popular tv shows"""

    response = TV.popular()

    assert isinstance(response, dict)
    assert isinstance(response['results'], list)
    assert isinstance(response['results'][0], dict)
    assert set(tv_keys).issubset(response['results'][0].keys())

# The following code is going to take test the tv show's info to
# ensure that it contains all the values in the tv_keys
@vcr.use_cassette('tests/vcr_cassettes/tv-info.yml')
def test_tv_info(tv_keys):
    """Tests an API call to get a TV show's info"""

    tv_instance = TV(1396)
    response = tv_instance.info()

    assert isinstance(response, dict)
    assert response['id'] == 1396, "The ID should be in the response"
    assert set(tv_keys).issubset(response.keys()), "All Keys should be in the response"
