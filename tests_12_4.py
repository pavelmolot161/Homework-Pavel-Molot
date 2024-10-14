import unittest
from unittest import TestCase
import logging
logging.basicConfig(level=logging.INFO, filemode= 'w', filename='runner_tests_12.4.log', encoding='UTF-8',
                        format='%(asctime)s | %(levelname)s | %(message)s')
class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
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

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            r1 = Runner('Вася', -5)
            for _ in range(10):
                r1.walk()
            self.assertEqual(r1.distance, 50, f'{r1.name}Должен пробежать 50, а пробежал {r1.distance}')
            logging.info('"test_walk" выполнен успешно')
        except ValueError as exc:
            logging.warning("Неверная скорость для Runner", exc_info=exc)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            r2 = Runner(2)
            for _ in range(10):
                r2.run()
            self.assertEqual(r2.distance, 100, f'{r2.name}Должен пробежать 100, а пробежал {r2.distance}')
            logging.info('"test_run" выполнен успешно')
        except TypeError as exc:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=exc)


    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        r1 = Runner('Вася')
        r2 = Runner('Коля')
        for _ in range(10):
            r1.walk()
            r2.run()
        self.assertNotEqual(r1.distance, r2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = False

    @classmethod
    def setUpClass(cls):
        cls.all_variants = []
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.first = Runner('Усэйн', -10)
        self.second = Runner(True, 9)
        self.third = Runner('Ник', 3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_first_tournament(self):
        tournament = Tournament(90, self.first, self.third)
        results = tournament.start()
        TournamentTest.all_variants.append(results)
        self.assertTrue(results[2] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_second_tournament(self):
        tournament = Tournament(90, self.second, self.third)
        results = tournament.start()
        TournamentTest.all_variants.append(results)
        self.assertTrue(results[2] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_third_tournament(self):
        tournament = Tournament(90, self.first, self.second, self.third)
        results = tournament.start()
        TournamentTest.all_variants.append(results)
        self.assertTrue(results[3] == 'Ник')

    @classmethod
    def tearDownClass(cls):
        for i, elem in enumerate(cls.all_variants):
            print(f'{i + 1}. {elem}')
