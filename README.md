## cmd to remmeber:

1. miration : 
- pip install alembic 
- alembic init -t async miration
- (after done changes in env file and script.py.mako) alembic revision --autogenerate -m 'init'
- alembic upgrade head (apply migration to DB)
- Reapeat last 2 cmd if any change happens in db

2. passlib for hashing the password