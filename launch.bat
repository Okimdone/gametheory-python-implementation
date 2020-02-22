@echo OFF

IF NOT EXIST ENV (
	pip install virtualenv && virtualenv ENV && .\ENV\Scripts\activate.bat && pip install -r requirements.txt && python .\nash_GUI\app.py
) ELSE (
	.\ENV\Scripts\activate.bat && python .\nash_GUI\app.py
)