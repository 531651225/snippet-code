# scoding=utf-8
import pylab as pl

points = [[int(eachpoint.split("#")[0]), int(eachpoint.split("#")[1])] for eachpoint in open("points","r")]

# ָ��������ʼ����
currentCenter1 = [20,190]; currentCenter2 = [120,90]; currentCenter3 = [170,140]

pl.plot([currentCenter1[0]], [currentCenter1[1]],'ok')
pl.plot([currentCenter2[0]], [currentCenter2[1]],'ok')
pl.plot([currentCenter3[0]], [currentCenter3[1]],'ok')

# ��¼ÿ�ε�����ÿ���ص����ĵĸ��¹켣
center1 = [currentCenter1]; center2 = [currentCenter2]; center3 = [currentCenter3]

# ������
group1 = []; group2 = []; group3 = []

for runtime in range(50):
	group1 = []; group2 = []; group3 = []
	for eachpoint in points:
		# ����ÿ���㵽�������ĵľ���
		distance1 = pow(abs(eachpoint[0]-currentCenter1[0]),2) + pow(abs(eachpoint[1]-currentCenter1[1]),2)
		distance2 = pow(abs(eachpoint[0]-currentCenter2[0]),2) + pow(abs(eachpoint[1]-currentCenter2[1]),2)
		distance3 = pow(abs(eachpoint[0]-currentCenter3[0]),2) + pow(abs(eachpoint[1]-currentCenter3[1]),2)
		
		# ���õ�ָ�ɵ�����������������ڵĴ�
		mindis = min(distance1,distance2,distance3)
		if(mindis == distance1):
			group1.append(eachpoint)
		elif(mindis == distance2):
			group2.append(eachpoint)
		else:
			group3.append(eachpoint)
	
	# ָ�������еĵ�󣬸���ÿ���ص�����
	currentCenter1 = [sum([eachpoint[0] for eachpoint in group1])/len(group1),sum([eachpoint[1] for eachpoint in group1])/len(group1)]
	currentCenter2 = [sum([eachpoint[0] for eachpoint in group2])/len(group2),sum([eachpoint[1] for eachpoint in group2])/len(group2)]
	currentCenter3 = [sum([eachpoint[0] for eachpoint in group3])/len(group3),sum([eachpoint[1] for eachpoint in group3])/len(group3)]
	
	# ��¼�ôζ����ĵĸ���
	center1.append(currentCenter1)
	center2.append(currentCenter2)
	center3.append(currentCenter3)

# ��ӡ���еĵ㣬����ɫ��ʶ�õ������Ĵ�
pl.plot([eachpoint[0] for eachpoint in group1], [eachpoint[1] for eachpoint in group1], 'or')
pl.plot([eachpoint[0] for eachpoint in group2], [eachpoint[1] for eachpoint in group2], 'oy')
pl.plot([eachpoint[0] for eachpoint in group3], [eachpoint[1] for eachpoint in group3], 'og')

# ��ӡÿ���ص����ĵĸ��¹켣
for center in [center1,center2,center3]:
	pl.plot([eachcenter[0] for eachcenter in center], [eachcenter[1] for eachcenter in center],'k')

pl.show()