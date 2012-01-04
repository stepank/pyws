RUN_CMD=python __init__.py
PID_FILE=_wsgi.pid

run:
	$(RUN_CMD)

runbg:
	$(RUN_CMD) > /dev/null 2>&1 & echo $$! > $(PID_FILE)

stop:
	if [ -e $(PID_FILE) ]; then \
		kill `cat $(PID_FILE)`; \
		rm $(PID_FILE); \
	fi

