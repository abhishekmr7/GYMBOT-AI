from fastapi import APIRouter

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
    request: ChatRequest
):
    return ChatService.ask_question(
        request.question
    )