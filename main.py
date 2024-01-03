
import flask
import json
import traceback


def save (json_data):
    json = json.dumps(dict)

    # open file for writing, "w" 
    f = open("dict.json","w")
    return "Saved"


def is_not_number(variable):
    return not isinstance(variable, (int, float))

app = flask.Flask(__name__)


@app.route("/users", methods=["POST"])

def users():
    try:
        # Access the JSON data from the POST request
        request_data = flask.request.get_json()
        print(request_data)

        if(request_data["name"] == None or request_data["name"] == "" or len(request_data["name"])>32):
            return flask.jsonify(message={"trace": traceback.format_exc()}, status=400), 400
        
        if(is_not_number(request_data["age"]) or request_data["age"] < 16):
            return flask.jsonify(message={"trace": traceback.format_exc()}, status=400), 400

        print(save(request_data))
        # Example response data
        response_data = {"message": "Data received successfully"}

        return flask.jsonify(response_data, status = 201), 201
    except Exception as e:
        # Log the exception traceback
        print(f"An error occurred: {e}")
        return flask.jsonify(message={"trace": traceback.format_exc()}, status=400), 400


if __name__ == "__main__":
    app.run()