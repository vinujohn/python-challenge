import unittest
import cli

class TestFilterAndSort(unittest.TestCase):
    def setUp(self):
        self.test_data = {
            "nbaResults":[
            {
                "id":1,
                "publicationDate":"May 2, 2020 6:07:03 PM"
            },
            {
                "id":2,
                "publicationDate":"May 2, 2020 6:07:04 PM"
            }],
            "Tennis":[
            {
                "id":3,
                "publicationDate":"May 1, 2020 6:07:03 PM"
            },
            {
                "id":4,
                "publicationDate":"May 1, 2020 6:07:04 PM"
            }]
        }

        for sport in self.test_data:
            sorted_events = sorted(self.test_data[sport], key=lambda x: x["id"], reverse=False)
            self.test_data[sport] = sorted_events

    def test_parse_results_all_sports_sorted(self):
        results = cli.filter_and_sort(self.test_data, None)
        self.assertEqual(len(results), 2, "2 sports should be returned")
        self.assertEqual(results["nbaResults"][0], self.test_data["nbaResults"][1])
        self.assertEqual(results["nbaResults"][1], self.test_data["nbaResults"][0])
        self.assertEqual(results["Tennis"][0], self.test_data["Tennis"][1])
        self.assertEqual(results["Tennis"][1], self.test_data["Tennis"][0])
    
    def test_parse_results_one_sport_sorted_when_filtered(self):
        results = cli.filter_and_sort(self.test_data, "Tennis")
        self.assertEqual(len(results), 1, "1 sport should be returned")
        self.assertEqual(results["Tennis"][0], self.test_data["Tennis"][1])
        self.assertEqual(results["Tennis"][1], self.test_data["Tennis"][0])

if __name__ == '__main__':
    unittest.main()