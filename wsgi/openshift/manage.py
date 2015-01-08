#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    repo_dir = os.environ.get('OPENSHIFT_REPO_DIR', os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
    sys.path.append(os.path.join(repo_dir, 'wsgi'))

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
