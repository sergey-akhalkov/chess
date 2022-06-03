from main import app


@app.get("/users")
async def get_users(skip: int = 0, limit: int = 10) -> int:
    return 1


@app.get("/users/me")
async def get_current_user() -> dict:
    return dict()


@app.get("/users/{user_id}")
async def get_user_by_id(user_id: int) -> dict:
    return dict()


@app.get("/users/{user_id}/games")
async def get_user_games(user_id: int, skip: int = 0, limit: int = 10) -> list:
    return []
