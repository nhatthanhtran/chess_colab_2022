"""
This is the helper functions
"""
__mcintLOWERBOUND = 0
__mcintUPPERBOUND = 7


def InBound(intXPos, intYPos):
    return (intXPos >= __mcintLOWERBOUND and intXPos <= __mcintUPPERBOUND and intYPos >= __mcintLOWERBOUND and intYPos <= __mcintUPPERBOUND)
