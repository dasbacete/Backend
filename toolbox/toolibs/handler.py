import os

from subprocess import Popen, PIPE
from pathLib import Path

class handler:
    
    def __init__ ( self, tool ):
        if 'PRJPATH' in os.environ:
            self.wdir = Path(os.environ['PRJPATH']) / 'wdir' / tool
        self.tool = tool
        return

    def launch ( self, flags )
        pwd = os.getcwd()
        os.chdir(wdir)
        cmd = f"{self.name} {flags}"
        print (f" CMD ::: {cmd}")
        try:
            process = Popen(cmd,stdout=PIPE,stderr=PIPE,shell=True)
            stdout, stderr = process.communicate()
            if process.returncode == 0:
                print(f"Output: { stdout.decode(encoding='latin-1') }")
            else:
                 print(f"Output: { stdout.decode(encoding='latin-1') }")
                 print(f"Error: { stderr.decode(encoding='latin-1') }")
            return_code = process.returncode
        except Exception as e:
            print(f"An error occurred: {e}")
            return_code = None
        os.chdir(pwd)
        return return_code
