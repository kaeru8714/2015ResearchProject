#-*- encoding: utf-8 -*-
import urllib2
import bs4
import time
from time import localtime, strftime
from mongoengine import Document, IntField, DateTimeField, StringField, connect
import datetime


class newNaverRankModel(Document):
    recoded_at = DateTimeField()
    rank_one = StringField()
    rank_two = StringField()
    rank_three = StringField()
    rank_four = StringField()
    rank_five = StringField()
    rank_six = StringField()
    rank_seven = StringField()
    rank_eight = StringField()
    rank_nine = StringField()
    rank_ten = StringField()

    def set_time(self, time):
        try:
            self.recoded_at = time
        except BaseException as E:
            print(str(E))

    def set_rank(self, ranks):
        try:
            self.rank_one = ranks[0]
            self.rank_two = ranks[1]
            self.rank_three = ranks[2]
            self.rank_four = ranks[3]
            self.rank_five = ranks[4]
            self.rank_six = ranks[5]
            self.rank_seven = ranks[6]
            self.rank_eight = ranks[7]
            self.rank_nine = ranks[8]
            self.rank_ten = ranks[9]
        except BaseException as E:
            print(str(E))


#0 프로그램 실행시각 기록 및 초기설정
inittime = strftime("%Y-%m-%d %H:%M:%S", localtime())
loop_active = True
counter = 0
print '\n\n실행 시각: %s\n\n' %inittime


def getRealRank():
    global counter

#1 네이버 메인페이지 HTML 파일을 가져옴
    url = "http://www.naver.com"
    content = urllib2.urlopen(url)
    soup = bs4.BeautifulSoup(content)

#2 받은 HTML파일에서 실시간 검색어에 해당하는 HTML 코드를 파싱
    realRankTags = soup.find_all(id='realrank')
    resultList = realRankTags[0].find_all('a')

#3 네이버 실시간검색어 코드 상 11번째 검색어 코드가 중복되어 파싱되므로 이를 제거
    del resultList[10]

#4 파싱한 HTML코드에서 검색어에 해당하는 항목을 가져온다
    realKeywords = [item['title'] for item in resultList]
    counter += 1
    current_rank = newNaverRankModel()
    current_rank.set_rank(realKeywords)
    current_rank.set_time(datetime.datetime.now())
    try:
        current_rank.save()
        print('%s: DB Saved!' % str(datetime.datetime.now()))
    except BaseException as E:
        print('%s: error! - %s' % (str(datetime.datetime.now()), str(E)))

#5 현재 시각, 파싱 카운터와 실시간 검색어를 finalResult에 담고, 이를 출력한다.
    finalResult =  '=============\n'
    finalResult += "Count: %d\n" %counter
    finalResult += time.ctime()

    for index, keyword in enumerate(realKeywords):
        finalResult += '\n[%d] %s'%(index + 1, keyword.encode('utf-8'))

    print finalResult

#6 파일 입출력. naverrank_<프로그램 실행시각>.txt을 생성하고 finalResult를 write한다.
    f = open("naverrank_%s.txt" % inittime, 'a')
    print >> f, finalResult


#7 프로그램 루프 시작. 7초마다 한번 파싱한다.
def loop():
    while (loop_active):
        getRealRank()
        time.sleep(7)

if __name__ == '__main__':
    connect('naverrank')
    loop()


# '메르스' 검색어 포함 여부를 확인하는 코드
'''     for EachKeyword in realKeywords:
        regexp = re.compile(r'메르스')
        if regexp.search(EachKeyword.encode('utf-8')) is not None:
            print '메르스 검색어 발견!'
'''
