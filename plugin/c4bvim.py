import os
import sys

try:
    import requests
except ImportError:
    print('The requests package is not installed. Please install the requests package using pip.')
    sys.exit()
import json

c4b_INFO = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'info')
c4b_WHITEBOARD = os.path.join(os.getcwd(), 'whiteboard')
c4b_SUBMIT_POST_PATH = 'submit_post'
c4b_MY_POINTS_PATH = 'my_points'
c4b_RECEIVE_BROADCAST_PATH = "receive_broadcast"
TIMEOUT = 10

def c4b_receive_broadcast():
    """
    Request the content of the whiteboard from the instructor.
    """
    info = c4b_get_info()

    if info is not None:
        url = "{url}/{path}".format(url=info['Server'],
                path=c4b_RECEIVE_BROADCAST_PATH)
        request = requests.get(url)

        try:
            whiteboard = request.json()
        except ValueError:
            print "No whiteboard content is available."

        if whiteboard:
            content, ext = whiteboard['whiteboard'], whiteboard['ext']
            wb = c4b_WHITEBOARD if ext == '' else "{}.{}".format(c4b_WHITEBOARD, ext)
            with open(wb, 'w') as f:
                f.write(content)
        return wb
    else:
        print('Code4Brownies user and server info has not been configured. Please see :help c4bvim for more information.')
        return None

def c4b_share(content):
    """
    Share the buffer with the a Code4Brownies server instance.
    """
    info = c4b_get_info()

    if info is not None:
        url = '{url}/{path}'.format(url=info['Server'],
                path=c4b_SUBMIT_POST_PATH)
        payload = {'uid': info['Name'],
                   'body': content }
        try:
            response = requests.post(url, data=payload, timeout=TIMEOUT)
            print(response.text)
        except requests.exceptions.ConnectionError:
            print('Unable to reach server. Please check server settings.')
    else:
        print('Code4Brownies user and server info has not been configured. Please see :help c4bvim for more information.')


def c4b_show_points():
    """
    Display the points for the user configured in INFO.
    """
    info = c4b_get_info()

    if info is not None:
        url = '{url}/{path}'.format(url=info['Server'],
                path=c4b_SUBMIT_POST_PATH)
        payload = {'uid': info['Name']}
        try:
            response = requests.post(url, data=payload, timeout=TIMEOUT)
            print(response.text)
        except requests.exceptions.ConnectionError:
            print('Unable to reach server. Please check server settings.')
    else:
        print('Code4Brownies user and server info has not been configured. Please see :help c4bvim for more information.')


def c4b_set_info(name, server):
    """
    Saves the user's name and the server to Code4Brownies server to connect to.
    The info is saved as JSON in the same folder as this script when installed.
    """
    info = {'Name': name, 'Server': server}

    with open(c4b_INFO, 'w') as f:
        f.write(json.dumps(info, indent=4))
        print('Set Name to {0}, Server to {1}'.format(name, server))


def c4b_get_info():
    """
    Returns the user and server name saved in the INFO file.
    """
    try:
        with open(c4b_INFO, 'r') as f:
            info = json.loads(f.read())
    except IOError:
        print('INFO file is missing. Please see :help c4bvim for info on configuring connection information.')
        return None

    if 'Server' not in info or 'Name' not in info:
        print('Info is not complete. You must provide a Name and a Server.')
        return None

    return info

