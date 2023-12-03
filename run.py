"""Run the application for development."""
from ezbudget import create_app

if __name__ == "__main__":
    app = create_app('config.py')
    app.run(debug=True, host='localhost', port=8080)
