from typing import Callable

import torch
from fastapi import FastAPI
from loguru import logger
from transformers import AutoModelForCausalLM, AutoTokenizer

from config import model_settings


def _load_model(app: FastAPI) -> None:
    logger.info("Start load model")
    model_path = model_settings.model_path
    app.state.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    logger.info("Load tokenizer")
    app.state.tokenizer = AutoTokenizer.from_pretrained(model_path)

    logger.info("Load model")
    app.state.model = AutoModelForCausalLM.from_pretrained(model_path).to(app.state.device)

    logger.info("Finish load model")


def _shutdown_model(app: FastAPI) -> None:
    del app.state.model
    del app.state.tokenizer
    del app.state.device


def start_app_handler(app: FastAPI) -> Callable:
    def startup() -> None:
        logger.info("Running App Start Handler")
        _load_model(app)

    return startup


def stop_app_handler(app: FastAPI) -> Callable:
    def shutdown() -> None:
        logger.info("Runing App Shutdown Handler")
        _shutdown_model(app)

    return shutdown
