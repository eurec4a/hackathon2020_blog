# -*- coding: utf-8 -*-
"""Statistical functions for binary cloud masks. """
import numpy as np
import scipy as sc

from skimage import measure
from scipy.spatial.distance import pdist


__all__ = [
    "filter_cloudmask",
    "cloudfraction",
    "get_cloudproperties",
    "neighbor_distance",
    "iorg",
    "get_binsize",
    "linfit2",
]


def filter_cloudmask(cloudmask, threshold=1, connectivity=1):
    """Filter a given cloudmask for small cloud objects defined by their pixel
    number. 
    
    Parameters:
        cloudmask (ndarray): 2d binary cloud mask (optional with NaNs).
        threshold (int): minimum pixel number of objects remaining in cloudmask.
        connectivity (int):  Maximum number of orthogonal hops to consider
            a pixel/voxel as a neighbor (see :func:`skimage.measure.label`).
    
    Return:
        ndarray: filtered cloudmask without NaNs.
    """
    cloudmask[np.isnan(cloudmask)] = 0
    labels = measure.label(cloudmask, connectivity=connectivity)
    props = measure.regionprops(labels)
    area = [prop.area for prop in props]

    # Find objects < threshold pixle number, get their labels, set them to 0-clear.
    smallclouds = [t[0] for t in filter(lambda a: a[1] < threshold, enumerate(area, 1))]
    for label in smallclouds:
        cloudmask[labels == label] = 0

    return cloudmask


def cloudfraction(cloudmask):
    """Calculate cloud fraction based on cloud mask, while irnoring NaNs.
    
    Parameters:
        cloudmask (ndarray): 2d binary cloud mask.
        
    Returns:
        float: cloud fraction.
    """
    return np.nansum(cloudmask) / np.sum(~np.isnan(cloudmask))


def get_cloudproperties(cloudmask, connectivity=1):
    """Calculate basic cloud properties from binary cloudmask.
    Note:
        All parameters are calculated in pixels!!
    See also:
        :func:`skimage.measure.label`:
            Used to find different clouds. 
        :func:`skimage.measure.regionprops`:
            Used to calculate cloud properties.
    Parameters:
        cloudmask (ndarray): 2d binary cloud mask.
        connectivity (int):  Maximum number of orthogonal hops to consider
            a pixel/voxel as a neighbor (see :func:`skimage.measure.label`).
    Returns:
        list:
            List of :class:`RegionProperties`
            (see :func:`skimage.measure.regionprops`)
    """
    cloudmask[np.isnan(cloudmask)] = 0

    labels = measure.label(cloudmask, connectivity=connectivity)

    return measure.regionprops(labels)


def neighbor_distance(cloudmask, connectivity=1):
    """Calculate nearest neighbor distance for each cloud.
    Note: 
        Distance is given in pixels.
    See also: 
        :class:`scipy.spatial.cKDTree`:
            Used to calculate nearest neighbor distances. 
    Parameters: 
        cloudmask (ndarray): 2d binary cloud mask.
        connectivity (int):  Maximum number of orthogonal hops to consider
            a pixel/voxel as a neighbor (see :func:`skimage.measure.label`).
    Returns: 
        ndarray: Nearest neighbor distances in pixels.
    """
    cloudproperties = get_cloudproperties(cloudmask, connectivity=connectivity)

    centroids = [prop.centroid for prop in cloudproperties]
    indices = np.arange(len(centroids))
    neighbor_distance = np.zeros(len(centroids))
    centroids_array = np.asarray(centroids)

    for n, point in enumerate(centroids):
        # use all center of mass coordinates, but the one from the point
        mytree = sc.spatial.cKDTree(centroids_array[indices != n])
        dist, indexes = mytree.query(point)
        neighbor_distance[n] = dist

    return neighbor_distance


def iorg(cloudmask, connectivity=1):
    """Calculate the cloud cluster index 'I_org'.
    See also: 
        :func:`scipy.integrate.trapz`:
            Used to calculate the integral along the given axis using
            the composite trapezoidal rule.
    Parameters: 
        cloudmask (ndarray): 2d binary cloud mask.
        connectivity (int):  Maximum number of orthogonal hops to consider
            a pixel/voxel as a neighbor (see :func:`skimage.measure.label`).
    Returns:
        float: cloud cluster index I_org.
    References: 
        Tompkins, A. M., and A. G. Semie (2017), Organization of tropical 
        convection in low vertical wind shears: Role of updraft entrainment, 
        J. Adv. Model. Earth Syst., 9, 1046–1068, doi: 10.1002/2016MS000802.
        
    """
    nn = neighbor_distance(cloudmask, connectivity=connectivity)
    nn_sorted = np.sort(nn)

    nncdf = np.linspace(0, 1, len(nn))

    # theoretical nearest neighbor cumulative frequency
    # distribution (nncdf) of a random point process (Poisson)
    lamb = nn.size / cloudmask.size
    nncdf_poisson = 1 - np.exp(-lamb * np.pi * nn_sorted ** 2)

    return sc.integrate.trapz(y=nncdf, x=nncdf_poisson)


def get_binsize(array):
    ''' optimal binsize calculated according to the Scott's rule [Scott, 2010]
    bin width according to Scott's rule: w = 3.49 * sigma * N**(-1/3) 
    e.g. for dx=0.015² is w=0.07458016 [km²] (corresponds to eqd = 308m)
    sigma:      standard deviation
    N:          total number of samples
    '''
    return 3.49 * np.std(array) * len(array)**(-1/3)


def linfit2(x, a, b, c, d):
    '''Fit piecewise linear function to a distribution. Return value depends on the distribution and can either be maximum or minimum!'''
    left = a * x + b
    right = c * x + d    
    
    return np.minimum(left, right)