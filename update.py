import subprocess    # Module permettant l'exécution de programmes externes en python

class Update:    # Définition de la classe Update qui donne les caractéristiques de notre opération
    
    def __init__(self, Uninstall_file_path_from_the_old_version = None, Path_to_the_new_version_installation_file = None):    # Attributs de l'objet qui sera créé et qui va prendre certains chemins
        
        self.Uninstall_file_path_from_the_old_version = Uninstall_file_path_from_the_old_version
        
        self.Path_to_the_new_version_installation_file = Path_to_the_new_version_installation_file
    
    def update(self):    # Méthode pour la mise à jour
        
        try:
            
            subprocess.run(self.Uninstall_file_path_from_the_old_version)    # Exécution du fichier de désinstallation
        
        except:
            
            pass
        
        finally:
            
            subprocess.run(self.Path_to_the_new_version_installation_file)    # Exécution du fichier de d'installation même en cas d'erreurs

obj = Update()

obj.update()