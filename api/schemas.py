# -*- coding: utf-8 -*-
"""
Author: Augusto Carlo Pareja
Description: This script defines the Pydantic schemas for character data in the Python Challenge application.
"""

from pydantic import BaseModel, Field

class CharacterBase(BaseModel):
    id: int = Field(..., example=1)
    name: str = Field(..., example="Darth Vader")
    height: int = Field(..., example=202)
    mass: int = Field(..., example=136)
    hair_color: str = Field(..., example="black")
    skin_color: str = Field(..., example="white")
    eye_color: str = Field(..., example="yellow")
    birth_year: int = Field(..., example=1954)
    
    class Config:
        from_attributes = True