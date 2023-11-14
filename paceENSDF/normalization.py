from .base_ensdf import *

class Normalization(BaseENSDF):
    __doc__="""Class to handle Normalization and Production Normalization
    records from ENSDF-decay data sets."""

    def __init__(self):
        BaseENSDF.__init__(self)
        
    def norm_record(self, list, str, index, **kwargs):
        """Normalization record from the corresponding alpha, beta-minus, or 
        electron-capture/beta-plus ENSDF-decay data set.

        The normalization records are used to convert photon, transition, or 
        beta-decay (lepton) intensities, to their corresponding intensities per 
        100 decays of the parent.  To get an absolute normalization for each of 
        these quantities, the branching-ratio multiplier must be factored 
        through the corresponding decay branch (see "prod_norm_record()" method)
        in each case.

        Arguments:
            list: A list of ENSDF-decay data JSON objects.
            str: A string object describing the parent ID.
            index: An integer object associated with the decay index of the 
                   parent state, where:
                   0: Ground-state decay;
                   >= 1: Isomer decay.
            kwargs: An additional keyword argument is needed for the appropriate
                    radioactive-decay mode:

                    mode='A'    : Alpha decay
                    mode='BM'   : Beta-minus decay
                    mode='ECBP' : Electron-capture/beta-plus decay

                    Only the above keyword arguments (case insensitive) are 
                    acceptable.  

        Returns:
            A dictionary object with a key containing the parent-daughter 
            information in a tuple:

            [0]: Parent ID (str);
            [1]: Parent atomic (Z) number (int);
            [2]: Parent mass (A) number (int);
            [3]: Decay-level index of parent nucleus (int);
            [4]: Decay-level energy of parent nucleus (float/str);
            [5]: Daughter ID (str);
            [6]: Daughter atomic (Z) number (int);
            [7]: Daughter mass (A) number (int).
        
            The corresponding dictionary values is a list containing the 
            normalization data in five individual tuples:

            Tuple 1:
            [0]: "NR" Photon-intensity multiplier (float);
            [1]: Photon-intensity multiplier uncertainty (float);
            [2]: "NR" Flag (bool).

            Tuple 2:
            [0]: "NT" Transition-intensity multiplier (float);
            [1]: Transition-intensity multiplier uncertainty (float);
            [2]: "NT" Flag (bool).

            Tuple 3:
            [0]: "BR" Branching-ratio multiplier (float);
            [1]: Branching-ratio multiplier uncertainty (float);
            [2]: "BR" Flag (bool).

            Tuple 4:
            [0]: "NB" Lepton-intensity multiplier (float);
            [1]: Lepton-intensity multiplier uncertainty (float);
            [2]: "NB" Flag (bool).

            Tuple 5:
            [0]: "NP" Delayed-particle intensity multiplier (float);
            [1]: Delayed-particle intensity multiplier uncertainty (float);
            [2]: "NP" Flag (bool).

            The intensity-multiplier flag in each case indicates whether the 
            record was extracted (True) from the original ENSDF data set or 
            derived (False).  The delayed-particle intensity multiplier ("NP") 
            is the same as in the "prod_norm_record()" method.

        Examples:
            norm_record(edata, "Ra226", 0, mode="A")
            norm_record(edata, "Co60", 0, mode="BM")
            norm_record(edata, "Y86", 0, mode="ECBP")
        """
        self.list = list
        self.str = str
        self.index = int(index)
        
        decay_mode = BaseENSDF.check_decay([mode for mode in kwargs.values()][0])
        if decay_mode == None:
            print("Invalid decay mode.")
        else:
            print(decay_mode)
            norm_dict = {}
            DECAY_DATA_EXISTS = False
            NR_tuple = None
            NT_tuple = None
            BR_tuple = None
            NB_tuple = None
            NP_tuple = None
            for jdict in self.list:
                if decay_mode == jdict["decayMode"] and self.str == jdict["parentID"] and self.index == jdict["decayIndex"]:
                    DECAY_DATA_EXISTS = True
                    pid = jdict["parentID"]
                    decay_index = jdict["decayIndex"]
                    pZ = jdict["parentAtomicNumber"]
                    pA = jdict["parentAtomicMass"]
                    did = jdict["daughterID"]
                    dZ = jdict["daughterAtomicNumber"]
                    dA = jdict["daughterAtomicMass"]

                    decay_level = None
                    for each_p in jdict["parentDecay"]:
                        decay_level = each_p["parentDecayLevelEnergy"]

                    for each_ds in jdict["decaySchemeNormalization"]:
                        for each_nr in each_ds["normalizationRecord"]:
                            NR = each_nr["multiplerPhotonIntensity"]
                            DNR = each_nr["dMultiplerPhotonIntensity"]
                            NR_exists = each_nr["recordExistsNR"]
                            NR_tuple = (NR, DNR, NR_exists)

                            NT = each_nr["multiplerTransitionIntensity"]
                            DNT = each_nr["dMultiplerTransitionIntensity"]
                            NT_exists = each_nr["recordExistsNT"]
                            NT_tuple = (NT, DNT, NT_exists)

                            BR = each_nr["multiplerBranchingRatio"]
                            DBR = each_nr["dMultiplerBranchingRatio"]
                            BR_exists = each_nr["recordExistsBR"]
                            BR_tuple = (BR, DBR, BR_exists)

                            NB = each_nr["multiplerLeptonIntensity"]
                            DNB = each_nr["dMultiplerLeptonIntensity"]
                            NB_exists = each_nr["recordExistsNB"]
                            NB_tuple = (NB, DNB, NB_exists)

                            NP = each_nr["multiplierDelayedParticleIntensity"]
                            DNP = each_nr["dMultiplierDelayedParticleIntensity"]
                            NP_exists = each_nr["recordExistsNP"]
                            NP_tuple = (NP, DNP, NP_exists)

                    norm_dict.update({(pid,pZ,pA,decay_index,decay_level,did,dZ,dA):[NR_tuple, NT_tuple, BR_tuple, NB_tuple, NP_tuple]})
            if DECAY_DATA_EXISTS == True:
                return norm_dict
            else:
                return
        
    def prod_norm_record(self, list, str, index, **kwargs):
        """Production-normalization record from the corresponding alpha, 
        beta-minus, or electron-capture/beta-plus ENSDF-decay data set.

        These records are to be used where an absolute normalization is 
        required.  The production-normalization records are used to convert 
        photon, transition, or beta-decay (lepton) intensities, to their 
        corresponding intensities per 100 decays of the parent.

        Arguments:
            list: A list of ENSDF-decay data JSON objects.
            str: A string object describing the parent ID.
            index: An integer object associated with the decay index of the 
                   parent state, where:
                   0: Ground-state decay;
                   >= 1: Isomer decay.
            kwargs: An additional keyword argument is needed for the appropriate
                    radioactive-decay mode:

                    mode='A'    : Alpha decay
                    mode='BM'   : Beta-minus decay
                    mode='ECBP' : Electron-capture/beta-plus decay

                    Only the above keyword arguments (case insensitive) are 
                    acceptable.  

        Returns:
            A dictionary object with a key containing the parent-daughter 
            information in a tuple:

            [0]: Parent ID (str);
            [1]: Parent atomic (Z) number (int);
            [2]: Parent mass (A) number (int);
            [3]: Decay-level index of parent nucleus (int);
            [4]: Decay-level energy of parent nucleus (float/str);
            [5]: Daughter ID (str);
            [6]: Daughter atomic (Z) number (int);
            [7]: Daughter mass (A) number (int).
        
            The corresponding dictionary values is a list containing the 
            normalization data in four individual tuples:

            Tuple 1:
            [0]: "NR x BR" Product of the photon-intensity multiplier and 
                 branching-ratio multiplier (float);
            [1]: Intensity-multiplier product uncertainty (float);
            [2]: "NR x BR" Flag (bool).

            Tuple 2:
            [0]: "NT x BR" Product of the transition-intensity multiplier and 
                 branching-ratio multiplier (float);
            [1]: Intensity-multiplier product uncertainty (float);
            [2]: "NT x BR" Flag (bool).

            Tuple 3:
            [0]: "NB x BR" Product of the lepton-intensity multiplier and 
                 branching-ratio multiplier (float);
            [1]: Intensity-multiplier product uncertainty (float);
            [2]: "NB x BR" Flag (bool).

            Tuple 4:
            [0]: "NP" Delayed-particle intensity multiplier (float);
            [1]: Delayed-particle intensity multiplier uncertainty (float);
            [2]: "NP" Flag (bool).

            The intensity-multiplier flag in each case indicates whether the 
            record was extracted (True) from the original ENSDF data set or 
            derived (False).  The delayed-particle intensity multiplier ("NP") 
            is the same as in the "norm_record()" method.

        Examples:
            prod_norm_record(edata, "Ra226", 0, mode="A")
            prod_norm_record(edata, "Co60", 0, mode="BM")
            prod_norm_record(edata, "Y86", 0, mode="ECBP")
        """
        self.list = list
        self.str = str
        self.index = int(index)
        
        decay_mode = BaseENSDF.check_decay([mode for mode in kwargs.values()][0])
        if decay_mode == None:
            print("Invalid decay mode.")
        else:
            print(decay_mode)
            prod_norm_dict = {}
            DECAY_DATA_EXISTS = False
            PNR_tuple = None
            PNT_tuple = None
            PNB_tuple = None
            PNP_tuple = None
            for jdict in self.list:
                if decay_mode == jdict["decayMode"] and self.str == jdict["parentID"] and self.index == jdict["decayIndex"]:
                    DECAY_DATA_EXISTS = True
                    pid = jdict["parentID"]
                    decay_index = jdict["decayIndex"]
                    pZ = jdict["parentAtomicNumber"]
                    pA = jdict["parentAtomicMass"]
                    did = jdict["daughterID"]
                    dZ = jdict["daughterAtomicNumber"]
                    dA = jdict["daughterAtomicMass"]

                    decay_level = None
                    for each_p in jdict["parentDecay"]:
                        decay_level = each_p["parentDecayLevelEnergy"]
                    
                    for each_ds in jdict["decaySchemeNormalization"]:
                        for each_nr in each_ds["productionNormalizationRecord"]:
                            PNR = each_nr["multiplierPhotonIntensityBranchingRatioCorrected"]
                            DPNR = each_nr["dMultiplierPhotonIntensityBranchingRatioCorrected"]
                            PNR_exists = each_nr["recordExistsPNR"]
                            PNR_tuple = (PNR, DPNR, PNR_exists)

                            PNT = each_nr["multiplierTransitionIntensityBranchingRatioCorrected"]
                            DPNT = each_nr["dMultiplierTransitionIntensityBranchingRatioCorrected"]
                            PNT_exists = each_nr["recordExistsPNT"]
                            PNT_tuple = (PNT, DPNT, PNT_exists)

                            PNB = each_nr["multiplierLeptonIntensityBranchingRatioCorrected"]
                            DPNB = each_nr["dMultiplierLeptonIntensityBranchingRatioCorrected"]
                            PNB_exists = each_nr["recordExistsPNB"]
                            PNB_tuple = (PNB, DPNB, PNB_exists)

                            # PNP is identical to NP in normalization record
                            PNP = each_nr["multiplierDelayedParticleIntensity"]
                            DPNP = each_nr["dMultiplierDelayedParticleIntensity"]
                            PNP_exists = each_nr["recordExistsPNP"]
                            PNP_tuple = (PNP, DPNP, PNP_exists)

                    prod_norm_dict.update({(pid,pZ,pA,decay_index,decay_level,did,dZ,dA):[PNR_tuple, PNT_tuple, PNB_tuple, PNP_tuple]})
            if DECAY_DATA_EXISTS == True:
                return prod_norm_dict
            else:
                return
