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

class myHS2PS(PostProcessorInterfaceBase):
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
    self.inputFormat  = 'HistorySet'
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
    outputDic = {'data' : {}}
    outputDic['dims'] = {}

    for key2 in inputDic[0]['data'].keys():
      #print('DEBUG inputDic: ',inputDic[0]['data'][key2], type(inputDic[0]['data'][key2]))
      #print('DEBUG inputDic with [0]:   ',inputDic[0]['data'][key2][0], type(inputDic[0]['data'][key2][0]))
      outputDic['data'].update({key2 : inputDic[0]['data'][key2][0]})
      outputDic['dims'][key2] = []

    outputDic['data'].update({'kcTF' : outputDic['data']['avg_fg_temp'],
      'kcTM' : outputDic['data']['avg_ms_temp'],
      'kcTrefl' : outputDic['data']['avg_refltemp'],
      'kcTcore' : outputDic['data']['avg_coretemp']})
    outputDic['dims'].update({'kcTF' : [],
      'kcTM' : [],
      'kcTrefl' : [],
      'kcTcore' : []})

    #print('DEBUG outputDic: ',outputDic)
    #print("DEBUG outputDic['data']",outputDic['data'])

    return outputDic
