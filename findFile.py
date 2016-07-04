#! /usr/bin/env python

import re
import sys

import git
# requires git module. To install, "sudo pip install gitpython --upgrade"


if len(sys.argv) != 3:
   print("Invoke with the arguments: pathToRepo fullPathToFile")
   sys.exit(-1)

repoPath = sys.argv[1]
fileName = sys.argv[2]

g = git.Git(repoPath)
fileID = g.hash_object(fileName)

commits = g.rev_list(["HEAD"]).split("\n")

for commit in commits:
   lines = g.ls_tree(["-r",commit]).split("\n")
   for line in lines:
      fields   = line.split('\t')
      filePath = fields[1]
      blobID   = fields[0].split(' ')[2]
      if (blobID == fileID):
         print("commit:%s file:%s" % (commit,filePath))
