from .base_ensdf import *
from .normalization import Normalization
from .parent import Parent
from .daughter import Daughter
from .beta_minus import BetaMinus
from .electron_capture_beta_plus import ElectronCaptureBetaPlus
from .alpha import Alpha

class GammaGamma(Alpha):
    __doc__="""Class to handle and manipulate coincidence gamma/gamma data 
    sets."""

    def __init__(self):
        BaseENSDF.__init__(self)
        Normalization.__init__(self)
        Parent.__init__(self)
        Daughter.__init__(self)
        BetaMinus.__init__(self)
        ElectronCaptureBetaPlus.__init__(self)
        Alpha.__init__(self)

    def get_gg(self, list, str, *args):
        """Gamma/gamma coincidence data for: (i) a given decay scheme (defined 
        by parent nucleus), or (ii) a particular transition within a given 
        decay scheme (defined by parent nucleus and transition indices 
        associated with the decay of the daughter nucleus).

        Arguments:
            list: A list of coincidence-data JSON objects.
            str: A string object describing the decay mode:
                  "BM": Beta-minus decay;
                  "ECBP": Electron-capture/beta-plus decay;
                  "A": Alpha decay.
            args: Takes either 2 or 4 additional arguments:

                  (i) If 2 args are given:
                  parent: A string object describing the parent ID must be given
                          as the first argument.
                  index: An integer object associated with the decay index of 
                         the parent state is to be given as the second argument,
                         where:
                         0: Ground-state decay;
                         >= 1: Isomer decay.

                  (ii) If 4 args are given:
                  parent: A string object describing the parent ID must be given
                          as the first argument.
                  index: An integer object associated with the decay index of 
                         the parent state is to be given as the second argument,
                         where:
                         0: Ground-state decay;
                         >= 1: Isomer decay.
                  level_i: An integer object corresponding to the initial level 
                           index associated with the gamma decay passed as the
                           third argument.
                  level_f: An integer object corresponding to the final level 
                           index associated with the gamma decay passed as the 
                           fourth argument.
        
        Returns:
            A list of lists containing coincident gammas and X rays.  The list 
            elements in each sublist correspond to:

            [0]: Gamma-ray energy gate (float);
            [1]: Coincident gamma-ray energy (float);
            [2]: Associated initial level index of gamma gate (int);
            [3]: Associated final level index of gamma gate (int);
            [4]: Associated initial level energy of gamma gate (float);
            [5]: Associated final level energy of gamma gate (float);
            [6]: Associated initial level index of coincident gamma (int);
            [7]: Associated final level index of coincident gamma (int);
            [8]: Associated initial level energy of coincident gamma (float);
            [9]: Associated final level energy of coincident gamma (float);
            [10]: Absolute gamma/gamma coincident intensity (float);
            [11]: Coincident-intensity uncertainty (float).

        Examples:
            (i) All coincidences in 60Ni following beta-minus decay of 60Co in 
            its ground state:

            get_gg(cdata, "BM", "Co60", 0)

            (ii) All transitions in coincidence with the 2->1 transition in 
            60Ni following beta-minus decay of 60Co in its ground state:

            get_gg(cdata, "BM", "Co60", 0, 2, 1)
        """
        self.list = list
        self.str = str
        NUM_ARGS_OK = False
        coinc_list = []
        DAUGHTER_EXISTS = False
        COINCIDENCE = False
        if len(args) == 2:
            #try:
            #    pid = str(args[0])
            #    decay_index = int(args[1])
            #except TypeError:
            #    pid = str(args[1])
            #    decay_index = int(args[0])
            NUM_ARGS_OK = True
            pid = args[0]
            decay_index = args[1]

            decay_mode = BaseENSDF.check_decay(self.str)
            if decay_mode == None:
                print("Invalid decay mode.")
                return
            else:
                #coinc_list = []
                #DAUGHTER_EXISTS = False
                for jdict in self.list:
                    if jdict["datasetID"] == "GG":
                        if jdict["parentID"] == pid and jdict["decayMode"] == decay_mode and jdict["decayIndex"] == decay_index:
                            DAUGHTER_EXISTS = True
                            for each_c in jdict["decayCoincidences"]:
                                gamma_gate = each_c["gammaEnergyGate"]
                                gamma_coinc = each_c["gammaEnergyCoincidence"]
                                
                                gate_index_i = each_c["gammaGateLevelIndexInitial"]
                                gate_index_f = each_c["gammaGateLevelIndexFinal"]
                                gate_level_i = each_c["gammaGateLevelEnergyInitial"]
                                gate_level_f = each_c["gammaGateLevelEnergyFinal"]
                                
                                coinc_index_i = each_c["gammaCoincidenceLevelIndexInitial"]
                                coinc_index_f = each_c["gammaCoincidenceLevelIndexFinal"]
                                coinc_level_i = each_c["gammaCoincidenceLevelEnergyInitial"]
                                coinc_level_f = each_c["gammaCoincidenceLevelEnergyFinal"]

                                abs_coinc_intensity = each_c["absoluteCoincidenceIntensity"]
                                d_abs_coinc_intensity = each_c["dAbsoluteCoincidenceIntensity"]

                                coinc_list.append([gamma_gate, gamma_coinc, gate_index_i, gate_index_f, gate_level_i, gate_level_f, coinc_index_i, coinc_index_f, coinc_level_i, coinc_level_f, abs_coinc_intensity, d_abs_coinc_intensity])

                

                #return sorted(coinc_list)

        elif len(args) == 4:
            NUM_ARGS_OK = True
            pid = args[0]
            decay_index = args[1]
            i_level = args[2]
            f_level = args[3]
            
            decay_mode = BaseENSDF.check_decay(self.str)
            if decay_mode == None:
                print("Invalid decay mode.")
                return
            else:
                #coinc_list = []
                #DAUGHTER_EXISTS = False
                #COINCIDENCE = False
                for jdict in self.list:
                    if jdict["datasetID"] == "GG":
                        if jdict["parentID"] == pid and jdict["decayMode"] == decay_mode and jdict["decayIndex"] == decay_index:
                            DAUGHTER_EXISTS = True
                            for each_c in jdict["decayCoincidences"]:
                                gamma_gate = each_c["gammaEnergyGate"]
                                gamma_coinc = each_c["gammaEnergyCoincidence"]
                                
                                gate_index_i = int(each_c["gammaGateLevelIndexInitial"])
                                gate_index_f = int(each_c["gammaGateLevelIndexFinal"])
                                gate_level_i = each_c["gammaGateLevelEnergyInitial"]
                                gate_level_f = each_c["gammaGateLevelEnergyFinal"]
                                
                                coinc_index_i = int(each_c["gammaCoincidenceLevelIndexInitial"])
                                coinc_index_f = int(each_c["gammaCoincidenceLevelIndexFinal"])
                                coinc_level_i = each_c["gammaCoincidenceLevelEnergyInitial"]
                                coinc_level_f = each_c["gammaCoincidenceLevelEnergyFinal"]

                                abs_coinc_intensity = each_c["absoluteCoincidenceIntensity"]
                                d_abs_coinc_intensity = each_c["dAbsoluteCoincidenceIntensity"]

                                if (int(i_level) == gate_index_i) and (int(f_level) == gate_index_f):
                                    COINCIDENCE = True
                                    coinc_list.append([gamma_gate, gamma_coinc, gate_index_i, gate_index_f, gate_level_i, gate_level_f, coinc_index_i, coinc_index_f, coinc_level_i, coinc_level_f, abs_coinc_intensity, d_abs_coinc_intensity])

                                elif (int(i_level) == coinc_index_i) and (int(f_level) == coinc_index_f):
                                    COINCIDENCE = True
                                    coinc_list.append([gamma_coinc, gamma_gate, coinc_index_i, coinc_index_f, coinc_level_i, coinc_level_f, gate_index_i, gate_index_f, gate_level_i, gate_level_f, abs_coinc_intensity, d_abs_coinc_intensity])

                if COINCIDENCE == False:
                    print("No gamma/gamma coincidences for defined gating-transition indices")
                    return
                #else:
                #    return sorted(coinc_list)

        else:
            print("Wrong number of input arguments")
            print("Function needs to be called using one of the following methods, e.g.:")
            print("e.get_gg(cdata, \"BM\", \"Co60\", 0)")
            print("e.get_gg(cdata, \"BM\", \"Co60\", 0, 2, 1)")
            return

        if len(args) == 2 and NUM_ARGS_OK == True and DAUGHTER_EXISTS == True:
            return sorted(coinc_list)
        elif len(args) == 4 and NUM_ARGS_OK == True and DAUGHTER_EXISTS == True and COINCIDENCE == True:
            return sorted(coinc_list)
        else:
            return
            

    def get_gamma_singles(self, list, mode, parent, index):
        """Absolute gamma-ray intensities from total-projection singles spectra.

        Arguments:
            list: A list of coincidence-data JSON objects.
            mode: A string object describing the decay mode:
                  "BM": Beta-minus decay;
                  "ECBP": Electron-capture/beta-plus decay;
                  "A": Alpha decay.
            parent: A string object describing the parent ID.
            index: An integer object associated with the decay index of the 
                   parent state, where:
                   0: Ground-state decay;
                   >= 1: Isomer decay.
        
        Returns: 
            A list containing gamma-ray energies, intensities and associated 
            decay-scheme information.  The elements in each sublist 
            correspond to:

            [0]: Gamma-ray energy in keV (float);
            [1]: Associated initial level index (int);
            [2]: Associated final level index (int);
            [3]: Associated initial level energy (float);
            [4]: Associated final level energy (float);
            [5]: Absolute gamma-ray intensity in percent (float);
            [6]: Absolute-intensity uncertainty (float).


        Example:
            get_gamma_singles(cdata, "BM", "Co60", 0)
        """
        self.list = list
        self.mode = mode
        self.parent = parent
        self.index = index

        decay_mode = BaseENSDF.check_decay(self.mode)
        singles_list = []
        DAUGHTER_EXISTS = False
        for jdict in self.list:
            if jdict["datasetID"] == "GG":
                if jdict["parentID"] == self.parent and jdict["decayMode"] == decay_mode and jdict["decayIndex"] == self.index:
                    DAUGHTER_EXISTS = True
                    for each_s in jdict["decaySingles"]:
                        gamma_energy = each_s["gammaEnergy"]
                        i_level_index = each_s["levelIndexInitial"]
                        f_level_index = each_s["levelIndexFinal"]
                        i_level_energy = each_s["levelEnergyInitial"]
                        f_level_energy = each_s["levelEnergyFinal"]
                        abs_intensity = each_s["absoluteGammaIntensity"]
                        d_abs_intensity = each_s["dAbsoluteGammaIntensity"]

                        singles_list.append([gamma_energy, i_level_index, f_level_index, i_level_energy, f_level_energy, abs_intensity, d_abs_intensity])

        if DAUGHTER_EXISTS == True:
            return sorted(singles_list)
        else:
            return

    def find_gamma(self, list, float, tolerance=0.5):
        """Searches for all gamma rays at a specified energy.  By default the 
        search will find all gamma rays within +/- 0.5 keV of the specified 
        energy passed to the function.

        Arguments:
            list: A list of coincidence-data JSON objects.
            float: Gamma-ray energy in keV (float).
            tolerance: Limit of the energy search; by default +/- 0.5 keV.

        Returns: 
            A DataFrame object containing the parent isotope, parent-decay 
            index, parent-decay energy, daughter isotope, decay mode, 
            gamma-ray energy.
        
        Examples:
            (i) Find all isotopes containing gamma rays within 1332+/-0.5 keV:
            
            find_gamma(cdata, 1332) 
                
            (ii) Finds all isotopes containing gamma rays within 1332+/-2.3 keV:

            find_gamma(cdata, 1332, 2.3)
        """
        self.list = list
        self.float = float

        isotope_list = []
        FOUND_GAMMA = False
        for jdict in self.list:
            if jdict["datasetID"] == "GG":
                for each_s in jdict["decaySingles"]:
                    gamma_energy = each_s["gammaEnergy"]

                    #if gamma_energy > (self.float - 0.5) and gamma_energy < (self.float + 0.5):
                    if gamma_energy > (self.float - tolerance) and gamma_energy < (self.float + tolerance):
                        FOUND_GAMMA = True
                        pid = jdict["parentID"]
                        did = jdict["daughterID"]
                        decay_mode = jdict["decayMode"]
                        decay_index = jdict["decayIndex"]
                        decay_energy = jdict["parentDecayLevelEnergy"]
                        abs_intensity = each_s["absoluteGammaIntensity"]
                        d_abs_intensity = each_s["dAbsoluteGammaIntensity"]
                        
                        isotope_list.append([pid, int(decay_index), decay_energy, did, decay_mode, gamma_energy, abs_intensity, d_abs_intensity])

        try:
            isotope_array = np.array(isotope_list)
            pid = isotope_array[:,0].astype(str)
            decay_index = isotope_array[:,1].astype(int)
            decay_energy = isotope_array[:,2]
            did = isotope_array[:,3].astype(str)
            decay_mode = isotope_array[:,4].astype(str)
            gamma_energy = isotope_array[:,5]
            abs_intensity = isotope_array[:,6]
            d_abs_intensity = isotope_array[:,7]
        
            #isotope_df = pd.DataFrame({'Parent':pid, 'Energy': decay_energy, 'Daughter':did, 'Decay': decay_mode, 'Gamma': gamma_energy, 'I': abs_intensity, 'dI': d_abs_intensity})
            isotope_df = pd.DataFrame({'Parent':pid, 'Decay Index':decay_index, 'Ex. Energy': decay_energy, 'Daughter':did, 'Decay Mode': decay_mode, 'Gamma': gamma_energy})

            pd.set_option('display.max_columns', None)
            pd.set_option('display.max_row', None)

            if FOUND_GAMMA == True:
                return isotope_df
            #else:
            #    return
            
        except IndexError:
            if FOUND_GAMMA == False:
                print("No decay gammas match specified search criterion: {0} \xb1 {1} keV.\nTry a different energy or expand the search window by adjusting the tolerance.".format(self.float,tolerance))
                return
            else:
                raise

    def find_gamma_coinc(self, list, gamma1, gamma2, tolerance=0.5):
        """Searches for all pairs of gamma rays at the energies specified.  By 
        default the tolerance window will search within +/- 0.5 keV of the 
        specified energies passed to the function.

        Arguments:
            list: A list of coincidence-data JSON objects.
            gamma1: Energy in keV of first gamma (float).
            gamma2: Energy in keV of second gamma (float).
            tolerance: Limit of the energy search; by default +/- 0.5 keV.

        Returns: 
            A DataFrame object containing the parent isotope, parent-decay 
            index, parent-decayenergy, daughter isotope, decay mode, 
            first (gate) gamma-ray energy, second (coincidence) gamma-ray 
            energy.
        
        Examples:
            (i) Find all isotopes containing 1332/1173 gamma/gamma 
            coincidences within a tolerance window of +/-0.5 keV:
            
            find_gamma_coinc(cdata, 1332, 1173) 
                
            (ii) Finds all isotopes containing 1332/1173 gamma/gamma 
            coincidences within a tolerance window of +/-2.3 keV:

            find_gamma_coinc(cdata, 1332, 1173, 2.3)
        """
        self.list = list
        self.gamma1 = gamma1
        self.gamma2 = gamma2

        isotope_list = []
        FOUND_GAMMA = False
        for jdict in self.list:
            if jdict["datasetID"] == "GG":
                for each_c in jdict["decayCoincidences"]:
                    # First try gate/coinc
                    gamma_gate = each_c["gammaEnergyGate"]
                    gamma_coinc = each_c["gammaEnergyCoincidence"]

                    if (gamma_gate > (self.gamma1 - tolerance) and gamma_gate < (self.gamma1 + tolerance)) and (gamma_coinc > (self.gamma2 - tolerance) and gamma_coinc < (self.gamma2 + tolerance)):

                        FOUND_GAMMA = True
                        pid = jdict["parentID"]
                        did = jdict["daughterID"]
                        decay_mode = jdict["decayMode"]
                        decay_index = jdict["decayIndex"]
                        decay_energy = jdict["parentDecayLevelEnergy"]
                        coinc_intensity = each_c["absoluteCoincidenceIntensity"]
                        d_coinc_intensity = each_c["dAbsoluteCoincidenceIntensity"]
                        
                        isotope_list.append([pid, int(decay_index), decay_energy, did, decay_mode, gamma_gate, gamma_coinc, coinc_intensity, d_coinc_intensity])

                    # Switch coinc/gate order
                    gamma_gate_switch = each_c["gammaEnergyCoincidence"]
                    gamma_coinc_switch = each_c["gammaEnergyGate"]

                    if (gamma_gate_switch > (self.gamma1 - tolerance) and gamma_gate_switch < (self.gamma1 + tolerance)) and (gamma_coinc_switch > (self.gamma2 - tolerance) and gamma_coinc_switch < (self.gamma2 + tolerance)):

                        FOUND_GAMMA = True
                        pid = jdict["parentID"]
                        did = jdict["daughterID"]
                        decay_mode = jdict["decayMode"]
                        decay_index = jdict["decayIndex"]
                        decay_energy = jdict["parentDecayLevelEnergy"]
                        coinc_intensity = each_c["absoluteCoincidenceIntensity"]
                        d_coinc_intensity = each_c["dAbsoluteCoincidenceIntensity"]
                        
                        isotope_list.append([pid, int(decay_index), decay_energy, did, decay_mode, gamma_gate_switch, gamma_coinc_switch, coinc_intensity, d_coinc_intensity])

        try:
            isotope_array = np.array(isotope_list)
            pid = isotope_array[:,0]
            decay_index = isotope_array[:,1].astype(int)
            decay_energy = isotope_array[:,2]
            did = isotope_array[:,3]
            decay_mode = isotope_array[:,4]
            gamma_g = isotope_array[:,5]
            gamma_c = isotope_array[:,6]
            coinc_intensity = isotope_array[:,7]
            d_coinc_intensity = isotope_array[:,8]
        
            #isotope_df = pd.DataFrame({'Parent':pid, 'Energy': decay_energy, 'Daughter':did, 'Decay': decay_mode, 'Gamma 1': gamma_g, 'Gamma 2': gamma_c, 'I': coinc_intensity, 'dI': d_coinc_intensity})
            isotope_df = pd.DataFrame({'Parent':pid, 'Decay Index':decay_index, 'Ex. Energy': decay_energy, 'Daughter':did, 'Decay Mode': decay_mode, 'Gamma 1': gamma_g, 'Gamma 2': gamma_c})

            pd.set_option('display.max_row', None)
            pd.set_option('display.max_columns', None)

            if FOUND_GAMMA == True:
                return isotope_df
            
        except IndexError:
            if FOUND_GAMMA == False:
                print("No coincidence gammas match specified gating energies:\n {0} \xb1 {1} keV;\n {2} \xb1 {3} keV.\nTry different energies or expand the search window by adjusting the tolerance.".format(self.gamma1,tolerance,self.gamma2,tolerance))
                return
            else:
                raise
    
