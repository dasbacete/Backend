from . import handler
from . import pfile

class ghdl_handler ( handler.handler, pfile.pfile ):

    def __init__ ( self, pff ): 
        handler.handler.__init__(self, tool='ghdl')
        pfile.pfile.__init__( self, pfile_path=pff )
        self.analyze_flags = "--std=08 --ieee=standard -a"
        self.elaborate_flags = "-e"
        self.simulate_flags = "-r"
        
    def analyze ( self ):
        srcs = self.list_sources()
        filelist = ' '.join(srcs)
        flags = f"{self.analyze_flags} {filelist}"
        return self.launch_cmd(flags)

    def elaborate ( self, top=None ):
        top_unit = self.top
        if top is not None:
            top_unit = top
        flags = f"{self.elaborate_flags} {top_unit}"
        return self.launch_cmd(flags)

    def simulate ( self, top=None, simulate_flags=None):
        top_unit = self.top
        if top is not None:
            top_unit = top
        sim_flags = ""
        if top_unit in self.pdata:
            if 'flags' in self.pdata[top_unit]:
                sim_flags += f"{self.pdata[top_unit]['flags']}"
        if simulate_flags is not None:
            sim_flags = f"{simulate_flags}"
        flags = f"{self.simulate_flags} {top_unit} {sim_flags}"
        return self.launch_cmd(flags)
