from flask import g
from app.routes.protected import protected_bp
from app.models.user import User
from app.extensions import db
from app.services.auth import firebase_required
from app.schemas import UserSchema, UserCreateSchema
from app.utils.json import model_to_dict

@protected_bp.route("/users/me", methods=["GET", "POST"])
@protected_bp.response(200, UserSchema)
@protected_bp.response(201, UserSchema, description="User was created")
@protected_bp.response(500, description="Database error")
@firebase_required
def get_current_user():
    """Get or create current user
    
    Returns the current authenticated user's details.
    If the user doesn't exist in the database, creates them automatically.
    """
    # Get firebase user from Flask's g object where it was stored by the decorator
    firebase_user = g.firebase_user
    
    if not firebase_user or "uid" not in firebase_user:
        return {"error": "Invalid Firebase user data"}, 400

    # Try to find existing user
    user = User.query.filter_by(firebase_uid=firebase_user["uid"]).first()
    
    # If user doesn't exist, create them
    if not user:
        # Extract basic info from Firebase user data
        email = firebase_user.get("email", "")
        name = firebase_user.get("name", "") or email.split("@")[0] if email else ""
        
        user = User(
            email=email,
            name=name,
            firebase_uid=firebase_user["uid"]
        )
        
        try:
            db.session.add(user)
            db.session.commit()
            return model_to_dict(user), 201  # Created
        except Exception as e:
            db.session.rollback()
            return {"error": "Failed to create user", "message": str(e)}, 500

    return model_to_dict(user), 200  # OK