from utils import *
from models import *

print(list(filter(lambda str: not ("__" in str), dir())))

create_admin("Viktor")
create_admin("Mary")

create_user("Kate")