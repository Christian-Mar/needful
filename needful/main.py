"""Entrypoint: FastAPI-app met NiceGUI erbovenop.

Start met:  uvicorn needful.main:app --reload
"""

from fastapi import FastAPI
from nicegui import ui

from needful.api.routes import router as api_router
from needful.ui import pages  # noqa: F401  (registreert de NiceGUI-pagina's)

app = FastAPI(title="needful.", version="0.1.0")
app.include_router(api_router, prefix="/api")

ui.run_with(app, title="needful.", storage_secret="dev-only-change-me")
