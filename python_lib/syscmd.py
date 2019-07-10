#!/usr/bin/env python3
# coding=utf-8

import sys
import re
import logging
import logging.handlers
import os
import time
import signal
import subprocess
from datetime import datetime
import pdb


logger = logging.getLogger()

def scp(host,sourcePath,targetPath,options="",get=True,printCmd=True):
    source=sourcePath
    target=targetPath
    if get:
        source=host+":"+sourcePath
    else:
        target=host+":"+targetPath

    ssh_cmd="scp "+options+" "+source+"  " + target
    if printCmd:
        logger.info("Execute scp:"+ssh_cmd)
    start = datetime.now()
    process = subprocess.Popen(ssh_cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    nochangeTimes=0
    lastSize=0
    sourceFileSize=1
    while process.poll() is None:
        time.sleep(1)
        now = datetime.now()
        workingTime=(now-start).seconds
        if nochangeTimes > 60 :
            logger.info("scp is expired ,kill it now.")
            os.kill(process.pid, signal.SIGKILL)
            os.waitpid(-1,os.WNOHANG)
            return False
        else:

            #if source is a directory , skip process step info show.
            if get:
                if os.path.isdir(targetPath):
                    continue
            else:
                if os.path.isdir(sourcePath):
                    continue;

            if workingTime % 10 == 0 :
                copiedFileSize=0
                if get:
                    if sourceFileSize==1:
                        outputSize=bash("ssh -p "+str(remotePort)+" "+logTargetHost+" ls -l "+sourcePath+" | awk 'NF>4 {print $5}' ",printCmd=False,printOutput=False
                        if outputSize is not None:
                            sourceFileSize = int(outputSize)/1024/1024
                        else:
                            continue
                    copiedFileSize = os.path.getsize(targetPath)/1024/1024
                else:
                    outputSize=bash("ssh -p "+str(remotePort)+" "+logTargetHost+" ls -l "+targetPath+" | awk 'NF>4 {print $5}' ",printCmd=False,printOutput=False)
                    sourceFileSize=os.path.getsize(sourcePath)/1024/1024
                    if outputSize is not None:
                        copiedFileSize=int(outputSize)/1024/1024
                    else:
                        continue

                if lastSize == int(copiedFileSize):
                    nochangeTimes+=1
                    logger.info("nochange times:"+str(nochangeTimes))
                else:
                    nochangeTimes=0
                    lastSize=int(copiedFileSize)
                logger.info("copied size "+str(round(copiedFileSize,2))+"M bytes, totalSize:"+str(round(sourceFileSize,2))+"M bytes. copied:"+str(round(copiedFileSize/sourceFileSize*100,2))+"%")
    info=process.stdout.read().decode("utf-8")
    if not info.isspace() and len(info)>0:
        logger.info(info)
    return True

def ssh(host,command,port=22,printCmd=True,printOutput=True):
    ssh_cmd="ssh -p "+str(port)+" "+host+" "+command
    if printCmd:
        logger.info("execute ssh:"+ssh_cmd)
    ret=subprocess.Popen(ssh_cmd,shell=True, stdout=subprocess.PIPE, bufsize=-1)
    info=ret.stdout.read().decode("utf-8")
    if not info.isspace() and len(info)>0:
        if printOutput:
            logger.info(info)
        return info

def bash(cmd,printCmd=True,printOutput=True):
    if printCmd:
        logger.info("Execute bash:"+cmd)
    ret=subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE, bufsize=-1)
    info=ret.stdout.read().decode("utf-8")
    if not info.isspace() and len(info)>0:
        if printOutput:
            logger.info(info)
        return info


def untar(dir,tarfile):
    untar="cd "+dir+";tar xvfz "+tarfile
