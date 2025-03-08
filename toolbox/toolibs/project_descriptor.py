import yaml

class project_descriptor:
    
    def __init__ ( self, file ):
        self.prj_data = None
        with open( file ) as stream:
            self.prj_data = yaml.safe_load( stream )

    def get_files ( ):
        pkg = self.prj_data['Common']['pkg'] + self.prj_data['pkg']
        rtl = self.prj_data['Common']['rtl'] + self.prj_data['rtl']
        return pkg + rtl
        
