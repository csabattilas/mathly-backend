from functools import wraps
from flask import request, jsonify, g
from firebase_admin import auth as firebase_auth

def firebase_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        id_token = None

        # Expect token in Authorization header as: Bearer <token>
        auth_header = request.headers.get("Authorization", None)
        if auth_header:
            parts = auth_header.split()
            if len(parts) == 2 and parts[0].lower() == "bearer":
                id_token = parts[1]

        if not id_token:
            return jsonify({"error": "Authorization header missing or invalid"}), 401

        try:
            decoded_token = firebase_auth.verify_id_token(id_token)
            # You can access uid and user info here
            g.firebase_user = decoded_token
        except Exception as e:
            return jsonify({"error": "Invalid or expired token", "message": str(e)}), 401

        return f(*args, **kwargs)

    return decorated_function
