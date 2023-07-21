#! /bin/bash

# cf : man test
# TIPS : return 1 = fails for bash shell
[ "$(curl http://127.0.0.1:8000)" ] || (echo "FAIL" && exit 1)


# TODO : with curl or playwrite : DO domain test on new db feature
echo "Need to test messages are correctly loaded for the domain";
exit 1


