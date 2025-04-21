python -m venv venv</br>
venv\Scripts\activate</br>
python -m pip install --upgrade pipx</br>
python -m pipx ensurepath</br>
pipx install uv</br>
</br>
uv pip install -r requirements.txt</br>
uv run mcp dev example2.py</br>