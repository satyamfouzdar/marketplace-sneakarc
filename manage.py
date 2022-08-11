#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from django.core.management import execute_from_command_line

def main():
    """Run administrative tasks."""

    mode = os.getenv('DJANGO_MODE', 'devel')

    if mode == 'devel':
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.devel")
    elif mode == 'prod':
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.prod")

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
