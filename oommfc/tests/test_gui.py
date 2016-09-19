 import oommfc.gui
import ipywidgets as widgets

# The following section is from the source of IPywidgets, and 
# is used to instantiate a dummy communicator, which allows the widgets
# to instantiate, as normally they require an active IPython Kernel.

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License. 

from ipykernel.comm import Comm
from traitlets import TraitError
from ipywidgets import interact, interactive, Widget, interaction, Output
from ipython_genutils.py3compat import annotate

class DummyComm(Comm):
    comm_id = 'a-b-c-d'

    def open(self, *args, **kwargs):
        pass

    def send(self, *args, **kwargs):
        pass

    def close(self, *args, **kwargs):
        pass

_widget_attrs = {}
displayed = []
undefined = object()

def setup():
    _widget_attrs['_comm_default'] = getattr(Widget, '_comm_default', undefined)
    Widget._comm_default = lambda self: DummyComm()
    _widget_attrs['_ipython_display_'] = Widget._ipython_display_
    def raise_not_implemented(*args, **kwargs):
        raise NotImplementedError()
    Widget._ipython_display_ = raise_not_implemented

def teardown():
    for attr, value in _widget_attrs.items():
        if value is undefined:
            delattr(Widget, attr)
        else:
            setattr(Widget, attr, value)

def f(**kwargs):
    pass

def clear_display():
    global displayed
    displayed = []

def record_display(*args):
    displayed.extend(args)

#### End Jupyter Stuff from ipywidgets source


def test_dictionary_assemble():
	setup() # Instantiate kernel
	w = oommfc.gui._widget() # Instantiate widget
	w.update_dictionary()
	assert w.dict['Lx'] == 10
	assert w.dict['Ly'] == 1
	assert w.dict['Lz'] == 1
	assert w.dict['Ms'] == 800000.0
	assert w.dict['anisotropy_axis'] == ()
	assert w.dict['anisotropy_constant_K1'] == 1.3e-11
	assert w.dict['demagnetisation_enabled'] == False
	assert w.dict['dimension'] == 1
	assert w.dict['domain_wall_width'] == 10.0
	assert w.dict['dt'] == 1e-09
	assert w.dict['dx'] == 1.0
	assert w.dict['dy'] == 1.0
	assert w.dict['dz'] == 1.0
	assert w.dict['exchange_constant'] == 1.3e-11
	assert w.dict['exchange_enabled'] == True
	assert w.dict['initial_magnetisation'] == 'Uniform'
	assert w.dict['maxsteps'] == 0
	assert w.dict['mx'] == 0.0
	assert w.dict['my'] == 0.0
	assert w.dict['mz'] == 0.0
	assert w.dict['periodic_x'] == False
	assert w.dict['periodic_y'] == False
	assert w.dict['periodic_z'] == False
	assert w.dict['rununtil'] == 1e-08
	assert w.dict['saveevery'] == 100
	assert w.dict['scale'] == 1e-09
	assert w.dict['simtype'] == 'Relax'
	assert w.dict['skyrmion_vortex_radius'] == 10.0
	assert w.dict['stopping_mxHxm'] == 0.01
	assert w.dict['uniaxial_anisotropy_enabled'] == False
