# Run the migrations and exit if it fails. Migrations are tried twice
# to mitigate multiple containers trying to run the migrations at
# the same time.
python manage.py migrate --noinput || (sleep 5 && python manage.py migrate --noinput) || exit 1
# Compile translation messages and exit if it fails
python manage.py compilemessages -l fr -l de --ignore .venv || exit 1
# Then run the CMD command
exec "$@"
