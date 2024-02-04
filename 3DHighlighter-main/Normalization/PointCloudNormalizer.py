import copy
from . import Normalizer


class PointCloudNormalizer:
    def __init__(self, point_cloud):
        self.point_cloud = point_cloud  # original copy of the mesh
        self.normalizer = Normalizer.get_bounding_sphere_normalizer(self.point_cloud.vertices)

    def __call__(self):
        self.point_cloud.vertices = self.normalizer(self.point_cloud.vertices)
        return self.point_cloud

