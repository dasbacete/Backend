import yaml
import os

from pathlib import Path

class pfile:
    
    def __init__ ( self, pfile_path=None ):    
        self.project_name = None
        self.pfile_path   = None
        self.top          = None
        self.pkg          = []
        self.rtl          = []
        self.sim          = dict()
        self.stageXflags  = dict()  
        if pfile_path:
            ## Location
            self.project_name = Path(pfile_path).name
            self.pfile_path   = os.path.abspath(Path(pfile_path).parent)
            # load pfile
            pdata = None
            if pfile_path:
                with open( pfile_path, 'r' ) as pff:
                    pdata = yaml.safe_load( pff )
            
            # load stage flags 
            if 'flags' in pdata:
                self.stageXflags  = pdata['flags'] 
            
            # load deps
            if 'deps' in pdata:
                for dep in pdata['deps']:
                    deps_pff = pfile( self.pfile_path / Path("..") / Path(dep) )
                    if deps_pff.pkg:
                        self.pkg = self.pkg + deps_pff.pkg
                    if deps_pff.rtl:
                        self.rtl = self.rtl + deps_pff.rtl
                    if deps_pff.sim:
                        self.sim = self.sim | deps_pff.sim
            # load top
            if 'top' in pdata:
                self.top = pdata['top']
            # load current 
            if 'pkg' in pdata['srcs']:
                self.pkg += [ f"{self.pfile_path}/../src/pkg/{file}" for file in pdata['srcs']['pkg'] ]
            if 'rtl' in pdata['srcs']:
                self.rtl += [ f"{self.pfile_path}/../src/rtl/{file}" for file in pdata['srcs']['rtl'] ]
            if 'sim' in pdata:
                for k in pdata['sim']:
                    pdata['sim'][k]['tb'] = f"{self.pfile_path}/../src/sim/tb/{pdata['sim'][k]['tb']}"
                self.sim = self.sim | pdata['sim']
    
    def list_sources( self ):
        sim_srcs = []
        for test in self.sim:
            sim_srcs.append(self.sim[test]['tb'])
        return self.pkg + self.rtl + sim_srcs

    def get_sim_flags( self, tb ):
        return self.sim[tb]['sim_flags']

    def get_top( self ):
        return self.top
