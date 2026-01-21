# SimAPI: Python Typing for CoppeliaSim

SimAPI is a Python package that enhances the way you interact with the CoppeliaSim simulation environment. 
It provides auto-generated Python stubs with enhanced typing and added documentation, 
making it easier to use the CoppeliaSim API and reducing common errors during development.

# Using in projects

```python
from typing import cast
from sim_api import SimAPI

sim: SimAPI = cast(SimAPI, client.require("sim"))
```

have only tested it with a few API calls. There is a good chance there are bugs or missing parts of the documentation,
but I tried my best to check everything important

