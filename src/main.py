from schema.Task import Task
from fastapi import Depends, FastAPI, Header, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

app = FastAPI()

tasks: list[Task] = []

@app.get("/")
def read_root():
    return {"Hello": "World"}

def ensure_json_content_type(content_type: str = Header(...)):
    if content_type != "application/json":
        raise HTTPException(
            status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            f"Tipo de mídia não suportado: {content_type}."
            " Precisa ser application/json",
        )

@app.post("/tasks", status_code=status.HTTP_201_CREATED, dependencies=[Depends(ensure_json_content_type)])
async def create_task(task: Task):
    for item in tasks:
        if task.id == item.id:
            raise HTTPException(status_code=400, detail="ID já existente. Tente outro.")
    tasks.append(task)
    json_compatible_item_data = jsonable_encoder(task)
    return JSONResponse(content=json_compatible_item_data, media_type="application/json")

@app.get("/tasks", status_code=status.HTTP_200_OK)
async def read_all_tasks():
    json_compatible_item_data = jsonable_encoder(tasks)
    return JSONResponse(json_compatible_item_data)

@app.get("/tasks/{id}", status_code=status.HTTP_200_OK)
async def read_task(id: int):
    for item in tasks:
        if item.id == id:
            json_compatible_item_data = jsonable_encoder(item)
            return JSONResponse(content=json_compatible_item_data)
    raise HTTPException(status_code=404, detail="Tarefa não encontrada.")
        
@app.put("/tasks/{id}", status_code=status.HTTP_200_OK, dependencies=[Depends(ensure_json_content_type)])
async def update_task(id: int, task: Task):
    for item in tasks:
        if item.id == id:
            item.description = task.description
            item.isFinished = task.isFinished
            json_compatible_item_data = jsonable_encoder(item)
            return JSONResponse(content=json_compatible_item_data, media_type="application/json")
    raise HTTPException(status_code=404, detail="Tarefa não encontrada.")

@app.delete("/tasks/{id}", status_code=status.HTTP_200_OK, response_description="Tarefa removida com sucesso!")
async def delete_task(id: int):
    for item in tasks:
        if item.id == id:
            tasks.remove(item)
            json_compatible_item_data = jsonable_encoder(item)
            return JSONResponse(content=json_compatible_item_data)
    raise HTTPException(status_code=404, detail="Tarefa não encontrada.")

if __name__ == '__main__':
    import uvicorn
    
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)