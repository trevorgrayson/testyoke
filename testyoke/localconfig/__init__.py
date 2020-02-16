from os import getcwd

CONFIG = '.testyoke'


class Config:
    def __init__(self, **kwargs):
        self.api_key = kwargs.get('api_key')
        self.project = kwargs.get('project')
        self.consent = kwargs.get('consent')


# TODO testing
def get_config():
    """ local config for publishing data """
    try:
        with open(CONFIG, 'r') as ty:
            config = {}

            for line in ty:
               key, value = line.split('=')
               config[key.strip()] = value.strip()

            return Config(**config)

    except FileNotFoundError:
        print("No config file found, generating.")
        api_key = input("API KEY (http://testyoke.ipsumllc.com/):")
        project = getcwd().split('/')[-1]
        project = input(f"What's the name of this project? [default: {project}]") or project
        sha_consent = input("May testyoke collect git sha information? Y/n") or 'yes'

        with open(CONFIG, 'w') as ty:
            ty.write(f"api_key={api_key}\n")
            ty.write(f"project={project}\n")
            ty.write(f"consent={sha_consent}\n")

        return get_config()
