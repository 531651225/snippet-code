import datetime

# �ӿ�ʼʱ����ÿ��50Сʱ�����Ӧʱ�������ڼ�

def mymain():
	datetimeStart=datetime.datetime.strptime('2012 03 04 15:15:33','%Y %m %d %H:%M:%S')
	datetimeEnd=datetime.datetime.now()
	
	while datetimeStart<datetimeEnd:
		print datetimeStart.strftime('%Y-%m-%d %H:%M:%S'),'\t',datetimeStart.isoweekday()
		datetimeStart+=datetime.timedelta(hours=50)
		
if __name__ == '__main__':
	mymain()