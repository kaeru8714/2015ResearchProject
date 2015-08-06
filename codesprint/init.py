# -*- coding: utf-8 -*-

import time
import os

#유용한 클래스들 모음

class TimeChecker: #시간측정 데코레이터
	def __init__(self, function):
		self.func = function

	def __call__(self):
		start_time = time.time()
		print self.func.__name__, ": Begin"
		self.func()
		print self.func.__name__, ": End --- %f seconds elapsed ---" %(time.time() - start_time)


class Item(object): #아이템 정보
	def __init__(self, item_list):
		self.GLSS_ID = item_list[0]
		self.SERIS_ID = item_list[1]
		self.INFO_TP_ID = item_list[2]
		self.CATEGORY = item_list[3]
		self.PRODUCTION_YR = item_list[6]
		self.DIRECTOR_NM_LIST = item_list[9]
		self.ACTR_NM_LIST = item_list[10]
		self.CNTRY_NM_LIST = item_list[12]
		self.LVL_CD = item_list[13]

class User(object): #유저 정보
	def __init__(self, user_list):
		self.USER_ID = user_list[0]
		self.BUY_DT = user_list[1]
		self.GLSS_ID = user_list[2]
		self.TOT_USE_AMOUT = user_list[3]

class CodeSprint(object): # 각 디렉토리별 path나 최대 유저수, 품목수등을 담았다.
	def __init__(self):
		path = os.getcwd()
		self.path_user = path + "/user_indexed/"
		self.path_item = path + "/item_sorted/"
		self.path_purchaseRecord_sorted = path + "/purchaseRecord_sorted/"
		self.path_item_reference = path + "/item_reference/"
		self.path_similarity = path + "/similarity/"
		self.num_user = 91223
		self.num_item = 41759

cs = CodeSprint()

def create_directories():
	os.makedirs(cs.path_item)
	print "A directory created at: " + cs.path_item
	os.makedirs(cs.path_user)
	print "A directory created at: " + cs.path_user
	os.makedirs(cs.path_user_indexed)
	print "A directory created at: " + cs.path_user_indexed
	os.makedirs(cs.path_purchaseRecord_sorted)
	print "A directory created at: " + cs.path_purchaseRecord_sorted
	os.makedirs(cs.path_similarity)
	print "A directory created at: " + cs.path_similarity

if __name__ == "__main__":
	create_directories()
	index.main()