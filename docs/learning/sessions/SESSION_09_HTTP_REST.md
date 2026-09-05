# Session 09 — HTTP & REST

**Status:** COMPLETED
**Confidence:** 8.5/10

## Concepts Covered

- HTTP request/response lifecycle
- GET, POST, PUT, PATCH, DELETE
- Path vs query parameters
- Headers and request body
- Response body and status codes
- Authentication vs authorization
- Timeout, retry and exponential backoff
- Rate limiting / 429
- Idempotency / `Idempotency-Key`
- REST resource-oriented API design
- FastAPI routing
- Pydantic request and response models
- Dependency Injection with `Depends`
- Middleware concept
- OpenAPI / Swagger concept

## Practical Restaurant API

```text
GET    /restaurants
GET    /restaurants/{restaurant_id}
POST   /restaurants
PATCH  /restaurants/{restaurant_id}
DELETE /restaurants/{restaurant_id}
```

```python
from fastapi import FastAPI, HTTPException, Query, status
from pydantic import BaseModel, Field

app = FastAPI(title="Restaurant API")

class CreateRestaurantRequest(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    city: str = Field(min_length=2, max_length=100)

class UpdateRestaurantRequest(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=100)
    city: str | None = Field(default=None, min_length=2, max_length=100)

class RestaurantResponse(BaseModel):
    id: int
    name: str
    city: str

restaurants: dict[int, RestaurantResponse] = {
    1: RestaurantResponse(id=1, name="Pizza House", city="Tehran"),
    2: RestaurantResponse(id=2, name="Cafe Roma", city="Shiraz"),
}

@app.get("/restaurants", response_model=list[RestaurantResponse])
async def get_restaurants(
    city: str | None = Query(default=None),
    limit: int = Query(default=10, ge=1, le=100),
):
    result = list(restaurants.values())
    if city is not None:
        result = [r for r in result if r.city.lower() == city.lower()]
    return result[:limit]

@app.get("/restaurants/{restaurant_id}", response_model=RestaurantResponse)
async def get_restaurant(restaurant_id: int):
    restaurant = restaurants.get(restaurant_id)
    if restaurant is None:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return restaurant

@app.post("/restaurants", response_model=RestaurantResponse,
          status_code=status.HTTP_201_CREATED)
async def create_restaurant(request: CreateRestaurantRequest):
    restaurant_id = max(restaurants.keys(), default=0) + 1
    restaurant = RestaurantResponse(
        id=restaurant_id,
        name=request.name,
        city=request.city,
    )
    restaurants[restaurant_id] = restaurant
    return restaurant

@app.patch("/restaurants/{restaurant_id}", response_model=RestaurantResponse)
async def update_restaurant(restaurant_id: int, request: UpdateRestaurantRequest):
    restaurant = restaurants.get(restaurant_id)
    if restaurant is None:
        raise HTTPException(status_code=404, detail="Restaurant not found")

    updated = RestaurantResponse(
        id=restaurant.id,
        name=request.name if request.name is not None else restaurant.name,
        city=request.city if request.city is not None else restaurant.city,
    )
    restaurants[restaurant_id] = updated
    return updated

@app.delete("/restaurants/{restaurant_id}",
            status_code=status.HTTP_204_NO_CONTENT)
async def delete_restaurant(restaurant_id: int) -> None:
    if restaurant_id not in restaurants:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    del restaurants[restaurant_id]
```

## Mental Model

```text
HTTP Request
    ↓
FastAPI Router
    ↓
Path / Query / Headers / Body
    ↓
Pydantic Validation
    ↓
Endpoint Function
    ↓
Business Logic
    ↓
Response Model
    ↓
JSON + HTTP Status
```

## Production Notes

The in-memory dictionary is intentionally educational. Production persistence belongs in PostgreSQL/SQLAlchemy. External network calls need explicit timeouts; retries should target transient failures and use backoff/jitter. Side-effecting operations need retry safety and often idempotency keys. Rate limiting protects availability and controls abuse/cost. Authentication identifies the caller while authorization determines what that caller may do.

## Completion

HTTP & REST was covered conceptually and verified through a complete resource-oriented FastAPI implementation. The request/response flow and Pydantic `response_model` behavior were also explicitly clarified during review.

## Next

Session 10 — FastAPI Fundamentals: formal application structure, routing, OpenAPI/Swagger, lifespan, graceful shutdown, and health/readiness endpoints.
