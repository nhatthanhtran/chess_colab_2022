"""
This is the helper functions
"""
mcintLOWERBOUND = 0
mcintUPPERBOUND = 7

def blnInBound(intXPos, intYPos):
	return (intXPos >= mcintLOWERBOUND and intXPos <= mcintUPPERBOUND and intYPos >=  mcintLOWERBOUND and intYPos <= mcintUPPERBOUND)



#print(blnInBound(-1,1))

