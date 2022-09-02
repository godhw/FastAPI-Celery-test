from pydantic import BaseSettings


class ServerSettings(BaseSettings):
    app_name: str = "Fast API with Celery"
    app_version: str = "0.0.1"
    app_env: str = "dev"


class ModelSettings(BaseSettings):
    model_path: str = "microsoft/CodeGPT-small-py"
    use_fast_tokenizer: bool = True
    model_min_length: int = 1


server_settings = ServerSettings()
model_settings = ModelSettings()
