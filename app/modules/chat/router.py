from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db

from app.modules.chat.schema import (
    ChatRequest,
    ChatResponse
)

from app.modules.chat.service import ChatService


router = APIRouter(
    prefix="/chat",
    tags=["AI Chat"]
)


@router.post(
    "/",
    response_model=ChatResponse
)
def chat(
    request: ChatRequest,
    db: Session = Depends(get_db)
):

    return ChatService.ask_question(
        db=db,
        session_id=request.session_id,
        question=request.question
    )