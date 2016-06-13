# under normal circumstances, this script would not be necessary. the
# sample_application would have its own setup.py and be properly installed;
# however since it is not bundled in the sdist package, we need some hacks
# to make it work

import os
import sys

HOST = '127.0.0.1'
sys.path.append(os.path.dirname(__name__))

from parktrack import create_app

if len(sys.argv) != 2:
    print '%s: <port>' % sys.argv[0]
    sys.exit()
# create an app instance
app = create_app()

app.run(debug=True, port=int(sys.argv[1]), host=HOST)
