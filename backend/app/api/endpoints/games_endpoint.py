from fastapi import APIRouter

router = APIRouter()


@router.get("/games")
async def get_games(skip: int = 0, limit: int = 10) -> list:
    return []


@router.get("/games/{game_id}")
async def get_game_by_id(game_id: int) -> dict:
    return dict()


@router.post("/games")
async def create_game() -> int:
    return 1


@router.post("/games/{game_id}/turns")
async def make_turn(game_id: int, from_cell: str, to_cell: str) -> dict:
    return dict()
