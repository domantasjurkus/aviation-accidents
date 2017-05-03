import os

print __file__

if __name__ == '__main__':
	os.system('cd pci && python import.py && cd ..')
	os.system('cd ntsb && python import.py && cd ..')