#coding=utf-8
import time,sched,os,urllib2,re,string

# ÿ��һ��ʱ����ʾ��������̳��ע���û���

#��ʼ��schedģ���scheduler��
#��һ��������һ�����Է���ʱ����ĺ������ڶ������������ڶ�ʱδ����֮ǰ������
s = sched.scheduler(time.time,time.sleep)

#�������Ե��ȴ����ĺ���
def event_func():
	req = urllib2.Request('http://bbs.byr.cn/index')
	response = urllib2.urlopen(req)
	rawdata = response.read()
	response.close()
	
	usernump = re.compile(r'span class="c-user">.*?</span>��')
	usernummatch = usernump.findall(rawdata)
	if usernummatch:
		currentnum=usernummatch[0]
		currentnum=currentnum[string.index(currentnum,'>')+1:string.index(currentnum,'<')]
		print "Current Time:",time.strftime('%Y,%m,%d,%H,%M',time.localtime(time.time())),'User num:',currentnum


#enter�ĸ������ֱ�Ϊ�����ʱ�䣬���ȼ�������ͬʱ�䵽��������¼�ͬʱִ��ʱ���򣩡������ô����ĺ����������Ĳ�����ע�⣺һ��Ҫ��tuple���磬���ֻ��һ��������(xx,)��
def perform(inc):
    s.enter(inc,0,perform,(inc,))
    event_func()
   
def mymain(inc=10):
    s.enter(0,0,perform,(inc,))
    s.run()

if __name__ == "__main__":
	mymain()