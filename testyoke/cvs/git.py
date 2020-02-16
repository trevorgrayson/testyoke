import subprocess

INCANTATION = ['git', 'rev-parse', 'HEAD']
DIRTY_INCANTATION = ['git', 'diff', 'HEAD']

class Git:
    @classmethod
    def sha(cls):
        output = subprocess.check_output(INCANTATION).strip()
        output = output.decode('utf-8')
        if cls.dirty():
            output += '-dirty' 
        return output

    @classmethod
    def dirty(cls):
        """ boolean of if changes have been made to present sha """
        output = subprocess.check_output(DIRTY_INCANTATION)
        return len(output.strip()) == 0
