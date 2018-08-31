"""
Python model "teacup.py"
Translated using PySD version 0.9.0
"""
from __future__ import division
import numpy as np
from pysd import utils
import xarray as xr

from pysd.py_backend.functions import cache
from pysd.py_backend import functions

_subscript_dict = {}

_namespace = {
    u'INITIAL TIME': u'initial_time',
    u'Characteristic Time': u'characteristic_time',
    u'Heat Loss to Room': u'heat_loss_to_room',
    'TIME': 'time',
    u'SAVEPER': u'saveper',
    u'FINAL TIME': u'final_time',
    u'Room Temperature': u'room_temperature',
    u'Teacup Temperature': u'teacup_temperature',
    'Time': 'time',
    u'TIME STEP': u'time_step'
}

__pysd_version__ = "0.9.0"


@cache('step')
def teacup_temperature():
    """
    Real Name: Teacup Temperature
    Original Eqn: INTEG ( -Heat Loss to Room, 180)
    Units: Degrees
    Limits: (None, None)
    Type: component


    """
    return integ_teacup_temperature()


@cache('run')
def final_time():
    """
    Real Name: FINAL TIME
    Original Eqn: 30
    Units: Minute
    Limits: (None, None)
    Type: constant

    The final time for the simulation.
    """
    return 30


integ_teacup_temperature = functions.Integ(lambda: -heat_loss_to_room(), lambda: 180)


@cache('run')
def room_temperature():
    """
    Real Name: Room Temperature
    Original Eqn: 70
    Units: 
    Limits: (None, None)
    Type: constant


    """
    return 70


@cache('step')
def heat_loss_to_room():
    """
    Real Name: Heat Loss to Room
    Original Eqn: (Teacup Temperature - Room Temperature) / Characteristic Time
    Units: Degrees/Minute
    Limits: (None, None)
    Type: component

    This is the rate at which heat flows from the cup into the room. We can \n    \t\tignore it at this point.
    """
    return (teacup_temperature() - room_temperature()) / characteristic_time()


@cache('run')
def characteristic_time():
    """
    Real Name: Characteristic Time
    Original Eqn: 10
    Units: Minutes
    Limits: (None, None)
    Type: constant


    """
    return 10


@cache('step')
def saveper():
    """
    Real Name: SAVEPER
    Original Eqn: TIME STEP
    Units: Minute
    Limits: (0.0, None)
    Type: component

    The frequency with which output is stored.
    """
    return time_step()


@cache('run')
def initial_time():
    """
    Real Name: INITIAL TIME
    Original Eqn: 0
    Units: Minute
    Limits: (None, None)
    Type: constant

    The initial time for the simulation.
    """
    return 0


@cache('run')
def time_step():
    """
    Real Name: TIME STEP
    Original Eqn: 0.125
    Units: Minute
    Limits: (0.0, None)
    Type: constant

    The time step for the simulation.
    """
    return 0.125
