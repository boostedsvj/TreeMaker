import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/047432C2-63AF-8049-8F25-CAEA9EA9D671.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/050FBE26-7300-9A42-BD00-D803A9EF94FA.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/08140254-E377-0D4A-8569-8B709F5260AC.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/08848E2F-376E-A442-824A-43EB179B128C.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/0AF0DF6D-DF2E-544D-80ED-C577F11FD3B5.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/0C0A0F0B-D0D8-0D47-A653-44A6960BD977.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/11717133-772B-B04B-BF9E-7051E3A1B182.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/1D231A88-7652-6E40-82F9-BCA1CCD07D01.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/1DF0BF28-316F-CB47-91FA-B7574B723F25.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/20BA0217-C77D-0049-A41B-0573ECF5C9A1.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/26019A3E-BE93-104C-8C9C-3CB06B7CD196.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/2EE69B6D-11BB-8C4A-B7E9-8231E4172929.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/3107026F-64ED-C24E-A745-15DEF496BA0A.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/332D2A4F-D92A-F448-9771-B8523A52A2C1.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/36510C91-2425-7B41-8DEE-17E3A93C532B.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/3BD06C08-2717-7D40-87AF-35C5C53A5F73.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/3E4B2E03-2315-6F49-A1FD-8D7105CA8CA1.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/43AA4CD4-B148-5D4E-B946-7BEB23C8C567.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/47D4F4BC-641B-2446-BB14-A141DC64541B.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/4A9C63BA-150A-F242-9F0F-C662173747BA.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/568D1043-CCFE-C14B-9611-FDF729C05B06.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/577FC318-191C-2643-B643-A8435BEA5C40.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/626994CC-8DBA-E849-B1B0-A55ADB2A5A40.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/63F83DE8-1ACD-074B-A947-FA135BA9C92A.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/65D4D599-735F-0742-A0A8-9846988217B6.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/6A233D91-1644-D74A-9E1C-5F1F8DE71137.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/71A60923-28A3-A748-9174-513363B66A68.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/76339695-ED5F-CC4E-8373-30B0340FFF66.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/7D990F05-B659-E74E-A0E3-09FBC4211A06.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/7F0ACEF0-4682-5643-B1C5-06981D6764F2.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/7F35BDBE-44D9-CA4A-B360-FF9B9127D4FD.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/812C341B-8C76-3B4C-AE48-B905C0A2D2C6.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/82268B8B-4735-E140-9EF7-3488880E5660.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/8445A23B-F640-5642-8FB1-E08765161D27.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/8661EFDF-CD2F-9344-8765-CC184BEB81F9.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/8940C2A2-74E6-F141-B423-1DD0D3731F2E.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/8A6BE1EC-AB3F-2F47-BD60-70752A942EF0.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/8A988160-E13F-D043-8F3E-D92528654B89.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/8B82A0F0-08A8-4F47-BBFC-ABE80E5EA458.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/90039881-37C7-6542-92EB-3B31EBB40B07.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/92FE2C8C-5B41-E343-829F-EDBD6306F2F6.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/95381DD6-6E24-CA45-8851-4C710E609C0E.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/96CEE96A-6EFE-B74E-B4EF-00A1354C0A77.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/99AEDA32-86B0-C545-8162-0ACD1DF1D3F9.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/9AF87A24-CB8C-C848-AAA6-6FB9777EB5A0.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/9BB97277-34F9-4242-B038-3704C8397D92.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/9EAB7834-20AA-2641-86BA-47BBF49EE529.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/A07B0B50-C9F9-EC4C-BDB6-F51284AF50F6.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/A6395409-93D6-E74A-BD1E-5297481601D3.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/A84B296A-99E0-E748-B360-B28BF65FD5C7.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/A93B0BB4-C416-9A43-A451-4438DD2C8D2A.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/AD582EAD-62C5-C94C-8709-4A7D6B940F9D.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/AD802FC9-3F4D-E941-A52A-0FEC0EE395B6.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/B4FD31A5-DFB4-404B-AA1E-657F0B323C44.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/B9190B77-3406-0740-B464-FBCAA147DA95.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/B93D78E6-7E53-C546-8E6F-4D31A0514D6F.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/BA51EA37-4AFE-7E45-A4BE-919A0D65CD5B.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/BDE40245-A479-0A4D-A5D5-5C48B3916F2C.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/C2BFCE0B-8764-FC44-AEF9-5CD6F6FE743E.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/C9AB6354-9C77-884E-B829-A59A74DDB756.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/CA76433E-3468-EA4E-A485-95EE4DD716DC.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/D77832CB-619C-524D-8EF1-F17404BDCEC1.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/D90BFE46-C0DC-5A4B-A212-EE4F3FBDFB17.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/DB0BFA1A-4C80-354A-9925-A10F90C0BB11.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/DB7ABDE6-D097-DE42-A1AC-DBBA0401D720.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/E274E076-2B81-C245-8F09-3642909D5A81.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/E9608846-3682-654D-819A-4058D4039199.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/EDBB921A-5B25-D345-BF44-67E6876A693C.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/F239C94B-7D34-1544-8FE2-D5F74BECF8C0.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/FC877DA4-0454-6340-98AC-DAB92684238A.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/482DACB6-0790-7B46-9FA1-8734251BE4A7.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/A2CDF907-26C9-1141-81D9-F78B5C1E2F23.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/20000/04C613A5-3155-824E-BD34-5BCB1BAB7541.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/20000/534DA0BE-B96F-3540-B247-BDDF9C47FD16.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/20000/8FED74D2-A677-AE45-9309-AF571077B044.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/280000/0454E3A7-2AED-384B-9F5A-98DAF28622D9.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/280000/0BDBF27A-4B83-F24E-8251-26E56BC8206C.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/280000/0BF0F203-4A4E-2541-9BF1-09FC3713CA47.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/280000/0E69BDB2-B8B6-6541-BD7C-37A7098E5041.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/280000/109E9AEB-E485-4243-A80B-00F8ABE41AF5.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/280000/1283CBA0-8850-9D48-95E9-C0F89D5994AA.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/280000/154EB4F6-AF38-B641-86EA-B45CB1AE9381.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/280000/16318429-33B9-FF4F-B29A-50663B8BDDD1.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/280000/1A917F4D-D9E8-5E4B-851F-3798EDF96507.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/280000/23752E98-6F1A-8E4D-A232-5B44BD4E4462.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/280000/25C9C52C-A853-ED4D-9E4C-7CFD6EC4A64C.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/280000/2D4D7551-159F-C04B-B688-4C649E4D8549.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/280000/37F63A28-57FF-A548-8C42-463FC1AE02A2.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/280000/39AA4A9F-C7E0-854A-8295-E29270BE755B.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/280000/3DAC58D9-545F-284D-AD99-42F264852592.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/280000/47859986-D3A4-124F-8E67-C8DBB66A8656.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/280000/4DC92B4C-032B-CA42-B6F6-D7CB70860925.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/280000/57D6D706-AB93-BE41-9F2E-4F02EADFE55F.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/280000/5837A07B-6CBF-4445-99DF-AEB37A0E145F.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/280000/5F8D7C40-A917-804B-BF20-E19F32625541.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/280000/618DE571-B937-E943-8CDD-4543BF3D546F.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/280000/6391E0E1-8732-6B44-B618-78A6580BA710.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/280000/7CC3B2CB-1ED9-6B48-BBFA-E65A9DEE1242.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/280000/92F106DE-CA24-D347-ABEB-D4698AAF9778.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/280000/9E04C81B-E5EC-EC4B-8D49-DA8DBDF0E060.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/280000/AC2C5DED-64F4-C140-839A-93904DA7EE18.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/280000/AE3CE86B-C04E-0A48-8795-79F498EDF175.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/280000/AFE9744F-C555-D549-9AFA-FE8AB101B42D.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/280000/B5AA2314-BF3E-EA46-B9B7-279FCDEEEF46.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/280000/CE2CAFD2-5A43-5443-9F52-62CFC1356A7B.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/280000/CEB9620C-A6CE-3541-B4AB-ABF8F85AC2B1.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/280000/D95A170A-94CD-9E47-B86B-1D97083E5030.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/280000/E1B370B9-D20F-A542-9049-54F064E35307.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/280000/E65E38A2-C5CF-AF4F-AA94-23560D8AA8FD.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/280000/E9D49FAA-16FF-BA4C-8679-B546286DF9B0.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/280000/EFC19A3F-FF47-A04C-805B-639362FEE712.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/280000/EFCC61AA-F076-464A-9C87-A81E5E7CCF18.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/280000/F4EE7C0E-F709-1E42-879F-F15A24FE5532.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/2C0FCE56-54E2-2F4E-9B91-D4589962A7C7.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/348CFB06-2C4D-3343-92F5-DE39D4E523FB.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/3582091A-C7AD-2B45-81E5-02B313C52180.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/39E1856C-3253-6D41-9A18-0038D5C4FEC4.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/43EF4963-CFE2-054F-A3D5-E033D27552F9.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/4D1D555B-FC6C-A240-B65A-6C6BE077DC04.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/77EA8571-3879-1141-A02D-CAD911CAC7B8.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/9202E3DC-01C9-1848-B21B-5B8FD6F94BBC.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/AA79CEF0-F68E-6042-8697-2C02128028E6.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/B0452677-A3E2-594B-90F3-250532B5370D.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/C2D4C103-79E9-0A44-83A2-04AFDB40388C.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/CD2EFF75-DCC8-AE4C-9AF5-31CD27677F6E.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/D4CC59C3-02B1-0C41-B6AD-E962FE461F7A.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/E164CC71-F950-E04C-867A-FC53D9500C57.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/E34ECE91-2F6C-864B-A606-E2E36DB4664E.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/EF259666-71A4-1643-B474-6BB8EE2F7A93.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/F0D433D6-4FA2-4C49-85D6-9EB61BDADF16.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/40000/FC983E9C-389F-A84C-9C34-080E8033FD2E.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/410000/11F959E6-889B-C748-A73B-A8BC7765040E.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/410000/883F9515-12DD-0C4C-B9DA-90C019DB344A.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/410000/EDA0CD41-DC95-5249-A4BB-993AA0EC8A5A.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/0434B45D-5A21-A34B-951F-299DB72814F3.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/07314824-2024-7A4D-9338-2793BBBC68A8.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/18A6B36D-43AF-CE41-8603-7B42C27E1086.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/34053EF2-C2D2-9E42-8A61-D5A220508477.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/3446C717-026A-2046-AE2E-5E0232A9CFCF.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/39C8304E-66E5-6C4F-87D7-E8A6866C8D5B.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/463C0567-EA46-F640-A980-C38A4DD4D9CA.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/561B0B0F-F5DD-C64A-AF45-70DAADC27CA2.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/6106C4A6-DC7F-0E4B-92C2-9E61C584C562.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/67E60891-FBDF-C84E-AFDB-E23B0ADCDF98.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/861270AB-60FA-0547-8CDA-7AA4F8CE95D8.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/861BD475-FFF0-1740-93C6-3698D24D89B9.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/976C0295-F559-8D44-8074-7427ED9B2EFE.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/98AF9EFD-3DC1-4D44-B282-BF4D2B8117F9.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/99C29A4B-F767-B447-8486-B8595B382E5D.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/9BC7ABB6-F069-E247-9AB3-2274753A96BC.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/9D96318C-5E82-4940-9A70-E05D4D8481AC.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/9F13ACD6-ECCB-DC44-8580-4174CB0D367B.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/A2C61F57-FA05-9F45-BF0F-84EB771C0722.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/A5589602-CA02-3A46-BEAF-9636014BB027.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/B60F6CA3-F8A6-F446-8BD4-406F9906A189.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/DCD4C5FE-91D1-364D-855E-84D45CD2276E.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/E0922181-14EE-2645-B6E2-D0029FC8AA2A.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/E8FAD238-637F-C34C-85EB-6E6770A78954.root',
] )
