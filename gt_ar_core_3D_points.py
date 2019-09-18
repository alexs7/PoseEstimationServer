import numpy as np
import pdb
from scipy.spatial.transform import Rotation as R

# sample point (-47.079 ,  -66.5551,  170.5197)
point_3D = np.array([-47.079 ,  -66.5551,  170.5197 , 1])

ar_core_pose_T = np.array([-0.020, -0.068, 0.023])
ar_core_pose_R_quat = np.array([[-0.03, -0.06, -0.72, -0.69]])
ar_core_pose_R = R.from_quat(ar_core_pose_R_quat)
ar_core_pose_R = np.array(ar_core_pose_R.as_dcm()[0])

rt_ar_core = np.concatenate((ar_core_pose_R, ar_core_pose_T.reshape([3,1])), axis=1)
bottom_row = np.array([0,0,0,1]).reshape([1,4])

rt_ar_core = np.concatenate((rt_ar_core, bottom_row), axis=0) #make homogeneous
rt_ar_core_inv = np.linalg.inv(rt_ar_core)

pdb.set_trace()

points3D_in_arcore_world_coordinate_system = np.dot(rt_ar_core_inv, point_3D.reshape([4,1]))

print points3D_in_arcore_world_coordinate_system

# Alternative way to getting the pose inverse (http://www.cg.info.hiroshima-cu.ac.jp/~miyazaki/knowledge/teche53.html)
# # R^T
# ar_core_pose_R_transpose = np.transpose(ar_core_pose_R)
# # -R^Tt
# minus_ar_core_pose_R_transpose_t = np.dot(-ar_core_pose_R_transpose,ar_core_pose_T.reshape([3,1]))
# rt_ar_core_inv_correct = np.concatenate((ar_core_pose_R_transpose, minus_ar_core_pose_R_transpose_t), axis=1)