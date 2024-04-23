# -*- coding: utf-8 -*-
"""
Author: Augusto Carlo Pareja
Description: This script defines the API routes for interacting with characters in the Python Challenge application.
"""
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from . import operations, schemas
from .database import SessionLocal

router = APIRouter()

def get_db():
    """
    Function to create a new database session and close it after the request is processed.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/character/getAll", response_model=list[schemas.CharacterBase])
def api_get_all_characters(db: Session = Depends(get_db)):
    """
    Retrieve all characters from the database.
    
    Returns:
        List of character objects.
    """
    db_all_characters = operations.get_all_characters(db)
    return db_all_characters

@router.get("/character/get/{character_id}", response_model=schemas.CharacterBase)
def api_get_character(character_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a specific character from the database.

    Args:
        character_id (int): ID of the character to retrieve.

    Raises:
        HTTPException: If the character with the given ID is not found.

    Returns:
        Character object.
    """
    db_character = operations.get_character(db, character_id)
    if db_character is None:
        raise HTTPException(status_code=404, detail="Character not found")
    return db_character

@router.post("/character/add", response_model=schemas.CharacterBase)
def api_create_character(character: schemas.CharacterBase, db: Session = Depends(get_db)):
    """
    Create a new character in the database.

    Args:
        character object: Character data to be created.

    Raises:
        HTTPException: If a character with the same ID already exists.

    Returns:
        The created character object.
    """
    db_existing_character = operations.get_character(db, character.id)
    if db_existing_character:
        raise HTTPException(status_code=400, detail="Character already exists")
    return operations.create_character(db, character)

@router.delete("/character/delete/{character_id}", response_model=dict, responses={200: {"description": "Character deleted successfully", "content": {"application/json": {"example": {"message": "Character deleted successfully"}}}}})
def api_delete_character(character_id: int, db: Session = Depends(get_db)):
    """
    Delete a character from the database.

    Args:
        character_id (int): ID of the character to delete.

    Raises:
        HTTPException: If the character with the given ID is not found.

    Returns:
        A message confirming the deletion of the character.
    """
    db_character = operations.delete_character(db, character_id)
    if db_character is None:
        raise HTTPException(status_code=404, detail="Character not found")
    return {"message": "Character deleted successfully"}