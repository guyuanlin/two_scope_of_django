from default import *

"""
Test settings and globals which
allow us to run our test suite
locally.
"""
########## TEST SETTINGS
TEST_DISCOVER_TOP_LEVEL = BASE_DIR
TEST_DISCOVER_ROOT = BASE_DIR
TEST_DISCOVER_PATTERN = "test_*"

########## IN-MEMORY TEST DATABASE
DATABASES = {
	"default": {
		"ENGINE": "django.db.backends.sqlite3",
		"NAME": ":memory:",
		"USER": "",
		"PASSWORD": "",
		"HOST": "",
		"PORT": "",
	},
}
