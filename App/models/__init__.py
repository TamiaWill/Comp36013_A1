# Add to application (import model to make available to the rest of the application)
# Everytime a model is formed, re-initialiation the database to ensure everything is working

from .Student import *
from .Admin import *
from .Competition import *
from .Result import *

from .user import *