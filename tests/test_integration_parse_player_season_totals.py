import os
from unittest import TestCase

from basketball_reference_web_scraper.data import Team, Position
from basketball_reference_web_scraper.parsers import players_season_totals

season_2001_totals_html = os.path.join(os.path.dirname(__file__), './NBA_2001_totals.html')
season_2018_totals_html = os.path.join(os.path.dirname(__file__), './NBA_2018_totals.html')
season_2019_totals_html = os.path.join(os.path.dirname(__file__), './NBA_2019_totals.html')
season_2019_totals_with_jemerrio_jones_blank_age = os.path.join(os.path.dirname(__file__), './NBA_2019_totals_jemerrio_jones_blank_age.html')


class TestPlayersSeasonTotals(TestCase):
    def setUp(self):
        self.season_2001_totals = open(season_2001_totals_html).read()
        self.season_2018_totals = open(season_2018_totals_html).read()
        self.season_2019_totals = open(season_2019_totals_html).read()
        self.season_2019_totals_with_jemerrio_jones_blank_age = open(season_2019_totals_with_jemerrio_jones_blank_age).read()

    def test_2001_players_season_totals(self):
        parsed_season_totals = players_season_totals.parse_players_season_totals(self.season_2001_totals)
        self.assertEqual(len(parsed_season_totals), 490)

        mahmoud_abdul_rauf = parsed_season_totals[0]

        self.assertEqual(mahmoud_abdul_rauf["slug"], "abdulma02")
        self.assertEqual(mahmoud_abdul_rauf["name"], "Mahmoud Abdul-Rauf")
        self.assertEqual(mahmoud_abdul_rauf["positions"], [Position.POINT_GUARD])
        self.assertEqual(mahmoud_abdul_rauf["team"], Team.VANCOUVER_GRIZZLIES)
        self.assertEqual(mahmoud_abdul_rauf["games_played"], 41)
        self.assertEqual(mahmoud_abdul_rauf["games_started"], 0)
        self.assertEqual(mahmoud_abdul_rauf["minutes_played"], 486)
        self.assertEqual(mahmoud_abdul_rauf["made_field_goals"], 120)
        self.assertEqual(mahmoud_abdul_rauf["attempted_field_goals"], 246)
        self.assertEqual(mahmoud_abdul_rauf["made_three_point_field_goals"], 4)
        self.assertEqual(mahmoud_abdul_rauf["attempted_three_point_field_goals"], 14)
        self.assertEqual(mahmoud_abdul_rauf["made_free_throws"], 22)
        self.assertEqual(mahmoud_abdul_rauf["attempted_free_throws"], 29)
        self.assertEqual(mahmoud_abdul_rauf["offensive_rebounds"], 5)
        self.assertEqual(mahmoud_abdul_rauf["defensive_rebounds"], 20)
        self.assertEqual(mahmoud_abdul_rauf["assists"], 76)
        self.assertEqual(mahmoud_abdul_rauf["steals"], 9)
        self.assertEqual(mahmoud_abdul_rauf["blocks"], 1)
        self.assertEqual(mahmoud_abdul_rauf["turnovers"], 26)
        self.assertEqual(mahmoud_abdul_rauf["personal_fouls"], 50)

    def test_2018_players_season_totals(self):
        parsed_season_totals = players_season_totals.parse_players_season_totals(self.season_2018_totals)
        self.assertEqual(len(parsed_season_totals), 605)

        alex_abrines = parsed_season_totals[0]

        self.assertEqual(alex_abrines["slug"], "abrinal01")
        self.assertEqual(alex_abrines["name"], "Alex Abrines")
        self.assertEqual(alex_abrines["positions"], [Position.SHOOTING_GUARD])
        self.assertEqual(alex_abrines["team"], Team.OKLAHOMA_CITY_THUNDER)
        self.assertEqual(alex_abrines["games_played"], 75)
        self.assertEqual(alex_abrines["games_started"], 8)
        self.assertEqual(alex_abrines["minutes_played"], 1134)
        self.assertEqual(alex_abrines["made_field_goals"], 115)
        self.assertEqual(alex_abrines["attempted_field_goals"], 291)
        self.assertEqual(alex_abrines["made_three_point_field_goals"], 84)
        self.assertEqual(alex_abrines["attempted_three_point_field_goals"], 221)
        self.assertEqual(alex_abrines["made_free_throws"], 39)
        self.assertEqual(alex_abrines["attempted_free_throws"], 46)
        self.assertEqual(alex_abrines["offensive_rebounds"], 26)
        self.assertEqual(alex_abrines["defensive_rebounds"], 88)
        self.assertEqual(alex_abrines["assists"], 28)
        self.assertEqual(alex_abrines["steals"], 38)
        self.assertEqual(alex_abrines["blocks"], 8)
        self.assertEqual(alex_abrines["turnovers"], 25)
        self.assertEqual(alex_abrines["personal_fouls"], 124)

    def test_2018_omer_asik_season_totals(self):
        parsed_season_totals = players_season_totals.parse_players_season_totals(self.season_2018_totals)

        pelicans_omer_asik = parsed_season_totals[22]

        self.assertEqual(pelicans_omer_asik["slug"], "asikom01")
        self.assertEqual(pelicans_omer_asik["name"], "Omer Asik")
        self.assertEqual(pelicans_omer_asik["positions"], [Position.CENTER])
        self.assertEqual(pelicans_omer_asik["team"], Team.NEW_ORLEANS_PELICANS)
        self.assertEqual(pelicans_omer_asik["games_played"], 14)
        self.assertEqual(pelicans_omer_asik["games_started"], 0)
        self.assertEqual(pelicans_omer_asik["minutes_played"], 121)
        self.assertEqual(pelicans_omer_asik["made_field_goals"], 7)
        self.assertEqual(pelicans_omer_asik["attempted_field_goals"], 16)
        self.assertEqual(pelicans_omer_asik["made_three_point_field_goals"], 0)
        self.assertEqual(pelicans_omer_asik["attempted_three_point_field_goals"], 0)
        self.assertEqual(pelicans_omer_asik["made_free_throws"], 4)
        self.assertEqual(pelicans_omer_asik["attempted_free_throws"], 12)
        self.assertEqual(pelicans_omer_asik["offensive_rebounds"], 7)
        self.assertEqual(pelicans_omer_asik["defensive_rebounds"], 30)
        self.assertEqual(pelicans_omer_asik["assists"], 2)
        self.assertEqual(pelicans_omer_asik["steals"], 1)
        self.assertEqual(pelicans_omer_asik["blocks"], 2)
        self.assertEqual(pelicans_omer_asik["turnovers"], 5)
        self.assertEqual(pelicans_omer_asik["personal_fouls"], 14)

        bulls_omer_asik = parsed_season_totals[23]

        self.assertEqual(pelicans_omer_asik["slug"], "asikom01")
        self.assertEqual(bulls_omer_asik["name"], "Omer Asik")
        self.assertEqual(bulls_omer_asik["positions"], [Position.CENTER])
        self.assertEqual(bulls_omer_asik["team"], Team.CHICAGO_BULLS)
        self.assertEqual(bulls_omer_asik["games_played"], 4)
        self.assertEqual(bulls_omer_asik["games_started"], 0)
        self.assertEqual(bulls_omer_asik["minutes_played"], 61)
        self.assertEqual(bulls_omer_asik["made_field_goals"], 2)
        self.assertEqual(bulls_omer_asik["attempted_field_goals"], 6)
        self.assertEqual(bulls_omer_asik["made_three_point_field_goals"], 0)
        self.assertEqual(bulls_omer_asik["attempted_three_point_field_goals"], 0)
        self.assertEqual(bulls_omer_asik["made_free_throws"], 0)
        self.assertEqual(bulls_omer_asik["attempted_free_throws"], 1)
        self.assertEqual(bulls_omer_asik["offensive_rebounds"], 2)
        self.assertEqual(bulls_omer_asik["defensive_rebounds"], 8)
        self.assertEqual(bulls_omer_asik["assists"], 1)
        self.assertEqual(bulls_omer_asik["steals"], 1)
        self.assertEqual(bulls_omer_asik["blocks"], 2)
        self.assertEqual(bulls_omer_asik["turnovers"], 4)
        self.assertEqual(bulls_omer_asik["personal_fouls"], 6)

    def test_2019_jimmy_butler_season_totals(self):
        parsed_season_totals = players_season_totals.parse_players_season_totals(self.season_2019_totals)

        philly_jimmy_butler = parsed_season_totals[72]

        self.assertEqual(philly_jimmy_butler["slug"], "butleji01")
        self.assertEqual(philly_jimmy_butler["name"], "Jimmy Butler")
        self.assertEqual(philly_jimmy_butler["positions"], [Position.SHOOTING_GUARD])
        self.assertEqual(philly_jimmy_butler["team"], Team.PHILADELPHIA_76ERS)
        self.assertEqual(philly_jimmy_butler["games_played"], 5)
        self.assertEqual(philly_jimmy_butler["games_started"], 5)
        self.assertEqual(philly_jimmy_butler["minutes_played"], 175)
        self.assertEqual(philly_jimmy_butler["made_field_goals"], 31)
        self.assertEqual(philly_jimmy_butler["attempted_field_goals"], 63)
        self.assertEqual(philly_jimmy_butler["made_three_point_field_goals"], 3)
        self.assertEqual(philly_jimmy_butler["attempted_three_point_field_goals"], 10)
        self.assertEqual(philly_jimmy_butler["made_free_throws"], 21)
        self.assertEqual(philly_jimmy_butler["attempted_free_throws"], 25)
        self.assertEqual(philly_jimmy_butler["offensive_rebounds"], 6)
        self.assertEqual(philly_jimmy_butler["defensive_rebounds"], 13)
        self.assertEqual(philly_jimmy_butler["assists"], 17)
        self.assertEqual(philly_jimmy_butler["steals"], 9)
        self.assertEqual(philly_jimmy_butler["blocks"], 3)
        self.assertEqual(philly_jimmy_butler["turnovers"], 11)
        self.assertEqual(philly_jimmy_butler["personal_fouls"], 12)

    def test_2019_jemerrio_jones_blank_age_season_totals(self):
        parsed_season_totals = players_season_totals.parse_players_season_totals(self.season_2019_totals_with_jemerrio_jones_blank_age)

        jemerrio_jones = parsed_season_totals[310]

        self.assertEqual(jemerrio_jones["slug"], "jonesje01")
        self.assertEqual(jemerrio_jones["name"], "Jemerrio Jones")
        self.assertEqual(jemerrio_jones["positions"], [Position.SMALL_FORWARD])
        self.assertIsNone(jemerrio_jones["age"])
        self.assertEqual(jemerrio_jones["team"], Team.LOS_ANGELES_LAKERS)
        self.assertEqual(jemerrio_jones["games_played"], 1)
        self.assertEqual(jemerrio_jones["games_started"], 0)
        self.assertEqual(jemerrio_jones["minutes_played"], 5)
        self.assertEqual(jemerrio_jones["made_field_goals"], 1)
        self.assertEqual(jemerrio_jones["attempted_field_goals"], 2)
        self.assertEqual(jemerrio_jones["made_three_point_field_goals"], 0)
        self.assertEqual(jemerrio_jones["attempted_three_point_field_goals"], 1)
        self.assertEqual(jemerrio_jones["made_free_throws"], 0)
        self.assertEqual(jemerrio_jones["attempted_free_throws"], 0)
        self.assertEqual(jemerrio_jones["offensive_rebounds"], 1)
        self.assertEqual(jemerrio_jones["defensive_rebounds"], 0)
        self.assertEqual(jemerrio_jones["assists"], 0)
        self.assertEqual(jemerrio_jones["steals"], 1)
        self.assertEqual(jemerrio_jones["blocks"], 0)
        self.assertEqual(jemerrio_jones["turnovers"], 0)
        self.assertEqual(jemerrio_jones["personal_fouls"], 0)

