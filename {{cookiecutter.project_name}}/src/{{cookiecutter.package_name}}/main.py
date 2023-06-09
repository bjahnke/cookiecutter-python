import socket
import typing

def hof_main(host, port, main_function: typing.Callable):
    """
    This function is a higher order function that wraps the main function of the app.
    It is used to make the app compatible with Google Cloud Run.
    Example usage: hof_main('0.0.0.0', 8080, main)
    :param host: ip address of host for socket to listen on
    :param port: port for socket to listen on
    :param main_function: main driver function of the app
    :return:
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        main_function(s)