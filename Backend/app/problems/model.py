import random

# Cria a classe para gerar problemas de soma
class CreatorSumProblem:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def difficult_level(self):
        if self.difficulty == "easy":
            return 0, 100
        elif self.difficulty == "medium":
            return 101, 1000
        elif self.difficulty == "hard":
                return 1001, 99999

        raise ValueError("Invalid difficulty")

    def sum_generator(self):
        first_value, last_value = self.difficult_level()

        x = random.randint(first_value, last_value)
        y = random.randint(first_value, last_value)

        return {
            "operation": "+",
            "x": x,
            "y": y,
            "difficulty": self.difficulty,
        }

    def sub_generator(self):
        first_value, last_value = self.difficult_level()

        x = random.randint(first_value, last_value)
        y = random.randint(first_value, last_value)

        return {
            "operation": "-",
            "x": x,
            "y": y,
            "difficulty": self.difficulty,
        }
    
    
