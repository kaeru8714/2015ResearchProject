# -*- coding: utf-8 -*-

import os
import time


ITEM_INFO = "itemInfo.tsv"
USER_INFO = "purchaseRecord.tsv"


class CodeSprint(object):
	def __init__(self, path):
		self.path = path
		self.path_movie = path + "/movie/"
		self.path_user = path + "/user/"
		self.num_user = 91223

curr_dir = os.getcwd()
cs = CodeSprint(curr_dir)

class Movie(object):
	def __init__(self, movie_list):
		movie_list = movie_list.split()

		self.GLSS_ID = movie_list[0]
		self.SERIS_ID = movie_list[1]
		self.INFO_TP_ID = movie_list[2]
		self.CATEGORY = movie_list[3]
		self.PRODUCTION_YR = movie_list[6]
		self.DIRECTOR_NM_LIST = movie_list[9]
		self.ACTR_NM_LIST = movie_list[10]
		self.CNTRY_NM_LIST = movie_list[12]
		self.LVL_CD = movie_list[13]

class User(object):
	def __init__(self, user_list):
		self.USER_ID = user_list[0]
		self.BUY_DT = user_list[1]
		self.GLSS_ID = user_list[2]
		self.TOT_USE_AMOUT = user_list[3]



def createIndexFolders():
	os.makedirs(cs.path_movie)
	print "A directory created at:" + cs.path_movie
	os.makedirs(cs.path_user)
	print "A directory created at:" + cs.path_user


def addUserData(line, user_no):
	target_file = open(cs.path_user + "user" + user_no + ".tsv", 'a')
	target_file.write(line)
	target_file.close()
	print("User #" + user_no + " indexed.")


def parseUser():
	user_data = open(USER_INFO, 'r')

	for single_lines in user_data.readlines():
		user = User(single_lines.split())
		addUserData(single_lines, user.USER_ID)
	user_data.close()

start_time = time.time()

createIndexFolders()
parseUser()

print "--- %d seconds elapsed---" %(time.time() - start_time)
