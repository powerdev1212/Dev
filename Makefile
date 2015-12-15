APP=hygeiais
DBNAME=hygeiais_sitedb
CHARACTER_SET=utf8
COLLATION=utf8_general_ci
DBUSER=root
DBPASS=<password>

MANAGE=./manage.py

PROJECTDIR=hygeiais
PYTHON=python2
SETTINGS=$(PROJECTDIR).settings

SUPERVISORD_CONFIG=/home/diadko_roman/supervisord/supervisord.conf

initGunicorn:
	if [ -f "gunicorn_start.sh" ]; then \
		chmod +x gunicorn_start.sh; \
	fi

mkVenvDir:
	if ! [ -d ".virtualenvs" ]; then mkdir .virtualenvs; fi


mkLogDir:
	if ! [ -d "logs" ]; then mkdir logs; fi


mkSocketDir:
	if ! [ -d "run" ]; then mkdir run; fi


mkdirs: mkVenvDir mkLogDir mkSocketDir


runserver:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(SETTINGS) $(PYTHON) $(MANAGE) runserver localhost:8010
	
makemigrations:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(SETTINGS) $(PYTHON) $(MANAGE) makemigrations
	
migrate: makemigrations
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(SETTINGS) $(PYTHON) $(MANAGE) migrate
	
syncdb:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(SETTINGS) $(PYTHON) $(MANAGE) syncdb
	
collectstatic:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(SETTINGS) $(PYTHON) $(MANAGE) collectstatic


setup: mkdirs initGunicorn
	(\
		virtualenv .virtualenvs/django27;\
		chmod +x .virtualenvs/django27/bin/activate;\
		source .virtualenvs/django27/bin/activate;\
		pip install -r ./requirements.txt;\
	)
	
platformTest:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(SETTINGS) $(PYTHON) $(MANAGE) test tests.PlatformTest
	
pathsTest:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(SETTINGS) $(PYTHON) $(MANAGE) test tests.PathsTest
	
xmlTest:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(SETTINGS) $(PYTHON) $(MANAGE) test tests.XmlFilesTest
	
loadersTest:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(SETTINGS) $(PYTHON) $(MANAGE) test loaders.tests.LoadersTest

tests: platformTest pathsTest xmlTest


testDeseases:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(SETTINGS) $(PYTHON) $(MANAGE) test deseases.tests

supervisor:
	if ! [ "$(pidof supervisord)" ]; then \
		supervisord -c $(SUPERVISORD_CONFIG); \
		supervisorctl -c $(SUPERVISORD_CONFIG); \
	fi

apprestart: supervisor
	supervisorctl restart $(APP)

appstart: supervisor
	supervisorctl start $(APP)

appstop:
	#supervisord -c $(SUPERVISORD_CONFIG)
	#supervisorctl -c $(SUPERVISORD_CONFIG)
	supervisorctl stop $(APP)
	if [ "$(pidof gunicorn)" ]; then killall gunicorn; fi

gshell:
	gcloud compute --project "pivotal-crawler-112414" ssh --zone "us-central1-b" "dr"


deploy:
	gcloud compute --project "pivotal-crawler-112414" copy-files ./hygeiais ./deseases diadko_roman@dr:/home/diadko_roman/hygeiais  --zone us-central1-b


