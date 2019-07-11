@SETLOCAL
@CALL py -m pipenv run python -m scripts.sqlcmd %*
@ENDLOCAL
