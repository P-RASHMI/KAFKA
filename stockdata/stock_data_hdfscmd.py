'''
@Author: Rashmi
@Date: 2021-11-7 19:31
@Last Modified by: Rashmi
@Last Modified time: 2021-11-7  00:30
@Title :Write a Python program for executing hadoop hdfs using subprocess to shift data 
from file stockdataconsole.txt to hdfs
'''

import subprocess

def run_cmd(args_list):
    """
    Description: To execute the hadoop hdfs commands using subprocess libraries 
    Parameter: It takes args_list as parameter
    Return: It returns s_return, s_output, e_err
    """
    print(f'Running system command: {args_list}')
    proc = subprocess.Popen(args_list,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    s_output, s_err = proc.communicate()
    s_return = proc.returncode
    return s_return,s_output,s_err

if __name__== "__main__":
    #to create directory in hdfs
    mkdir = run_cmd(['hadoop','fs','-mkdir','/Kafka_Stock_Data'])
    print(mkdir)
    # copy stockdataconsole.txt from local system to hdfs  
    copy_file = run_cmd(['hadoop','fs','-copyFromLocal', '/home/lenovo/Desktop/Python_work/hadoop/KAFKA/stockdata/stockdataconsole.txt', '/Kafka_Stock_Data'])   
    print(copy_file)