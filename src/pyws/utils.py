from functools import wraps


def cache_method_result(attr):
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            if not hasattr(self, attr_name):
                setattr(self, attr_name, func(self, *args, **kwargs))
            return getattr(self, attr_name)
        return wrapper
    if callable(attr):
        attr_name = '_cached_' + attr.__name__
        return decorator(attr)
    attr_name = attr
    return decorator


def cached_property(func):
    return property(cache_method_result(func))
