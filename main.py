#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 16:58:39 2018

@author: liucheng
"""

from FaceDetector import mtcnn as detector
import os


fd = detector("./model/mtcnn",useGPU = True)

file_path = "/home/liucheng/tmp/"
lisst = os.listdir(file_path)
lisst.sort()
for name in lisst:
    filename = os.path.join(file_path,name)
    aa,bb = fd.detect(filename)