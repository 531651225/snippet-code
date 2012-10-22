# scoding=utf-8
# Agglomerative Hierarchical Clustering(AHC)
import pylab as pl
from operator import itemgetter
from collections import OrderedDict,Counter

points = [[int(eachpoint.split('#')[0]), int(eachpoint.split('#')[1])] for eachpoint in open("points","r")]

# ��ʼʱÿ����ָ��Ϊ����һ��
groups = [idx for idx in range(len(points))]

# ����ÿ�����֮��ľ���
disP2P = {}
for idx1,point1 in enumerate(points):
	for idx2,point2 in enumerate(points):
		if (idx1 < idx2):
			distance = pow(abs(point1[0]-point2[0]),2) + pow(abs(point1[1]-point2[1]),2)
			disP2P[str(idx1)+"#"+str(idx2)] = distance

# �����뽵�򽫸����������
disP2P = OrderedDict(sorted(disP2P.iteritems(), key=itemgetter(1), reverse=True))

# ��ǰ�еĴظ���
groupNum = len(groups)

# ���ֺϲ�������������Ӱ�죬��������ΪfinalGroupNumʱ��ֹͣ�ϲ�
finalGroupNum = int(groupNum*0.1)

while groupNum > finalGroupNum:
	# ѡȡ��һ����������ĵ��
	twopoins,distance = disP2P.popitem()
	pointA = int(twopoins.split('#')[0])
	pointB = int(twopoins.split('#')[1])
	
	pointAGroup = groups[pointA]
	pointBGroup = groups[pointB]
	
	# ��ǰ�����������������ͬһ���У�����B���ڵĴ��е����е�ϲ�����A���ڵĴ��У���ʱ��ǰ������1
	if(pointAGroup != pointBGroup):
		for idx in range(len(groups)):
			if groups[idx] == pointBGroup:
				groups[idx] = pointAGroup
		groupNum -= 1

# ѡȡ��ģ����3���أ������ع�Ϊ������
wantGroupNum = 3
finalGroup = Counter(groups).most_common(wantGroupNum)
finalGroup = [onecount[0] for onecount in finalGroup]

dropPoints = [points[idx] for idx in range(len(points)) if groups[idx] not in finalGroup]

# ��ӡ��ģ����3�����еĵ�
group1 = [points[idx] for idx in xrange(len(points)) if groups[idx]==finalGroup[0]]
group2 = [points[idx] for idx in xrange(len(points)) if groups[idx]==finalGroup[1]]
group3 = [points[idx] for idx in xrange(len(points)) if groups[idx]==finalGroup[2]]
pl.plot([eachpoint[0] for eachpoint in group1], [eachpoint[1] for eachpoint in group1], 'or')
pl.plot([eachpoint[0] for eachpoint in group2], [eachpoint[1] for eachpoint in group2], 'oy')
pl.plot([eachpoint[0] for eachpoint in group3], [eachpoint[1] for eachpoint in group3], 'og')	

# ��ӡ�����㣬��ɫ
pl.plot([eachpoint[0] for eachpoint in dropPoints], [eachpoint[1] for eachpoint in dropPoints], 'ok')	

pl.show()