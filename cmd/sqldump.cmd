@SETLOCAL
@py -m pipenv run python.exe -m scripts.sqldump %*
@ENDLOCAL
