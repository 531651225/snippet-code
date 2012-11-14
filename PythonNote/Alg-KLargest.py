# -*- coding: utf-8 -*-
# ��Ŀ��Ѱ��N����������K����

import math,heapq,random
from timeit import Timer

# �ⷨһ��	   
# Ѱ��N����������K�����������Ͼ���Ѱ������K��������С���Ǹ���Ҳ���ǵ�K�����������ʹ�ö��������Ĳ�����Ѱ��N�����еĵ�K�����������һ����������p��������O��N����ʱ�临�Ӷ����ҳ����в�С��p����������N������������ΪVmax����С����ΪVmin����ô��N�����еĵ�K����һ��������[Vmin, Vmax]֮�䡣��ô����������������ڶ�������N�����еĵ�K����p��
def KLargest1(myList,N):
	maxElement=max(myList)
	minElement=min(myList)
	while ((maxElement-minElement)>0.5):
		midElement=minElement+(maxElement-minElement)*0.5
		numK=len([element for element in myList if element >= midElement])
		if numK>=N:
			minElement=midElement
		else:
			maxElement=midElement
	
	kLargest=[oneElement for oneElement in myList if oneElement>minElement]
	# print kLargest


# �ⷨ����ά��һ��Ԫ�ظ���ΪK����С�ѣ�����һ������󼴻������K����
# The heapq Module:http://docs.python.org/library/heapq.html
def KLargest2(myList,N):
	kLargest=myList[0:N]
	heapq.heapify(kLargest)
	for index in range(N,len(myList)):
		if myList[index]>kLargest[0]:
			heapq.heapreplace(kLargest,myList[index])
	# print kLargest


# �ⷨ����
# �������N���������������������ǵ�ȡֵ��Χ��̫�󣬿��Կ�������ռ䣬��¼ÿ���������ֵĴ�����Ȼ���ٴӴ�Сȡ����K�������磬�����������ڣ�0, MAXN�������еĻ�������һ������count[MAXN]����¼ÿ���������ֵĸ�����count[i]��ʾ����i�����������г��ֵĸ�����������ֻ��Ҫɨ��һ��Ϳ��Եõ�count���顣Ȼ��Ѱ�ҵ�K���Ԫ��
def KLargest3(myList,N):
	maxElement=max(myList)
	countElement=[0 for index in range(maxElement+1)]
	for eachElement in myList:
		countElement[eachElement]+=1
	
	sunCount=0;kLargest=[]
	for eachElement in range(maxElement,0,-1):
		sunCount+=countElement[eachElement]
		if sunCount<=N:
			kLargest.extend([eachElement]*countElement[eachElement])
		else:
			break
	# print kLargest
	

if __name__=='__main__':
	myList=[random.randint(1,100000) for one in range(1000)]
	# KLargest1(myList,5)
	# KLargest2(myList,5)
	# KLargest3(myList,5)
	
	# ��ʱ���Σ�ÿ��ִ�к���10000�顣����������õ�ʱ�䡣���������е���ȡֵ��Χ̫�󣬽ⷨ����ʤ
	t1=Timer("KLargest1(myList,5)","from __main__ import *")
	print max(t1.repeat(3,10000))
	
	t2=Timer("KLargest2(myList,5)","from __main__ import *")
	print max(t2.repeat(3,10000))
	
	t3=Timer("KLargest3(myList,5)","from __main__ import *")
	print max(t3.repeat(3,10000))