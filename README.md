# SimAPI: Python Typing for CoppeliaSim

SimAPI is a Python package that enhances the way you interact with the CoppeliaSim simulation environment. 
It provides Python stubs for enhanced typing and adds the documentation from CoppeliaSim, 
making it easier to use the CoppeliaSim API and reducing switching back and forth from the docs during development.

have only tested it with a few API calls. There is a good chance there are bugs or missing parts of the documentation.
But I tried my best to check everything important

You can find the documentation here: https://manual.coppeliarobotics.com/

# Using in projects

```python
from typing import cast
from sim_api import SimAPI

sim: SimAPI = cast(SimAPI, client.require("sim"))
```


There is an MIT License for open-source use
