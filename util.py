def lines(file):
	for line in file: 
		yield line
	yield '\n'
	
def blocks(file):
	block = []
	for line in lines(file):
		if line.strip():
			block.append(line)
			#print 'block.apend {{{%s}}}' %line
		elif block:
			#print 'join(block).strip {{{%s}}}' % ''.join(block).strip()
			yield ''.join(block).strip()
			block = []
			