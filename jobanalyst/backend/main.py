import os
from fastapi import FastAPI
from dotenv import load_dotenv
from supabase import create_client, Client
from fastapi.middleware.cors import CORSMiddleware

# 1. Load environment variables
load_dotenv()
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

# 2. Initialize Supabase Client
supabase: Client = create_client(url, key)

# 3. Initialize FastAPI
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Backend is running, intellectual sir! 🧐"}


@app.get("/items")
def get_items():
    # Example: Fetches all rows from a table named 'my_table'
    response = supabase.table("my_table").select("*").execute()
    return response.data


@app.get("/test-data")
def get_test_item():
    # Fetch only the 'tester' column from the first row
    response = supabase.table("test").select("tester").limit(1).execute()
    if response.data:
        return response.data[0]["tester"]
    return {"tester": "No data found"}
