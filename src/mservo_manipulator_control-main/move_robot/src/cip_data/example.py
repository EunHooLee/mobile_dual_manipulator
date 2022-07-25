# Dependency: Docker, Python3
# Run docker.sh before using gqcnn module
# calc_grasping_point(rgb_path, depth_path, result_path='./results', docker_container='gqcnn')

from gqcnn import calc_grasping_point

rgb_path = 'sample/ham2_nip_snap_rgb_0.jpg'
depth_path = 'sample/ham2_nip_snap_depth_0.npy'
grasping_point = calc_grasping_point(rgb_path, depth_path, result_path='./results')
print(grasping_point)