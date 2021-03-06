#!/usr/bin/python
#encoding:utf-8
import subprocess
import shlex
import privateutil
ORIGINHOSTS=u'/etc/hosts'
ADDITIONHOSTS=u'/etc/addition_hosts'


def update_origin_hosts_file():
    #backup
    (hostsfile_update_date,hostsfile_update_version)=privateutil.get_hosts_info_from_config_file()
    commandline='cp /etc/hosts /etc/hosts-'+hostsfile_update_date+'-v'+str(hostsfile_update_version)
    args=shlex.split(commandline)
    try:
        result=subprocess.check_call(args)
    except Exception,e:
        print '执行备份失败',e
        return False

    #测试ADDITIONHOSTS是否存在
    commandline='ls '+ADDITIONHOSTS
    args=shlex.split(commandline)
    try:
        result=subprocess.check_call(args)
    except Exception,e:
        print ADDITIONHOSTS+'文件不存在！'
        commandline='touch '+ADDITIONHOSTS
        args=shlex.split(commandline)
        subprocess.check_call(args) 
    #覆盖
    commandline='sh -c "cat '+ADDITIONHOSTS+' hosts '+' > /etc/hosts"'
    args=shlex.split(commandline)
    print args
    try:
        result=subprocess.check_call(args)
    except Exception,e:
        print '执行覆盖失败',e
        return False
    return True
        
if __name__=='__main__':
    update_origin_hosts_file()
    pass
