import ROOT

f  = ROOT.TFile.Open("/home/snabili/Bsvj/June/June9/BKGSIG/L2/ROOT/SIG_m250r0p3mDark20_L2truthJets_06212021.root")
f1 = ROOT.TFile.Open("/home/snabili/Bsvj/June/June9/BKGSIG/L2/ROOT/BKG_QCD-Highstat_L2Jets_06092021_300to470.root")

output_file = ROOT.TFile.Open("outputfile_secondbin_weight.root", 'recreate')

tb_300to470   = f1.Get("jetb")
ts	      = f.Get("jets")

nsignal_entries     = ts.GetEntries()
n300to470_entries   = tb_300to470.GetEntries()

h_300to470_pt	 = ROOT.TH1F("h_300to470_pt", 	"AK152LJets Pt 300to470", 	100, 0, 2400)
h_300to470_girth = ROOT.TH1F("h_300to470_girth","AK152LJets girth 300to470",    100, 0, 1.20)
h_sig_pt 	 = ROOT.TH1F("h_sig_pt",	"AK152LJets Pt signal",		100, 0, 2400)
h_sig_girth      = ROOT.TH1F("h_sig_girth",     "AK152LJets girth signal",      100, 0, 1.20)
h_300to470_pt_norm    = ROOT.TH1F("h_300to470_pt_norm",   "AK152LJets Pt 300to470 normalized",       100, 0, 2400)
h_300to470_girth_norm = ROOT.TH1F("h_300to470_girth_norm","AK152LJets girth 300to470 normalized",    100, 0, 1.20)
h_sig_pt_norm         = ROOT.TH1F("h_sig_pt_norm",        "AK152LJets Pt signal normalized",         100, 0, 2400)
h_sig_girth_norm      = ROOT.TH1F("h_sig_girth_norm",     "AK152LJets girth signal normalized",      100, 0, 1.20)

for i_event in range(nsignal_entries):
    ts.GetEntry(i_event)
    h_sig_pt.Fill(ts.L2_pt)
    h_sig_girth.Fill(ts.L2_girth)
    h_sig_pt_norm.Fill(ts.L2_pt)
    h_sig_girth_norm.Fill(ts.L2_girth)
print("signal is done")
print("****************************")

for i_event in range(n300to470_entries):
    tb_300to470.GetEntry(i_event)
    h_300to470_pt.Fill(tb_300to470.L2_pt)
    h_300to470_girth.Fill(tb_300to470.L2_girth)
    h_300to470_pt_norm.Fill(tb_300to470.L2_pt)
    h_300to470_girth_norm.Fill(tb_300to470.L2_girth)
print("300to470 is done")
print("****************************")

h_sig_pt_norm.Scale(1.0/h_sig_pt_norm.Integral(0,h_sig_pt_norm.GetNbinsX()+1))
h_300to470_pt_norm.Scale(1.0/h_300to470_pt_norm.Integral(0,h_300to470_pt_norm.GetNbinsX()+1))
h_sig_girth_norm.Scale(1.0/h_sig_girth_norm.Integral(0,h_sig_girth_norm.GetNbinsX()+1))
h_300to470_girth_norm.Scale(1.0/h_300to470_girth_norm.Integral(0,h_300to470_girth_norm.GetNbinsX()+1))

h_300to470_pt.Divide(h_sig_pt)
h_300to470_girth.Divide(h_sig_girth)
h_300to470_pt_norm.Divide(h_sig_pt_norm)
h_300to470_girth_norm.Divide(h_sig_girth_norm)
output_file.Write()
output_file.Close()
