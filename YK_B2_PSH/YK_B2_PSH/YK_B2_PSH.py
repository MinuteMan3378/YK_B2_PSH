import time
import sys
import os
import random
import csv

def selectSort():    
    print "[*] Select sort start"
    t1 = time.time() # 코드 시작 시간 설정
    for i in range(listLen - 1): 
        for j in range(i+1, listLen):
            if randList[i] > randList[j]: # 리스트를 차례로 검색하다 더 작은 것이 나오면
                randList[i], randList[j] = randList[j], randList[i] # 자리를 바꾼다
    t2 = time.time() # 코드 종료 시간 설정
    exeTime = str(t2-t1) # 코드 실행 시간 계산
    with open(resFile, "ab") as csvFile: # 결과 파일에 저장
        selCSV = csv.writer(csvFile, delimiter=',',
                            quoting=csv.QUOTE_MINIMAL)
        selCSV.writerow(['Selection Sort', exeTime, randList])
    print "[*] Select sort end, execution time : "+exeTime+" seconds"
    for i in range(len(randList)):
        print randList[i]

def bubSort():
    print "[*] Bubble sort start"
    t1 = time.time() # 코드 시작 시간 설정
    for i in range(len(randList)-1): 
        for j in range(1, len(randList) - i ):
            if randList[j-1] > randList[j]: # 앞뒤를 비교하고, 앞이 더 크면
                randList[j-1], randList[j] = randList[j], randList[j-1] # 자리를 바꾼다
    t2 = time.time() # 코드 종료 시간 설정
    exeTime = str(t2-t1) # 코드 실행 시간 계산
    with open(resFile, "ab") as csvFile: # 결과 파일에 저장
        bubCSV = csv.writer(csvFile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        bubCSV.writerow(['Bubble Sort', exeTime, randList])
    print "[*] Bubble sort end, execution time : "+exeTime+" seconds"
    for i in range(len(randList)):
        print randList[i]

def insSort():
    print "[*] Insert sort start"
    t1 = time.time() # 코드 시작 시간 설정
    randList.insert(0, -1) # 인덱스 비교를 줄이기 위해 임시 요소 설정
    for i in range( 2, len(randList) ):
        tmp = randList[i]
        j = i
        while randList[j-1] > tmp:
            randList[j] = randList[j-1]
            j = j - 1
        randList[j] = tmp
    del randList[0] # 임시 요소 제거
    t2 = time.time() # 코드 종료 시간 설정
    exeTime = str(t2-t1) # 코드 실행 시간 계산
    with open(resFile, "ab") as csvFile: # 결과 파일에 저장
        insCSV = csv.writer(csvFile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        insCSV.writerow(['Insertion Sort', exeTime, randList])
    print "[*] Insert sort end, execution time : "+exeTime+" seconds"
    for i in range(len(randList)):
        print randList[i]

file = open(sys.argv[1], "rb") # n개의 숫자가 줄바꿈으로 입력된 파일의 이름을 인자로 받음

dirpath = os.path.expanduser('~') + '\Desktop\\' 
resFile = dirpath+'resFile.csv' # 결과 파일이 저장될 위치 설정

line = file.readline()
randList = []
while line: # 정렬에 사용될 리스트 제작
    randList.append(int(line[:4])) # 숫자 뒤의 줄바꿈('\r\n')을 제거하고 int화
    line = file.readline() 

with open(resFile, "wb") as csvFile: # 결과 파일 세팅
        insCSV = csv.writer(csvFile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        insCSV.writerow(['Sort Method', 'Execution Time', 'Sorted List'])

listLen = len(randList) # 리스트 길이 확인
selectSort()
random.shuffle(randList) # 정렬된 상태의 리스트를 다시 섞기
insSort()
random.shuffle(randList) # 정렬된 상태의 리스트를 다시 섞기
bubSort()
