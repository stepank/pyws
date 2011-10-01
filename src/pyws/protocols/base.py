from pyws.errors import ET_CLIENT

__all__ = ('Protocol', )


class Protocol(object):

    def __init__(
            self, context_data_getter=None, common_context_data_getter=None):
        self.context_data_getter = context_data_getter or (lambda a: None)
        self.common_context_data_getter = \
            common_context_data_getter or (lambda a: None)

    def get_context_data(self, request):
        return self.context_data_getter(request)

    def get_common_context_data(self, request):
        return self.common_context_data_getter(request)

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
