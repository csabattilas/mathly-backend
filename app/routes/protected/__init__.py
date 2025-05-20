from flask_smorest import Blueprint

protected_bp = Blueprint('protected', 'protected', url_prefix='/api/v1', description='Protected endpoints')

from . import user  # add other protected route modules here
