from .base_ensdf import *
from .normalization import Normalization
from .parent import Parent
from .daughter import Daughter
from .beta_minus import BetaMinus

class ElectronCaptureBetaPlus(BetaMinus):
    __doc__="""Class to handle and manipulate electron-capture/beta-plus decay 
    data from ENSDF data sets."""

    def __init__(self):
        BaseENSDF.__init__(self)
        Normalization.__init__(self)
        Parent.__init__(self)
        Daughter.__init__(self)
        BetaMinus.__init__(self)

    def get_ecbp(self, list, str, index, **kwargs):
        """Electron-capture/beta-plus decay properties to all states populated 
        following the decay of the associated parent nucleus.

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
            A dictionary of containing electron-capture/beta-plus decay 
            information for the parent-daughter pair.  The dictionary key is a 
            tuple with information associated with the parent nucleus:

            [0]: Parent ID (str);
            [1]: Parent atomic (Z) number (int); 
            [2]: Parent mass (A) number (int);
            [3]: Daughter ID (str);
            [4]: Daughter atomic (Z) number (int); 
            [5]: Daughter mass (A) number (int);
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
            [7]: Electron-capture energy to level in keV (float); 
            [8]: Electron-capture energy uncertainty (float); 
            [9]: Electron-capture intensity (float); 
            [10]: Electron-capture intensity uncertainty (float); 
            [11]: Average beta-plus energy (float); 
            [12]: Average beta-plus energy uncertainty (float);
            [13]: Intensity of beta-plus decay branch (float);
            [14]: Intensity of beta-plus decay branch uncertainty (float);
            [15]: Total electron-capture and beta-plus decay intensity (float);
            [16]: Total decay intensity uncertainty (float);
            [17]: The logft for the transition (float);
            [18]: The logft uncertainty for the transition (float);
            [19]: End-point energy for beta-plus decay (float);
            [20]: End-point energy uncertainty for beta-plus decay (float);
            [21]: Forbiddenness classification of the decay (str).  The 
                  following classifications are used:

                  '0A': Allowed or allowed Gamow-Teller;
                  '1F': First forbidden;
                  '1UF': First-forbidden unique;
                  '2F': Second forbidden;
                  '2UF': Second-forbidden unique;
                  '3F': Third forbidden;
                  '3UF': Third-forbidden unique;
                  '4F': Fourth forbidden;
                  '4UF': Fourth-forbidden unique;
                  '5F': Fifth forbidden;
                  '5UF': Fifth-forbidden unique.

            [22]: Forbiddenness classification string (str).  The following 
                  strings are used to describe the transition forbiddenness:
                  
                  'allowed';
                  'allowedGamowTeller;;
                  'firstForbidden';
                  'firstForbiddenUnique';
                  'secondForbidden';
                  'secondForbiddenUnique';
                  'thirdForbidden';
                  'thirdForbiddenUnique';
                  'fourthForbidden';
                  'fourthForbiddenUnique';
                  'fifthForbidden';
                  'fifthForbiddenUnique'.

            [23]: Orbital-angular momentum associated with the transition (int).

        Examples:
            get_ecbp(edata, "Y86", 0, units='best')
            get_ecbp(edata, "Y86", 0, units='seconds')
            get_ecbp(edata, "Y86", 0, units='s')
        """
        self.list = list
        self.str = str
        self.index = int(index)
        
        BEST_UNITS = False
        WRONG_UNITS = True
        units = BaseENSDF.check_time_units([unit for unit in kwargs.values()][0])

        if units == None:
            return
        else:
            WRONG_UNITS = False
            if units == 'best':
                BEST_UNITS = True

            bp_dict = {}
            for jdict in self.list:
                if jdict["decayMode"] == "electronCaptureBetaPlusDecay" and self.str == jdict["parentID"] and self.index == jdict["decayIndex"]:

                    bp_list_all = []

                    pid = jdict["parentID"]
                    decay_index = jdict["decayIndex"]
                    pZ = jdict["parentAtomicNumber"]
                    pA = jdict["parentAtomicMass"]
                    did = jdict["daughterID"]
                    dZ = jdict["daughterAtomicNumber"]
                    dA = jdict["daughterAtomicMass"]

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

                    bp_tuple = (pid, pZ, pA, did, dZ, dA, decay_energy, d_decay_energy,
                                spin_parent, spin_parent_flag, parity_parent, parity_parent_flag,
                                thalf, d_thalf, units_thalf)

                    for each_l in jdict["levelScheme"]:
                        bp_list = []
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

                        # ec_energy => energy for EC to level; given only if measured
                        # or deduced from beta-plus end-point energy
                        # ep_bp_energy => end-point BP energy

                        ec_energy, d_ec_energy = None, None
                        ec_intensity, d_ec_intensity = None, None
                        bp_ave_energy, d_bp_ave_energy = None, None
                        bp_intensity, d_bp_intensity = None, None
                        tot_ecbp_intensity, d_tot_ecbp_intensity = None, None
                        logft, d_logft = None, None
                        ep_bp_energy, d_ep_bp_energy = None, None
                        forbid_deg, forbid_class, orb_am = None, None, None
                        if len(each_l["betaPlusDecay"]) > 0:
                            for each_b in each_l["betaPlusDecay"]:
                                ec_energy = each_b["electronCaptureEnergy"]
                                d_ec_energy = each_b["dElectronCaptureEnergy"]
                                ec_intensity = each_b["electronCaptureIntensity"]
                                d_ec_intensity = each_b["dElectronCaptureIntensity"]
                                bp_ave_energy = each_b["averageBetaPlusEnergy"]
                                d_bp_ave_energy = each_b["dAverageBetaPlusEnergy"]
                                bp_intensity = each_b["betaPlusIntensity"]
                                d_bp_intensity = each_b["dBetaPlusIntensity"]
                                tot_ecbp_intensity = each_b["totalElectronCaptureBetaPlusIntensity"]
                                d_tot_ecbp_intensity = each_b["dTotalElectronCaptureBetaPlusIntensity"]
                                logft = each_b["logFT"]
                                d_logft = each_b["dLogFT"]
                                ep_bp_energy = each_b["endPointBetaPlusEnergy"]
                                d_ecp_bp_energy = each_b["dEndPointBetaPlusEnergy"]
                                forbid_deg = each_b["forbiddennessDegree"]
                                forbid_class = each_b["forbiddennessClassification"]
                                orb_am = each_b["orbitalAngularMomentum"]

                            bp_list.append([level_index, level_energy, num_spins,
                                           spin, spin_flag, parity, parity_flag,
                                           ec_energy, d_ec_energy, ec_intensity, d_ec_intensity,
                                           bp_ave_energy, d_bp_ave_energy, bp_intensity, d_bp_intensity,
                                           tot_ecbp_intensity, d_tot_ecbp_intensity, logft, d_logft, 
                                           ep_bp_energy, d_ep_bp_energy, forbid_deg, forbid_class, orb_am])
                            bp_list_all.append(bp_list[0])
                    bp_dict.update({bp_tuple:bp_list_all})

                    return bp_dict

    def get_ec_fractions(self, list, str, index, **kwargs):
        """Electron-capture decay fractions to all states populated 
        following the decay of the associated parent nucleus.

        Arguments:
            list: A list of ENSDF-decay data JSON objects.
            str: A string object describing the parent ID.
            index: An integer object associated with the decay index of the 
                   parent state, where:
                   0: Ground-state decay;
                   >= 1: Isomer decay.
            kwargs: An additional keyword argument is needed for the desired 
                    atomic-shell electron-capture data:

                    subshell='calc'
                    subshell='sumcalc'
                    subshell='expt'

                    Only the above keyword arguments (case insensitive) are 
                    acceptable.  

        Returns: 
            A list object containing electron-capture/beta-plus decay 
            information associated with levels populated in the corresponding 
            daughter nucleus.  The keyword argument passed to the function 
            defines the output:

            (i) subshell='calc':

            Calculated fraction of decay by electron capture from the K, L, M, 
            N, O, P, and Q shells:

            [0]: Level index corresponding to populated level (int);
            [1]: Associated level energy populated (float);
            [2]: Calculated fraction from the K-shell (float);
            [3]: Calculated fraction from the K-shell uncertainty (float);
            [4]: Calculated fraction from the L-shell (float);
            [5]: Calculated fraction from the L-shell uncertainty (float);
            [6]: Calculated fraction from the M-shell (float);
            [7]: Calculated fraction from the M-shell uncertainty (float);
            [8]: Calculated fraction from the N-shell (float);
            [9]: Calculated fraction from the N-shell uncertainty (float);
            [10]: Calculated fraction from the O-shell (float);
            [11]: Calculated fraction from the O-shell uncertainty (float);
            [12]: Calculated fraction from the P-shell (float);
            [13]: Calculated fraction from the P-shell uncertainty (float);
            [14]: Calculated fraction from the Q-shell (float);
            [15]: Calculated fraction from the Q-shell uncertainty (float).

            (ii) subshell='sumcalc':

            Summed calculated fraction of decay by electron capture from the 
            L+, M+, N+, O+, P+, and Q+ (where, e.g., L+ is the sum of 
            atomic-shell contributions from L to Q) shells:

            [0]: Level index corresponding to populated level (int);
            [1]: Associated level energy populated (float);
            [2]: Summed calculated contribution from the L+ shells (float);
            [3]: L+ shell contribution uncertainty (float);
            [4]: Summed calculated contribution from the M+ shells (float);
            [5]: M+ shell contribution uncertainty (float);
            [6]: Summed calculated contribution from the N+ shells (float);
            [7]: N+ shell contribution uncertainty (float);
            [8]: Summed calculated contribution from the O+ shells (float);
            [9]: O+ shell contribution uncertainty (float);
            [10]: Summed calculated contribution from the P+ shells (float);
            [11]: P+ shell contribution uncertainty (float);
            [12]: Summed calculated contribution from the Q+ shells (float);
            [13]: Q+ shell contribution uncertainty (float);

            (iii) subshell='expt':

            Measured fraction of decay by electron capture from the K, L, M, 
            and N shells:

            [0]: Level index corresponding to populated level (int);
            [1]: Associated level energy populated (float);
            [2]: Measured fraction from the K-shell (float);
            [3]: Measured fraction from the K-shell uncertainty (float);
            [4]: Measured fraction from the L-shell (float);
            [5]: Measured fraction from the L-shell uncertainty (float);
            [6]: Measured fraction from the M-shell (float);
            [7]: Measured fraction from the M-shell uncertainty (float);
            [8]: Measured fraction from the N-shell (float);
            [9]: Measured fraction from the N-shell uncertainty (float);

        Examples:
            get_ec_fractions(edata, "Y86", 0, subshell='calc')
            get_ec_fractions(edata, "Y86", 0, subshell='sumcalc')
            get_ec_fractions(edata, "Y86", 0, subshell='expt')
        """
        self.list = list
        self.str = str
        self.index = int(index)
        
        if kwargs == {} or kwargs == None:
            print("Please pass one of the following keyword arguments:")
            print("subshell='calc'")
            print("subshell='sumcalc'")
            print("subshell='expt'")

        else:
            # Check for subshell keyword:
            SUBSHELL_TYPE = False
            SUBSHELL_CALC = False
            SUBSHELL_SUMCALC = False
            SUBSHELL_EXPT = False

            for subshell in kwargs.values():
                if subshell=='calc': 
                    SUBSHELL_TYPE = True
                    SUBSHELL_CALC = True
                elif subshell=='sumcalc': 
                    SUBSHELL_TYPE = True
                    SUBSHELL_SUMCALC = True
                elif subshell=='expt': 
                    SUBSHELL_TYPE = True
                    SUBSHELL_EXPT = True
                #else:
            if SUBSHELL_TYPE == False:
                print("Inavlid atomic-subshell argument.  The only arguements accepted are:")
                print("subshell='calc'")
                print("subshell='sumcalc'")
                print("subshell='expt'")

            elif SUBSHELL_TYPE == True:
                bp_list = []
                ECBP_DECAY_LEVELS = False
                for jdict in self.list:
                    #if decay_mode == jdict["decayMode"] and str == jdict["parentID"] and index == jdict["decayIndex"]:
                    if jdict["decayMode"] == "electronCaptureBetaPlusDecay" and self.str == jdict["parentID"] and self.index == jdict["decayIndex"]:

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

                        for each_l in jdict["levelScheme"]:
                            if len(each_l["betaPlusDecay"]) > 0:
                                ECBP_DECAY_LEVELS = True
                                level_index = each_l["levelIndex"]
                                level_energy = each_l["levelEnergy"]

                                # Append list according to subshell keyword argument

                                sub_K, d_sub_K = None, None
                                sub_L, d_sub_L = None, None
                                sub_M, d_sub_M = None, None
                                sub_N, d_sub_N = None, None
                                sub_O, d_sub_O = None, None
                                sub_P, d_sub_P = None, None
                                sub_Q, d_sub_Q = None, None

                                for each_bp in each_l["betaPlusDecay"]:

                                    if SUBSHELL_CALC == True:
                                        for each_ss in each_bp["calculatedAtomicShellElectronCaptureFractions"]:
                                            sub_K = each_ss["calculatedElectronCaptureFractionAtomicShellK"]
                                            d_sub_K = each_ss["dCalculatedElectronCaptureFractionAtomicShellK"]
                                            sub_L = each_ss["calculatedElectronCaptureFractionAtomicShellL"]
                                            d_sub_L = each_ss["dCalculatedElectronCaptureFractionAtomicShellL"]
                                            sub_M = each_ss["calculatedElectronCaptureFractionAtomicShellM"]
                                            d_sub_M = each_ss["dCalculatedElectronCaptureFractionAtomicShellM"]
                                            sub_N = each_ss["calculatedElectronCaptureFractionAtomicShellN"]
                                            d_sub_N = each_ss["dCalculatedElectronCaptureFractionAtomicShellN"]
                                            sub_O = each_ss["calculatedElectronCaptureFractionAtomicShellO"]
                                            d_sub_O = each_ss["dCalculatedElectronCaptureFractionAtomicShellO"]
                                            sub_P = each_ss["calculatedElectronCaptureFractionAtomicShellP"]
                                            d_sub_P = each_ss["dCalculatedElectronCaptureFractionAtomicShellP"]
                                            sub_Q = each_ss["calculatedElectronCaptureFractionAtomicShellQ"]
                                            d_sub_Q = each_ss["dCalculatedElectronCaptureFractionAtomicShellQ"]

                                        bp_list.append([level_index, level_energy, sub_K, d_sub_K, sub_L, d_sub_L, sub_M, d_sub_M, sub_N, d_sub_N, sub_O, d_sub_O, sub_P, d_sub_P, sub_Q, d_sub_Q])

                                    elif SUBSHELL_SUMCALC == True:
                                        for each_ss in each_bp["sumCalculatedAtomicShellElectronCaptureFractions"]:
                                            sub_L = each_ss["sumElectronCaptureFractionAtomicShellPlusL"]
                                            d_sub_L = each_ss["dSumElectronCaptureFractionAtomicShellPlusL"]
                                            sub_M = each_ss["sumElectronCaptureFractionAtomicShellPlusM"]
                                            d_sub_M = each_ss["dSumElectronCaptureFractionAtomicShellPlusM"]
                                            sub_N = each_ss["sumElectronCaptureFractionAtomicShellPlusN"]
                                            d_sub_N = each_ss["dSumElectronCaptureFractionAtomicShellPlusN"]
                                            sub_O = each_ss["sumElectronCaptureFractionAtomicShellPlusO"]
                                            d_sub_O = each_ss["dSumElectronCaptureFractionAtomicShellPlusO"]
                                            sub_P = each_ss["sumElectronCaptureFractionAtomicShellPlusP"]
                                            d_sub_P = each_ss["dSumElectronCaptureFractionAtomicShellPlusP"]
                                            sub_Q = each_ss["sumElectronCaptureFractionAtomicShellPlusQ"]
                                            d_sub_Q = each_ss["dSumElectronCaptureFractionAtomicShellPlusQ"]

                                        bp_list.append([level_index, level_energy, sub_L, d_sub_L, sub_M, d_sub_M, sub_N, d_sub_N, sub_O, d_sub_O, sub_P, d_sub_P, sub_Q, d_sub_Q])

                                    elif SUBSHELL_EXPT == True:
                                        for each_ss in each_bp["experimentalAtomicShellElectronCaptureFractions"]:
                                            sub_K = each_ss["experimentalElectronCaptureFractionAtomicShellK"]
                                            d_sub_K = each_ss["dExperimentalElectronCaptureFractionAtomicShellK"]
                                            sub_L = each_ss["experimentalElectronCaptureFractionAtomicShellL"]
                                            d_sub_L = each_ss["dExperimentalElectronCaptureFractionAtomicShellL"]
                                            sub_M = each_ss["experimentalElectronCaptureFractionAtomicShellM"]
                                            d_sub_M = each_ss["dExperimentalElectronCaptureFractionAtomicShellM"]
                                            sub_N = each_ss["experimentalElectronCaptureFractionAtomicShellN"]
                                            d_sub_N = each_ss["dExperimentalElectronCaptureFractionAtomicShellN"]

                                        bp_list.append([level_index, level_energy, sub_K, d_sub_K, sub_L, d_sub_L, sub_M, d_sub_M, sub_N, d_sub_N])


                if ECBP_DECAY_LEVELS == True:
                    return bp_list
                else:
                    print("No EC/BP decay observed to low-lying levels.")
