from . import public_bp

@public_bp.route("/health")
@public_bp.response(200, description="Health check successful")
def health_check():
    """Health check endpoint
    
    Returns status ok if the server is running
    """
    return {"status": "ok"}
    