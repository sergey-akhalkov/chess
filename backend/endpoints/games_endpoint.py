from main import app


@app.get("/games")
async def get_games(skip: int = 0, limit: int = 10) -> list:
    return []


@app.get("/games/{game_id}")
async def get_game_by_id(game_id: int) -> dict:
    return dict()


@app.post("/games")
async def create_game() -> int:
    return 1


@app.post("/games/{game_id}/turns")
async def make_turn(game_id: int, from_cell: str, to_cell: str) -> dict:
    return dict()
