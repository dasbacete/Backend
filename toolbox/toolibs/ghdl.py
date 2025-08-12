import os

from . import handler
from . import pfile

class ghdl_handler ( handler.handler, pfile.pfile ):

    def __init__ ( self, pff ): 
        handler.handler.__init__(self, tool='ghdl')
        pfile.pfile.__init__( self, pfile_path=pff )
        self.analyze_flags   = "--std=08 --ieee=standard"
        self.elaborate_flags = "--std=08"
        self.simulate_flags  = ""
        
    def analyze ( self, pfile_path=None, analyze_flags=None ):
        srcs = None
        local_pfile = None
        if pfile_path:
            local_pfile = pfile.pfile( pfile_path=pfile_path )
            srcs = local_pfile.list_sources()
        else:
            srcs = self.list_sources()
        filelist = ' '.join(srcs)
        flags = f"-a {self.analyze_flags} -frelaxed {filelist}"
        return self.launch(flags)

    def elaborate ( self, top=None, elaborate_flags=None ):
        top_unit = self.get_top()
        if top is not None:
            top_unit = top
        flags = f"-e {self.elaborate_flags} {top_unit}"
        return self.launch(flags)

    def simulate ( self, top=None, simulate_flags=None):
        top_unit = self.get_top()
        if top is not None:
            top_unit = top
        sim_flags = ""
        if self.sim:
            if top_unit in self.sim:
                if 'sim_flags' in self.sim[top_unit]:
                    sim_flags += f"{self.sim[top_unit]['sim_flags']}"
                if 'cosim' in self.sim[top_unit]:
                    sim_flags += f" --vpi=$(cocotb-config --lib-name-path vpi ghdl)"
                    os.environ['PYTHONPATH']    = f":{self.pfile_path}/../src/sim/cocotb"
                    os.environ['TOPLEVEL']      = top_unit
                    os.environ['TOPLEVEL_LANG'] = 'vhdl' 
                    os.environ['MODULE']        = self.sim[top_unit]['cosim']
                    os.environ['TESTCASE']      = ''
        if simulate_flags is not None:
            sim_flags = f"{simulate_flags}"
        flags = f"-r {self.simulate_flags} {top_unit} {sim_flags}"
        return self.launch(flags)
