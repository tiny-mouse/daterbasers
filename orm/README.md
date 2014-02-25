# Setup (just run the following commands from this directory)
# They add virtualenv so you can keep things siloed http://www.virtualenv.org/en/latest/
# Then they install all the project requirements and set up the db.

```
pip install virtualenv

mkdir env

virtualenv env

source env/bin/activate

pip install -r requirements.txt
CLAY_CONFIG=config/local.yaml alembic upgrade head
```

# Running
```
CLAY_CONFIG=config/local.yaml clay-devserver
```
