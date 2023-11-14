from .base_ensdf import *
from .normalization import Normalization

class Parent(Normalization):
    __doc__="""Class to handle and maniulate data from the Parent record in 
    ENSDF-decay data sets."""

    def __init__(self):
        BaseENSDF.__init__(self)
        Normalization.__init__(self)

        
    def find_parents_multiple_jpi(self, list, **kwargs):
        """Find all parents with multiple spin-parity permutations.

        Arguments:
            list: A list of ENSDF-decay data JSON objects.
            kwargs: An additional keyword argument is needed for the appropriate
                    radioactive-decay mode:

                    mode='A'    : Alpha decay
                    mode='BM'   : Beta-minus decay
                    mode='ECBP' : Electron-capture/beta-plus decay

                    Only the above keyword arguments (case insensitive) are 
                    acceptable.

        Returns: 
            A dictionary object with a single key containing parent information 
            in a tuple:

            [0]: Parent ID (str);
            [1]: Decay-level index of parent nucleus (int);
            [2]: Decay-level energy of parent nucleus (float);
            [3]: Number of spin-parity assignments for parent-decay level (int);
        
            The corresponding dictionary values are lists containing the 
            different permutations of the spin-parity assignments for the parent
            level:

            [0]: Spin assignment for parent level (float);
            [1]: Parity assignment for parent level (int):
                 1: Positive parity;
                 -1: Negative parity;
                 0: No parity given.

        Examples:
            find_parents_multiple_jpi(edata, mode="A") 
            find_parents_multiple_jpi(edata, mode="BM") 
            find_parents_multiple_jpi(edata, mode="ECBP") 
        """
        self.list = list
        decay_mode = BaseENSDF.check_decay([mode for mode in kwargs.values()][0])
        if decay_mode == None:
            print("Invalid decay mode.")
        else:
            print(decay_mode)
            parent_spin_dict = {}
            for jdict in self.list:
                if decay_mode == jdict["decayMode"]:
                    for each_p in jdict["parentDecay"]:
                        if each_p["numberOfSpins"] > 1:
                            pid = jdict["parentID"]
                            decay_index = jdict["decayIndex"]
                            decay_level = each_p["parentDecayLevelEnergy"]
                            nspins = each_p["numberOfSpins"]
                            #print(pid, decay_index)
                            spin_list = []
                            for each_s in each_p["spins"]:
                                spin_real = each_s["spinReal"]
                                parity = each_s["parity"]
                                spin_list.append([spin_real, parity])
                            parent_spin_dict.update({(pid, decay_index, decay_level, nspins): spin_list})

            return parent_spin_dict

        
    def get_parent_jpi(self, list, str, index, **kwargs):
        """Spins and parities for a defined parent and associated decay mode.

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
            A list object with the spins and parities associated with the parent
            decay-energy state.  If the parent state has multiple spins and 
            parities then all permutations are returned:

            [0]: Spin assignment of parent level (float);
            [1]: Parity assignment of parent level (int):
                 1: Positive parity;
                 -1: Negative parity;
                 0: No parity given.

        Example:
            A parent with multiple spin-parity assignments:

            get_parent_jpi(edata, "Db258", 0, mode="ECBP")

            A parent with a single spin-parity assignment:

            get_parent_jpi(edata, "Co60", 1, mode="BM")
        """
        self.list = list
        self.str = str
        decay_mode = BaseENSDF.check_decay([mode for mode in kwargs.values()][0])
        if decay_mode == None:
            print("Invalid decay mode.")
        else:
            print(decay_mode)

        for jdict in self.list:
            if decay_mode == jdict["decayMode"] and str == jdict["parentID"] and index == jdict["decayIndex"]:
                pid = jdict["parentID"]
                decay_index = jdict["decayIndex"]
                spin_list = []
                for each_p in jdict["parentDecay"]:
                    for each_s in each_p["spins"]:
                                spin_real = each_s["spinReal"]
                                parity = each_s["parity"]
                                spin_list.append([spin_real, parity])
                return spin_list

            
    def find_all_parent_isomers(self, list, **kwargs):
        """Finds all isomeric parent-daughter pairs for a given decay mode.

        Arguments:
            list: A list of ENSDF-decay data JSON objects.
            kwargs: An additional keyword argument is needed for the appropriate
                    radioactive-decay mode:

                    mode='A'    : Alpha decay
                    mode='BM'   : Beta-minus decay
                    mode='ECBP' : Electron-capture/beta-plus decay

                    Only the above keyword arguments (case insensitive) are 
                    acceptable.

        Returns: 
            A list object describing all parent-daughter isomer decays:

            [0]: Parent ID (str);
            [1]: Decay-level index of parent nucleus (int);
            [2]: Decay-level energy of parent nucleus (float/str);
            [3]: Parent atomic (Z) number (int);
            [4]: Parent mass (A) number (int);
            [5]: Daughter ID (str);
            [6]: Daughter atomic (Z) number (int);
            [7]: Daughter mass (A) number (int);

        Example:
            All alpha-decaying isomers:

            find_all_parent_isomers(edata, mode="A")

            All beta-minus decaying isomers:

            find_all_parent_isomers(edata, mode="BM")

            All electron-capture/beta-plus decaying isomers:

            find_all_parent_isomers(edata, mode="ECBP")
        """
        self.list = list
        decay_mode = BaseENSDF.check_decay([mode for mode in kwargs.values()][0])
        if decay_mode == None:
            print("Invalid decay mode.")
        else:
            print(decay_mode)
            parent_list = []
            for jdict in self.list:
                if decay_mode == jdict["decayMode"]:
                    for each_p in jdict["parentDecay"]:
                        if each_p["parentIsIsomer"] == True:
                            pid = jdict["parentID"]
                            decay_index = jdict["decayIndex"]
                            pZ = jdict["parentAtomicNumber"]
                            pA = jdict["parentAtomicMass"]
                            did = jdict["daughterID"]
                            dZ = jdict["daughterAtomicNumber"]
                            dA = jdict["daughterAtomicMass"]
                            decay_level = each_p["parentDecayLevelEnergy"]

                            parent_list.append([pid, decay_index, decay_level, pZ, pA, did, dZ, dA])
            print("{0} {1} nuclides are isomer decays".format(len(parent_list), decay_mode))
            return parent_list

        
    def get_parent_decay(self, list, str, index, **kwargs):
        """Decay-level energy of the parent and its Q-value.

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
            A dictionary object with a single key containing parent-daughter
            information in a tuple:

            [0]: Parent ID (str);
            [1]: Parent atomic (Z) number (int);
            [2]: Parent mass (A) number (int);
            [3]: Decay-level index of parent nucleus (int);
            [4]: Daughter ID (str);
            [5]: Daughter atomic (Z) number (int);
            [6]: Daughter mass (A) number (int).

            The corresponding dictionary value is a list of two tuples 
            containing the (i) parent decay-level energy, and (ii) Q-value 
            information:

            First tuple:
            [0]: Decay-level energy of parent nucleus (float/str);
            [1]: Decay-level energy of parent nucleus uncertainty (float).

            Second tuple:
            [0]: Q-value for decay (float);
            [1]: Q-value uncertainty (float).
        
        Examples:
            get_parent_decay(edata, "Ir173", 0, mode="A")
            get_parent_decay(edata, "Tc102", 1, mode="BM")
            get_parent_decay(edata, "V50", 0, mode="ECBP") 
        """
        self.list = list
        self.str = str
        self.index = int(index)
        decay_mode = BaseENSDF.check_decay([mode for mode in kwargs.values()][0])
        if decay_mode == None:
            print("Invalid decay mode.")
        else:
            print(decay_mode)

            parent_dict = {}
            PARENT_DECAY_EXISTS = False
            for jdict in self.list:
                if decay_mode == jdict["decayMode"] and self.str == jdict["parentID"] and self.index == jdict["decayIndex"]:
                    PARENT_DECAY_EXISTS = True
                    pid = jdict["parentID"]
                    decay_index = jdict["decayIndex"]
                    pZ = jdict["parentAtomicNumber"]
                    pA = jdict["parentAtomicMass"]
                    did = jdict["daughterID"]
                    dZ = jdict["daughterAtomicNumber"]
                    dA = jdict["daughterAtomicMass"]

                    for each_p in jdict["parentDecay"]:
                        decay_level = each_p["parentDecayLevelEnergy"]
                        d_decay_level = each_p["dParentDecayLevelEnergy"]
                        q_value = each_p["valueQ"]
                        d_q_value = each_p["dValueQ"]

                    parent_dict.update({(pid, pZ, pA, decay_index, did, dZ, dA): [(decay_level, d_decay_level), (q_value, d_q_value)]})
            if PARENT_DECAY_EXISTS == True:
                return parent_dict
            else:
                return

        
    def get_parent_halflife(self, list, str, index, **kwargs):
        """Halflife of the parent-decaying nucleus.

        Arguments:
            list: A list of ENSDF-decay data JSON objects.
            str: A string object describing the parent ID.
            index: An integer object associated with the decay index of the 
                   parent state, where:
                   0: Ground-state decay;
                   >= 1: Isomer decay.
            kwargs: Two additional keyword arguments are required:
                   
                    (i) Radioactive-decay mode:

                    mode='A'    : Alpha decay
                    mode='BM'   : Beta-minus decay
                    mode='ECBP' : Electron-capture/beta-plus decay

                    (ii) Halflife time units

                    units='best'     
                    units='seconds'  
                    units='s'       

                    Only the above keyword arguments (case insensitive) are 
                    acceptable.  The 'best' units are those parsed from the 
                    original ENSDF file. 

        Returns: 
            A dictionary object with a single key containing parent-daughter 
            information in a tuple:

            [0]: Parent ID (str);
            [1]: Parent atomic (Z) number (int);
            [2]: Parent mass (A) number (int);
            [3]: Decay-level index of parent nucleus (int);
            [4]: Decay-level energy of parent nucleus (float);
            [5]: Daughter ID (str);
            [6]: Daughter atomic (Z) number (int);
            [7]: Daughter mass (A) number (int);

            The corresponding dictionary value is a list containing the 
            halflife information associated with the parent nucleus:

            [0]: Halflife in 'best' units or in 'seconds' (float);
            [1]: Halflife uncertainty (float);
            [2]: Halflife time units (str).

        Example:
            Ground-state decay of 60Co parent:

            get_parent_halflife(edata, "Co60", 0, mode="BM", units="best")

            Isomer decay of 60Co parent:

            get_parent_halflife(edata, "Co60", 1, mode="BM", units="best")
        """
        self.list = list
        self.str = str
        self.index = int(index)
        decay_mode = None
        #decay_mode = check_decay([mode for mode in kwargs.values() if mode != None][0])
        for kwarg in kwargs.values():
            decay_mode = BaseENSDF.check_decay(kwarg)
            if decay_mode != None:
                break

        if decay_mode == None:
            print("Invalid decay mode.")
        else:
            print(decay_mode)

            BEST_UNITS = False
            WRONG_UNITS = True
            for unit in kwargs.values():
                if unit.lower()=='best': 
                    BEST_UNITS = True
                    WRONG_UNITS = False
                elif (unit.lower()=='seconds') or (unit.lower()=='s'): 
                    BEST_UNITS = False
                    WRONG_UNITS = False
                #else:
            if WRONG_UNITS == True:
                print("Inavlid units for halflife.  The only arguements accepted are:")
                print("units='best'")
                print("units='seconds'")

            if WRONG_UNITS == False:
                parent_dict = {}
                PARENT_DECAY_EXISTS = False
                for jdict in self.list:
                    if decay_mode == jdict["decayMode"] and self.str == jdict["parentID"] and self.index == jdict["decayIndex"]:
                        PARENT_DECAY_EXISTS = True
                        pid = jdict["parentID"]
                        decay_index = jdict["decayIndex"]
                        pZ = jdict["parentAtomicNumber"]
                        pA = jdict["parentAtomicMass"]
                        did = jdict["daughterID"]
                        dZ = jdict["daughterAtomicNumber"]
                        dA = jdict["daughterAtomicMass"]

                        for each_p in jdict["parentDecay"]:
                            decay_level = each_p["parentDecayLevelEnergy"]
                            halflife, d_halflife, unit_halflife = None, None, None
                            for each_h in each_p["halfLife"]:
                                if BEST_UNITS == True:
                                    halflife = each_h["halfLifeBest"]
                                    d_halflife = each_h["dHalfLifeBest"]
                                    unit_halflife = each_h["unitHalfLifeBest"]
                                else:
                                    halflife = each_h["halfLifeConverted"]
                                    d_halflife = each_h["dHalfLifeConverted"]
                                    unit_halflife = each_h["unitHalfLifeConverted"]

                            parent_dict.update({(pid, pZ, pA, decay_index, decay_level, did, dZ, dA): [halflife, d_halflife, unit_halflife]})

                if PARENT_DECAY_EXISTS == True:
                    return parent_dict
                else:
                    return
            else:
                return None
