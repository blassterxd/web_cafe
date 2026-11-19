from pathlib import Path
from typing import Literal

from fastapi import Query
from fastapi.responses import FileResponse
from fastapi_offline import FastAPIOffline

app = FastAPIOffline(title="Кофейня «Перемена»", redoc_url=None)
prices = {"cappuccino": 180, "cocoa": 150}


@app.get("/", include_in_schema=False)
def home():
    return FileResponse(Path(__file__).with_name("index.html"))


@app.get("/api/price", summary="Рассчитать заказ")
def calculate_price(
    drink: Literal["cappuccino", "cocoa"],
    quantity: int = Query(1, ge=1, le=10),
    oat: bool = False,
):
    unit_price = prices[drink]
    if oat:
        unit_price += 30
    return {
        "drink": drink,
        "quantity": quantity,
        "unit_price": unit_price,
        "total": unit_price * quantity,
    }
