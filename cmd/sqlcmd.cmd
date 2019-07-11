@SETLOCAL
@CALL py -m pipenv run python.exe -m scripts.sqlcmd %*
@ENDLOCAL
