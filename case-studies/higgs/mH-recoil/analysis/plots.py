import ROOT

flavor = "ee"
flavor_l = "#mu" if flavor == "mumu" else "e"


# global parameters
intLumi         = 1. # already scaled in histmaker
intLumiLabel    = "L = 7.2 ab^{-1}"
ana_tex         = f'e^{{+}}e^{{-}} #rightarrow ZH #rightarrow {flavor_l}^{{#plus}}{flavor_l}^{{#minus}} + X'
delphesVersion  = '3.4.2'
energy          = 240.0
collider        = 'FCC-ee'
inputDir        = f'output_{flavor}/'
formats         = ['png','pdf']
outdir          = f'plots_{flavor}/'
plotStatUnc     = False

colors = {}
colors['ZH']    = ROOT.kRed
colors['WW']    = ROOT.TColor.GetColor(248, 206, 104)
colors['ZZ']    = ROOT.TColor.GetColor(222, 90, 106)
colors['Zg']    = ROOT.TColor.GetColor(100, 192, 232)
colors['rare']  = ROOT.TColor.GetColor(155, 152, 204)


procs = {}
procs['signal'] =   {'ZH':[f'wzp6_ee_{flavor}H_ecm240']}
procs['backgrounds'] = {}
procs['backgrounds']['WW'] = ['p8_ee_WW_ecm240']
procs['backgrounds']['ZZ'] = ['p8_ee_ZZ_ecm240']
procs['backgrounds']['Zg'] = ['wzp6_ee_tautau_ecm240', 'wzp6_ee_mumu_ecm240' if flavor=="mumu" else 'wzp6_ee_ee_Mee_30_150_ecm240']
procs['backgrounds']['rare'] = [f'wzp6_egamma_eZ_Z{flavor}_ecm240', f'wzp6_gammae_eZ_Z{flavor}_ecm240', f'wzp6_gaga_{flavor}_60_ecm240', 'wzp6_gaga_tautau_60_ecm240', 'wzp6_ee_nuenueZ_ecm240']


legend = {}
legend['ZH']    = "ZH"
legend['WW']    = "W^{+}W^{#minus}"
legend['ZZ']    = "ZZ"
legend['Zg']    = "Z/#gamma^{*}"
legend['rare']  = "Rare"


hists = {}

hists["zll_recoil_m"] = {
    "output":   "zll_recoil_m",
    "logy":     False,
    "stack":    False,
    "rebin":    10,
    "xmin":     120,
    "xmax":     140,
    "xtitle":   "Recoil (GeV)",
    "ytitle":   "Events",
}

hists["zll_m"] = {
    "output":   "zll_m",
    "logy":     False,
    "stack":    True,
    "rebin":    1,
    "xmin":     86,
    "xmax":     96,
    "xtitle":   f"m({flavor_l}^{{#plus}}{flavor_l}^{{#minus}}) (GeV)",
    "ytitle":   "Events ",
}

hists["zll_p"] = {
    "output":   "zll_p",
    "logy":     False,
    "stack":    False,
    "rebin":    2,
    "xmin":     20,
    "xmax":     60,
    "xtitle":   f"p({flavor_l}^{{#plus}}{flavor_l}^{{#minus}}) (GeV)",
    "ytitle":   "Events ",
}

hists["cosThetaMiss"] = {
    "output":   "cosThetaMiss",
    "logy":     False,
    "stack":    False,
    "rebin":    50,
    "xmin":     0,
    "xmax":     1,
    "xtitle":   "cos(#theta_{miss})",
    "ytitle":   "Events ",
}


hists["cutFlow"] = {
    "output":   "cutFlow",
    "logy":     True,
    "stack":    False,
    "xmin":     0,
    "xmax":     6,
    "ymin":     1e4,
    "ymax":     1e11,
    "xtitle":   ["All events", f"#geq 1 {flavor_l}^{{#pm}} + ISO", f"#geq 2 {flavor_l}^{{#pm}} + OS", f"86 < m({flavor_l}^{{#plus}}{flavor_l}^{{#minus}}) < 96", f"20 < p({flavor_l}^{{#plus}}{flavor_l}^{{#minus}}) < 70", "120 < m_{rec} < 140", "|cos#theta_{miss}| < 0.98"],
    "ytitle":   "Events ",
    "scaleSig": 10
}