python -m venv venv
venv\Scripts\activate
python -m pip install --upgrade pipx
python -m pipx ensurepath
pipx install uv

uv pip install -r requirements.txt
uv run mcp dev example2.py