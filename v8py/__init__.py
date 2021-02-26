try:
    from gevent import monkey
    monkey.patch_all()
    
    from _v8py import *
    from .debug import Debugger, DebuggerError
    
    import geventwebsocket
    import greenstack
except ImportError:
    pass
else:
    from .devtools import start_devtools
