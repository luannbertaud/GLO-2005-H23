echo "--------------------------------------------------------------------------"
echo "    Using a virtual environment in VERY recommended. (See python venv)    "
echo "--------------------------------------------------------------------------"
sleep 3
pip install -r requirements.txt

python -m build
pip install dist/instapaper-0.0.1-py3-none-any.whl

uvicorn --host 127.0.0.1 --port 8080 app:app