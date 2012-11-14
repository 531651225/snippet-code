# -*- coding: utf-8 -*-
# ��Ŀ������һ���������飬������������Ҳ�и�����������������һ�������������һ�������飬ÿ�������鶼��һ���͡�������������ĺ͵����ֵ��

# �ⷨһ�� 
# ��ֱ�ӵĽⷨ��Ȼ����ٱ����ˣ������е��������г�����Ȼ�����͡�
# ���Ӷȿ��Լ򵥵��������������������i��jΪ������߽磬������������Ҫ�����������飬Ȼ����Ҫһ���α�k����������������������͡������ܵĸ��Ӷ���O��n^3����

def maxSubSum1(MyList):
	ListLength=len(MyList)
	sum=max=0
	for Lindex in range(ListLength): 
		for Rindex in range(Lindex,ListLength):
			sum=0
			for index in range(Lindex,Rindex+1): 
				sum+=MyList[index]
			print 'F',Lindex,'T',Rindex,'=',sum
			
			if sum>max:
				max=sum
	
	print max


# �ⷨһ�Ľ��棺
# ��ϸ��ĥ�ͻᷢ�֣���ʵ����Ҫ��ʹ��kȥ���������飬��Ϊÿ��j�ƶ���������µ������飬����ֻҪ��ÿ��j�ƶ�ʱ����һ�±Ƚϣ��Ͳ�������ֵ©��������ֻ��i��j�ƶ������ӶȽ��͵�O��n^2����
def maxSubSum2(MyList):
	ListLength=len(MyList)
	max=0
	for Lindex in range(ListLength):
		sum=0
		for Rindex in range(Lindex,ListLength): 
			sum+=MyList[Rindex]
			
			print 'F',Lindex,'T',Rindex,'=',sum
			
			if sum>max:
				max=sum
	
	print max


# �ⷨ���������㷨
# �����ֲ��ҵ�˼�����ƣ����ǿ��Է����������������ǲ��Ƿ��϶��ֲ��ҵ�������
# ���1.����������͵�������ȫ���ڱ��������벿�����Ұ벿�����磺��벿A[i]����A[n/2-1]�����Ұ벿A[n/2]����A[j]����������¿���ֱ��ʹ�õݹ���á�
# ���2.�������͵����������˱�������м�㡣���磺A[i]����A[n/2-1] A[n/2]����A[j]�����������������ֻҪ����벿Ѱ����A[n/2-1]��β�����Ұ벿Ѱ����A[n/2]��ͷ�������������͵��������飬����ͼ��ɡ����������֪��㣬ֻ��Ҫһ���α꼴�ɣ����Ը��Ӷ���2*O��n/2��=O��n����
# �ۺ����������������������㷨�ݹ�ʽ��T��n��=2T��n/2��+O��n��=O��n*logn����

def maxSubSum3(MyList,Left,Right):
	if Left==Right:
		return MyList[Left] if MyList[Left]>0 else 0
	
	Center = (Left+Right)/2;   
	LeftMaxSum = maxSubSum3(MyList,Left,Center)
	RightMaxSum = maxSubSum3(MyList,Center+1,Right) 
	
	LeftPartSum=MaxLeftPartSum=0
	for Lindex in range(Center,Left-1,-1):
		LeftPartSum+=MyList[Lindex]
		if LeftPartSum > MaxLeftPartSum: MaxLeftPartSum=LeftPartSum 

	RightPartSum=MaxRightPartSum=0
	for Rindex in range(Center+1,Right+1,1):
		RightPartSum+=MyList[Rindex]
		if RightPartSum > MaxRightPartSum:MaxRightPartSum=RightPartSum
	
	print 'F',Left,'T',Right,'=',max(LeftMaxSum,RightMaxSum,MaxLeftPartSum+MaxRightPartSum)
	return max(LeftMaxSum,RightMaxSum,MaxLeftPartSum+MaxRightPartSum)

# �ⷨ����
# �����A[0]��A[n-1]����������������ֽ�ɣ�
# �����������а���A[0]�����������A[1]����A[0]�Լ�������������ʱMax��A[0]����A[n-1]��=A[0]���������A[1]����Max��A[0]����A[n-1]��=A[0]+Max��A[1]����A[n-1]����
# �����������в�����A[0]��Max��A[0]����A[n-1]��=Max��A[1]����A[n-1]����
# ���ս��ȡ�������ߵ����ֵ���ɣ���Max��A[0]����A[n-1]��=max�� A[0], A[0]+Max��A[1]����A[n-1]��, Max��A[1]����A[n-1]������

def maxSubSum4(MyList,ListLength):
	NIncludeLargest=MyList[ListLength-1]
	NAllLargest=MyList[ListLength-1]
	for index in range(ListLength-2,-1,-1):
		NIncludeLargest=max(MyList[index],MyList[index]+NIncludeLargest)
		NAllLargest=max(NIncludeLargest,NAllLargest)
		print 'F',index,'T',ListLength-1,'=',NAllLargest
	
	return NAllLargest

if __name__ == '__main__':
	# maxSubSum1([1,-2,3,10,-4,7,2,-5])
	# maxSubSum1([-100,-2,-3,10,-4,-7,-2,1005])
	# print '*'*20
	# maxSubSum2([1,-2,3,10,-4,7,2,-5])
	# maxSubSum2([-100,-2,-3,10,-4,-7,-2,1005])
	# print '*'*20
	# print maxSubSum3([1,-2,3,10,-4,7,2,-5],0,len([1,-2,3,10,-4,7,2,-5])-1)
	# print maxSubSum3([-100,-2,-3,10,-4,-7,-2,1005],0,len([-100,-2,-3,10,-4,-7,-2,1005])-1)
	# print '*'*20
	print maxSubSum4([1,-2,3,10,-4,7,2,-5],len([1,-2,3,10,-4,7,2,-5]))
	print maxSubSum4([-100,-2,-3,10,-4,-7,-2,1005],len([-100,-2,-3,10,-4,-7,-2,1005]))