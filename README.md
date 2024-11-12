## cmd to remmeber:

1. miration : - pip install alembic 
              - alembic init -t async miration
              - (after changes in env, script) alembic revision --autogenerate -m 'init'
              - alembic upgrade head (apply migration to DB)