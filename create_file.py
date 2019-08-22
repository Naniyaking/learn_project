# encoding: utf-8

import os
import sys
import time

timestamp=str(int(time.time()))
dir_name_txt = "/data/cache11/cache9_dir_name.txt"+"."+timestamp
home_dir = "/data/cache9/ztest"
print(dir_name_txt)
def create_dir(dir_name):
    dir = ("%s%s%s" % (home_dir, "/", dir_name))
    with open(dir_name_txt, 'a') as f:
      f.write(dir)
      f.write("\n")
      f.close()
    if os.path.exists(dir):
      print(dir+" is exist!")
    else:
      os.mkdir(dir)
    return dir



def create_file(set_dir):
    get_dir = set_dir 
    file_name = ("%s%s%s" % (get_dir, "/", "test.html"))
    with open(file_name, 'w') as f:
      f.write("test file-------------------------------------------------------------------")
      f.close()

wjb="wjb"
level="level"
for i in range(1, 11):
    wjb_dir = ("%s%s%s" % (wjb, "_", i))
    print(wjb_dir)
    set_dir = create_dir(wjb_dir)
    
    create_file(set_dir)

    for n in range(1, 11):
       level_1_dir=("%s%s%s%s%s%s" % (wjb_dir, "/", level, "1", "_", n))
       set_dir = create_dir(level_1_dir)
    
       create_file(set_dir)

       for a in range(1, 11):
         level_2_dir=("%s%s%s%s%s%s" % (level_1_dir, "/", level, "2", "_", a))
         set_dir = create_dir(level_2_dir)
	 create_file(set_dir)

         for b in range(1, 11):
           level_3_dir=("%s%s%s%s%s%s" % (level_2_dir, "/", level, "3", "_", b))
           set_dir = create_dir(level_3_dir)
	   create_file(set_dir)

	   for c in range(1, 11):
	     level_4_dir=("%s%s%s%s%s%s" % (level_3_dir, "/", level, "3", "_", c))
	     set_dir = create_dir(level_4_dir)
	     create_file(set_dir)

	     for c in range(1, 11):
	       level_5_dir=("%s%s%s%s%s%s" % (level_4_dir, "/", level, "5", "_", c))
	       set_dir = create_dir(level_5_dir)
	       create_file(set_dir)


