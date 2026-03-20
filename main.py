from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "AI Business OS is running"}
@app.get("/product")
def get_product():
    return {
        "products": [
            "Мини-пылесос для клавиатуры",
            "LED подсветка для комнаты",
            "Умная бутылка с температурой",
            "Портативный блендер",
            "Массажёр для шеи"
        ]
    }
