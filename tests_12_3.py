

### - tests_12_3.py

import unittest
from unittest import TestCase

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

#____________________________________________________________________________________________________________

class RunnerTest(TestCase):

    is_frozen = False

    def __init__(self, name):
        super().__init__(name)

    def setUp(self):
        self.runner = Runner('running')
        self.runner_2 = Runner('running_2')
        self.runner_a = Runner('running_a')
        self.runner_b = Runner('running_b')

        '''Декоратор @unittest.skipIf — это один из встроенных декораторов модуля unittest в Python, 
        который используется для пропуска тестов в зависимости от определенного условия. 
        Это позволяет гибко управлять набором тестов, в нашем случае мы определили атрибут класса is_frozen = False
        для удобного создания условия в декораторе, после чего в декораторе пропишем is_frozen == True что 
        позволит методу работать беспрепятственно, а еще можно контролировать работу всего класса.'''

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        self.runner = Runner('running')
        for _ in range(10):
            self.runner.walk()
        self.assertEqual(self.runner.distance,50)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        self.runner_2 = Runner('running_2')
        for _ in range(10):
            self.runner_2.run()
        self.assertEqual(self.runner_2.distance, 100)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        self.runner_a = Runner('running_a')
        for _ in range(10):
            self.runner_a.run()
        self.runner_b = Runner('running_b')
        for _ in range(10):
            self.runner_b.walk()
        self.assertNotEqual(self.runner_a.distance, self.runner_b.distance, '(running_a) должно быть '
                                                                            'не равно (running_b)')
#############################################################################################################

class Runner_2:
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
        elif isinstance(other, Runner_2):
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
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = Runner_2('Усэйн', 10)
        self.runner_2 = Runner_2('Андрей', 9)
        self.runner_3 = Runner_2('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        # print('Результаты всех забегов: ')
        for key, results in cls.all_results.items():
            names = {place: str(participant) for place, participant in results.items()}
            print(f'Забег {key}: {names}')

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_first_tournament(self):
        tournament = Tournament(90, self.runner_1, self.runner_3)
        results = tournament.start()
        self.all_results[1] = results
        self.assertEqual(list(results.values())[-1], self.runner_3)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_second_tournament(self):
        tournament = Tournament(90, self.runner_2, self.runner_3)
        results = tournament.start()
        self.all_results[2] = results
        self.assertEqual(list(results.values())[-1], self.runner_3)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_third_tournament(self):
        tournament = Tournament(90,  self.runner_1,  self.runner_2,  self.runner_3)
        results = tournament.start()
        self.all_results[3] = results
        self.assertEqual(list(results.values())[-1], self.runner_3)

if __name__ == "__main__":
    import unittest
    unittest.main()

