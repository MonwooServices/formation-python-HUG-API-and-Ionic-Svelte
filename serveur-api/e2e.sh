#! /bin/bash

# cf : man test
# TIPS : return 1 = fails for bash shell
[ "$(curl http://127.0.0.1:8000)" ] || (echo "FAIL" && exit 1)
