# -*- coding: utf-8 -*-
"""
Created on Tue Nov  4

@author: elliotstaudt
"""

from nltk.corpus import wordnet as wn
import glob

tag_dict = {}
total = 0
max_key_word = ''
max_image_tags = 0

# MIRFLICKR-25000
#tagsDir = '/Users/elliotstaudt/Documents/MIRFLICKR-25000/tags/'
# MIRFLICKR
tagsDir = '/Users/elliotstaudt/Documents/MIRFLICKR/tags/2/'
# Get the names of each of the tag files in the tag directory.
tag_file_names = glob.glob(tagsDir + '*.txt')
# Read the tags and find the synonym for each one, if one exists.
for num in range(25000,30000):
  fname = tagsDir + str(num) + '.txt'
  with open(fname) as f:
    content = [x.strip('\n') for x in f.readlines()]
    content = [x.strip('\r') for x in content]
  
  # define file in which to store synonyms
  fsavename = tagsDir + str(num) + '_synonyms.txt'
  sf = open(fsavename, 'w')
  
  local_count = 0
  for word in content:
    total+=1
    # check to see the word is ascii encoded
    try:
      word = word.decode('ascii')
    except UnicodeDecodeError:
      continue
    # word is ascii encoded so attempt to find the synonym
    syn = wn.morphy(word)
    if syn != None:
      # a synonym was found, so write it to the new file
      local_count+=1
      if local_count > 1:
        sf.write('\n')
      sf.write(syn)
      if syn in tag_dict:
        tag_dict[syn].append(num)
      else:
        tag_dict[syn]=[num]
  # close the file for writing
  sf.close()
    
#print tag_dict
print len(tag_dict.keys())

max_tags = 0
for key in tag_dict:
  tag_len = len(tag_dict[key])
  if tag_len > max_tags:
    max_tags = tag_len
    max_key_word = key
    print "new most used word:", max_key_word, '... at:', max_tags

print "most used word:", max_key_word, '... at:', max_tags
print "total:", total