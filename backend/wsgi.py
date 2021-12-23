from backend import create_app

app = create_app()
logging.init_logging()
app.logger.info("Start Falsk server for Home Automation backend")
if __name__ == "__main__":
    app.run(threaded=True)