"""
This type stub file was generated by pyright.
"""

"""Provides Drone-based login credentials"""
def create_drone_client(host, secret, method, name, port=..., **kwargs): # -> Client:
    """Create a Client instance using drone credentials.

    :param str host: The hostname of the flywheel instance
    :param str secret: The drone secret
    :param str method: The method (device type)
    :param str name: The name of the device
    :param int port: The optional port (if not 443)
    :param kwargs: Additional arguments to pass to the created Client instance
    :return: The authorized Client instance
    :rtype: flywheel.Client
    """
    ...

