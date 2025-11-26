# backend/wamini_package/run.py

from wamini_package.app import create_app
import os

# Create a Flask app instance using the factory pattern
app = create_app()

# Only run the Flask development server if this file is executed directly
if __name__ == "__main__":
    # Determine if the app should run in debug mode based on the environment
    debug_mode = os.getenv("FLASK_ENV") == "development"
    
    # Run the Flask development server locally
    # host="0.0.0.0" allows external access
    # port is taken from the PORT environment variable (Render provides this)
    # debug_mode enables debug mode only in development
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=debug_mode)
