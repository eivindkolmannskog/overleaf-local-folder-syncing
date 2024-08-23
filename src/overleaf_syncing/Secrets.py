from dotenv import set_key, load_dotenv
import os
from dataclasses import dataclass
from .utilities import request_app_key, request_app_secret


@dataclass
class Secrets:

    CLIENT_APP_KEY: str | None = None
    CLIENT_APP_SECRET: str | None = None
    CLIENT_ACCESS_TOKEN: str | None = None
    CLIENT_REFRESH_TOKEN: str | None = None

    def __init__(self):
        load_dotenv()

        self.CLIENT_APP_KEY = os.getenv("CLIENT_APP_KEY")
        if self.CLIENT_APP_KEY is None:
            self.CLIENT_APP_KEY = request_app_key()
            set_key(".env", "CLIENT_APP_KEY", self.CLIENT_APP_KEY)

        self.CLIENT_APP_SECRET = os.getenv("CLIENT_APP_SECRET")
        if self.CLIENT_APP_SECRET is None:
            self.CLIENT_APP_SECRET = request_app_secret()
            set_key(".env", "CLIENT_APP_SECRET", self.CLIENT_APP_SECRET)

        self.CLIENT_ACCESS_TOKEN = os.getenv("CLIENT_ACCESS_TOKEN")
        self.CLIENT_REFRESH_TOKEN = os.getenv("CLIENT_REFRESH_TOKEN")

    def update_tokens(self, access_token: str, refresh_token: str):
        self.CLIENT_ACCESS_TOKEN = access_token
        set_key(".env", "CLIENT_ACCESS_TOKEN", access_token)

        self.CLIENT_REFRESH_TOKEN = refresh_token
        set_key(".env", "CLIENT_REFRESH_TOKEN", refresh_token) 


    

    
