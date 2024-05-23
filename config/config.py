import os

class Config:
    try:
        __path = os.path.join(os.getcwd(), ".env")
        if os.path.exists(__path):
            from dotenv import load_dotenv
            load_dotenv(dotenv_path=__path)
        SECRET_KEY :str = os.environ.get("SECRET_KEY")
        SQLALCHEMY_DATABASE_URI :str = os.environ.get("SUPABASE_CONNECTION_STRING")
        APP :dict = {
            "env" : os.environ.get("APP_ENV")
        }
        UPLOAD_PATH :str = os.environ.get("UPLOAD_PATH")
        LOG_PATH :str = os.environ.get("LOG_PATH")
        CALL_API_TIMEOUT :int = os.environ.get("TIME_OUT_CALL_API")
        CALL_API_TIME_INTERVAL :int = os.environ.get("TIME_INTERVAL_CALL_API")
        DATABASE :dict = {
            "url": os.environ.get("SUPABASE_URL"),
            "api_key": os.environ.get("SUPABASE_API_KEY"),
            "tables" : os.environ.get("SUPABASE_TABLE").rsplit(",")
        }
    except KeyError as e:
        print(f"Error: { type(e).__name__} - { e}. Make sure all required variables are defined in the .env file.")

