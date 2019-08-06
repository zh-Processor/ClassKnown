import idaapi
import idc
idaapi.require("utils")
idaapi.require("msvc")
from idaapi import autoIsOk
from msvc import run_msvc

def main():
    idc.Wait()
    if autoIsOk():
        classes = run_msvc()
        print classes
    else:
        print "Take it easy, man"
    print "Done"
    idc.Exit(0)

if __name__ == '__main__':
    main()