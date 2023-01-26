# -*- coding: utf-8 -*-
import re
import logging
from django.test.runner import DiscoverRunner
from django.conf import settings


class TestRunner(DiscoverRunner):
    """
    Custom test runner to fix test execution
    -> Error when you have the same name for the root folder and the project folder.
       https://stackoverflow.com/a/28476388
    """

    def run_tests(self, *args, **kwargs):

        # Don't show logging messages while testing
        logging.disable(logging.CRITICAL)

        apps_list = []

        if len(args[0]) > 0:
            # If apps are provided, remove the "backend." part:
            # backend.viability -> viability
            for app in args[0]:
                app_new = re.sub(r"^backend\.", "", app)
                apps_list.append(app_new)

            apps_list = (tuple(apps_list),)
        else:
            # All add installed apps
            apps_list = (tuple(settings.INSTALLED_APPS),)

        return super().run_tests(*apps_list, **kwargs)
