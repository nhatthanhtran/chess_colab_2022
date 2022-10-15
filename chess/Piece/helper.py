"""
This is the helper functions
"""
__mcintLOWERBOUND = 0
__mcintUPPERBOUND = 7


def in_bound(int_x_pos, int_y_pos):
    return (
        int_x_pos >= __mcintLOWERBOUND
        and int_x_pos <= __mcintUPPERBOUND
        and int_y_pos >= __mcintLOWERBOUND
        and int_y_pos <= __mcintUPPERBOUND
    )
