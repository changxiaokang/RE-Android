#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys
import time
import getopt

def get_pkg_act(path):
    cmd = "aapt dump badging " + path
    print "\r\n" + cmd

    pkg = ""
    act = ""
    lines = os.popen(cmd).readlines()
    for line in lines:
        if line.find("package") != -1:
            print line.split("\'")
            pkg = line.split("\'")[1]
        elif line.find("launchable-activity") != -1:
            print line.split("\'")
            act = line.split("\'")[1]
        else:
            continue

    time.sleep(1)
    return pkg, act
         
def start_dbgsrv(port):
    cmd = "adb shell su /data/local/tmp/dbgSrv"
    print "\r\n" + cmd
    os.system(cmd)
    time.sleep(1)
   
def am_start(pkg, act):
    cmd = "adb shell am start -D -n " + pkg + "/" + act
    print "\r\n" + cmd
    os.system(cmd)
    time.sleep(1)

def get_pkg_pid(pkg):
    cmd = "adb shell ps | findstr " + pkg
    print "\r\n" + cmd
    lines = os.popen(cmd).readlines()
    print lines
    
    for line in lines:
        tmp = line.split(" ")
        print tmp
        xxx = tmp[-1].strip('\r\n')
        
        if tmp[0] == "":
            pid = tmp[1]
        else:
            pid = tmp[0]
        
        if xxx == pkg:
            print pkg + "_pid: " + pid
            return pid
        else:
            print "ERR: " + pkg + " no start!"
            
    return ""

def tcp_forward(src, dst):
    cmd = "adb forward tcp:" + src + " tcp:" + dst
    print "\r\n" + cmd
    os.system(cmd)
    time.sleep(1)

def jdwp_forward(src, dst):
    cmd = "adb forward tcp:" + src + " jdwp:" + dst
    print "\r\n" + cmd
    os.system(cmd)
    time.sleep(1)

def jdb_connect(ipaddr, port):
    cmd = "jdb -connect com.sun.jdi.SocketAttach:hostname=" + ipaddr + ",port=" + port
    print "\r\n" + cmd
    print "Press any key to start debugging >>>>>>"
    os.system("pause")
    os.system(cmd)
    time.sleep(1)

def main(argv):
    pkg, act = get_pkg_act(argv[1])
    print "pkg: " + pkg
    print "act: " + act
    if pkg == "" and act == "":
        print "ERR: get_pkg_act error!"
        return 
   
    if am_start(pkg, act):
        print "ERR: am start error!"
        return 

    pid = get_pkg_pid(pkg)
    if pid == "":
        print ">>> " + pkg, pid
        print "ERR: get pkg pid error!"
        return 
   
    tcp_forward("23946", "23946")
    jdwp_forward("8700", pid)
    jdb_connect("127.0.0.1", "8700")
   
if __name__ == "__main__":
    main(sys.argv)
    os.system("pause")
