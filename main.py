from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import products, orders, auth, upload
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="SOUTOURA_KS API", version="1.0.0")

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(products.router, prefix="/api/products", tags=["products"])
app.include_router(orders.router, prefix="/api/orders", tags=["orders"])
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(upload.router, prefix="/api/upload", tags=["upload"])

@app.get("/")
def read_root():
    return {"message": "Welcome to SOUTOURA_KS API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
