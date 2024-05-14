"""
oevt_python.py
OpenExVis translator for Python.
Copyright (C) 2005 Tero Kuusela
"""

import bdb

import oev_dis
import visualizer

class OevTranslator(bdb.Bdb):
    """Translate Python code to OpenExVis visualization data."""

    def __init__(self, visualizer):
        bdb.Bdb.__init__(self)
        # The OpenExVis visualizer we interact with, given from the UI.
        self.vis = visualizer

    ##
    # Override the user_* methods from bdb to control the flow. We only care of
    # the lines.
    ##

    #def user_call(self, frame, arg):
    #    pass

    def user_line(self, frame):
        """Send visualization data of an executed line to the visualizer.

        For each line we execute, we call the vis_step() method of the
        visualizer, giving it the information it needs, which is received
        from mydis.

        """
        visdata = oev_dis.disassemble(frame.f_code, frame.f_lineno)
        print "\nDEBUG: In user_line we have:\n",visdata
        self.vis.vis_step(visdata)
        return self.trace_dispatch

    #def user_return(self, frame, arg):
    #    pass

    #def user_exception(self, frame, arg):
    #    pass

    def translate(self, code):
        """Translate Python code to OpenExVis visualization data.

        Start with fresh empty copy of globals and locals and tell the script
        that it's being run as __main__ to avoid scripts being able to access
        the oevt_python.py namespace.

        The Python code to translate is given as a string, which is compiled
        and then executed via bdb's run() method.

        """
        globals_ = {"__name__" : "__main__"}
        locals_ = globals_
        statement = compile(code, "", 'exec')
        self.run(statement, globals=globals_, locals=locals_)
