
from . import handler

class ghdl_handler ( handler.handler ):

    def __init__ ( self, config=None ):
        
        handler.handler.__init__(self, tool='ghdl')
        
        self.analyze_flags   = None
        self.elaborate_flags = None
        self.simulate_flags  = None
        if config is not None:
            self.analyze_flags   =  
            self.elaborate_flags =  
            self.simulate_flags  =  
        else:
            self.analyze_flags   =  
            self.elaborate_flags =  
            self.simulate_flags  =  

