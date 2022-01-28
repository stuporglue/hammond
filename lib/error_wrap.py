from openrgb import utils
import functools
import park

# https://stackoverflow.com/questions/24024966/try-except-every-method-in-class
def ORGBServerReconnect(func):
    num_retries = 3
    @functools.wraps(func)
    def wrapper(*a, **kw):

        # Self may be useful some day down the road, but isn't currently used
        #if len(a) > 0:
        #    self,*args = a

        for i in range(num_retries):
            try:
                return func(*a, **kw)
            except utils.CONNECTION_ERRORS + (utils.OpenRGBDisconnected,) as e:
                # If we get a connection error, get the park instance and ask it to reconnect us
                mypark = park.Park.get_instance()
                mypark.connect_all()
                return False
    return wrapper    

import inspect
def decorate_all_methods(decorator):
    def apply_decorator(cls):
        for k, f in cls.__dict__.items():
            if inspect.isfunction(f):
                setattr(cls, k, decorator(f))
        return cls
    return apply_decorator
