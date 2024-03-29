@SETLOCAL

@REM --- Detect run interactive
@SET FIND_EXE=C:\Windows\System32\find.exe
@ECHO %CMDCMDLINE% | %FIND_EXE% /i "%~0" >NUL
@SET RUN_INTERACTIVE=%ERRORLEVEL%

@REM --- prepare execution environment
@SET "SCRIPT_DIR=%~dp0"
@SET "PATH=%SCRIPT_DIR%cmd;%PATH%"
@SET PYTHONPATH=%SCRIPT_DIR%
@SET PIPENV_PIPFILE=%SCRIPT_DIR%Pipfile
@SET PIPENV_VENV_IN_PROJECT=1
@SET PIPENV_SKIP_LOCK=1
@SET PIPENV_TIMEOUT=300

@REM --- exit on no command
@IF [%1] == [] GOTO :EOF

:RUN_COMMAND
@CALL %*
@SET RESULT=%ERRORLEVEL%
@IF %RESULT% NEQ 0 (
	@IF [%RUN_INTERACTIVE%] == [0] PAUSE
)
@EXIT /B %RESULT%

:EOF
@ENDLOCAL