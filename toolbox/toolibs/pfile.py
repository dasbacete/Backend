import yaml
import os

from pathlib import Path

class pfile:
    
    def __init__ ( self, pfile_path=None ):    
        self.project_name = Path(pfile_path).name
        self.pfile_path = os.path.abspath(Path(pfile_path).parent)
        self.pdata = None
        if pfile_path:
            with open( pfile_path, 'r' ) as pff:
                self.pdata = yaml.safe_load( pff )

    def list_sources( self ):
        srcs = [] 
        if self.pdata is not None and 'srcs' in self.pdata:
            ## Common dependencies
            for k in self.pdata['srcs']:
                if k != 'pkg' and k != 'rtl':
                    if 'pkg' in self.pdata['srcs'][k]:
                        srcs += [ f"{self.pfile_path}/{k}/pkg/{file}" for file in self.pdata['srcs'][k]['pkg'] ]
                    if 'rtl' in self.pdata['srcs'][k]:
                        srcs += [ f"{self.pfile_path}/{k}/rtl/{file}" for file in self.pdata['srcs'][k]['rtl'] ]
                    if 'sim' in self.pdata['srcs'][k]:
                        srcs += [ f"{self.pfile_path}/{k}/sim/{file}" for file in self.pdata['srcs'][k]['sim'] ]
            ## Main repo dependencies
            if 'pkg' in self.pdata['srcs']:
                srcs += [ f"{self.pfile_path}/pkg/{file}" for file in self.pdata['srcs']['pkg'] ]
            if 'rtl' in self.pdata['srcs']:
                srcs += [ f"{self.pfile_path}/rtl/{file}" for file in self.pdata['srcs']['rtl'] ]
            if 'sim' in self.pdata:
                srcs += [ f"{self.pfile_path}/sim/{test['rtl']}" for test in self.pdata['sim'] ]

        return srcs

    def get_top():
        if 'top' in self.pdata:
            return self.pdata['top']
        else:
            return None
