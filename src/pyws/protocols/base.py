from pyws.errors import ET_CLIENT

__all__ = ('Protocol', )


class Protocol(object):
    """
    Abstract protocol class. Implements basic constructor, context and error
    handling.
    """

    def __init__(
            self, context_data_getter=None, common_context_data_getter=None):
        """
        Both arguments are callable objects that accept exactly one argument
        (namely a request) and return context data. ``context_data_getter``
        is used to get context data for registered functions.
        ``common_context_data_getter`` is used for functions returned directly
        by a protocol. If you need to override this method don't forget to call
        it from successors' constructor.
        """
        self.context_data_getter = context_data_getter or (lambda a: None)
        self.common_context_data_getter = \
            common_context_data_getter or (lambda a: None)

    def get_function(self, request):
        """
        Extracts a function name or a function from the request.
        """
        raise NotImplementedError('Protocol.get_function')

    def get_arguments(self, request, arguments):
        """
        Extracts argument values from the request according to the arguments
        specification.
        """
        raise NotImplementedError('Protocol.get_arguments')

    def get_response(self, result, name, return_type):
        """
        Forms a response from the result returned by a function according to
        the return type specification. ``name`` is the of name the function.
        """
        raise NotImplementedError('Protocol.get_response')

    def get_error_response(self, error):
        """
        Forms an error response from the error.
        """
        raise NotImplementedError('Protocol.get_error_response')

    def get_context_data(self, request):
        """
        Gets context data from the request. These context data is used by a
        server for registered functions.
        """
        return self.context_data_getter(request)

    def get_common_context_data(self, request):
        """
        Gets context data from the request. These context data is used by a
        server for functions returned directly by a protocol.
        """
        return self.common_context_data_getter(request)

    def get_error(self, error):
        """
        A helper function, gets standard information from the error.
        """
        error_type = type(error)
        if error.error_type == ET_CLIENT:
            error_type_name = 'Client'
        else:
            error_type_name = 'Server'
        return {
            'type': error_type_name,
            'name': error_type.__name__,
            'prefix': getattr(error_type, '__module__', ''),
            'message': unicode(error),
            'params': error.args,
        }
