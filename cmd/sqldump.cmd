@SETLOCAL
@py -m pipenv run python -m scripts.sqldump %*
@ENDLOCAL
