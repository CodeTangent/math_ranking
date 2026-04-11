from .model import CreatorSumProblem


def spitter_of_sums(difficulty):
    try:
        problem = CreatorSumProblem(difficulty)
        return problem.generate()

    except ValueError:
        return {
            "operation": None,
            "x": None,
            "y": None,
            "difficulty": None,
            "error": "Invalid difficulty",
        }
    