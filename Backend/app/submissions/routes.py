from flask import Blueprint, jsonify, request

from .service import validate_submission

submissions_blueprint = Blueprint("submissions", __name__)


@submissions_blueprint.route("/submit", methods=["POST"])
def submit():
    if not (data := request.get_json()):
        return jsonify(
            {
                "is_correct": False,
                "correct_answer": None,
                "difficulty": None,
                "error": "No data provided",
            }
        ), 400

    result = validate_submission(data)

    if result.get("error"):
        return jsonify(result), 400

    return jsonify(result)
