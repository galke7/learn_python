from sys import argv

script, filename = argv

txt_file = open(filename, 'r')
print(f"script {script} open file {filename}:")
print(txt_file.read())
txt_file.close()
