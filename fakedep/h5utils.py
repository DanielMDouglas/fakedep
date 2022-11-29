import h5py

from .dtypes import *

def initHDF5File(fileName):
    with h5py.File(fileName, 'w') as f:
        f.create_dataset('segments', (0,),
                         dtype = segments_dtype,
                         maxshape = (None,)) 
        f.create_dataset('trajectories', (0,),
                         dtype = trajectories_dtype,
                         maxshape = (None,)) 
        f.create_dataset('vertices', (0,),
                         dtype = vertices_dtype,
                         maxshape = (None,)) 

def updateHDF5File(fileName, segments, trajectories, vertices):
    if any([len(segments), len(trajectories), len(vertices)]):
        with h5py.File(fileName, 'a') as f:
            if len(segments):
                nseg = len(f['segments'])
                f['segments'].resize((nseg+len(segments),))
                f['segments'][nseg:] = segments

            if len(trajectories):
                nseg = len(f['trajectories'])
                f['trajectories'].resize((nseg+len(trajectories),))
                f['trajectories'][nseg:] = trajectories

            if len(vertices):
                nseg = len(f['vertices'])
                f['vertices'].resize((nseg+len(vertices),))
                f['vertices'][nseg:] = vertices
