from fastapi import FastAPI, HTTPException

app = FastAPI()

robots = [
    {
        "id": 1,
        "name": "Кьюриосити",
        "planet": "Марс",
        "status": "active"
    },
    {
        "id": 2,
        "name": "Персеверанс",
        "planet": "Марс",
        "status": "active"
    },
    {
        "id": 3,
        "name": "Окпорьюнити",
        "planet": "Марс",
        "status": "offline"
    }
]

@app.get("/")
def read_root():
    return {
        "service": "API каталога роботов-исследователей",
        "path": "/robots"
    }

@app.get("/robots")
def get_robots(status: str | None = None):
    if status is None:
        return robots
    filtered_robots = [robot for robot in robots if robot["status"] == status]
    return filtered_robots

@app.get("/robots/{robot_id}")
def get_robot_by_id(robot_id: int):
    for robot in robots:
        if robot["id"] == robot_id:
            return robot
    raise HTTPException(status_code=404, detail="Робот не найден")