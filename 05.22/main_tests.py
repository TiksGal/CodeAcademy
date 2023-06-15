import unittest
from unittest.mock import patch
import requests_mock
from pokemon import Pokemon, Statistic

from main import (get_random_pokemon, convert_json_to_pokemon, get_all_stats_names, 
                         choose_winner, POKEMON_ENDPOINT)

class TestPokemonScript(unittest.TestCase):

    @requests_mock.Mocker()
    def test_get_random_pokemon(self, mock):
        mock.get(requests_mock.ANY, json={"name": "pikachu"})
        pokemon = get_random_pokemon()
        self.assertEqual(pokemon["name"], "pikachu")

    def test_convert_json_to_pokemon(self):
        api_response = {
            "name": "pikachu",
            "stats": [
                {"base_stat": 45, "stat": {"name": "health"}},
                {"base_stat": 55, "stat": {"name": "attack"}},
            ],
        }
        pokemon = convert_json_to_pokemon(api_response)
        self.assertEqual(pokemon.name, "pikachu")
        self.assertIsInstance(pokemon, Pokemon)

    @requests_mock.Mocker()
    def test_get_all_stats_names(self, mock):
        mock.get(requests_mock.ANY, json={"results": [{"name": "health"}, {"name": "attack"}]})
        stats = get_all_stats_names()
        self.assertListEqual(stats, ["health", "attack"])

    def test_choose_winner(self):
        pokemon1 = Pokemon("pikachu", [Statistic(45, "health"), Statistic(55, "attack")])
        pokemon2 = Pokemon("charmander", [Statistic(39, "health"), Statistic(52, "attack")])
        winner = choose_winner(pokemon1, pokemon2)
        self.assertEqual(winner.name, "pikachu")

if __name__ == "__main__":
    unittest.main()
