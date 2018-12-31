#!/usr/bin/env python
import os
import sys
from setup_apps import setup_all

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'protosite.settings')



    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django."
        ) from exc

    setup_all()
    execute_from_command_line(sys.argv)
