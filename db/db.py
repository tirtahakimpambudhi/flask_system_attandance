
from supabase import create_client, Client
import logging

def new_connection(supabase_url: str, supabase_api_key: str) -> Client:
    """
    Creates a new connection to the Supabase client.

    :param supabase_url: The URL of the Supabase instance.
    :param supabase_api_key: The API key for the Supabase instance.
    :return: A Supabase Client object if the connection is successful.
    :raises Exception: If the connection fails.
    """
    try:
        pool: Client = create_client(supabase_url, supabase_api_key)
        logging.info("Successfully created Supabase client connection.")
        return pool
    except Exception as e:
        logging.error("Failed to create Supabase client connection: %s", e)
        raise e

