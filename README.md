> **Warning** : This repository/project is no longer maintained. If you are interested, it's free software under the GPL-3.0 license.

# FOSS-Shield
A Python module to display an error message and exit if it was running via proprietary operating system.

## Installation
### Coping a file
Every thing in one file; therefor, you can just copy the `foss_shield.py` to your project's source code.
You can use `wget` to download it:
```bash
$ wget https://raw.githubusercontent.com/zer0-x/python-fossshield/main/foss_shield/foss_shield.py
```
### With PIP
To be added later...

## Usage
Just import the module, then use the `run` function.
```python
import foss_shield

foss_shield.run()
```
For one line import:
```python
__import__("foss_shield").run()
```

## TODO
- [ ] Add Internationalization support.
- [ ] Add more UI frameworks.
- [ ] Add web UI using web frameworks.
- [ ] Add messages using the system notifications.
