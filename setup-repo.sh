#!/bin/sh

echo "Installing clean/smudge filters"
git config filter.progverstr.clean "python crbasic/versionstr.py --remove"
git config filter.progverstr.smudge "cat"

echo "Installing hooks"
ln -f crbasic/update-version.sh .git/hooks/post-commit
ln -f crbasic/update-version.sh .git/hooks/post-rewrite
