# PostgreSQL Migration Guide

## Overview
Your Notes API has been upgraded from SQLite to PostgreSQL.

## Changes Made

### 1. **Database Connection** (`app/db/session.py`)
- **Before**: SQLite with local file storage
  ```python
  DATABASE_URL = "sqlite:///./notes.db"
  engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
  ```
- **After**: PostgreSQL with environment-based configuration
  ```python
  DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
  engine = create_engine(DATABASE_URL)
  ```

### 2. **Dependencies** (`requirements.txt`)
- Added `psycopg2-binary` - PostgreSQL driver for Python
- Updated all dependencies to latest compatible versions

### 3. **Configuration** (`.env.example`)
- Created example environment variables file for PostgreSQL setup

## Setup Instructions

### Step 1: Install PostgreSQL
- Download from [postgresql.org](https://www.postgresql.org/download/)
- Make note of your password for the `postgres` user

### Step 2: Create Database
```bash
psql -U postgres
CREATE DATABASE notes_db;
\q
```

### Step 3: Install Python Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables
Create a `.env` file in your project root (copy from `.env.example`):
```bash
DB_USER=postgres
DB_PASSWORD=your_postgres_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=notes_db
```

### Step 5: Run the Application
```bash
python -m uvicorn app.main:app --reload
```

## Benefits of PostgreSQL

✅ **Production-Ready**: Suitable for enterprise deployments  
✅ **ACID Compliance**: Ensures data integrity  
✅ **Advanced Features**: JSON support, full-text search, custom types  
✅ **Scalability**: Handles large datasets efficiently  
✅ **Concurrent Users**: Better handling of simultaneous connections  

## Troubleshooting

### Connection Error: "could not translate host name"
- Verify PostgreSQL is running
- Check `.env` file has correct `DB_HOST` (usually `localhost` for local)

### Authentication Failed
- Verify `DB_USER` and `DB_PASSWORD` in `.env`
- Ensure user has permission on the database

### Database Does Not Exist
```bash
psql -U postgres
CREATE DATABASE notes_db;
```

### Port Already in Use
If PostgreSQL uses a different port (default is 5432), update `DB_PORT` in `.env`

## Data Migration

If you have existing SQLite data:
1. Export data from SQLite
2. Import to PostgreSQL using a migration script

(Contact for assistance if needed)

## Next Steps

- Set up automated backups for PostgreSQL
- Consider connection pooling for production (PgBouncer)
- Add database monitoring and logging
- Implement proper user authentication
