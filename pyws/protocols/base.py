from pyws.errors import ET_CLIENT

__all__ = ('Protocol', )


class Protocol(object):

    def __init__(self, auth_data_getter=None):
        self.auth_data_getter = auth_data_getter

    def get_auth_data(self, request):
        return self.auth_data_getter(request)

    def get_function(self, request):
        raise NotImplementedError('Protocol.get_function')

    def get_response(self, result, name, return_type):
        raise NotImplementedError('Protocol.get_response')

    def get_error(self, error):
        error_type = type(error)
        if error.error_type == ET_CLIENT:
            error_type_name = 'Client'
        else:
            error_type_name = 'Server'
        #noinspection PyUnresolvedReferences
        return {
            'type': error_type_name,
            'name': error_type.__name__,
            'prefix': error_type.__module__,
            'message': unicode(error),
            'params': error.args,
        }
