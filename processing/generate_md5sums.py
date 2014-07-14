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

def sort_by_directory(filelist):
    dirs = {}
    sort = []
    for ea in filelist:
        dirname, fname = osp.dirname(ea), osp.basename(ea)
        flist = dirs.setdefault(dirname, [])
        flist.append(fname)
    for ea in sorted(dirs):
        sort.extend([osp.join(ea, f) for f in sorted(dirs[ea])])
    return sort


if __name__ == '__main__':
    here = osp.abspath(osp.dirname(sys.argv[0])) + osp.sep
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

    basedir = osp.dirname(osp.commonprefix(files_to_hash))+os.sep
    md5file = osp.join(basedir, 'md5sums')

    files_to_hash.discard(osp.abspath(sys.argv[0]))
    files_to_hash.discard(md5file)
    filelist = sort_by_directory(files_to_hash)

    print 'Preparing to generate md5 checksums...'
    print 'Common parent folder:', basedir
    print 'Files to hash:'
    for each in filelist:
        print ' ', each.replace(basedir, '')
    print 'Output file name:', md5file

    ans = raw_input("Proceed? Enter 'y' to continue: ")
    if ans.lower().strip() != 'y':
        print 'Aborting!'
        sys.exit(0)

    blocksize = 2**20
    with open(md5file, mode='w') as md5sums:
        for each in filelist:
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


