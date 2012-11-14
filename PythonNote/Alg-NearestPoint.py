# -*- coding: utf-8 -*-
# ��Ŀ����p1=(x1, y1), p2=(x2, y2), ��, pn=(xn, yn)��ƽ����n���㹹�ɵļ���S������㷨�ҳ�����S�о�������ĵ�ԡ�
import math,sys,random

# �ⷨһ��
# ��֪����S����n���㣬һ���������n(n-1)/2�Ե�ԣ����������Ƕ���n(n-1)/2�Ե����Խ��о�����㣬ͨ��ѭ����õ㼯�е�������.
def nearestPoint1(Points):
	nearestDistance=sys.maxint
	nearestPointA=[]
	nearestPointB=[]
	for onePoint in Points:
		for anotherPoint in Points:
			if onePoint != anotherPoint:
				distance=math.sqrt(math.pow((onePoint[0]-anotherPoint[0]),2)+math.pow((onePoint[1]-anotherPoint[1]),2))
				if distance<nearestDistance:
					nearestDistance=distance
					nearestPointA=onePoint
					nearestPointB=anotherPoint

	print 'F',nearestPointA,'T',nearestPointB,'=',nearestDistance


# �ⷨ����
# �㷨��������֪����S����n���㣬���η���˼����ǽ�S���в�֣���Ϊ2�����������ԡ��㷨ÿ��ѡ��һ������L����S�������������ΪSL��SR��Lһ��ȡ�㼯S�����е���м���x���������֣��������Ա�֤SL��SR�еĵ���Ŀ��Ϊn/2
# �����ҳ����������е���С��Ծ��룺��L�ͦ�R����SL��SR����С��Ծ���� = min����L����R����
# ��LΪ���ߣ���Ϊ�����һ����������С����Ի��п��ܴ�����SL��SR�Ľ��紦��p���q��ֱ�λ��SL��SR�����߷�Χ�ڡ�p�㲻�������е�q�������룬ֻ������������ϵʽ(q[x]-p[x])<=2*�� and |q[y]-p[y]|<=�ĵ�q��ľ��롣
def nearestPoint2(Points):
	if len(Points)==1:return sys.maxint
	if len(Points)==2:return math.sqrt(math.pow((Points[0][0]-Points[1][0]),2)+math.pow((Points[0][1]-Points[1][1]),2))
	
	DivideX=sum([onePoint[0] for onePoint in Points])/len(Points)
	leftPoints=[onePoint for onePoint in Points if onePoint[0]<=DivideX]
	rightPoints=[onePoint for onePoint in Points if onePoint[0]>DivideX]
	
	leftNearestDistance=nearestPoint2(leftPoints)
	rightNearestDistance=nearestPoint2(rightPoints)
	
	MDist=min(leftNearestDistance,rightNearestDistance)
	leftMidPoints=[onePoint for onePoint in leftPoints if (DivideX-onePoint[0])<=MDist]
	rightMidPoints=[onePoint for onePoint in rightPoints if (onePoint[0]-DivideX)<=MDist]
	
	midNearestDistance=sys.maxint
	for oneleftPoint in leftMidPoints:
		partRightPoints=[onerightPoint for onerightPoint in rightMidPoints if (onerightPoint[0]-oneleftPoint[0])<=2*MDist and abs(onerightPoint[1]-oneleftPoint[1])<=MDist]
		for onerightPoint in partRightPoints:
			distance=math.sqrt(math.pow((oneleftPoint[0]-onerightPoint[0]),2)+math.pow((oneleftPoint[1]-onerightPoint[1]),2))
			if distance<midNearestDistance:
				midNearestDistance=distance
		
	return min(midNearestDistance,MDist)

if __name__=='__main__':	
	# ȡ30���㣬x,y���귶Χ����1-100֮��
	Points=[[random.randint(1,100),random.randint(1,100)] for one in range(30)]

	nearestPoint1(Points)
	print '*'*20
	Points=sorted(Points,key=lambda x:(x[0],x[1]),reverse=False)
	print nearestPoint2(Points)