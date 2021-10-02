from flask import Flask
from flask import jsonify
from flask import request

from database import Database
from methods import Token, Restricted
from convert import CidrMaskConvert


app = Flask(__name__)

database = Database()

token = Token()
convert = CidrMaskConvert()
restricted = Restricted()


# e.g. http://127.0.0.1:8000/
@app.route("/")
def url_root():
    response = jsonify({"status": "OK"})
    return response


# e.g. http://127.0.0.1:8000/_health
@app.route("/_health")
def url_health():
    response = jsonify({"status": "OK"})
    return response


# e.g. http://127.0.0.1:8000/login
@app.route("/login", methods=["POST"])
def url_login():
    try:
        username = request.form["username"]
        password = request.form["password"]

        userData = database.get_user(username, password)
        
        if userData is not None:
            userData = token.generate_token(userData)

        res = {
            "data": userData
        }
        return jsonify(res)
    except:
        return jsonify({"data": None})


# e.g. http://127.0.0.1:8000/cidr-to-mask?value=24
@app.route("/cidr-to-mask")
def cidr_to_mask():
    try:
        auth_token = request.headers.get('Authorization')
        headerToken = auth_token.split(' ')

        if len(headerToken) == 0 or restricted.access_data(headerToken[1]) is None:
            response = jsonify({
                "status": "ACCESS DENIED"
            })
            response.status_code = 401
            return response

        reqValue = request.args.get('value', None)
        if reqValue is None or reqValue.isdigit() is False:
            output = 'invalid'
        else:
            output = convert.cidr_to_mask(int(reqValue))

        response = {
            "status": "OK",
            "function": "cidrToMask",
            "input": reqValue,
            "output": output
        }
        return jsonify(response)
    except:
        response = jsonify({
            "status": "ACCESS DENIED"
        })
        response.status_code = 401
        return response



# e.g. http://127.0.0.1:8000/mask-to-cidr?value=255.255.0.0
@app.route("/mask-to-cidr")
def mask_to_cidr():
    try:
        auth_token = request.headers.get('Authorization')
        headerToken = auth_token.split(' ')

        if len(headerToken) == 0 or restricted.access_data(headerToken[1]) is None:
            response = jsonify({
                "status": "ACCESS DENIED"
            })
            response.status_code = 401
            return response

        reqValue = request.args.get('value', None)
        if reqValue is None:
            output = 'invalid'
        else:
            output = convert.mask_to_cidr(str(reqValue))

        response = {
            "status": "OK",
            "function": "maskToCidr",
            "input": reqValue,
            "output": output
        }
        return jsonify(response)
    except:
        response = jsonify({
            "status": "ACCESS DENIED"
        })
        response.status_code = 401
        return response


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)