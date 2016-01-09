from ctypes import *
from my_debugger_defines import *

kernal64 = CDLL('libc.so.6')

class debugger():

  def __init__(self):
    pass

  def load(self, path_to_exec):

    creation_flags = DEBUG_PROCESS

    startupinfo         = STARTUPINFO()
    process_information = PROCESS_INFORMATION()

    startupinfo.dwFlags     = 0x1
    startupinfo.wShowWindow = 0x0

    startupinfo.cb = sizeof(startupinfo)

    print path_to_exec

    if kernal64.vfork() == 0: 
    
      status = kernal64.execl(path_to_exec)

      process_information.dwProcessId = kernal64.getpid()
      print "[*] We have successfully lauched the process!"
      print "[*] PID: %d" % process_information.dwProcessId
      # exit();
    else:

      print "[*] Error: 0x%08x." % kernal64.strerror()