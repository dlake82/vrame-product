from fastapi import APIRouter, Depends, status

from ..db import models
from ..db.db import get_db
from sqlalchemy.orm import Session
from .. import oauth2
from app.schemas import users, base
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

router = APIRouter()


@router.get('/data', response_model=base.TestResponse)
def data():
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(
            {"detail": "Success to send test data.", "body": {
            "영남": {
            "사과": {
                "더 좋은 사과": {
                "청사과": "500",
                "적사과": "1000",
                },
                "더 싫은 사과": "1200",
            },
            "딸기": {
                "더 좋은 딸기": "400",
                "더 싫은 딸기": "1200",
            },
            },
            "송탄": {
            "포도": {
                "더 좋은 포도": "500",
                "더 싫은 포도": "1200",
            },
            "배": {
                "더 좋은 배": "500",
                "더 싫은 배": "1200",
            },
            },
        }
    }))
    