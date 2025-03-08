from subprocess import Popen, PIPE

class handler:
    
    def __init__ ( self, tool ):
        self.tool = tool
        return

    def launch ( self, flags )
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
        return return_code
