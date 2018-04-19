#!/usr/bin/env python
""" Jira Command Line Interface Tool.

    This will be expanded to create/update and find jira issues.
    Currently it just lists all projects and issues.
"""
from __future__ import print_function

import logging
import jiracore
import click


@click.command()
@click.option('--server',
              default='http://localhost:8080',
              help='Jira server url')
def run(server):
    """
    Run Main program
    :param server:
    :return:
    """
    try:
        # create logger
        log = start_logging()

        # create a connection object
        jc = jiracore.JiraCore(log, server)
        jira_con = jc.connect_jira()

        # Get list of all jira projects
        projects = jc.list_projects(jira_con)

        # Fpr each project, list the issues in it.
        for p in projects:
            jc.list_issues(jira_con,'project={}'.format(str(p)))

        return 0
    except Exception as e:
        print('jiracli.py failed: {}'.format(str(e)))
        return 1


def start_logging():
    """ Turn on logging to jiracli.log """
    log = logging.getLogger('jiracli')
    log.setLevel(logging.DEBUG)
    # create console handler with a higher log level
    console_h = logging.StreamHandler()
    console_h.setLevel(logging.DEBUG)
    # create file handler which logs even debug messages
    fh = logging.FileHandler('jiracli.log')
    fh.setLevel(logging.DEBUG)
    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    # console_h.setFormatter(formatter)
    # add the handlers to the logger
    log.addHandler(fh)
    log.addHandler(console_h)
    return log


if __name__ == '__main__':
    rc = run()
    exit(rc)
