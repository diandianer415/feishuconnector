rm -rf dist/*
python3 setup.py sdist build && twine upload dist/*