#for future compatibility with Python 3--------------------------------------------------------------
from __future__ import division, print_function, unicode_literals, absolute_import
import warnings
warnings.simplefilter('default',DeprecationWarning)
if not 'xrange' in dir(__builtins__):
  xrange = range
#End compatibility block for Python 3----------------------------------------------------------------

#External Modules------------------------------------------------------------------------------------
import os
import copy
import itertools
import numpy as np
#External Modules End--------------------------------------------------------------------------------

from PostProcessorInterfaceBaseClass import PostProcessorInterfaceBase

class funcrho(PostProcessorInterfaceBase):
  """
  Talk to Adam Z. about this.
  """

  def initialize(self):
    """
     Method to initialize the Interfaced Post-processor
     @ In, None,
     @ Out, None,

    """
    PostProcessorInterfaceBase.initialize(self)
    self.inputFormat  = 'PointSet'
    self.outputFormat = 'PointSet'

    self.pivotParameter       = None
    #pivotParameter identify the ID of the temporal variable in the data set; it is used so that in the
    #conversion the time array is not inserted since it is not needed (all histories have same length)
    self.features     = 'all'

  def readMoreXML(self,xmlNode):
    """
      Function that reads elements this post-processor will use
      @ In, xmlNode, ElementTree, Xml element node
      @ Out, None
    """
    return

  def run(self,inputDic):
    """
    This method performs the actual transformation of the data object from history set to point set
      @ In, inputDic, list, list of dictionaries which contains the data inside the input DataObjects
      @ Out, outputDic, dict, output dictionary
    """
    outputDic = {'data': {}}
    outputDic['dims'] = {}

    k_cent = inputDic[0]['data']['eigenvalue'][-1]
    drho_TF = inputDic[1]['data']['sens_rho_Tfgrn'][-1]
    drho_TM = inputDic[1]['data']['sens_rho_Tmoder'][-1]

    outputDic['data'] = {'kcent': np.array([k_cent]), 'dr_dTF': np.array([drho_TF]), 'dr_dTM': np.array(
      [drho_TM])}

    return outputDic
