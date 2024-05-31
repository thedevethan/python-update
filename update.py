import subprocess

class Update:
    
    def __init__(self, Uninstall_file_path_from_the_old_version = None, Path_to_the_new_version_installation_file = None):
        
        self.Uninstall_file_path_from_the_old_version = Uninstall_file_path_from_the_old_version
        
        self.Path_to_the_new_version_installation_file = Path_to_the_new_version_installation_file
    
    def update(self):
        
        try:
            
            subprocess.run(self.Uninstall_file_path_from_the_old_version)
        
        except:
            
            pass
        
        finally:
            
            subprocess.run(self.Path_to_the_new_version_installation_file)

obj = Update("C:\\Program Files (x86)\\Close the Window J\\unins000.exe", "close_setup.exe")

obj.update()