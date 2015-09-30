import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-950-975_mLSP-825to925-750to925_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/04F58B49-B15C-E511-A966-001517F7F410.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-950-975_mLSP-825to925-750to925_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/0A52FAD5-D05C-E511-8A8B-0002C94D5618.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-950-975_mLSP-825to925-750to925_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/0E2B7CF3-B35C-E511-B315-001517E73B50.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-950-975_mLSP-825to925-750to925_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/10580B61-B55C-E511-88BE-001517E73B50.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-950-975_mLSP-825to925-750to925_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/18465454-D85C-E511-8607-0025901ABB72.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-950-975_mLSP-825to925-750to925_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/1ABE1656-C25C-E511-9E36-0026182FD77F.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-950-975_mLSP-825to925-750to925_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/1AEDD692-AF5C-E511-AB26-F45214C74880.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-950-975_mLSP-825to925-750to925_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/22056868-AB5C-E511-8A1D-001E67A40523.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-950-975_mLSP-825to925-750to925_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/245B5BAA-AF5C-E511-A971-001E675A69DC.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-950-975_mLSP-825to925-750to925_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/24C7B17B-AD5C-E511-A259-F45214C748C2.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-950-975_mLSP-825to925-750to925_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/24FC8082-AC5C-E511-BD6D-001E675A6C2A.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-950-975_mLSP-825to925-750to925_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/38A53245-D55C-E511-AEB6-5065F3819221.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-950-975_mLSP-825to925-750to925_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/3E520421-B15C-E511-9BBB-485B3919F0B5.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-950-975_mLSP-825to925-750to925_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/42FABFCD-BF5C-E511-902F-001E675A6AA9.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-950-975_mLSP-825to925-750to925_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/4663530A-C95C-E511-A656-F45214C748B4.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-950-975_mLSP-825to925-750to925_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/4EA131BD-AB5C-E511-A410-0002C92958E8.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-950-975_mLSP-825to925-750to925_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/5047A0E6-BB5C-E511-AF72-0002C90A342E.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-950-975_mLSP-825to925-750to925_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/5047AA8E-DC5C-E511-8B44-0CC47A0AD6DA.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-950-975_mLSP-825to925-750to925_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/54B6A3DE-BB5C-E511-9A9F-003048FE40E2.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-950-975_mLSP-825to925-750to925_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/5A3DF86E-C25C-E511-921B-001E67A3EAB1.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-950-975_mLSP-825to925-750to925_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/5AF08684-BB5C-E511-97BF-0002C90B7F2C.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-950-975_mLSP-825to925-750to925_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/5C021C68-BB5C-E511-B798-A0040420FE80.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-950-975_mLSP-825to925-750to925_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/64D7EB59-C25C-E511-A363-90B11C12D371.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-950-975_mLSP-825to925-750to925_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/688CCD89-AC5C-E511-BC10-001517F7F410.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-950-975_mLSP-825to925-750to925_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/70F37088-C85C-E511-A6E6-5065F3815281.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-950-975_mLSP-825to925-750to925_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/764395B2-B55C-E511-9F07-001E67A3FEB1.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-950-975_mLSP-825to925-750to925_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/808D2DCB-BF5C-E511-84BF-001E67A404B0.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-950-975_mLSP-825to925-750to925_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/9493CF88-D75C-E511-BCCA-B8CA3A70A5E8.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-950-975_mLSP-825to925-750to925_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/94ABAB78-AD5C-E511-B85F-24BE05C488E1.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-950-975_mLSP-825to925-750to925_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/9643EAE9-B35C-E511-8906-001E67A3FEB1.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-950-975_mLSP-825to925-750to925_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/9A079BFC-D75C-E511-A743-0025901FB188.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-950-975_mLSP-825to925-750to925_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/A01466FA-AB5C-E511-8DAC-F45214C748C8.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-950-975_mLSP-825to925-750to925_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/A0A7D912-C45C-E511-B5C8-0002C94D5614.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-950-975_mLSP-825to925-750to925_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/A0CCE1C5-AC5C-E511-9C67-001E67A40523.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-950-975_mLSP-825to925-750to925_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/B209BEA8-D05C-E511-B082-0002C90B7F2E.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-950-975_mLSP-825to925-750to925_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/BEA65B3F-BC5C-E511-8FC1-002590D9D822.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-950-975_mLSP-825to925-750to925_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/C4232EBB-AE5C-E511-A1E4-485B3919F0B5.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-950-975_mLSP-825to925-750to925_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/CEA7F88E-AF5C-E511-BA42-F45214C748D6.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-950-975_mLSP-825to925-750to925_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/D4D12143-BB5C-E511-8E45-0002C94D5614.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-950-975_mLSP-825to925-750to925_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/DAFE82BA-AF5C-E511-9979-90B11C06954E.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-950-975_mLSP-825to925-750to925_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/E45909F7-C85C-E511-A5C3-5065F3812291.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-950-975_mLSP-825to925-750to925_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/EA020BB9-AB5C-E511-93A8-001E67A3FB91.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-950-975_mLSP-825to925-750to925_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/F68ECEC6-AB5C-E511-A89C-0002C92A102E.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-950-975_mLSP-825to925-750to925_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/FC1471FC-B05C-E511-B960-90B11C06954E.root' ] );


secFiles.extend( [
               ] )
