from flask_smorest import Blueprint

public_bp = Blueprint('public', 'public', url_prefix='/api/v1/public', description='Public endpoints')

from . import health  # add other public route modules here
