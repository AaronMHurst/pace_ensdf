from .base_ensdf import *
from .normalization import Normalization
from .parent import Parent
from .daughter import Daughter
from .beta_minus import BetaMinus
from .electron_capture_beta_plus import ElectronCaptureBetaPlus

class Alpha(ElectronCaptureBetaPlus):
    __doc__="""Class to handle and manipulate alpha-decay data from ENSDF data 
    sets."""

    def __init__(self):
        BaseENSDF.__init__(self)
        Normalization.__init__(self)
        Parent.__init__(self)
        Daughter.__init__(self)
        BetaMinus.__init__(self)
        ElectronCaptureBetaPlus.__init__(self)

    def get_alpha(self, list, str, index, **kwargs):
        """Alpha-decay properties to all states populated following alpha decay 
        of a defined parent nucleus.

        Arguments:
            list: A list of ENSDF-decay data JSON objects.
            str: A string object describing the parent ID.
            index: An integer object associated with the decay index of the 
                   parent state, where:
                   0: Ground-state decay;
                   >= 1: Isomer decay.
            kwargs: An additional keyword argument is needed for the desired 
                    halflife units:

                    units='best'
                    units='seconds'
                    units='s'

                    Only the above keyword arguments (case insensitive) are 
                    acceptable.  The 'best' units are those parsed from the 
                    original ENSDF file.

        Returns: 
            A dictionary of containing alpha-decay information for the 
            parent-daughter pair.  The dictionary key is a tuple with 
            information associated with the parent nucleus:

            [0]: Parent ID (str);
            [1]: Parent atomic number (int); 
            [2]: Parent mass number (int);
            [3]: Daughter ID (str);
            [4]: Daughter atomic number (int); 
            [5]: Daughter mass number (int);
            [6]: Decay-level energy of parent nucleus (float);
            [7]: Decay-level energy uncertainty (float);
            [8]: Spin of parent nucleus (float); 
            [9]: Spin flag (int).  Only permitted integers are: 
                1: Firm spin assignment; 
                -1: Tentative spin assignment.
            [10]: Parity of parent nucleus (int).  Only permitted integers are:
                1: Positive parity; 
                -1: Negative parity; 
                0: No parity given.
            [11]: Parity flag (int).  Only permitted integers are: 
                1: Firm parity assignment; 
                -1: Tentative parity assignment.
            [12]: Halflife of parent nucleus (float);
            [13]: Halflife uncertainty (float);
            [14]: Halflife units (str).

            The dictionary values are lists containing information associated 
            with levels populated in the corresponding daughter nucleus:

            [0]: Level index corresponding to populated level (int);
            [1]: Associated level energy populated (float);
            [2]: Number of spin-parity assignments for level (int);
            [3]: Spin assignment for level (float).  If more than one spin is 
                 permissable, the first permutation is given.
            [4]: Spin flag (int).  Only permitted integers are: 
                1: Firm spin assignment; 
                -1: Tentative spin assignment.
            [5]: Parity assignment for level (int).  If more than one parity is 
                 permissable, the first permutation is given.
            [6]: Parity flag (int).  Only permitted integers are: 
                1: Firm parity assignment; 
                -1: Tentative parity assignment.
            [7]: Alpha-decay energy (float); 
            [8]: Alpha-decay energy uncertainty (float); 
            [9]: Alpha-decay intensity (float); 
            [10]: Alpha-decay intensity uncertainty (float); 
            [11]: Hindrance factor (float); 
            [12]: Hindrance factor uncertainty (float).

        Examples:
            get_alpha(edata, "Ra226", 0, units='best')
            get_alpha(edata, "Ra226", 0, units='seconds')
            get_alpha(edata, "Ra226", 0, units='s')
        """
        self.list = list
        self.str = str
        self.index = int(index)
        
        if kwargs == {} or kwargs == None:
            print("Please pass one of the following keyword arguments:")
            print("units='best'")
            print("units='seconds'")

        else:
            BEST_UNITS = False
            WRONG_UNITS = True
            units = BaseENSDF.check_time_units([unit for unit in kwargs.values()][0])

            if units == None:
                return
            else:
                WRONG_UNITS = False
                if units == 'best':
                    BEST_UNITS = True

                a_dict = {}
                a_list_all = []
                ALPHA_DECAY_LEVELS = False
                ALPHA_DECAY = False
                for jdict in self.list:
                    if jdict["decayMode"] == "alphaDecay" and self.str == jdict["parentID"] and self.index == jdict["decayIndex"]:
                        ALPHA_DECAY = True

                        pid = jdict["parentID"]
                        decay_index = jdict["decayIndex"]
                        pZ = jdict["parentAtomicNumber"]
                        pA = jdict["parentAtomicMass"]
                        did = jdict["daughterID"]
                        dZ = jdict["daughterAtomicNumber"]
                        dA = jdict["daughterAtomicMass"]

                        decay_gs_m = None
                        if int(decay_index) > 0:
                            decay_gs_m = 'ISOMER'
                        else:
                            decay_gs_m = 'GS'

                        print("Parent nucleus: {0} Z={1}, A={2}, decay index: {3}".format(pid, pZ, pA, decay_gs_m))
                        print("Daughter nucleus: {0} Z={1}, A={2}".format(did, dZ, dA))

                        thalf, d_thalf, units_thalf = None, None, None
                        decay_energy, d_decay_energy = None, None
                        spin_parent, spin_parent_flag = None, None
                        parity_parent, parity_parent_flag = None, None

                        for each_p in jdict["parentDecay"]:
                            decay_energy = each_p["parentDecayLevelEnergy"]
                            d_decay_energy = each_p["dParentDecayLevelEnergy"]
                            for each_t in each_p["halfLife"]:
                                if BEST_UNITS == True:
                                    thalf = each_t["halfLifeBest"]
                                    d_thalf = each_t["dHalfLifeBest"]
                                    units_thalf = each_t["unitHalfLifeBest"]
                                else:
                                    thalf = each_t["halfLifeConverted"]
                                    d_thalf = each_t["dHalfLifeConverted"]
                                    units_thalf = each_t["unitHalfLifeConverted"]

                            for each_ps in each_p["spins"]:
                                if each_ps["spinIndex"] == 0:
                                    spin_parent = each_ps["spinReal"]
                                    if each_ps["spinIsTentative"] == False:
                                        spin_parent_flag = 1
                                    else:
                                        spin_parent_flag = -1
                                    parity_parent = each_ps["parity"]
                                    if each_ps["parityIsTentative"] == False:
                                        parity_parent_flag = 1
                                    else:
                                        parity_parent_flag = -1


                        a_tuple = (pid, pZ, pA, did, dZ, dA, decay_energy, d_decay_energy,
                                   spin_parent, spin_parent_flag, parity_parent, parity_parent_flag,
                                   thalf, d_thalf, units_thalf)

                        for each_l in jdict["levelScheme"]:
                            if len(each_l["alphaDecay"]) > 0:
                                a_list = []
                                ALPHA_DECAY_LEVELS = True
                                level_index = each_l["levelIndex"]
                                level_energy = each_l["levelEnergy"]
                                num_spins = each_l["numberOfSpins"]
                                spin, spin_flag = None, None
                                parity, parity_flag = None, None
                                for each_s in each_l["spins"]:
                                    if each_s["spinIndex"] == 0:
                                        spin = each_s["spinReal"]
                                        if each_s["spinIsTentative"] == False:
                                            spin_flag = 1
                                        else:
                                            spin_flag = -1
                                        parity = each_s["parity"]
                                        if each_s["parityIsTentative"] == False:
                                            parity_flag = 1
                                        else:
                                            parity_flag = -1

                                energy_alpha, d_energy_alpha = None, None
                                intensity_alpha, d_intensity_alpha = None, None
                                HF, dHF = None, None
                                for each_a in each_l["alphaDecay"]:
                                    energy_alpha = each_a["alphaEnergy"]
                                    d_energy_alpha = each_a["dAlphaEnergy"]
                                    intensity_alpha = each_a["alphaIntensity"]
                                    d_intensity_alpha = each_a["dAlphaIntensity"]
                                    HF = each_a["hindranceFactor"]
                                    dHF = each_a["dHindranceFactor"]


                                a_list.append([level_index, level_energy, num_spins,
                                               spin, spin_flag, parity, parity_flag,
                                               energy_alpha, d_energy_alpha, intensity_alpha,
                                               d_intensity_alpha, HF, dHF])
                                a_list_all.append(a_list[0])
                        a_dict.update({a_tuple:a_list_all})

                if ALPHA_DECAY == False:
                    print("No alpha-decay dataset for parent nucleus.")
                    return
                if ALPHA_DECAY_LEVELS == True:
                    return a_dict
                else:
                    print("No alpha decay observed to low-lying levels.") 
                    return
