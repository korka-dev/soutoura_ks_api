from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models.survey import CustomerSurvey
from schemas.survey import SurveyCreate, SurveyResponse

router = APIRouter(prefix="/surveys", tags=["Sondages"])

@router.post("/", response_model=SurveyResponse, status_code=201)
def create_survey(data: SurveyCreate, db: Session = Depends(get_db)):
    """Créer un nouveau sondage (client)"""
    survey = CustomerSurvey(**data.dict())
    db.add(survey)
    db.commit()
    db.refresh(survey)
    return survey

@router.get("/", response_model=List[SurveyResponse])
def get_all_surveys(db: Session = Depends(get_db)):
    """Lister tous les sondages (admin)"""
    surveys = db.query(CustomerSurvey).order_by(CustomerSurvey.created_at.desc()).all()
    return surveys

@router.get("/{survey_id}", response_model=SurveyResponse)
def get_survey_by_id(survey_id: int, db: Session = Depends(get_db)):
    """Récupérer un sondage par ID"""
    survey = db.query(CustomerSurvey).filter(CustomerSurvey.id == survey_id).first()
    if not survey:
        raise HTTPException(status_code=404, detail="Sondage introuvable")
    return survey


@router.delete("/{survey_id}")
def delete_survey(survey_id: int, db: Session = Depends(get_db)):
    """Supprimer un sondage"""
    survey = db.query(CustomerSurvey).filter(CustomerSurvey.id == survey_id).first()
    if not survey:
        raise HTTPException(status_code=404, detail="Sondage introuvable")
    db.delete(survey)
    db.commit()
    return {"message": "Sondage supprimé avec succès"}

