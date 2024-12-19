from fastapi import APIRouter, Depends

from app.api.controller.rooms import RoomsController

router = APIRouter()


@router.get("")
async def get_rooms(
        controller: RoomsController = Depends()
):
    return await controller.get_rooms()
