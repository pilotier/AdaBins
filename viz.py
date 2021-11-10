import open3d as o3d
import numpy as np


#pcd = o3d.geometry.PointCloud()

cam = o3d.camera.PinholeCameraIntrinsic(o3d.camera.PinholeCameraIntrinsicParameters.PrimeSenseDefault)
#cam.intrinsic_matrix =  [[914, 0.00, 640] , [0.00, 274.2, 192], [0.00, 0.00, 1.00]]

#img = o3d.io.read_image("D:/8th_Avenue_Stereo/Depth/R/img_000001.jpeg")
color_raw = o3d.io.read_image("D:/8th_Avenue_Stereo/RGB/R/img_000800.jpeg")
#depth_raw = o3d.io.read_image("D:/8th_Avenue_Stereo/Depth/R/img_000009.jpeg")
depth_raw = o3d.io.read_image("sim1/img_000800.jpeg")
rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(color_raw, depth_raw, convert_rgb_to_intensity=False)
print("hellow")
print(rgbd_image.color)
pcd = o3d.geometry.PointCloud.create_from_rgbd_image(rgbd_image, cam)

#pcd.points = o3d.utility.Vector3dVector(np.random.randn(500,3))
pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
o3d.visualization.draw_geometries([pcd])

