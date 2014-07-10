#!python
"""
Simple script for creating an md5sum file

Created 2014-07-09 

Patrick O'Keeffe <pokeeffe@wsu.edu>

TODO:
- skip files if no longer exist when trying to hash
- support CLI parameters: block size, output file name, explicit base 
    directory
- ability to verify against existing md5sums files
- make output of md5sums files optional & add ability to write output to 
    stdout without prompts for batch processing
"""

import os, os.path as osp
import sys, hashlib

if __name__ == '__main__':
    here = osp.abspath(osp.dirname(sys.argv[0])) + '\\'
    dirs_to_search = set()
    files_to_hash = set()

    args = sys.argv[1:]
    if not args: 
        dirs_to_search.add(here)
    for arg in args:
        if os.path.isdir(arg): dirs_to_search.add(arg)
        if os.path.isfile(arg): files_to_hash.add(arg)

    for dir in dirs_to_search:
        for path, dirs, files in os.walk(dir):
            files_to_hash.update([osp.join(path, f) for f in files])
    files_to_hash.discard(osp.abspath(sys.argv[0])) # remove this file
    files_to_hash.discard(osp.join(here, 'md5sums')) # & output file
    files_to_hash = sorted(files_to_hash)

    basedir = osp.dirname(osp.commonprefix(files_to_hash))+os.sep
    md5file = osp.join(basedir, 'md5sums')
    
    print 'Preparing to generate md5 checksums...'
    print 'Common parent folder:', basedir
    print 'Files to hash:'
    for each in files_to_hash:
        print ' ', each.replace(basedir, '')
    print 'Output file name:', md5file

    ans = raw_input("Proceed? Enter 'y' to continue: ")
    if ans.lower().strip() != 'y':
        print 'Aborting!'
        sys.exit(0)

    blocksize = 2**20
    with open(md5file, mode='w') as md5sums:
        for each in files_to_hash:
            md5 = hashlib.md5()
            hashname = each.replace(basedir, '')
            with open(each, mode='rb') as srcfile:
                block = srcfile.read(blocksize)
                while len(block) > 0:
                    md5.update(block)
                    block = srcfile.read(blocksize)
            hash = md5.hexdigest()
            line = hash+'  '+hashname+'\n'
            print line,
            md5sums.write(line)


