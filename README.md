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

# Adding as a submodule and updatting
### To Add
```git
git submodule add https://github.com/samduckett/coppeliaSum-Python-Typing-Reference/edit/main/README.md simAPI # or the path you want
```
Then simply commit the changes

### To Clone a repo with simAPI
```git
git clone --recurse-submodules your/url/or/ssh_key
```
if alrady cloned
```
cd main-repo
git submodule init
git submodule update
```
### how to update submodule
```
cd simAPI
git pull
cd ..
```
Then simply commit the changes

There is an MIT License for open-source use
