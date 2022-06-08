from typer import Typer
import uvicorn

main = Typer()

@main.command("init")
def init_service() -> Typer:
    uvicorn.run(
        "bookmark_api.base_api:app", host="127.0.0.1", port=8000,
        log_level="info", reload=True
        )