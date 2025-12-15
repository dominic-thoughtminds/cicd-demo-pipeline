from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/health")
def health():
    return JSONResponse(status_code=200, content={"status": "ok"})

@app.get("/")
def hello():
    return {"message": "Hello from demo app 2!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)