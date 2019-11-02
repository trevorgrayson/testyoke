import os
from . import app

YOKE_PORT = os.environ.get("YOKE_PORT", 7357)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=YOKE_PORT)
    
