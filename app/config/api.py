"""API configuration for the application."""

class ApiConfig:
    """API configuration settings."""
    
    @staticmethod
    def get_config():
        """Get the API configuration.
        
        Returns:
            dict: The API configuration settings
        """
        return {
            "API_TITLE": "Mathly API",
            "API_VERSION": "v1",
            "OPENAPI_VERSION": "3.0.2",
            "OPENAPI_URL_PREFIX": "/api/docs",
            "OPENAPI_SWAGGER_UI_PATH": "/swagger",
            "OPENAPI_SWAGGER_UI_URL": "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
        }
