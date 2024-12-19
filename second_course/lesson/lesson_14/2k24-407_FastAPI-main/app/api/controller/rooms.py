from fastapi import Depends

from app.api.repositories.rooms import RoomsRepository


class RoomsController:
    def __init__(
            self,
            rooms_repo: RoomsRepository = Depends()
    ):
        self.__rooms_repo = rooms_repo

    async def get_rooms(self):
        return await self.__rooms_repo.get_all_rooms()
