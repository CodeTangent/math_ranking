from flask import Blueprint, jsonify, request

from .service import spitter_of_sums

problems_blueprint = Blueprint("problems", __name__)


@problems_blueprint.route("/problems", methods=["GET"])
def get_problems():
    if not (difficulty := request.args.get("difficulty")):
        return jsonify({"error": "Difficulty not provided"})

    problem = spitter_of_sums(difficulty)

    if problem.get("error"):
        return jsonify(problem)

    return jsonify(problem)
