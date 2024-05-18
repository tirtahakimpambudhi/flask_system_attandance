import os

class Config:
    try:
        __path = os.path.join(os.getcwd(), ".env")
        if os.path.exists(__path):
            from dotenv import load_dotenv
            load_dotenv(dotenv_path=__path)
        SECRET_KEY :str = os.environ.get("SECRET_KEY")
        APP :dict = {
            "env" : os.environ.get("APP_ENV")
        }
        DATABASE :dict = {
            "url": os.environ.get("SUPABASE_URL"),
            "api_key": os.environ.get("SUPABASE_API_KEY"),
            "table" : os.environ.get("SUPABASE_TABLE")
        }
    except KeyError as e:
        print(f"Error: { type(e).__name__} - { e}. Make sure all required variables are defined in the .env file.")

