@SETLOCAL
@ECHO OFF

SET "SCRIPT_DIR=%~dp0"
SET "PATH=%SCRIPT_DIR%cmd;%PATH%"

IF NOT [%1] == [] GOTO :RUN_COMMAND
GOTO :EOF

:RUN_COMMAND
SET RUN_INTERACTIVE=1
echo %CMDCMDLINE% | find /i "%~0" >nul
IF NOT errorlevel 1 set RUN_INTERACTIVE=0

SET PYTHONPATH=%SCRIPT_DIR%
SET PIPENV_PIPFILE=%SCRIPT_DIR%Pipfile
SET PIPENV_VENV_IN_PROJECT=1
SET PIPENV_SKIP_LOCK=1
SET PIPENV_TIMEOUT=300

CALL %*
SET RESULT=%ERRORLEVEL%
IF %RESULT% NEQ 0 (
  IF _%RUN_INTERACTIVE%_==_0_ ( pause )
)
EXIT /B %RESULT%

:EOF
@ENDLOCAL