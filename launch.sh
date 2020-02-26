DIR="./ENV"
if [ -d "$DIR" ]; then
        source ENV/bin/activate
        ./nash_GUI/app.py
else
	python3 -m pip install virtualenv
        virtualenv ENV
        source ENV/bin/activate
        pip install -r requirements.txt
        ./nash_GUI/app.py
fi
