# def add(a: int, b: int) -> int:
#     """Adds two numbers and returns the result."""
#     return a + b

# if __name__ == "__main__":
#     result = add(2, 3)
#     print(f"2 + 3 = {result}")
    
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}