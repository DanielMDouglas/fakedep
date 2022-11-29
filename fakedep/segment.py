import numpy as np
from .dtypes import *

class Segment:
    def __init__(self, vertex = [0, 0, 0], mip = True, length = 10):
        self.things = things

        self.vertexPos = vertex
        
        self.direction = np.random.random(3)
        self.direction /= np.linalg.norm(self.direction)

        self.length = 10

        if mip:
            self.dEdx = 2 # MeV g^-1 cm^-2
            self.pdg = 13
        else:
            self.dEdx = 1 # I don't know
            self.pdg = -1
        
        self.segment = np.empty(1, dtype = segments_dtype)
        self.trajectory = np.empty(1, dtype = trajectories_dtype)
        self.vertex = np.empty(1, dtype = vertices_dtype)

        self.pop_segment()
        self.pop_trajectory()
        self.pop_vertex()

    def pop_segment(self):
        self.segment[0]["segment_id"] = 0
        self.segment[0]["trackID"] = 0
        self.segment[0]["x_start"] = self.vertexPos[0]
        self.segment[0]["y_start"] = self.vertexPos[1]
        self.segment[0]["z_start"] = self.vertexPos[2]
        self.segment[0]["t0_start"] = 0 
        self.segment[0]["t_start"] = 0
        self.segment[0]["x_end"] = self.vertexPos[0] + self.direction[0]*self.length
        self.segment[0]["y_end"] = self.vertexPos[1] + self.direction[1]*self.length
        self.segment[0]["z_end"] = self.vertexPos[2] + self.direction[2]*self.length
        self.segment[0]["t0_end"] = 0
        self.segment[0]["t_end"] = 0
        self.segment[0]["dE"] = self.dEdx*self.length
        xd = self.segment[0]["x_end"] - self.segment[0]["x_start"]
        yd = self.segment[0]["y_end"] - self.segment[0]["y_start"]
        zd = self.segment[0]["z_end"] - self.segment[0]["z_start"]
        dx = sqrt(xd**2 + yd**2 + zd**2)
        self.segment[0]["dx"] = dx
        self.segment[0]["x"] = (self.segment[0]["x_start"] + self.segment[0]["x_end"]) / 2.
        self.segment[0]["y"] = (self.segment[0]["y_start"] + self.segment[0]["y_end"]) / 2.
        self.segment[0]["z"] = (self.segment[0]["z_start"] + self.segment[0]["z_end"]) / 2.
        self.segment[0]["t0"] = (self.segment[0]["t0_start"] + self.segment[0]["t0_end"]) / 2.
        self.segment[0]["t"] = 0
        self.segment[0]["dEdx"] = self.dEdx
        self.segment[0]["pdgId"] = self.pdg
        self.segment[0]["n_electrons"] = 0
        self.segment[0]["long_diff"] = 0
        self.segment[0]["tran_diff"] = 0
        self.segment[0]["pixel_plane"] = 0
        self.segment[0]["n_photons"] = 0

    def pop_trajectory(self):
        self.trajectory[0]["eventID"] = 0
        self.trajectory[0]["trackID"] = 0
        self.trajectory[0]["parentID"] = 0
        self.trajectory[0]["pxyz_start"] = (0, 0, 0)
        self.trajectory[0]["pxyz_end"] = (0, 0, 0)
        self.trajectory[0]["xyz_start"] = self.vertexPos
        self.trajectory[0]["xyz_end"] = self.vertexPos
        self.trajectory[0]["t_start"] = 0
        self.trajectory[0]["t_end"] = 0
        self.trajectory[0]["start_process"] = 0
        self.trajectory[0]["start_subprocess"] = 0
        self.trajectory[0]["end_process"] = 0
        self.trajectory[0]["end_subprocess"] = 0
        self.trajectory[0]["pdgId"] = self.pdg
        
    def pop_vertex(self):
        self.vertex["eventID"] = 0
        self.vertex["x_vert"] = self.vertexPos[0]
        self.vertex["y_vert"] = self.vertexPos[1]
        self.vertex["z_vert"] = self.vertexPos[2]
