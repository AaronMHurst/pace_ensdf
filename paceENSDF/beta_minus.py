from .base_ensdf import *
from .normalization import Normalization
from .parent import Parent
from .daughter import Daughter

class BetaMinus(Daughter):
    __doc__="""Class to handle and manipulate beta-minus decay data from ENSDF 
    data sets."""

    def __init__(self):
        BaseENSDF.__init__(self)
        Normalization.__init__(self)
        Parent.__init__(self)
        Daughter.__init__(self)

    def get_beta_minus(self, list, str, index, **kwargs):
        """Beta-minus decay properties to all states populated following the 
        decay of the associated parent nucleus.

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
            A dictionary of containing beta-minus decay information for the 
            parent-daughter pair.  The dictionary key is a tuple with 
            information associated with the parent nucleus:

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
                 permissable, the first permutation is given:
                 1: Positive parity;
                 -1: Negative parity;
                 0: No parity given.
            [6]: Parity flag (int).  Only permitted integers are: 
                 1: Firm parity assignment; 
                 -1: Tentative parity assignment.
            [7]: End-point energy of beta-minus decay in keV (float); 
            [8]: End-point energy uncertainty (float); 
            [9]: Intensity of beta-minus decay branch(float); 
            [10]: Intensity uncertainty (float); 
            [11]: The logft for the beta-minus transition (float);
            [12]: The logft uncertainty for the transition (float);
            [13]: Average beta-minus energy (float); 
            [14]: Average beta-minus energy uncertainty (float);
            [15]: Forbiddenness classification of the decay (str).  The 
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

            [16]: Forbiddenness classification string (str).  The following 
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

            [17]: Orbital-angular momentum associated with the transition (int).

        Examples:
            get_beta_minus(edata, "Co60", 0, units='best')
            get_beta_minus(edata, "Co60", 0, units='seconds')
            get_beta_minus(edata, "Co60", 0, units='s')
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

            bm_dict = {}
            for jdict in self.list:
                if jdict["decayMode"] == "betaMinusDecay" and self.str == jdict["parentID"] and self.index == jdict["decayIndex"]:

                    bm_list_all = []

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


                    bm_tuple = (pid, pZ, pA, did, dZ, dA, decay_energy, d_decay_energy, spin_parent, spin_parent_flag, parity_parent, parity_parent_flag, thalf, d_thalf, units_thalf)

                    for each_l in jdict["levelScheme"]:
                        bm_list = []
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

                        ep_energy, d_ep_energy = None, None
                        bm_intensity, d_bm_intensity = None, None
                        logft, d_logft = None, None
                        bm_ave_energy, d_bm_ave_energy = None, None
                        forbid_deg, forbid_class, orb_am = None, None, None
                        if len(each_l["betaMinusDecay"]) > 0:
                            for each_b in each_l["betaMinusDecay"]:
                                ep_energy = each_b["endPointBetaMinusEnergy"]
                                d_ep_energy = each_b["dEndPointBetaMinusEnergy"]
                                bm_intensity = each_b["betaMinusIntensity"]
                                d_bm_intensity = each_b["dBetaMinusIntensity"]
                                logft = each_b["logFT"]
                                d_logft = each_b["dLogFT"]
                                bm_ave_energy = each_b["averageBetaMinusEnergy"]
                                d_bm_ave_energy = each_b["dAverageBetaMinusEnergy"]
                                forbid_deg = each_b["forbiddennessDegree"]
                                forbid_class = each_b["forbiddennessClassification"]
                                orb_am = each_b["orbitalAngularMomentum"]

                            bm_list.append([level_index, level_energy, num_spins, spin, spin_flag, parity, parity_flag, ep_energy, d_ep_energy, bm_intensity, d_bm_intensity, logft, d_logft, bm_ave_energy, d_bm_ave_energy, forbid_deg, forbid_class, orb_am])
                            bm_list_all.append(bm_list[0])
                    bm_dict.update({bm_tuple:bm_list_all})

                    return bm_dict
                        
        
    def get_logft(self, list, str, index, **kwargs):
        """The logft values to states populated in beta-decay transitions.

        Arguments:
            list: A list of ENSDF-decay data JSON objects.
            str: A string object describing the parent ID.
            index: An integer object associated with the decay index of the 
                   parent state, where:
                   0: Ground-state decay;
                   >= 1: Isomer decay.
            kwargs: An additional keyword argument is needed for the 
                    appropriate beta-decay mode:

                    mode='BM'
                    mode='ECBP'

                    Only the above keyword arguments (case insensitive) are 
                    acceptable.

        Returns: 
            A list object containing decay-scheme information associated with 
            the residual levels populated in the daughter following the 
            beta-decay (beta-minus or electron-capture/beta-plus) transition:

            [0]: Level index corresponding to populated level (int);
            [1]: Associated level energy populated (float);
            [2]: Number of spin-parity assignments for level (int);
            [3]: Spin assignment for level (float).  If more than one spin is 
                 permissable, the first permutation is given.
            [4]: Spin flag (int).  Only permitted integers are: 
                 1: Firm spin assignment; 
                 -1: Tentative spin assignment.
            [5]: Parity assignment for level (int).  If more than one parity is 
                 permissable, the first permutation is given.  Only permitted 
                 integers are:
                 1: Positive parity; 
                 -1: Negative parity; 
                 0: No parity given.
            [6]: Parity flag (int).  Only permitted integers are: 
                 1: Firm parity assignment; 
                 -1: Tentative parity assignment.
            [7]: Transition logft value (float).
            [8]: Transition logft value uncertainty (float).

        Examples:
            get_logft(edata,"Co60",0,mode='BM')
            get_logft(edata,"Y86",0,mode='ECBP')
        """
        self.list = list
        self.str = str
        self.index = int(index)
        
        if kwargs == {} or kwargs == None:
            print("Please pass one of the following keyword arguments:")
            print("mode='BM'")
            print("mode='ECBP'")

        else:
            decay_mode = None
            decay_mode = BaseENSDF.check_decay([mode for mode in kwargs.values() if mode != None][0])

            if decay_mode == None or decay_mode == 'alphaDecay':
                print("Invalid decay mode.")
            else:
                #print(decay_mode)

                beta_list = []
                for jdict in self.list:
                    if decay_mode == jdict["decayMode"] and self.str == jdict["parentID"] and self.index == jdict["decayIndex"]:
                        for each_l in jdict["levelScheme"]:

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

                            logft, d_logft = None, None

                            if decay_mode == "betaMinusDecay" and len(each_l["betaMinusDecay"]) > 0:
                                for each_b in each_l["betaMinusDecay"]:
                                    if each_b["logFT"] != None:
                                        logft = each_b["logFT"]
                                        d_logft = each_b["dLogFT"]
                                        beta_list.append([level_index, level_energy, num_spins, spin, spin_flag, parity, parity_flag, logft, d_logft])
                                        
                            elif decay_mode == "electronCaptureBetaPlusDecay" and len(each_l["betaPlusDecay"]) > 0:
                                for each_b in each_l["betaPlusDecay"]:
                                    if each_b["logFT"] != None:
                                        logft = each_b["logFT"]
                                        d_logft = each_b["dLogFT"]
                                        beta_list.append([level_index, level_energy, num_spins, spin, spin_flag, parity, parity_flag, logft, d_logft])

                if len(beta_list) > 0:
                    return beta_list
                else:
                    return
                                
            
    def find_forbidden(self, list, *args, **kwargs):
        """Finds all transitions for a given forbiddenness classification 
        depending on input arguments for: 
        
        (i) a defined parent nucleus and beta-decay mode;
        (ii) all decay data sets for a given decay mode.

        Only associated beta-decay transitions where both spin and parity are 
        firmly assigned in both the initial (parent) and final (daughter) state
        are returned.
        
        Arguments:
            list: A list of coincidence-data JSON objects.
            args: Takes either 1 or 3 additional arguments:

                  (i) If 1 args is given:
                  forbiddenness: A string object describing the desired 
                                 forbiddenness classification parent must be 
                                 passed as the first argument.

                  (ii) If 3 args are given:
                  parent: A string object describing the parent ID must be given 
                          as the first argument.
                  index: An integer object associated with the decay index of  
                         the parent state is to be given as the second argument, 
                         where:
                         0: Ground-state decay;
                         >= 1: Isomer decay.
                  forbiddenness: A string object describing the desired 
                                 forbiddenness classification parent must be 
                                 passed as the third argument.

                  Acceptable forbiddenness classifications are to be given as:
                  
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

            kwargs: An additional keyword argument is needed for the desired 
                    beta-decay mode:

                    mode='BM'
                    mode='ECBP'

                    Only the above keyword arguments (case insensitive) are 
                    acceptable.

        Returns: 
            A dictionary object for a given forbiddenness classification and 
            decay mode.  The dictionary key is a tuple describing the 
            corresponding parent-daughter combination:

            [0]: Parent ID (str);
            [1]: Parent atomic (Z) number (int); 
            [2]: Parent mass (A) number (int);
            [3]: Decay-level index of parent nucleus (int);
            [4]: Decay-level energy of parent nucleus (float);
            [5]: Spin of parent nucleus (float); 
            [6]: Spin flag (int).  Only permitted integers are: 
                1: Firm spin assignment; 
                -1: Tentative spin assignment.
            [7]: Parity of parent nucleus (int).  Only permitted integers are:
                1: Positive parity; 
                -1: Negative parity; 
                0: No parity given.
            [8]: Parity flag (int).  Only permitted integers are: 
                1: Firm parity assignment; 
                -1: Tentative parity assignment.
            [9]: Daughter ID (str);
            [10]: Daughter atomic (Z) number (int); 
            [11]: Daughter mass (A) number (int);

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
                 permissable, the first permutation is given.  Only permitted 
                 integers are:
                 1: Positive parity; 
                 -1: Negative parity; 
                 0: No parity given.
            [6]: Parity flag (int).  Only permitted integers are: 
                 1: Firm parity assignment; 
                 -1: Tentative parity assignment.
            [7]: The logft for the beta-decay transition (float);
            [8]: The logft uncertainty for the transition (float);
            [9]: Forbiddenness classification of the decay (str).  The 
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

            [10]: Forbiddenness classification string (str).  The following 
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

            [11]: Delta J for parent and daughter spins associated with the 
                  beta-decay transition (int).
            [12]: Delta pi for parent and daughter parities associated with the 
                  beta-decay transition (int).  Only takes the following 
                  values:
                  
                  1: no parity change between initial and final states;
                  -1: change in parity between initial and final states.

            [13]: Orbital-angular momentum associated with the transition (int).


        Examples:
            To find all 'second-forbidden' transitions in all 
            electron-capture/beta-plus decay data sets:

            find_forbidden(edata,'2F',mode='ECBP')
            
            To find all 'second-forbidden unique' transitions in the 60Co 
            beta-minus decay data set:

            find_forbidden(edata,"Co60",0,'2UF',mode='BM')
        """
        self.list = list
        
        if kwargs == {} or kwargs == None:
            print("Please pass one of the following keyword arguments:")
            print("mode='BM'")
            print("mode='ECBP'")
            return

        else:
            decay_mode = None
            decay_mode = BaseENSDF.check_decay([mode for mode in kwargs.values() if mode != None][0])

            if decay_mode == None or decay_mode == 'alphaDecay':
                print("Invalid decay mode.")
                return
            else:
                #print(decay_mode)

                forbidden = None
                forbidden_dict = {}
                if len(args) == 3:
                    print(args)
                    pid = None
                    decay_index = None

                    try:
                        pid = args[0]
                        decay_index = args[1]
                        forbidden = args[2]
                    except TypeError:
                        raise
                    except IndexError:
                        raise    

                    for jdict in self.list:
                        forbidden_list = []
                        if decay_mode == jdict["decayMode"] and pid == jdict["parentID"] and decay_index == jdict["decayIndex"]:

                            pZ = jdict["parentAtomicNumber"]
                            pA = jdict["parentAtomicMass"]
                            did = jdict["daughterID"]
                            dZ = jdict["daughterAtomicNumber"]
                            dA = jdict["daughterAtomicMass"]

                            decay_energy = None
                            num_parent_spins = None
                            spin_parent, spin_parent_flag = None, None
                            parity_parent, parity_parent_flag = None, None

                            for each_p in jdict["parentDecay"]:
                                num_parent_spins = each_p["numberOfSpins"]
                                decay_energy = each_p["parentDecayLevelEnergy"]
                                #d_decay_energy = each_p["dParentDecayLevelEnergy"]

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

                            forbidden_tuple = (pid, pZ, pA, decay_index, decay_energy, spin_parent, spin_parent_flag, parity_parent, parity_parent_flag, did, dZ, dA)

                            for each_l in jdict["levelScheme"]:

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

                                forbidden_class = None
                                sel_rules_delta_j, sel_rules_del_pi = None, None
                                orb_am = None
                                logft, d_logft = None, None

                                decay_mode_str = None
                                if decay_mode == "betaMinusDecay":
                                    decay_mode_str = decay_mode
                                elif decay_mode == "electronCaptureBetaPlusDecay":
                                    decay_mode_str = "betaPlusDecay"
                                #if len(each_l["betaMinusDecay"]) > 0:
                                if len(each_l["%s"%decay_mode_str]) > 0:
                                    #for each_b in each_l["betaMinusDecay"]:
                                    for each_b in each_l["%s"%decay_mode_str]:
                                        if forbidden == each_b["forbiddennessDegree"]:
                                            logft = each_b["logFT"]
                                            d_logft = each_b["dLogFT"]
                                            forbidden_class = each_b["forbiddennessClassification"]
                                            sel_rules_delta_j = each_b["selectionRulesDeltaJ"]
                                            sel_rules_delta_pi = each_b["selectionRulesDeltaPi"]
                                            orb_am = each_b["orbitalAngularMomentum"]

                                            forbidden_list.append([level_index, level_energy, num_spins, spin, spin_flag, parity, parity_flag, logft, d_logft, forbidden, forbidden_class, sel_rules_delta_j, sel_rules_delta_pi, orb_am])

                            forbidden_dict.update({forbidden_tuple: forbidden_list})

                    if len(forbidden_dict) > 0:
                        return forbidden_dict
                    else:
                        return


                elif len(args) == 1:
                    try:
                        forbidden = str(args[0])
                    except TypeError:
                        raise
                    except IndexError:
                        raise    

                    for jdict in self.list:
                        forbidden_list = []
                        if decay_mode == jdict["decayMode"]:

                            pid = jdict["parentID"]
                            decay_index = jdict["decayIndex"]

                            pZ = jdict["parentAtomicNumber"]
                            pA = jdict["parentAtomicMass"]
                            did = jdict["daughterID"]
                            dZ = jdict["daughterAtomicNumber"]
                            dA = jdict["daughterAtomicMass"]

                            decay_energy = None
                            num_parent_spins = None
                            spin_parent, spin_parent_flag = None, None
                            parity_parent, parity_parent_flag = None, None

                            for each_p in jdict["parentDecay"]:
                                num_parent_spins = each_p["numberOfSpins"]
                                decay_energy = each_p["parentDecayLevelEnergy"]
                                #d_decay_energy = each_p["dParentDecayLevelEnergy"]

                                if num_parent_spins == 1:
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
                                                
                                            if each_ps["spinIsTentative"] == False and each_ps["parityIsTentative"] == False:

                                                forbidden_tuple = (pid, pZ, pA, decay_index, decay_energy, spin_parent, spin_parent_flag, parity_parent, parity_parent_flag, did, dZ, dA)

                                                for each_l in jdict["levelScheme"]:

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

                                                    forbidden_class = None
                                                    sel_rules_delta_j, sel_rules_del_pi = None, None
                                                    orb_am = None
                                                    logft, d_logft = None, None

                                                    decay_mode_str = None
                                                    if decay_mode == "betaMinusDecay":
                                                        decay_mode_str = decay_mode
                                                    elif decay_mode == "electronCaptureBetaPlusDecay":
                                                        decay_mode_str = "betaPlusDecay"
                                                    #if len(each_l["betaMinusDecay"]) > 0:            
                                                    if len(each_l["%s"%decay_mode_str]) > 0:
                                                        #for each_b in each_l["betaMinusDecay"]:
                                                        for each_b in each_l["%s"%decay_mode_str]:
                                                            if forbidden == each_b["forbiddennessDegree"]:
                                                                logft = each_b["logFT"]
                                                                d_logft = each_b["dLogFT"]
                                                                forbidden_class = each_b["forbiddennessClassification"]
                                                                sel_rules_delta_j = each_b["selectionRulesDeltaJ"]
                                                                sel_rules_delta_pi = each_b["selectionRulesDeltaPi"]
                                                                orb_am = each_b["orbitalAngularMomentum"]

                                                                forbidden_list.append([level_index, level_energy, num_spins, spin, spin_flag, parity, parity_flag, logft, d_logft, forbidden, forbidden_class, sel_rules_delta_j, sel_rules_delta_pi, orb_am])

                                                    if len(forbidden_list) > 0:
                                                        forbidden_dict.update({forbidden_tuple: forbidden_list})            

                    if len(forbidden_dict) > 0:
                        return forbidden_dict
                    else:
                        return
                    

