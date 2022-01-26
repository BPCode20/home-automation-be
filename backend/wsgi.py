from backend import create_app
from backend import backend_logging

app = create_app()
# backend_logging.init_logging()
app.logger.info("Start Falsk server for Home Automation backend")
if __name__ == "__main__":
    app.run(threaded=True)