```
#!/usr/bin/env python3

import argparse


def options():
    parser = argparse.ArgumentParser()
    
    parser.add_argument(
      "-short_cmd", "lng_cmd",
      help="Description",
      action="store" -- to store a value or action="store_true" to verify usage,
      type=specify type,
    )

    # optional -- make sure at least one command is given
    # if not arguments are given, print usage message
	  if len(sys.argv[1:]) == 0:
		  parser.print_help()
		  parser.exit()

   

    args = parser.parse_args()

    return args
    
```

# also nargs can be used like so:
	nargs=+ for one or more options
