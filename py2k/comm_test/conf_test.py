#! /usr/bin/env python
# -*- coding: utf-8 -*-
from ..comm import ReadConf

CONFFILEPATH = 'py2k/comm_test/test.conf'
SSESSIONNM = 'ss1'
KEY1 = 'key1'
KEY2 = 'key2'
KEY3 = 'key3'

if __name__ == "__main__":
	v1 = ReadConf.ReadConf.read_val(CONFFILEPATH, SSESSIONNM, KEY1) 	
	print(v1 + 'です')
	v2 = ReadConf.ReadConf.read_val(CONFFILEPATH, SSESSIONNM, KEY2) 	
	print(v2 + 'です')
	v3 = ReadConf.ReadConf.read_val(CONFFILEPATH, 'ss2', KEY3) 	
	print(v3 + 'です')
