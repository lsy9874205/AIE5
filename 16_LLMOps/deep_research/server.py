from fastapi import FastAPI
from langserve import add_routes
from open_deep_research.graph import graph

app = FastAPI()

add_routes(
    app,
    graph,
    path="/research",
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)