import numpy as np

p = np.matrix([[5],[5]])
t = np.matrix([[np.cos(np.pi/4), np.sin(np.pi/4)],
                [-np.sin(np.pi/4), np.cos(np.pi/4)]])

print(t * p + np.matrix([[2], [2]]))

def ComputeLBP(img_mat):
    indexOffsetDict = {0:(-1, -1), 1:(0, -1), 2:(1, -1),
                   3:(1, 0), 4:(1, 1), 5:(0, 1),
                   6:(-1, 1), 7:(-1, 0)}

    padded = np.pad(img_mat, pad_width=1, mode='constant', constant_values=0)
    LBP_img = np.zeros(img_mat.shape)
    for x in range(1, len(padded) - 1):
        for y in range(1, len(padded[0]) - 1):
            bin_str = ''
            for i in range(8):
                cur_ind = (indexOffsetDict[i][1] + x, indexOffsetDict[i][0] + y)
                center = padded[x][y]
                compare = padded[cur_ind[0]][cur_ind[1]]
                if center > compare:
                    bin_str += str(0)
                else:
                    bin_str += str(1)
            bin_str = bin_str[::-1]
            int_rep = int(bin_str, 2)
            LBP_img[x-1][y-1] = int_rep
    return LBP_img

img = np.matrix([[5,6,7],
                 [6,3,2],
                 [1,4,4]])
print(ComputeLBP(img))
