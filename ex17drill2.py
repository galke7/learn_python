from sys import argv ; script, frome_file, to_file = argv ; indata = open(frome_file).read() ; open(to_file, 'w').write(indata)


