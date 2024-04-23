# -*- coding: utf-8 -*-
"""
Author: Augusto Carlo Pareja
Description: This script initializes the FastAPI application for the Python Challenge.
"""

from fastapi import FastAPI
from . import models, database, routes

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

app.include_router(routes.router)