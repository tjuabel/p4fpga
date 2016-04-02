'''
Control flow with bsv backend
'''

import logging
from pif_ir.bir.objects.control_flow import ControlFlow
from bsvgen_control_state import BSVControlState

from pif_ir.bir.utils.validate import check_control_state

class BSVControlFlow(ControlFlow):
    '''
    TODO
    '''
    def __init__(self, name, control_flow_attrs, basic_blocks, bir_parser):
        super(BSVControlFlow, self).__init__(name, control_flow_attrs,
                                             basic_blocks, bir_parser)
        cf = control_flow_attrs['start_control_state']
        check_control_state(self.name, cf)
        self.control_state = BSVControlState(cf, None, bir_parser)

    def bsvgen(self):
        ''' TODO '''
        offset, basic_block = self.control_state.bsvgen()
        while basic_block:
            logging.info("PROCESS: {}.{}".format(self.name, basic_block))
            print 'mmm', offset, basic_block
            print 'mmm', self.basic_blocks[basic_block]
            offset, basic_block = self.basic_blocks[basic_block].bsvgen()

        #self.next_processor.bsvgen()