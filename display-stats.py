#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import pygame
import sys
import time
import datetime
import psutil
import cbplib

pygame.init()
window = pygame.display.set_mode((320,240))
 
font0 = pygame.font.SysFont("droidsans", 22)
label0 = font0.render("Excelsior Status", 1, (255,0,0))

font1 = pygame.font.SysFont("droidsans", 22)
font2 = pygame.font.SysFont("droidsans", 22)
font3 = pygame.font.SysFont("droidsans", 22)
font4 = pygame.font.SysFont("droidsans", 22)
font5 = pygame.font.SysFont("droidsans", 22)
font6 = pygame.font.SysFont("droidsans", 22)
font7 = pygame.font.SysFont("droidsans", 22)

cbplib.init()
cbplib.clear()
cbplib.backlight(80)

while True:
	try:
		window.fill(pygame.Color(0,0,0))		
		
		lt = time.localtime()
		x = psutil.virtual_memory()
		y = psutil.disk_usage("/")
		z = psutil.net_io_counters()
		
                label1 = font1.render("Date: %s / Time: %s" %(time.strftime("%d.%m.%Y", lt), time.strftime("%H:%M:%S", lt)), 1, (255,255,0))
                label2 = font2.render("Load Average: 1(%s) / 5(%s) / 15(%s)" %(os.getloadavg()[0], os.getloadavg()[1], os.getloadavg()[2]), 1, (255,255,255))
                label3 = font3.render("RAM Usage: used %.1fMB / free %.1fMB" %(float((x[0] - x[1]) / 1000000), float(x[1] / 1000000)), 1, (0,0,255))
		label4 = font4.render("CPU Time in Per cent: %s" % psutil.cpu_percent(), 1, (0,255,0))
		label5 = font5.render("Disk: used %sM/%s%% / free %sM/%s%%" %(int(y[1] / 1000000), y[3], int(y[2] / 1000000), 100.0 - y[3]), 1, (255,140,0))
		label6 = font6.render("Net Usage: sent %sK / recv %sK" %(z[0] / 1000, z[1] / 1000), 1, (0,255,255))
		label7 = font7.render("Raspberry Pi Uptime: %s" % datetime.datetime.fromtimestamp(time.time() - psutil.boot_time()).strftime("%H:%M:%S"), 1, (255,0,255))

		window.blit(label0, (0,0))
		window.blit(label1, (10,50)) 
		window.blit(label2, (10,75))
		window.blit(label3, (10,100))
		window.blit(label4, (10,125))
		window.blit(label5, (10,150))
		window.blit(label6, (10,175))
		window.blit(label7, (10,200))
		
		pygame.image.save(window, "/ram/temp.bmp")        	
		cbplib.image("/ram/temp.bmp")
        	time.sleep(1)
		
	except:
		cbplib.clear()
		raise
                sys.exit(1)

