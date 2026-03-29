import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

# Initialize
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)


def fetch_tester_column():
    # 1. Fetch only the 'tester' column from the 'test' table
    response = supabase.table("test").select("tester").execute()

    # 2. Extract the data
    data = response.data

    if data:
        # 3. Print the 'tester' value from the first row
        print(f"Success! Column value: {data[0]['tester']}")
    else:
        print("Table is empty or not found.")


if __name__ == "__main__":
    fetch_tester_column()
