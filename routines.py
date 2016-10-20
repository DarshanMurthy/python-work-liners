class Test(object):
	def __init__(self,name=None,id=None):
		self.name = name 
		self.id = id

	def display(self):
		return self.id



class Service(object):
	def __init__(self,host,binary,topic,manager,report_interval=None,periodic_interval=None, *args, **kwargs):
		print('Initializing Service')
		super(Service,self).__init__(*args,**kwargs)

class Color(object):
	def __init__(self, color='red', **kwargs):
		print('Initializing Color')
		self.color = color
		super(Color, self).__init__(**kwargs)

class ColoredService(Service,Color):
	def __init__(self, *args, **kwds):
		print('Initializing Colored Service')
		super(ColoredService,self).__init__(*args, **kwds)

c = ColoredService('host','bin','top','mgr','ivl', color='blue')







