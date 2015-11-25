# This is a small example how the crab api can easily be used to create something like multi crab.
# It has some additional features like also creating the xml files for you. 
# For it to work you need inputDatasets & requestNames apart from the classical part 
#
# Usage ./CrabConfig ConfigFile [options]
#
# Take care here to make the request names *nice*
# 
# autocomplete_Datasets(ListOfDatasets) works also for several entries with *
#
from DasQuery import autocomplete_Datasets

inputDatasets = ['/QCD_Pt-*to*_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM']
inputDatasets = autocomplete_Datasets(inputDatasets)
requestNames = []
for x in inputDatasets:
    name = x.split('/')[1]
    modified_name =name.replace('TuneCUETP8M1_13TeV-madgraph-pythia8','25ns')
    requestNames.append(modified_name)

# ===============================================================================
# Classical part of crab, after resolving the * it uses in the example below just the first entry
#

from CRABClient.UserUtilities import config, getUsernameFromSiteDB


config = config()
config.General.workArea = 'qcd_crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True
        
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '../../core/python/ntuplewriter.py'
config.JobType.outputFiles = ["Ntuple.root"]
config.JobType.inputFiles = ['../../core/python/Summer15_25nsV2_MC.db']
        
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/user/%s/QCD_20151125' % (getUsernameFromSiteDB())
config.Data.publication = False
#config.Data.allowNonValidInputDataset = True
#config.Data.publishDataName = 'CRAB3_tutorial_May2015_MC_analysis'

config.Site.storageSite = 'T2_DE_DESY'
config.Site.whitelist = ['T2_DE_DESY']

config.General.requestName = requestNames[0]
config.Data.inputDataset = inputDatasets[0]


