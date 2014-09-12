import json
import requests
import urllib

from helga.plugins import command

_help_text = 'Look up a definition on urbandictionary.com. \
Usage: helga urban[dictionary] TERM'

_api_host = 'http://urbanscraper.herokuapp.com/define/'


@command('urbandictionary', aliases=['urban'], help=_help_text)
def urbandictionary(client, channel, nick, message, cmd, args):
    """
    Fetch a definition from urban dictionary
    """
    if len(args) == 0:
        return u'You need to give me a term to look up.'
    else:
        # the api spec says that it wants terms RFC3986 encoded but it lies
        term = urllib.quote(' '.join(args))
        response = requests.get(_api_host + term)
        error_response = 'No definition found or a problem talking to the api.'
        if response.status_code != 200:
            return error_response
        return json.loads(response.content).get('definition', error_reponse)
