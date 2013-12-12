from rbtools.api.errors import APIError
from rbtools.commands import Command, CommandError, Option


class MyCommand(Command):
    """Description for my command."""
    # The name of your command. This should match the entrypoint in setup.py,
    # and is the command that follows 'rbt'.
    name = 'my-command'

    # Your name.
    author = 'My Name'

    # The description of your command. This will be shown in the help output.
    description = 'Description for my command'

    # The descriptive list of arguments the command takes, for help output.
    args = '<review-request-id>'

    # A list of options. This is a good default. Currently, RBTools requires
    # that you define these for most operations.
    #
    # You can add custom options and access them through self.options.
    option_list = [
        Option("--server",
               dest="server",
               metavar="SERVER",
               config_key="REVIEWBOARD_URL",
               default=None,
               help="Specify a different Review Board server to use"),
        Option("--username",
               dest="username",
               metavar="USERNAME",
               config_key="USERNAME",
               default=None,
               help="The user name to be supplied to the Review Board server"),
        Option("--password",
               dest="password",
               metavar="PASSWORD",
               config_key="PASSWORD",
               default=None,
               help="The password to be supplied to the Review Board server"),
        Option('--repository-type',
               dest='repository_type',
               config_key="REPOSITORY_TYPE",
               default=None,
               help='The type of repository in the current directory. '
                    'In most cases this should be detected '
                    'automatically but some directory structures '
                    'containing multiple repositories require this '
                    'option to select the proper type.'),
    ]

    def main(self, review_request_id):
        """The main function for your command.

        This takes any required positional arguments as parameters.
        """
        # This sets up the command. It will check for the current repository,
        # create an RBClient instance, fetch the root resource, and fetch
        # the capabilities from the server.
        repository_info, tool = self.initialize_scm_tool(
            client_name=self.options.repository_type)
        server_url = self.get_server_url(repository_info, tool)
        api_client, api_root = self.get_api(server_url)
        self.setup_tool(tool, api_root=api_root)

        # All your own logic goes below here.
        #
        # Here's a sample that gets the review request with the ID passed
        # on the command line, and prints its summary and description.
        try:
            review_request = api_root.get_review_request(
                review_request_id=review_request_id)
        except APIError, e:
            raise CommandError('Error getting review request %s: %s'
                               % (review_request_id, e))

        print '= Summary ='
        print review_request.summary
        print
        print '= Description ='
        print review_request.description
