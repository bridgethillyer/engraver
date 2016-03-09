#!/usr/bin/env python

from prettytable import PrettyTable
from subprocess import call
from colors import bcolors
from os import listdir, walk, chdir

def service_new(arg_vars, project_root):
  print(bcolors.OKBLUE + "> Invoking ansible-galaxy. Streaming its output ..." + bcolors.ENDC)
  role = project_root + "/ansible/roles/" + arg_vars['service-name']
  call(["ansible-galaxy", "init", role])
  print(bcolors.OKBLUE + bcolors.BOLD + "> Service role created. Edit at: " + role + bcolors.ENDC)

def service_remove(arg_vars, project_root):
  role = project_root + "/ansible/roles/" + arg_vars['service-name']
  call(['rm', '-rf', role])
  print(bcolors.OKBLUE + "> Deleted service: " + arg_vars['service-name'] + bcolors.ENDC)

def service_pull(arg_vars, project_root):
  print(bcolors.OKBLUE + "> Invoking Git. Streaming its output ..." + bcolors.ENDC)
  role = project_root + "/ansible/roles/" + arg_vars['service-name']
  call(["git", "clone", arg_vars['service-repo'], role])
  print(bcolors.OKBLUE + "> Install service at: " + role + bcolors.ENDC)

def service_describe(arg_vars, project_root):
  path = project_root + "/ansible/roles"
  services = next(walk(path))[1]
  t = PrettyTable(['Service Name'])
  t.align = "l"

  for s in services:
    t.add_row([s])

  print t
