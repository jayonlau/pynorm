#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author:jayonlau

import os


#openstack_project git dir
openstack_dir = "/tmp/openstack/"



#out 
openstack_report_dir = "/tmp/openstack_report/"


white_list = "./openstack/white_list"


#get openstack_project_dir
def Project_Dir(openstack_dir):
  project_filePaths = []
  for file in os.listdir(openstack_dir):
      project_filePaths.append(os.path.join(file))
  return(project_filePaths)

#get openstack_project_dir alerdy download
project_dir = Project_Dir(openstack_dir)

if not os.path.exists(openstack_report_dir):
   os.mkdir(openstack_report_dir)

for project in project_dir:
  os.system('python3  ./pynorm.py ' + openstack_dir + project + ' > ' + openstack_report_dir + project + '.txt')
