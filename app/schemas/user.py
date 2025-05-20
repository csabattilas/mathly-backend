from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow import fields, validates, ValidationError
from app.models.user import User

class UserSchema(SQLAlchemyAutoSchema):
    """Schema for the User model."""
    class Meta:
        model = User
        include_relationships = True
        load_instance = True
    
    # You can override fields or add custom ones
    email = auto_field(required=True)
    
    @validates('email')
    def validate_email(self, value):
        if not value or '@' not in value:
            raise ValidationError('Not a valid email address.')

class UserCreateSchema(SQLAlchemyAutoSchema):
    """Schema for creating a new user."""
    class Meta:
        model = User
        include_relationships = True
        load_instance = True
        exclude = ('id', 'firebase_uid')  # These are set by the system