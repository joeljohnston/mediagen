#!/bin/bash
projectname=$1
classname=$2
LANG=C

find . \! -name 'rename.sh' -type f -exec sed -i '' 's/class1/'$classname'/g' {} \;
find . \! -name 'rename.sh' -type f -exec sed -i '' 's/myproject/'$projectname'/g' {} \;

find . \! -name 'rename.sh' -name 'myproject' -type d -exec mv {} $projectname \;
find . \! -name 'rename.sh' -name 'class1' -type d -exec mv {} $classname\;
