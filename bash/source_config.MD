```
# This one liner will help with finding config files or other files you wish to source, from the directory that the current script is running from.
# Reference:

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

```
