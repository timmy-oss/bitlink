from pydantic import BaseSettings, AnyUrl


class Settings(BaseSettings):
    " Model for the application settings  "
    debug : bool = True
    app_name : str = "LinkLite"
    allowed_origins : list[str] = ["http://localhost:3000",]
    db_url : AnyUrl = "redis://127.0.0.1:10005"
    db_username : str = "default"
    db_password  : str = "root"
    base_domain : str = "localhost:8000"
    


    class Config:
        env_file = ".secrets"