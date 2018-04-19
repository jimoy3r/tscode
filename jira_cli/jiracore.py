""" Common jira CLI code:
- init jira
- search jira project/issues
- create jira project/issue
- edit jira project/issue
- tranistion jira project/issue state
- list jira project/issues
"""
from __future__ import print_function

from jira.client import JIRA
import logging
import requests.exceptions
from operator import itemgetter


class JiraCore(object):
    """ Class to interface with jira """

    def __init__(self, log, jira_server):
        self.log = log
        self.server = jira_server

    def connect_jira(self):
        """
        Connect to jira
        :return:
        """
        assert self.server
        assert self.log
        try:
            self.log.info('Connecting to JIRA: {}'.format(self.server))
            jira_options = {'server': self.server}
            jira = JIRA(options=jira_options, timeout=10)
            return jira
        except requests.exceptions.RequestException as e:
            self.log.error('Failed to connect to Jira server: {}: {}'.format(self.server, e.message))
            raise

    def list_projects(self, jira_c):
        """
        List projects
        :param jira_c: jira connection
        :return projects: list of projects found
        """
        assert jira_c
        assert self.log
        projects = jira_c.projects()
        self.log.info("Results for list_projects:")
        for i, proj in enumerate(projects):
            self.log.info("{}: {}".format(i, str(proj)))
        return projects

    def list_issues(self, jira_con, search_jql):
        """
        Search for and list issues
        :param jira_con: jira connection
        :param search_jql: Jira Query Language string
        :return: issues: list of issues found
        """
        assert jira_con, "Requires jira_con"
        assert search_jql, "Requires search_jql"
        assert self.log
        dict_keys = ('name', 'percent', 'watchCount', 'votes', 'progress', 'value')

        issues = jira_con.search_issues(search_jql + ' order by issue')
        self.log.info('\nResults for {}:'.format(search_jql))
        for issue in issues:
            s = str(issue)
            for key, value in issue.raw['fields'].iteritems():
                if value:
                    found = False
                    if type(value) is not dict:
                        found = True
                        s += ', ' + key + '=' + unicode(value)
                    else:
                        for k in dict_keys:
                            if k in value:
                                found = True
                                s += ', ' + key + '=' + str(value[k])
                    if not found:
                        s += ', ' + key + '=(' + unicode(type(value)) + ') ' + str(value)
            self.log.info(s)
        return issues


def main():
    """
    Test jira connection
    :return:
    """
    # create logger
    try:
        log = logging.getLogger(__name__)
        log.level = logging.DEBUG
        server = 'http://localhost:8080'
        jc = JiraCore(log, server)
        jira_con = jc.connect_jira()
        print('Success testing jira connection: {}'.format(server))
        exit(0)
    except Exception as e:
        print('Error: {}'.format(str(e.message)))
        exit(1)


if __name__ == "__main__":
    main()

