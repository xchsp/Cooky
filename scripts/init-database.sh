echo "Starting database initiation scripts. This might take a while..."

echo "1/6  Creating database..."
docker exec -i mysql1 mysql < bd_init/0_database.sql

echo "2/6  Creating tables..."
docker exec -i mysql1 mysql < bd_init/1_tables.sql

echo "3/6  Adding constraints..."
docker exec -i mysql1 mysql < bd_init/2_constraints.sql

echo "4/6  Adding triggers..."
docker exec -i mysql1 mysql < bd_init/3_triggers.sql

echo "5/6  Filling static tables..."
docker exec -i mysql1 mysql < bd_init/4_populate_static.sql

echo "6/6  Filling other tables...(longer)"
python3 fill_db.py

echo "Done!"