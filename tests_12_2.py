
### - tests_12_2.py

from unittest import TestCase

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name

class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

#________________________________________________________________________________________________________

class TournamentTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = Runner('Усэйн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        print('Результаты всех забегов: ')
        for key, results in cls.all_results.items():
            names = {place: str(participant) for place, participant in results.items()}
            print(f'Забег {key}: {names}')

    def test_usain_nik(self):
        tournament = Tournament(90, self.runner_1, self.runner_3)
        results = tournament.start()
        self.all_results[1] = results ### - Результаты турнира, сохраненные в переменной results, записываются в
                                       ## словарь self.all_results по индексу 1.
                                        # Это позволяет сохранить результаты теста для дальнейшего использования или проверки.
        self.assertEqual(list(results.values())[-1], self.runner_3)

    def test_andrei_nik(self):
        tournament = Tournament(90, self.runner_2, self.runner_3)
        results = tournament.start()
        self.all_results[2] = results
        self.assertEqual(list(results.values())[-1], self.runner_3)

    def test_usain_andrei_nik(self):
        tournament = Tournament(90,  self.runner_1,  self.runner_2,  self.runner_3)
        results = tournament.start()
        self.all_results[3] = results
        self.assertEqual(list(results.values())[-1], self.runner_3)

if __name__ == "__main__":
    import unittest
    unittest.main()
