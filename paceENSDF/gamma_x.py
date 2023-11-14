from .base_ensdf import *
from .normalization import Normalization
from .parent import Parent
from .daughter import Daughter
from .beta_minus import BetaMinus
from .electron_capture_beta_plus import ElectronCaptureBetaPlus
from .alpha import Alpha
from .gamma_gamma import GammaGamma

class GammaX(GammaGamma):
    __doc__="""Class to handle and manipulate coincidence gamma/X-ray data 
    sets."""

    def __init__(self):
        BaseENSDF.__init__(self)
        Normalization.__init__(self)
        Parent.__init__(self)
        Daughter.__init__(self)
        BetaMinus.__init__(self)
        ElectronCaptureBetaPlus.__init__(self)
        Alpha.__init__(self)
        GammaGamma.__init__(self)

    def get_gx(self, list, str, *args):
        """Gamma/X-ray coincidence data for: (i) a given decay scheme (defined 
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
                  index: An integer object associated with the decay index of the 
                         parent state is to be given as the second argument, where:
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

            [0]: Gamma-ray energy (float);
            [1]: Associated initial level index (int);
            [2]: Associated final level index (int);
            [3]: Coincident X-ray energy (float);
            [4]: X-ray transition label (str);
            [5]: Absolute gamma/X-ray coincident intensity (float);
            [6]: Coincident-intensity uncertainty (float).

        Examples:
            (i) All coincidences in 60Ni following beta-minus decay of 60Co in 
            its ground state:

            get_gx(cdata, "BM", "Co60", 0)

            (ii) All transitions in coincidence with the 2->1 transition in 
            60Ni following beta-minus decay of 60Co in its ground state:

            get_gx(cdata, "BM", "Co60", 0, 2, 1)
        """
        self.list = list
        self.str = str
        NUM_ARGS_OK = False
        coinc_list = []
        DAUGHTER_EXISTS = False
        COINCIDENCE = False
        if len(args) == 2:
            NUM_ARGS_OK = True
            pid = args[0]
            decay_index = args[1]

            decay_mode = BaseENSDF.check_decay(self.str)
            if decay_mode == None:
                print("Invalid decay mode.")
                return
            else:
                #coinc_list = []
                for jdict in self.list:
                    if jdict["datasetID"] == "GX":
                        if jdict["parentID"] == pid and jdict["decayMode"] == decay_mode and jdict["decayIndex"] == decay_index:
                            DAUGHTER_EXISTS = True
                            for each_c in jdict["gammaXrayCoincidences"]:
                                gamma_gate = each_c["gammaEnergy"]
                                gate_index_i = each_c["levelIndexInitial"]
                                gate_index_f = each_c["levelIndexFinal"]

                                xray_energy = each_c["XrayEnergy"]
                                xray_label = each_c["labelXrayTransition"]
                                
                                abs_coinc_intensity = each_c["absoluteCoincidenceIntensityGammaXray"]
                                d_abs_coinc_intensity = each_c["dAbsoluteCoincidenceIntensityGammaXray"]

                                coinc_list.append([gamma_gate, gate_index_i, gate_index_f, xray_energy, xray_label, abs_coinc_intensity, d_abs_coinc_intensity])

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
                #COINCIDENCE = False
                for jdict in self.list:
                    if jdict["datasetID"] == "GX":
                        if jdict["parentID"] == pid and jdict["decayMode"] == decay_mode and jdict["decayIndex"] == decay_index:
                            DAUGHTER_EXISTS = True
                            for each_c in jdict["gammaXrayCoincidences"]:
                                gamma_gate = each_c["gammaEnergy"]
                                gate_index_i = each_c["levelIndexInitial"]
                                gate_index_f = each_c["levelIndexFinal"]

                                xray_energy = each_c["XrayEnergy"]
                                xray_label = each_c["labelXrayTransition"]
                                
                                abs_coinc_intensity = each_c["absoluteCoincidenceIntensityGammaXray"]
                                d_abs_coinc_intensity = each_c["dAbsoluteCoincidenceIntensityGammaXray"]

                                if (int(i_level) == gate_index_i) and (int(f_level) == gate_index_f):
                                    COINCIDENCE = True
                                    coinc_list.append([gamma_gate, gate_index_i, gate_index_f, xray_energy, xray_label, abs_coinc_intensity, d_abs_coinc_intensity])


                if COINCIDENCE == False:
                    print("No gamma/X-ray coincidences for defined gating-transition indices")
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

        
    def get_xray_singles(self, list, mode, parent, index):
        """Absolute X-ray intensities from total-projection singles spectra.

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
            A list of 6 lists containing X-ray energies and intensities 
            associated with the K-shell.  The elements in each sublist 
            correspond to:

            [0]: X-ray energy (float);
            [1]: Absolute X-ray intensity (float);
            [2]: Absolute-intensity uncertainty (float).

            The order of the lists correspond to K-alpha-1, K-alpha-2, 
            K-alpha-3, K-beta-1, K-beta-2, and K-beta-3.

        Example:
            get_xray_singles(cdata, "BM", "Co60", 0)
        """
        self.list = list
        self.mode = mode
        self.parent = parent
        self.index = index

        decay_mode = BaseENSDF.check_decay(self.mode)
        singles_list = []
        DAUGHTER_EXISTS = False
        for jdict in self.list:
            if jdict["datasetID"] == "GX":
                if jdict["parentID"] == self.parent and jdict["decayMode"] == decay_mode and jdict["decayIndex"] == self.index:
                    DAUGHTER_EXISTS = True
                    for each_s in jdict["totalProjectionXrays"]:
                        xray_energy_KA1 = each_s["energyKalpha1"]
                        intensity_KA1 = each_s["intensityKalpha1"]
                        d_intensity_KA1 = each_s["dIntensityKalpha1"]

                        singles_list.append([xray_energy_KA1, intensity_KA1, d_intensity_KA1])
                        
                        xray_energy_KA2 = each_s["energyKalpha2"]
                        intensity_KA2 = each_s["intensityKalpha2"]
                        d_intensity_KA2 = each_s["dIntensityKalpha2"]

                        singles_list.append([xray_energy_KA2, intensity_KA2, d_intensity_KA2])

                        xray_energy_KA3 = each_s["energyKalpha3"]
                        intensity_KA3 = each_s["intensityKalpha3"]
                        d_intensity_KA3 = each_s["dIntensityKalpha3"]

                        singles_list.append([xray_energy_KA3, intensity_KA3, d_intensity_KA3])

                        xray_energy_KB1 = each_s["energyKbeta1"]
                        intensity_KB1 = each_s["intensityKbeta1"]
                        d_intensity_KB1 = each_s["dIntensityKbeta1"]

                        singles_list.append([xray_energy_KB1, intensity_KB1, d_intensity_KB1])

                        xray_energy_KB2 = each_s["energyKbeta2"]
                        intensity_KB2 = each_s["intensityKbeta2"]
                        d_intensity_KB2 = each_s["dIntensityKbeta2"]

                        singles_list.append([xray_energy_KB2, intensity_KB2, d_intensity_KB2])

                        xray_energy_KB3 = each_s["energyKbeta3"]
                        intensity_KB3 = each_s["intensityKbeta3"]
                        d_intensity_KB3 = each_s["dIntensityKbeta3"]

                        singles_list.append([xray_energy_KB3, intensity_KB2, d_intensity_KB3])

                        #singles_list.append([xray_energy_KA1, intensity_KA1, d_intensity_KA1,
                        #                     xray_energy_KA2, intensity_KA2, d_intensity_KA2,
                        #                     xray_energy_KA3, intensity_KA3, d_intensity_KA3,
                        #                     xray_energy_KB1, intensity_KB1, d_intensity_KB1,
                        #                     xray_energy_KB2, intensity_KB2, d_intensity_KB2,
                        #                     xray_energy_KB3, intensity_KB3, d_intensity_KB3,])

        if DAUGHTER_EXISTS == True:
            return singles_list
        else:
            return
    

    def get_xray_contribution(self, list, mode, parent, index):
        """Absoulte-intensity contribution of individual gamma rays to the 
        total X-ray yield for K-shell X-rays (K-alpha-1, K-alpha-2, K-alpha-3,
        K-beta-1, K-beta-2, K-beta-3).

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
            A DataFrame object containing the gamma energy and associated 
            X-ray energy and intensity contribution.
        
        Example:
            get_xray_contribution(cdata, "BM", "Co60", 0)
        """
        self.list = list
        self.mode = mode
        self.parent = parent
        self.index = index

        decay_mode = BaseENSDF.check_decay(self.mode)
        singles_list = []
        DAUGHTER_EXISTS = False
        for jdict in self.list:
            if jdict["datasetID"] == "GX":
                if jdict["parentID"] == self.parent and jdict["decayMode"] == decay_mode and jdict["decayIndex"] == self.index:
                    DAUGHTER_EXISTS = True
                    for each_s in jdict["gammaXraySingles"]:
                        gamma_energy = each_s["gammaEnergy"]
                        xray_label = each_s["labelXrayTransition"]
                        xray_energy = each_s["XrayEnergy"]
                        intensity = each_s["absoluteSingleIntensityContributionGammaXray"]
                        d_intensity = each_s["dAbsoluteSingleIntensityContributionGammaXray"]

                        singles_list.append([gamma_energy, xray_label, xray_energy, intensity, d_intensity])

        if len(singles_list) > 0 and DAUGHTER_EXISTS == True:
            singles_array = np.array(singles_list)
            gamma_energy = singles_array[:,0].astype(float)
            xray_label = singles_array[:,1]
            xray_energy = singles_array[:,2].astype(float)
            intensity = singles_array[:,3].astype(float)
            d_intensity = singles_array[:,4].astype(float)

            pd.set_option('display.max_row', None)
            pd.set_option('display.max_columns', None)

            singles_df = pd.DataFrame({'Eg (keV)':gamma_energy, 'X-ray':xray_label, 'Ex (keV)':xray_energy, 'Ix (%)':intensity, 'dIx':d_intensity})
            return singles_df

        else:
            print("No data available for parent decay.")
            return

        
    def find_xray(self, list, float, tolerance=0.5):
        """Searches for all X rays at a specified energy.  By default the 
        search will find all X rays within +/- 0.5 keV of the specified energy 
        passed to the function.

        Arguments:
            list: A list of coincidence-data JSON objects.
            float: X-ray energy in keV (float).
            tolerance: Limit of the energy search; by default +/- 0.5 keV.

        Returns: 
            A DataFrame object containing the parent isotope, parent-decay 
            energy, daughter isotope, decay mode, X-ray label, X-ray energy.
        
        Examples:
            (i) Find all isotopes containing X rays within 52+/-0.5 keV:
            
            find_xray(cdata, 52) 
                
            (ii) Finds all isotopes containing X rays within 52+/-1.5 keV:

            find_xray(cdata, 52, 1.5)
        """
        self.list = list
        self.float = float

        isotope_list = []
        FOUND_XRAY = False
        for jdict in self.list:
            if jdict["datasetID"] == "GX":
                for each_s in jdict["totalProjectionXrays"]:
                    xray_dict = {}
                    x_energy_KA1 = each_s["energyKalpha1"]
                    x_intensity_KA1 = each_s["intensityKalpha1"]
                    d_x_intensity_KA1 = each_s["dIntensityKalpha1"]

                    x_energy_KA2 = each_s["energyKalpha2"]
                    x_intensity_KA2 = each_s["intensityKalpha2"]
                    d_x_intensity_KA2 = each_s["dIntensityKalpha2"]

                    x_energy_KA3 = each_s["energyKalpha3"]
                    x_intensity_KA3 = each_s["intensityKalpha3"]
                    d_x_intensity_KA3 = each_s["dIntensityKalpha3"]

                    x_energy_KB1 = each_s["energyKbeta1"]
                    x_intensity_KB1 = each_s["intensityKbeta1"]
                    d_x_intensity_KB1 = each_s["dIntensityKbeta1"]

                    x_energy_KB2 = each_s["energyKbeta2"]
                    x_intensity_KB2 = each_s["intensityKbeta2"]
                    d_x_intensity_KB2 = each_s["dIntensityKbeta2"]

                    x_energy_KB3 = each_s["energyKbeta3"]
                    x_intensity_KB3 = each_s["intensityKbeta3"]
                    d_x_intensity_KB3 = each_s["dIntensityKbeta3"]

                    xray_dict.update({'Kalpha1': [x_energy_KA1, x_intensity_KA1, d_x_intensity_KA1],
                                      'Kalpha2': [x_energy_KA2, x_intensity_KA2, d_x_intensity_KA2],
                                      'Kalpha3': [x_energy_KA3, x_intensity_KA3, d_x_intensity_KA3],
                                      'Kbeta1': [x_energy_KB1, x_intensity_KB1, d_x_intensity_KB1],
                                      'Kbeta2': [x_energy_KB2, x_intensity_KB2, d_x_intensity_KB2],
                                      'Kbeta3': [x_energy_KB3, x_intensity_KB3, d_x_intensity_KB3]})


                    for (xkey, xvalue) in xray_dict.items():
                        if xvalue[0] > (self.float - tolerance) and xvalue[0] < (self.float + tolerance):
                            FOUND_XRAY = True
                            pid = jdict["parentID"]
                            did = jdict["daughterID"]
                            decay_mode = jdict["decayMode"]
                            decay_index = jdict["decayIndex"]
                            decay_energy = jdict["parentDecayLevelEnergy"]
                            xray_type = xkey
                            xray_energy = xvalue[0]
                            abs_intensity = xvalue[1]
                            d_abs_intensity = xvalue[2]

                            isotope_list.append([pid, int(decay_index), decay_energy, did, decay_mode, xray_type, xray_energy, abs_intensity, d_abs_intensity])
                                
        try:
            isotope_array = np.array(isotope_list)
            pid = isotope_array[:,0]
            decay_index = isotope_array[:,1].astype(int)
            decay_energy = isotope_array[:,2]
            did = isotope_array[:,3]
            decay_mode = isotope_array[:,4]
            xray_type = isotope_array[:,5]
            xray_energy = isotope_array[:,6]
            abs_intensity = isotope_array[:,7]
            d_abs_intensity = isotope_array[:,8]
        
            isotope_df = pd.DataFrame({'Parent':pid, 'Decay Index':decay_index, 'Ex. Energy': decay_energy, 'Daughter':did, 'Decay Mode': decay_mode, 'X-ray Label': xray_type, 'X-ray Energy': xray_energy})

            pd.set_option('display.max_columns', None)
            pd.set_option('display.max_row', None)

            if FOUND_XRAY == True:
                return isotope_df

        except IndexError:
            if FOUND_XRAY == False:
                print("No X-rays match specified search criterion: {0} \xb1 {1} keV.".format(self.float, tolerance))
                print("Try a different energy or expand the search window by adjusting the tolerance.")
                return
            else:
                raise


    def find_xray_coinc(self, list, xray, gamma, tolerance=0.5):
        """Searches for all pairs of X rays and gamma rays at specified 
        energies.  By default the tolerance window will search within 
        +/- 0.5 keV of the specified energies passed to the function.

        Arguments:
            list: A list of coincidence-data JSON objects.
            xray: X-ray energy in keV (float).
            gamma: Gamma-ray energy in keV (float).
            tolerance: Limit of the energy search; by default +/- 0.5 keV.

        Returns: 
            A DataFrame object containing the parent isotope, parent-decay 
            energy, daughter isotope, decay mode, X-ray label, first energy,
            second energy.
        
        Examples:
            (i) Find all isotopes containing 52/688 X-ray/gamma coincidences 
            within +/-0.5 keV:
            
            find_xray_coinc(cdata, 52, 688) 
                
            (ii) Finds all isotopes containing 52/688 X-ray/gamma coincidences 
            within +/-0.3 keV:

            find_xray_coinc(cdata, 52, 688, 0.3)
        """
        self.list = list
        self.xray = xray
        self.gamma = gamma

        isotope_list = []
        FOUND_PHOTONS = False
        for jdict in self.list:
            if jdict["datasetID"] == "GX":
                for each_c in jdict["gammaXrayCoincidences"]:
                    # First try gate/coinc
                    xray_gate = each_c["XrayEnergy"]
                    gamma_coinc = each_c["gammaEnergy"]

                    if (xray_gate > (self.xray - tolerance) and xray_gate < (self.xray + tolerance)) and (gamma_coinc > (self.gamma - tolerance) and gamma_coinc < (self.gamma + tolerance)):

                        FOUND_PHOTONS = True
                        
                        pid = jdict["parentID"]
                        did = jdict["daughterID"]
                        decay_mode = jdict["decayMode"]
                        decay_index = jdict["decayIndex"]
                        decay_energy = jdict["parentDecayLevelEnergy"]
                        coinc_intensity = each_c["absoluteCoincidenceIntensityGammaXray"]
                        d_coinc_intensity = each_c["dAbsoluteCoincidenceIntensityGammaXray"]
                        xray_label = each_c["labelXrayTransition"]
                        
                        isotope_list.append([pid, int(decay_index), decay_energy, did, decay_mode, xray_gate, gamma_coinc, coinc_intensity, d_coinc_intensity, xray_label])

                    # Switch coinc/gate order
                    xray_gate_switch = each_c["gammaEnergy"]
                    gamma_coinc_switch = each_c["XrayEnergy"]

                    if (xray_gate_switch > (self.xray - tolerance) and xray_gate_switch < (self.xray + tolerance)) and (gamma_coinc_switch > (self.gamma - tolerance) and gamma_coinc_switch < (self.gamma + tolerance)):

                        FOUND_PHOTONS = True
                        
                        pid = jdict["parentID"]
                        did = jdict["daughterID"]
                        decay_mode = jdict["decayMode"]
                        decay_index = jdict["decayIndex"]
                        decay_energy = jdict["parentDecayLevelEnergy"]
                        coinc_intensity = each_c["absoluteCoincidenceIntensityGammaXray"]
                        d_coinc_intensity = each_c["dAbsoluteCoincidenceIntensityGammaXray"]
                        xray_label = each_c["labelXrayTransition"]
                        
                        isotope_list.append([pid, int(decay_index), decay_energy, did, decay_mode, xray_gate_switch, gamma_coinc_switch, coinc_intensity, d_coinc_intensity, xray_label])
                        
        #if len(isotope_list) > 0:
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
            xray_label = isotope_array[:,9]
        
            #isotope_df = pd.DataFrame({'Parent':pid, 'Energy ': decay_energy, 'Daughter':did, 'Decay': decay_mode, 'Gamma 1': gamma_g, 'Gamma 2': gamma_c, 'I': coinc_intensity, 'dI': d_coinc_intensity})
            isotope_df = pd.DataFrame({'Parent': pid, 'Decay Index':decay_index, 'Ex. Energy': decay_energy, 'Daughter': did, 'Decay Mode': decay_mode, 'X-ray Label': xray_label, 'Photon 1': gamma_g, 'Photon 2': gamma_c})
            
            pd.set_option('display.max_row', None)
            pd.set_option('display.max_columns', None)
            if FOUND_PHOTONS == True:
                return isotope_df

        except IndexError:
            if FOUND_PHOTONS == False:
                print("No X-ray/gamma coincidences match specified gating energies:\n {0} \xb1 {1} keV;\n {2} \xb1 {3} keV.".format(self.xray, tolerance, self.gamma, tolerance))
                print("Try different energies or expand the search window by adjusting the tolerance.")
                return
            else:
                raise
            

    def get_binding_energies(self, list, *args, **kwargs):
        """Atomic subshell binding energies in keV for K, L1-3, and M1-5 
        shells.  The data are taken from:

        [2008Ki07] - T.Kibedi et al., Nucl. Instrum. Methods Phys. Res. 
        Sect. A 589, 202 (2008).

        No data for Z=1,2,101,103,106, and 110 currently.  These will be added 
        in the future.

        Arguments:
            list: A list of coincidence-data JSON objects.
            args: The function call takes either the chemical symbol (string) 
                  or the atomic number (integer) as an input argument.
            kwargs: An additional keyword argument is needed for the desired 
                    atomic shell:

                    shell='K'
                    shell='L'
                    shell='M'
                    shell='all'

                    Only the above keyword arguments (case insensitive) are 
                    acceptable.

        Returns:
            A DataFrame object containing the chemical symbol for the element,
            atomic number, and subshell binding-energy data.

        Examples:
            get_binding_energies(cdata, "Yb", shell=<str>)
            get_binding_energies(cdata, 70, shell=<str>)
        """
        self.list = list
        be_list = []
        for jdict in self.list:
            FOUND_ELEMENT = False
            if jdict["datasetID"] == "GX":
                for each_b in jdict["bindingEnergies"]:
                    try:
                        if (args[0].upper() == each_b["elementID"].upper()):
                            FOUND_ELEMENT = True
                            be_list.append([each_b["elementID"], each_b["atomicNumber"], each_b["KsubshellBindingEnergy"], each_b["L1subshellBindingEnergy"], each_b["L2subshellBindingEnergy"], each_b["L3subshellBindingEnergy"], each_b["M1subshellBindingEnergy"], each_b["M2subshellBindingEnergy"], each_b["M3subshellBindingEnergy"], each_b["M4subshellBindingEnergy"], each_b["M5subshellBindingEnergy"]])
                    except AttributeError:
                        if (args[0] == each_b["atomicNumber"]):
                            FOUND_ELEMENT = True
                            be_list.append([each_b["elementID"], each_b["atomicNumber"], each_b["KsubshellBindingEnergy"], each_b["L1subshellBindingEnergy"], each_b["L2subshellBindingEnergy"], each_b["L3subshellBindingEnergy"], each_b["M1subshellBindingEnergy"], each_b["M2subshellBindingEnergy"], each_b["M3subshellBindingEnergy"], each_b["M4subshellBindingEnergy"], each_b["M5subshellBindingEnergy"]])
            if FOUND_ELEMENT == True:
                break

        try:
            be_array = np.array(be_list)
            if len(kwargs) == 0:
                print("Please pass one of the following keyword arguments:")
                print("shell='K'")
                print("shell='L'")
                print("shell='M'")
                print("shell='all'")
                return
            else:
                for kwarg in kwargs.values():
                    if kwarg.upper() == "K":
                        df = pd.DataFrame({'ID':be_array[:,0], 'Z':be_array[:,1].astype(int), 'K':be_array[:,2].astype(float)})
                        return df
                    elif kwarg.upper() == "L":
                        df = pd.DataFrame({'ID':be_array[:,0], 'Z':be_array[:,1].astype(int), 'L1':be_array[:,3].astype(float), 'L2':be_array[:,4].astype(float), 'L3':be_array[:,5].astype(float)})
                        return df
                    elif kwarg.upper() == "M":
                        df = pd.DataFrame({'ID':be_array[:,0], 'Z':be_array[:,1].astype(int), 'M1':be_array[:,6].astype(float), 'M2':be_array[:,7].astype(float), 'M3':be_array[:,8].astype(float), 'M4':be_array[:,9].astype(float), 'M5':be_array[:,10].astype(float)})
                        return df
                    elif kwarg.lower() == "all":
                        df = pd.DataFrame({'ID':be_array[:,0], 'Z':be_array[:,1].astype(int), 'K':be_array[:,2].astype(float), 'L1':be_array[:,3].astype(float), 'L2':be_array[:,4].astype(float), 'L3':be_array[:,5].astype(float), 'M1':be_array[:,6].astype(float), 'M2':be_array[:,7].astype(float), 'M3':be_array[:,8].astype(float), 'M4':be_array[:,9].astype(float), 'M5':be_array[:,10].astype(float)})
                        return df
                    else:
                        print("No subshell for corresponding keyword argument.")
                        print("Only the following keyword arguments are accepted:")
                        print("shell='K'")
                        print("shell='L'")
                        print("shell='M'")
                        print("shell='all'")
                        return
        except IndexError:
            print("No binding-energy data available for element.")
            return

        
    def get_valence_config(self, list, *args):
        """Valence electronic configuration for all elements from Z=3-110.  
        No data for Z=1,2,101,103,106, and 110 currently.  These will be added 
        in the future.

        Arguments:
            list: A list of coincidence-data JSON objects.
            args: The function call takes either the chemical symbol (string) 
                  or the atomic number (integer) as an input argument.

        Returns:
            A list object containing the valence-electronic subshell 
            information.  For each subshell the list elements are given as:

            [0]: Electronic subshell;
            [1]: Total angular momentum (l.s);
            [2]: Particle number occupancy.

            The function call also prints to screen the corresponding 
            configuration in an easy-to-read display.
            
        Examples:
            get_valence_config(cdata, "Yb")
            get_valence_config(cdata, 70)
        """
        self.list = list
        electronic_config = []
        chemical_symbol = None
        element_Z = None
        for jdict in self.list:
            FOUND_ELEMENT = False
            if jdict["datasetID"] == "GX":
                for each_b in jdict["bindingEnergies"]:
                    try:
                        if (args[0].upper() == each_b["elementID"].upper()):
                            FOUND_ELEMENT = True
                            chemical_symbol = each_b["elementID"]
                            element_Z = each_b["atomicNumber"]
                            df = pd.json_normalize(jdict["valenceElectronicConfiguration"])
                            for i in df['valenceSubshells']:
                                for j in i:
                                    subshell = j['electronicSubshell']
                                    real_am = j['totalAngularMomentumRealLS']
                                    occupancy = j['particleNumberOccupancy']
                                    #print(subshell, real_am, occupancy)
                                    electronic_config.append([subshell, real_am, occupancy])

                    except AttributeError:
                        if (args[0] == each_b["atomicNumber"]):
                            FOUND_ELEMENT = True
                            chemical_symbol = each_b["elementID"]
                            element_Z = each_b["atomicNumber"]
                            df = pd.json_normalize(jdict["valenceElectronicConfiguration"])
                            for i in df['valenceSubshells']:
                                for j in i:
                                    subshell = j['electronicSubshell']
                                    real_am = j['totalAngularMomentumRealLS']
                                    occupancy = j['particleNumberOccupancy']
                                    #print(subshell, real_am, occupancy)
                                    electronic_config.append([subshell, real_am, occupancy])

            if FOUND_ELEMENT == True:
                break
        if len(electronic_config) > 0:
            electronic_str = ''
            for value in electronic_config:
                subshell = value[0]
                two_times_real_am = int(2*float(value[1]))
                occupancy = int(value[2])

                electronic_str += "%s(%i/2)[%i]"%(subshell,two_times_real_am,occupancy)
            print("{0} ({1}): {2}".format(chemical_symbol, element_Z, electronic_str))
            return electronic_config
        else:
            print("Electronic configuration undefined or does not exist.")
            return
        

    # TYPOS IN JSON SCHEMA: "XrayBranchingRatios"
    # DON'T USE THIS FUNCTION FOR NOW
    def get_XBR(self, list, *args):
        """X-ray energies and fluorescence-yield-corrected branching ratios 
        from the Table of Isotopes:

        1996FiZX: R.B. Firestone et al., "Table of Isotopes", 8th Ed., John 
        Wiley and Sons, Inc., New York, Vol. 2 (1996).

        Arguments:
            list: A list of coincidence-data JSON objects.
            args: The function call takes either the chemical symbol (string) 
                  or the atomic number (integer) as an input argument.

        Returns:
            A DataFrame object containing the X-ray energies, branching ratios,
            and uncertainties on the branching ratios for K-shell X rays 
            corresponding to Kalpha1, Kalpha2, Kalpha3, Kbeta1, Kbeta2, and 
            Kbeta3 emission.
        
        Example:
            get_XBR(cdata, "Yb")
            get_XBR(cdata, 70)
        """
        self.list = list
        xray_list = []
        for jdict in self.list:
            FOUND_ELEMENT = False
            if jdict["datasetID"] == "GX":
                for each_b in jdict["XrayBranchingRatios"]:
                    try:
                        if (args[0].upper() == each_b["elementID"].upper()):
                            FOUND_ELEMENT = True
                            xray_list.append([each_b["energyKalpha1"], each_b["Kalpha1BR"], each_b["dKalpha1BR"], each_b["energyKalpha2"], each_b["Kalpha2BR"], each_b["dKalpha2BR"], each_b["energyKalpha3"], each_b["Kalpha3BR"], each_b["dKalpha3BR"], each_b["energyKbeta1"], each_b["Kbeta1BR"], each_b["dKbeta1BR"], each_b["energyKbeta2"], each_b["Kbeta2BR"], each_b["dKbeta2BR"], each_b["energyKbeta3"], each_b["Kbeta3BR"], each_b["dKbeta3BR"]])
                    except AttributeError:
                        if (args[0] == each_b["atomicNumber"]):
                            FOUND_ELEMENT = True
                            xray_list.append([each_b["energyKalpha1"], each_b["Kalpha1BR"], each_b["dKalpha1BR"], each_b["energyKalpha2"], each_b["Kalpha2BR"], each_b["dKalpha2BR"], each_b["energyKalpha3"], each_b["Kalpha3BR"], each_b["dKalpha3BR"], each_b["energyKbeta1"], each_b["Kbeta1BR"], each_b["dKbeta1BR"], each_b["energyKbeta2"], each_b["Kbeta2BR"], each_b["dKbeta2BR"], each_b["energyKbeta3"], each_b["Kbeta3BR"], each_b["dKbeta3BR"]])
            if FOUND_ELEMENT == True:
                break

        if len(xray_list) > 0:
            xray_array = np.array(xray_list)
            eKa1 = xray_array[:,0]
            IKa1 = xray_array[:,1]
            dIKa1 = xray_array[:,2]
            eKa2 = xray_array[:,3]
            IKa2 = xray_array[:,4]
            dIKa2 = xray_array[:,5]
            eKa3 = xray_array[:,6]
            IKa3 = xray_array[:,7]
            dIKa3 = xray_array[:,8]
            eKb1 = xray_array[:,9]
            IKb1 = xray_array[:,10]
            dIKb1 = xray_array[:,11]
            eKb2 = xray_array[:,12]
            IKb2 = xray_array[:,13]
            dIKb2 = xray_array[:,14]
            eKb3 = xray_array[:,15]
            IKb3 = xray_array[:,16]
            dIKb3 = xray_array[:,17]                        
            
            xray_br_df = pd.DataFrame({'E(Ka1)':eKa1, 'BR(Ka1)':IKa1, 'dBR(Ka1)':dIKa1, 'E(Ka2)':eKa2, 'BR(Ka2)':IKa2, 'dBR(Ka2)':dIKa2, 'E(Ka3)':eKa3, 'BR(Ka3)':IKa3, 'dBR(Ka3)':dIKa3, 'E(Kb1)':eKb1, 'BR(Kb1)':IKb1, 'dBR(Kb1)':dIKb1, 'E(Kb2)':eKb2, 'BR(Kb2)':IKb2, 'dBR(Kb2)':dIKb2, 'E(Kb3)':eKb3, 'BR(Kb3)':IKb3, 'dBR(Kb3)':dIKb3})

            return xray_br_df

        else:
            print("No X-ray branching ratio data found.")
            return
        
