import os

from subprocess import Popen, PIPE
from pathlib import Path

class handler:
    
    def __init__ ( self, tool ):
        if 'PRJ_PATH' in os.environ:
            self.wdir = Path(os.environ['PRJ_PATH']) / 'wdir' / tool
        else:
            print("Error: project file not sourced.")
        if not os.path.exists(self.wdir):
            os.makedirs(self.wdir)
        self.tool = tool
        return

    def launch ( self, flags ):
        pwd = os.getcwd()
        os.chdir(self.wdir)
        cmd = f"{self.tool} {flags}"
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
