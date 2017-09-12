#Task 3 Previous exercise 17
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print ("Coppying from %s to %s" % (from_file, to_file))

# we could do their two on one line too, how?
in_file = open(from_file)
# print (in_file) # Do test
indata = in_file.read()
# print (indata) # Do test
# print (from_file) # Do test
# indata = from_file.read() # AttributeError: 'str' object has no attribute 'read'

print ("The input file is %d bytes long" % len(indata))

print ("Does the output file exist? %r" % exists(to_file))
print ("Ready, hit RETURN to continue, CTRL-C to abort.")
input () # achieve the function of any key.

out_file = open(to_file, 'w') # <_io.TextIOWrapper name='You2' mode='w' encoding='cp936'>
# print (out_file)
out_file.write(indata) # <built-in method write of _io.TextIOWrapper object at 0x0000000001F3DC18>
# print (out_file.write)
print ("Alright,all done.")

out_file.close()
in_file.close()
