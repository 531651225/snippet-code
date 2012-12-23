# scoding=utf-8
import pylab as pl
from collections import defaultdict,Counter

points = [[int(eachpoint.split("#")[0]), int(eachpoint.split("#")[1])] for eachpoint in open("points","r")]

# ����ÿ�����ݵ����ڵ����ݵ㣬������Ϊ�Ըõ�Ϊ�����Ա߳�Ϊ2*EPs������
Eps = 10
surroundPoints = defaultdict(list)
for idx1,point1 in enumerate(points):
	for idx2,point2 in enumerate(points):
		if (idx1 < idx2):
			if(abs(point1[0]-point2[0])<=Eps and abs(point1[1]-point2[1])<=Eps):
				surroundPoints[idx1].append(idx2)
				surroundPoints[idx2].append(idx1)

# �������������ڵ����ݵ�ĸ�������4��Ϊ���ĵ�
MinPts = 5
corePointIdx = [pointIdx for pointIdx,surPointIdxs in surroundPoints.iteritems() if len(surPointIdxs)>=MinPts]

# �����ڰ���ĳ�����ĵ�ķǺ��ĵ㣬����Ϊ�߽��
borderPointIdx = []
for pointIdx,surPointIdxs in surroundPoints.iteritems():
	if (pointIdx not in corePointIdx):
		for onesurPointIdx in surPointIdxs:
			if onesurPointIdx in corePointIdx:
				borderPointIdx.append(pointIdx)
				break

# ������Ȳ��Ǳ߽��Ҳ���Ǻ��ĵ�
noisePointIdx = [pointIdx for pointIdx in range(len(points)) if pointIdx not in corePointIdx and pointIdx not in borderPointIdx]

corePoint = [points[pointIdx] for pointIdx in corePointIdx]	
borderPoint = [points[pointIdx] for pointIdx in borderPointIdx]
noisePoint = [points[pointIdx] for pointIdx in noisePointIdx]

# pl.plot([eachpoint[0] for eachpoint in corePoint], [eachpoint[1] for eachpoint in corePoint], 'or')
# pl.plot([eachpoint[0] for eachpoint in borderPoint], [eachpoint[1] for eachpoint in borderPoint], 'oy')
# pl.plot([eachpoint[0] for eachpoint in noisePoint], [eachpoint[1] for eachpoint in noisePoint], 'ok')

groups = [idx for idx in range(len(points))]

# �������ĵ����������ڵ����к��ĵ����ͬһ������
for pointidx,surroundIdxs in surroundPoints.iteritems():
	for oneSurroundIdx in surroundIdxs:
		if (pointidx in corePointIdx and oneSurroundIdx in corePointIdx and pointidx < oneSurroundIdx):
			for idx in range(len(groups)):
				if groups[idx] == groups[oneSurroundIdx]:
					groups[idx] = groups[pointidx]

# �߽����������ڵ�ĳ�����ĵ����ͬһ������
for pointidx,surroundIdxs in surroundPoints.iteritems():
	for oneSurroundIdx in surroundIdxs:
		if (pointidx in borderPointIdx and oneSurroundIdx in corePointIdx):
			groups[pointidx] = groups[oneSurroundIdx]
			break

# ȡ�ع�ģ����5����
wantGroupNum = 3
finalGroup = Counter(groups).most_common(3)
finalGroup = [onecount[0] for onecount in finalGroup]

group1 = [points[idx] for idx in xrange(len(points)) if groups[idx]==finalGroup[0]]
group2 = [points[idx] for idx in xrange(len(points)) if groups[idx]==finalGroup[1]]
group3 = [points[idx] for idx in xrange(len(points)) if groups[idx]==finalGroup[2]]

pl.plot([eachpoint[0] for eachpoint in group1], [eachpoint[1] for eachpoint in group1], 'or')
pl.plot([eachpoint[0] for eachpoint in group2], [eachpoint[1] for eachpoint in group2], 'oy')
pl.plot([eachpoint[0] for eachpoint in group3], [eachpoint[1] for eachpoint in group3], 'og')

# ��ӡ�����㣬��ɫ
pl.plot([eachpoint[0] for eachpoint in noisePoint], [eachpoint[1] for eachpoint in noisePoint], 'ok')	

pl.show()