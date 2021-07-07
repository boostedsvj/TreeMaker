import ROOT
import math
from ROOT import TFile, TTree, TH1F
from ROOT import TLorentzVector
from array import array
from math import *

hf_300to470 = ROOT.TFile.Open("outputfile_firstbin_weight.root")#weighted to signal samples 2LJetPt
histo_300to470_pt	  = hf_300to470.Get("h_300to470_pt")
histo_300to470_girth 	  = hf_300to470.Get("h_300to470_girth")
histo_300to470_pt_norm    = hf_300to470.Get("h_300to470_pt_norm")
histo_300to470_girth_norm = hf_300to470.Get("h_300to470_girth_norm")


tf_300to470 = ROOT.TFile.Open("/home/snabili/Bsvj/QCD/HighStat_May05-2021/ROOT/300to470.root")
tb_300to470   = tf_300to470.Get("PreSelection")

n300to470_entries   = tb_300to470.GetEntries()

f = ROOT.TFile.Open("BKG_QCD-Highstat_L2Jets_07062021_300to470_jetptgirthreweight.root", 'recreate')
Jet_bkg     = TTree("jetb", "jetb")
weight_pt   = array('d', [0])
weight_girth= array('d', [0])
weight_pt_norm    = array('d', [0])
weight_girth_norm = array('d', [0])
weight_xsec = array('d', [0])
L2_pt       = array('d', [0])
Jet_bkg.Branch("L2_pt",       L2_pt,       'L2_pt/D')
Jet_bkg.Branch("weight_pt",   weight_pt,   'weight_pt/D')
Jet_bkg.Branch("weight_girth", weight_girth, 'weight_girth/D')
Jet_bkg.Branch("weight_pt_norm",   weight_pt_norm,   'weight_pt_norm/D')
Jet_bkg.Branch("weight_girth_norm", weight_girth_norm, 'weight_girth_norm/D')
Jet_bkg.Branch("weight_xsec", weight_xsec, 'weight_xsec/D')
weight                          = array('d', [0])
JetPt                           = array('d', [0])
MET                             = array('d', [0])
z_pt                            = array('d', [0])
qvaqv_dR                        = array('d', [0])
Jet_bkg.Branch("weight",                             weight,                      'weight/D')
Jet_bkg.Branch("JetPt",                              JetPt,                       'JetPt/D')
Jet_bkg.Branch("MET",                                MET,                         'MET/D')
Jet_bkg.Branch("z_pt",                               z_pt,                        'z_pt/D')
Jet_bkg.Branch("qvaqv_dR",                           qvaqv_dR,                    'qvaqv_dR/D')

L2_MT                           = array('d', [0])
L2_M                            = array('d', [0])
L2_eta                          = array('d', [0])
L2_phi                          = array('d', [0])
L2_RTone                        = array('d', [0])
L2_girth                        = array('d', [0])
L2_ptD                          = array('d', [0])
L2_axismajor                    = array('d', [0])
L2_axisminor                    = array('d', [0])
L2_ecfN2b1                      = array('d', [0])
L2_ecfN2b2                      = array('d', [0])
L2_ecfM2b1                      = array('d', [0])
L2_ecfM2b2                      = array('d', [0])
L2_ecfC2b1                      = array('d', [0])
L2_ecfC2b2                      = array('d', [0])
L2_ecfD2b1                      = array('d', [0])
L2_ecfD2b2                      = array('d', [0])
L2_1e3                          = array('d', [0])
L2_e2                           = array('d', [0])
L2_eta                          = array('d', [0])
L2_phi                          = array('d', [0])
L2_e                            = array('d', [0])
L2_JetMET_dphi                  = array('d', [0])
L2_pt_sum_stabledarkmeson       = array('d', [0])
L2_pt_vecsum_stabledarkmeson    = array('d', [0])
L2_count_stabledarkmeson        = array('d', [0])
L2_qvjet_dR                     = array('d', [0])
L2_aqvjet_dR                    = array('d', [0])
L2_zpjet_dR                     = array('d', [0])
L2_tau21                        = array('d', [0])
L2_multiplicity                 = array('d', [0])
L2_chargedmultiplicity          = array('d', [0])
L2_neutralmultiplicity          = array('d', [0])
L2_NumChadrons                  = array('d', [0])
L2_NumBhadrons                  = array('d', [0])
L2_AK4Jets_partonflavor         = array('d', [0])
Jet_bkg.Branch("L2_MT",                                 L2_MT,                          'L2_MT/D')
Jet_bkg.Branch("L2_M",                                  L2_M,                           'L2_M/D')
Jet_bkg.Branch("L2_pt",                                 L2_pt,                          'L2_pt/D')
Jet_bkg.Branch("L2_RTone",                              L2_RTone,                       'L2_RTone/D')
Jet_bkg.Branch("L2_girth",                              L2_girth,                       'L2_girth/D')
Jet_bkg.Branch("L2_ptD",                                L2_ptD,                         'L2_ptD/D')
Jet_bkg.Branch("L2_axismajor",                          L2_axismajor,                   'L2_axismajor/D')
Jet_bkg.Branch("L2_axisminor",                          L2_axisminor,                   'L2_axisminor/D')
Jet_bkg.Branch("L2_ecfN2b1",                            L2_ecfN2b1,                     'L2_ecfN2b1/D')
Jet_bkg.Branch("L2_ecfN2b2",                            L2_ecfN2b2,                     'L2_ecfN2b2/D')
Jet_bkg.Branch("L2_ecfM2b1",                            L2_ecfM2b1,                     'L2_ecfM2b1/D')
Jet_bkg.Branch("L2_ecfM2b2",                            L2_ecfM2b2,                     'L2_ecfM2b2/D')
Jet_bkg.Branch("L2_ecfC2b1",                            L2_ecfC2b1,                     'L2_ecfC2b1/D')
Jet_bkg.Branch("L2_ecfC2b2",                            L2_ecfC2b2,                     'L2_ecfC2b2/D')
Jet_bkg.Branch("L2_ecfD2b1",                            L2_ecfD2b1,                     'L2_ecfD2b1/D')
Jet_bkg.Branch("L2_ecfD2b2",                            L2_ecfD2b2,                     'L2_ecfD2b2/D')
Jet_bkg.Branch("L2_eta",                                L2_eta,                         'L2_eta/D')
Jet_bkg.Branch("L2_phi",                                L2_phi,                         'L2_phi/D')
Jet_bkg.Branch("L2_e",                                  L2_e,                           'L2_e/D')
Jet_bkg.Branch("L2_JetMET_dphi",                        L2_JetMET_dphi,                 'L2_JetMET_dphi/D')
Jet_bkg.Branch("L2_1e3",                                L2_1e3,                         'L2_1e3/D')
Jet_bkg.Branch("L2_e2",                                 L2_e2,                          'L2_e2/D')
Jet_bkg.Branch("L2_pt_sum_stabledarkmeson",             L2_pt_sum_stabledarkmeson,      'L2_pt_sum_stabledarkmeson/D')
Jet_bkg.Branch("L2_pt_vecsum_stabledarkmeson",          L2_pt_vecsum_stabledarkmeson,   'L2_pt_vecsum_stabledarkmeson/D')
Jet_bkg.Branch("L2_count_stabledarkmeson",              L2_count_stabledarkmeson,       'L2_count_stabledarkmeson/D')
Jet_bkg.Branch("L2_qvjet_dR",                           L2_qvjet_dR,                    'L2_qvjet_dR/D')
Jet_bkg.Branch("L2_aqvjet_dR",                          L2_aqvjet_dR,                   'L2_aqvjet_dR/D')
Jet_bkg.Branch("L2_zpjet_dR",                           L2_zpjet_dR,                    'L2_zpjet_dR/D')
Jet_bkg.Branch("L2_tau21",                              L2_tau21,                       'L2_tau21/D')
Jet_bkg.Branch("L2_multiplicity",                       L2_multiplicity,                'L2_multiplicity/D')
Jet_bkg.Branch("L2_chargedmultiplicity",                L2_chargedmultiplicity,         'L2_chargedmultiplicity/D')
Jet_bkg.Branch("L2_neutralmultiplicity",                L2_neutralmultiplicity,         'L2_neutralmultiplicity/D')
Jet_bkg.Branch("L2_NumChadrons",                        L2_NumChadrons,                 'L2_NumChadrons/D')
Jet_bkg.Branch("L2_NumBhadrons",                        L2_NumBhadrons,                 'L2_NumBhadrons/D')
Jet_bkg.Branch("L2_AK4Jets_partonflavor",               L2_AK4Jets_partonflavor,        'L2_AK4Jets_partonflavor/D')
def delta(a,b):
    dphi = abs(a-b);
    if dphi > pi: dphi = 2*pi-dphi
    return dphi


for i_event in range(n300to470_entries):
    tb_300to470.GetEntry(i_event)
    if tb_300to470.JetsAK8.size()<1 or tb_300to470.JetsAK15.size()<2: continue
    #if i_event > 10000: break
    #print i_event
    '''dR_ak4ak15subjet = 100.0
    for ak4 in range(tb_300to470.Jets.size()): # this is to check the gluon and quark like jets
      dR_ak4ak15subjet = ((tb_300to470.Jets[ak4].eta()-tb_300to470.JetsAK15[1].Eta())**2+(tb_300to470.Jets[ak4].phi()-tb_300to470.JetsAK15[1].Phi())**2)**0.5
      if dR_ak4ak15subjet < 1.5:
        L2_AK4Jets_partonflavor[0] = tb_300to470.Jets_partonFlavor[ak4]'''
    dR_ak4ak15subjet_min = 100.0
    AK4 = 1000
    for ak4 in range(tb_300to470.Jets.size()): # this is to check the gluon and quark like jets
      dR_ak4ak15subjet = ((tb_300to470.Jets[ak4].eta()-tb_300to470.JetsAK15[1].Eta())**2+(tb_300to470.Jets[ak4].phi()-tb_300to470.JetsAK15[1].Phi())**2)**0.5
      if dR_ak4ak15subjet_min>dR_ak4ak15subjet:
        dR_ak4ak15subjet_min = dR_ak4ak15subjet
        AK4 = ak4
    L2_AK4Jets_partonflavor[0] = tb_300to470.Jets_partonFlavor[AK4]
    JetPt[0] = tb_300to470.JetsAK8[0].Pt()
    L2_pt[0] = tb_300to470.JetsAK15[1].Pt()
    weight_pt[0] = histo_300to470_pt.GetBinContent(histo_300to470_pt.FindBin(tb_300to470.JetsAK15[1].Pt()))
    weight_girth[0] = histo_300to470_girth.GetBinContent(histo_300to470_girth.FindBin(tb_300to470.JetsAK15_girth[1]))
    weight_pt_norm[0] = histo_300to470_pt_norm.GetBinContent(histo_300to470_pt_norm.FindBin(tb_300to470.JetsAK15[1].Pt()))
    weight_girth_norm[0] = histo_300to470_girth_norm.GetBinContent(histo_300to470_girth_norm.FindBin(tb_300to470.JetsAK15_girth[1]))
    weight_xsec[0] = tb_300to470.weighted_samples
    weight[0] = tb_300to470.weighted_samples* histo_300to470_pt.GetBinContent(histo_300to470_pt.FindBin(tb_300to470.JetsAK15[1].Pt()))
    MET[0] = tb_300to470.MET
    z_pt[0] = 0.0
    qvaqv_dR[0] = 0.0
    L2_qvjet_dR[0] = 0.0
    L2_aqvjet_dR[0] = 0.0
    L2_zpjet_dR[0] = 0.0
    L2_M[0] = tb_300to470.JetsAK15[1].M()
    L2_MT[0] = sqrt(tb_300to470.JetsAK15[1].M()**2+2*(sqrt(tb_300to470.JetsAK15[1].M()**2+tb_300to470.JetsAK15[1].Pt()**2)*tb_300to470.MET-tb_300to470.JetsAK15[1].Pt()*tb_300to470.MET*cos(delta(tb_300to470.METPhi,tb_300to470.JetsAK15[1].Phi()))))
    L2_JetMET_dphi[0] = delta(tb_300to470.METPhi,tb_300to470.JetsAK15[1].Phi())
    L2_RTone[0] = sqrt(1+tb_300to470.MET/tb_300to470.JetsAK15[1].Pt())
    L2_girth[0] = tb_300to470.JetsAK15_girth[1]
    L2_ptD[0] = tb_300to470.JetsAK15_ptD[1]
    L2_axismajor[0] = tb_300to470.JetsAK15_axismajor[1]
    L2_axisminor[0] = tb_300to470.JetsAK15_axisminor[1]
    L2_ecfN2b1[0] = tb_300to470.JetsAK15_ecfN2b1[1]
    L2_ecfN2b2[0] = tb_300to470.JetsAK15_ecfN2b2[1]
    L2_ecfM2b1[0] = tb_300to470.JetsAK15_ecfM2b1[1]
    L2_ecfM2b2[0] = tb_300to470.JetsAK15_ecfM2b2[1]
    L2_ecfC2b1[0] = tb_300to470.JetsAK15_ecfC2b1[1]
    L2_ecfC2b2[0] = tb_300to470.JetsAK15_ecfC2b2[1]
    L2_ecfD2b1[0] = tb_300to470.JetsAK15_ecfD2b1[1]
    L2_ecfD2b2[0] = tb_300to470.JetsAK15_ecfD2b2[1]
    L2_eta[0] = tb_300to470.JetsAK15[1].Eta()
    L2_phi[0] = tb_300to470.JetsAK15[1].Phi()
    L2_e[0] = tb_300to470.JetsAK15[1].E()
    L2_1e3[0] = tb_300to470.JetsAK15_ecfM2b1[1]*tb_300to470.JetsAK15_ecfC2b1[1]/tb_300to470.JetsAK15_ecfD2b1[1]
    L2_e2[0] = tb_300to470.JetsAK15_ecfC2b1[1]/tb_300to470.JetsAK15_ecfD2b1[1]
    L2_count_stabledarkmeson[0]   = 0.0
    L2_pt_sum_stabledarkmeson[0]  = 0.0
    L2_pt_vecsum_stabledarkmeson[0]  = 0.0
    L2_tau21[0] = tb_300to470.JetsAK15_NsubjettinessTau2[1]/tb_300to470.JetsAK15_NsubjettinessTau1[1]
    L2_multiplicity[0] = tb_300to470.JetsAK15_multiplicity[1]
    L2_chargedmultiplicity[0] = tb_300to470.JetsAK15_chargedMultiplicity[1]
    L2_neutralmultiplicity[0] = tb_300to470.JetsAK15_neutralMultiplicity[1]
    L2_NumChadrons[0] = tb_300to470.JetsAK15_NumChadrons[1]
    L2_NumBhadrons[0] = tb_300to470.JetsAK15_NumBhadrons[1]
    Jet_bkg.Fill()
print("300to470 is done")

print("****************************")
f.Write()
f.Close()
