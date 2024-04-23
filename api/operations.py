# -*- coding: utf-8 -*-
"""
Author: Augusto Carlo Pareja
Description: This script contains operations related to database CRUD (Create, Read, Update, Delete) for characters in the Python Challenge application.
"""

from sqlalchemy.orm import Session
from . import models, schemas

def get_all_characters(db: Session):
    characters = db.query(models.Character).all()
    return [schemas.CharacterBase.model_validate(character) for character in characters]

def get_character(db: Session, character_id: int):
    character = db.query(models.Character).filter(models.Character.id == character_id).first()
    return schemas.CharacterBase.model_validate(character) if character else None

def create_character(db: Session, character: schemas.CharacterBase):
    character = models.Character(**character.model_dump())
    db.add(character)
    db.commit()
    db.refresh(character)
    return schemas.CharacterBase.model_validate(character)

def delete_character(db: Session, character_id: int):
    character = db.query(models.Character).filter(models.Character.id == character_id).first()
    if character is None:
        return None
    db.delete(character)
    db.commit()