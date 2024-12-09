# https://gist.github.com/st4lk/6725777

# Logging settings for django projects, works with django 1.5+
# If DEBUG=True, all logs (including django logs) will be
# written to console and to debug_file.
# If DEBUG=False, logs with level INFO or higher will be
# saved to production_file.

# ################# Logging usage:
# import logging
# logger = logging.getLogger(__name__)
# logger.info("Log this message")

from os import path
from conf import ROOT
try:
    from conf import LOGGING_LEVEL
except ImportError:
    LOGGING_LEVEL = "INFO"


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue'
        }
    },
    'formatters': {
        'main_formatter': {
            'format': '%(levelname)s:%(name)s: %(message)s '
                      '(%(asctime)s; %(filename)s:%(lineno)d)',
            'datefmt': "%Y-%m-%d %H:%M:%S",
        },
    },
    'handlers': {
        'mail_admins': {
            'filters': ['require_debug_false'],
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'filters': ['require_debug_true'],
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'main_formatter',
        },
        'production_file': {
            'filters': ['require_debug_false'],
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': path.join(ROOT, '../logs/main.log'),
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 7,
            'formatter': 'main_formatter',
        },
        'debug_file': {
            'filters': ['require_debug_true'],
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': path.join(ROOT, '../logs/main_debug.log'),
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 7,
            'formatter': 'main_formatter',
        },
        'null': {
            "class": 'django.utils.log.NullHandler',
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins', 'console'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django': {
            'handlers': ['null', ],
        },
        'py.warnings': {
            'handlers': ['null', ],
        },
        '': {
            'handlers': ['console', 'production_file', 'debug_file'],
            'level': LOGGING_LEVEL,  # or 'CRITICAL','ERROR','WARN','WARNING','INFO','DEBUG','NOTSET'

        },
    }
}
