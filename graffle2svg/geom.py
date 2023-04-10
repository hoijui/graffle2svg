#!/usr/bin/env python3
# SPDX-License-Identifier: BSD-3-Clause

"""simple geometry functions"""

import math

def findcentre(pts):
    """Finds the centre of the points ( *not* Centre of Mass)"""
    xmax,ymax,xmin,ymin = pts[0] + pts[0]
    for x,y in pts:
        if xmax < x:
            xmax = x
        elif xmin > x:
            xmin = x
        if ymax < y:
            ymax = y
        elif ymin > y:
            ymin = y
    return 0.5*(xmax+xmin), 0.5*(ymax+ymin)


def h_flip_points(pts,centre=None):
    """Horizontal flip"""
    if centre is None:
        centre = findcentre(pts)
    xc,yc = centre
    outpts = []
    for (x,y) in pts:
        outpts.append([xc + (-1. * (x-xc)), y])
    return outpts


def v_flip_points(pts,centre=None):
    """Vertical flip"""
    if centre is None:
        centre = findcentre(pts)
    xc,yc = centre
    outpts = []
    for (x,y) in pts:
        outpts.append([x, yc + (-1 * (y-yc))])
    return outpts

def rotate_points(pts, angle=0, centre=None):
    if centre is None:
        centre = findcentre(pts)
    if round(angle % 360,7) == 0:
        return pts
    elif round(angle % 180,7) == 0:
        return h_flip_points (
                   v_flip_points(pts, centre),
                   centre)
    # in radians
    phi = (angle * math.pi * 2.) / 360.
    xc,yc = centre
    outpts = []
    cs = math.cos(phi)
    sn = math.sin(phi)
    # angle we're changing by
    for (x,y) in pts:
        # relative to centres
        relx,rely = x-xc, y-yc
        if (relx,rely) == (0.,0.):
            outpts.append(0.,0.)
            continue
        newx = xc + (cs*relx-sn*rely)
        newy = yc + (sn*relx+cs*rely)
        outpts.append( [newx,newy] )
    return outpts

def out_of_boundingbox(points,  boundingbox):
    ''' returns True if one of the points is out of selected boundingbox. If boundingbox is None, returns False'''
    if not boundingbox:
        return False
    for point in points:
        if ((point[0] - boundingbox[0][0]) * (point[0] - boundingbox[1][0])>0) or \
            ((point[1] - boundingbox[0][1]) * (point[1] - boundingbox[1][1])>0):
                return True
    return False
