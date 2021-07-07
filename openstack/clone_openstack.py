#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author:jayonlau

import os

openstack_dir = "/tmp/openstack"

if not os.path.exists(openstack_dir):
   os.mkdir(openstack_dir)


current_dir = os.getcwd()
white_list = current_dir + "/white_list"


git_url = "http://git.trystack.cn/openstack/"

f = open(white_list, encoding='utf-8')
projects = f.read().splitlines()
for project in projects:
    project_dir = openstack_dir + '/' + project
    if not os.path.exists(project_dir):
       os.system('git clone ' + git_url + project + ' ' + project_dir)



