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



    def get_gg_timecut(self, list, str, *args):
        """Gamma/gamma coincidence data with imposed timecut for: (i) a given 
        decay scheme (defined by parent nucleus), or (ii) a particular 
        transition within a given decay scheme (defined by parent nucleus and 
        transition indices associated with the decay of the daughter nucleus).

        Arguments:
            list: A list of coincidence-data JSON objects.
            str: A string object describing the decay mode:
                  "BM": Beta-minus decay;
                  "ECBP": Electron-capture/beta-plus decay;
                  "A": Alpha decay.
            args: Takes either 3 or 5 additional arguments:

                  (i) If 2 args are given:
                  parent: A string object describing the parent ID must be given
                          as the first argument.
                  index: An integer object associated with the decay index of 
                         the parent state is to be given as the second argument,
                         where:
                         0: Ground-state decay;
                         >= 1: Isomer decay.
                  timecut: A float object to define timecut.  Must be given in 
                           units of [s] where values:
                           > 0: returns coincidences where level associated with
                                gamma-gate transition is longer-lived than 
                                imposed timecut.
                           < 0: returns coincidences where level associated with
                                gamma-gate transition is shorter-lived than 
                                imposed timecut.

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
                  timecut: A float object to define timecut.  Must be given in 
                           units of [s] where values:
                           > 0: returns coincidences where level associated with
                                gamma-gate transition is longer-lived than 
                                imposed timecut.
                           < 0: returns coincidences where level associated with
                                gamma-gate transition is shorter-lived than 
                                imposed timecut.
        
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
            [11]: Coincident-intensity uncertainty (float);
            [12]: Halflife in units of [s] related to initial level associated 
                  with gamma-gate transition (float);
            [13]: Associated uncertainty of halflife in units of [s] related to 
                  initial level associated with gamma-gate transition (float).

        Examples:
            A 6.0072-h isomer is populated in 99Tc (level index=2; E=142.7 keV) 
            following the beta-minus decay of 99Mo.  Cascade transition 
            sequences through the isomer can filtered using the following 
            methods.  It is best to use the transient-equilibrium intensities 
            to assess these coincidences.

            (i) All coincidences in 99Tc following beta-minus decay of 99Mo in  
            its ground state assuming a timecut < 6 h (21600 s):

            get_gg_timecut(cdata, "BM", "Mo99", 0, -21600)

            (ii) All transitions in coincidence with the 1->0 transition in 
            99Tc following beta-minus decay of 99Mo in its ground state assuming
            a timecut < 6 h (21600 s):

            get_gg_timecut(cdata, "BM", "Mo99", 0, 1, 0, -21600)

            (iii) All coincidences in 99Tc following beta-minus decay of 99Mo in
            its ground state assuming a timecut > 6 h (21600 s):

            get_gg_timecut(cdata, "BM", "Mo99", 0, 21600)

            (iv) All transitions in coincidence with the 1->0 transition in 
            99Tc following beta-minus decay of 99Mo in its ground state assuming
            a timecut > 6 h (21600 s):

            get_gg_timecut(cdata, "BM", "Mo99", 0, 1, 0, 21600)

            Note that methods (i) and (ii) above remove any coincidences with 
            cascade transition sequences that go through the 6-h isomer, while 
            methods (iii) and (iv) only return coincidences with transition 
            sequences in the path of the isomer.
        """
        self.list = list
        self.str = str
        NUM_ARGS_OK = False
        coinc_list = []
        DAUGHTER_EXISTS = False
        COINCIDENCE = False
        gg = GammaGamma()
        if len(args) == 3:
            #try:
            #    pid = str(args[0])
            #    decay_index = int(args[1])
            #except TypeError:
            #    pid = str(args[1])
            #    decay_index = int(args[0])
            NUM_ARGS_OK = True
            pid = args[0]
            decay_index = args[1]
            timecut = args[2]

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
                                if timecut >= 0:
                                    
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

                                    # Need to recalculate coincidence intensities to removes cascades that go through the isomer and don't satisfy imposed timecut
                                        
                                    #abs_coinc_intensity = each_c["absoluteCoincidenceIntensity"]
                                    #d_abs_coinc_intensity = each_c["dAbsoluteCoincidenceIntensity"]

                                    # Not sure if we still need this info, but leaving it in for now
                                    ilevel_gammagate_halflife = each_c["gammaGateLevelHalfLifeConverted"]
                                    d_ilevel_gammagate_halflife = each_c["dGammaGateLevelHalfLifeConverted"]

                                    # Call the `show_cascades` method to figure out cascade
                                    casc = gg.show_cascades(self.list,self.str,pid,decay_index,gate_index_i,gate_index_f,coinc_index_i,coinc_index_f,True)

                                    surviving_paths = []
                                    for i,p in enumerate(casc):
                                        HITS_ISOMER = False
                                        for c in casc[i]:
                                            Ei = c[0]
                                            Ef = c[1]
                                            for each_d in jdict["decaySingles"]:
                                                if Ei == int(each_d["levelIndexInitial"]) and Ef == int(each_d["levelIndexFinal"]):
                                                    if each_d["levelIsomer"] == True and each_d["levelHalfLifeConverted"] is not None:
                                                        if float(each_d["levelHalfLifeConverted"]) > abs(timecut):
                                                            #print(Ei,"->",Ef)
                                                            HITS_ISOMER = True

                                        if HITS_ISOMER == True:
                                            surviving_paths.append(casc[i])
                                    if len(surviving_paths) > 0:
                                        ci_dci = gg.recalculate_ci(self.list, decay_mode, pid, decay_index, surviving_paths)
                                        abs_coinc_intensity = ci_dci[0]
                                        d_abs_coinc_intensity = ci_dci[1]
                                                        
                                        coinc_list.append([gamma_gate, gamma_coinc, gate_index_i, gate_index_f, gate_level_i, gate_level_f, coinc_index_i, coinc_index_f, coinc_level_i, coinc_level_f, abs_coinc_intensity, d_abs_coinc_intensity, ilevel_gammagate_halflife, d_ilevel_gammagate_halflife])

                                elif timecut < 0:

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

                                    #abs_coinc_intensity = each_c["absoluteCoincidenceIntensity"]
                                    #d_abs_coinc_intensity = each_c["dAbsoluteCoincidenceIntensity"]

                                    # Keeping these in for now
                                    ilevel_gammagate_halflife = each_c["gammaGateLevelHalfLifeConverted"]
                                    d_ilevel_gammagate_halflife = each_c["dGammaGateLevelHalfLifeConverted"]

                                    # Call the `show_cascades` method to figure out cascade
                                    casc = gg.show_cascades(self.list,self.str,pid,decay_index,gate_index_i,gate_index_f,coinc_index_i,coinc_index_f,True)

                                    surviving_paths = []
                                    for i,p in enumerate(casc):
                                        PATH_KILLER = False
                                        for c in casc[i]:
                                            Ei = c[0]
                                            Ef = c[1]
                                            for each_d in jdict["decaySingles"]:
                                                if Ei == int(each_d["levelIndexInitial"]) and Ef == int(each_d["levelIndexFinal"]):
                                                    if each_d["levelIsomer"] == True and each_d["levelHalfLifeConverted"] is not None:
                                                        if float(each_d["levelHalfLifeConverted"]) >= abs(timecut):
                                                            #print("DEAD-END: ",Ei,"->",Ef)
                                                            PATH_KILLER = True

                                        if PATH_KILLER == False:
                                            surviving_paths.append(casc[i])
                                    if len(surviving_paths) > 0:
                                        ci_dci = gg.recalculate_ci(self.list, decay_mode, pid, decay_index, surviving_paths)
                                        abs_coinc_intensity = ci_dci[0]
                                        d_abs_coinc_intensity = ci_dci[1]
                                    
                                        coinc_list.append([gamma_gate, gamma_coinc, gate_index_i, gate_index_f, gate_level_i, gate_level_f, coinc_index_i, coinc_index_f, coinc_level_i, coinc_level_f, abs_coinc_intensity, d_abs_coinc_intensity, ilevel_gammagate_halflife, d_ilevel_gammagate_halflife])

                if coinc_list == [] or len(coinc_list) == 0:
                    print("No gamma/gamma coincidences with imposed timecut")
                    return

                #return sorted(coinc_list)

        elif len(args) == 5:
            NUM_ARGS_OK = True
            pid = args[0]
            decay_index = args[1]
            i_level = args[2]
            f_level = args[3]
            timecut = args[4]
            
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

                            # Call function recursively to find specified coincidences
                            all_gg_list = gg.get_gg_timecut(self.list,self.str,pid,decay_index,timecut)
                            for g in all_gg_list:
                                if i_level == g[2] and f_level == g[3]:
                                    # coincidences below gate
                                    COINCIDENCE = True
                                    coinc_list.append([g[0],g[1],g[2],g[3],g[4],g[5],g[6],g[7],g[8],g[9],g[10],g[11],g[12],g[13]])
                                elif i_level == g[6] and f_level == g[7]:
                                    # coincidences above gate
                                    COINCIDENCE = True
                                    # re-arrange order to lead with defined coincidence gates
                                    coinc_list.append([g[0],g[1],g[6],g[7],g[8],g[9],g[2],g[3],g[4],g[5],g[10],g[11],g[12],g[13]])
                                else:
                                    COINCIDENCE = False
                
                if COINCIDENCE == False:
                    print("No gamma/gamma coincidences for defined gating-transition indices with imposed timecut")
                    return
                #else:
                #    return sorted(coinc_list)

        else:
            print("Wrong number of input arguments")
            print("Function needs to be called using one of the following methods, e.g.:")
            print("g-g coincidences with timecut < 1 ns (1E-09 s):")
            print("e.get_gg_timecut(cdata, \"ECBP\", \"Ga67\", 0, -1e-09)")
            print("e.get_gg_timecut(cdata, \"ECBP\", \"Ga67\", 0, 1, 0, -1e-09)")
            print("g-g coincidences with timecut > 0.5 ns (5E-10 s):")
            print("e.get_gg_timecut(cdata, \"ECBP\", \"Ga67\", 0, 5e-10)")
            print("e.get_gg_timecut(cdata, \"ECBP\", \"Ga67\", 0, 1, 0, 5e-10)")
            return

        if len(args) == 3 and NUM_ARGS_OK == True and DAUGHTER_EXISTS == True:
            return sorted(coinc_list, key=lambda x: x[2])
        elif len(args) == 5 and NUM_ARGS_OK == True and DAUGHTER_EXISTS == True and COINCIDENCE == True:
            return sorted(coinc_list, key=lambda x: x[6])
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


    def show_cascades(self, list, str1, str2, index, int1, int2, int3, int4, quiet=False):
        """Displays the gamma-ray cascades for each parallel path between a 
        coincident pair of gamma rays in the decay scheme of the daughter 
        nucleus populated following radioactive decay.

        Arguments:
            list: A list of coincidence-data JSON objects.
            str1: A string object describing the decay mode:
                  "BM": Beta-minus decay;
                  "ECBP": Electron-capture/beta-plus decay;
                  "A": Alpha decay.
            str2: A string object describing the parent ID.
            index: An integer object associated with the decay index of the 
                   parent state, where:
                   0: Ground-state decay;
                   >= 1: Isomer decay.
            int1: An integer object corresponding to the initial level of the 
                  gamma-ray gate transition.
            int2: An integer object corresponding to the final level of the 
                  gamma-ray gate transition.
            int3: An integer object corresponding to the initial level of the 
                  coincident gamma-ray transition.
            int4: An integer object corresponding to the final level of the 
                  coincident gamma-ray transition.


        Returns: 
            A list object of 2-element tuples containing transition indices 
            associated with initial and final levels corresponding to the 
            gamma-ray transitions in the cascade between a pair of coincident 
            gamma rays.  Each tuple in the list contains the following elements:

            [0]: Level index of initial level associated with cascade gamma-ray 
                 transition (int);
            [1]: Level index of final level associated with cascade gamma-ray 
                 transition (int).
        Examples:
            To display cascade gamma rays between the 3->2 and 1->0 pair of 
            coincident gamma-rays in 60Ni following 60Co beta-minus decay, i.e.,
            g(347.17 keV)-g(1332.492 keV):

            show_cascades(cdata,"BM","Co60",0,3,2,1,0)
        """
        self.list = list
        self.str1 = str1
        self.str2 = str2
        self.index = int(index)
        self.int1 = int(int1)
        self.int2 = int(int2)
        self.int3 = int(int3)
        self.int4 = int(int4)

        decay_mode = BaseENSDF.check_decay(self.str1)
        if decay_mode is None:
            print("Invalid decay mode.")
            return
        else:
            Ei_gate = self.int1
            Ef_gate = self.int2
            Ei_coinc = self.int3
            Ef_coinc = self.int4
            cascade = []
            FOUND_PAIR = False
            NO_COINC = False
            DAUGHTER_EXISTS = False
            for jdict in self.list:
                if jdict["datasetID"] == "GG":
                    if jdict["decayMode"] == decay_mode and jdict["parentID"] == self.str2 and jdict["decayIndex"] == self.index:
                        DAUGHTER_EXISTS = True
                        for each_d in jdict["decayCoincidences"]:
                            if each_d["gammaGateLevelIndexInitial"]==Ei_gate and each_d["gammaGateLevelIndexFinal"]==Ef_gate \
                               and each_d["gammaCoincidenceLevelIndexInitial"]==Ei_coinc and each_d["gammaCoincidenceLevelIndexFinal"]==Ef_coinc:
                                FOUND_PAIR = True
                                for each_c in each_d["coincidenceCascadeSequences"]:
                                    cascade.append(each_c["indexedTransitionSequence"])
                            if FOUND_PAIR == False:
                                if each_d["gammaGateLevelIndexInitial"]==Ei_coinc and each_d["gammaGateLevelIndexFinal"]==Ef_coinc \
                                   and each_d["gammaCoincidenceLevelIndexInitial"]==Ei_gate and each_d["gammaCoincidenceLevelIndexFinal"]==Ef_gate:
                                    for each_c in each_d["coincidenceCascadeSequences"]:
                                        cascade.append(each_c["indexedTransitionSequence"])

            if len(cascade) == 0:
                NO_COINC = True
            if DAUGHTER_EXISTS == False:
                print("No gammas in observed daughter nucleus.")
                return
            else:
                if NO_COINC == True:
                    print("No gamma cascades between defined coincidence pairs.")
                    return
                else:
                    # Find gammas and levels associated with indices
                    list_gamma_tuples = []
                    gamma_gate, gamma_coinc = None, None
                    Ei_gate_energy, Ef_gate_energy = None, None
                    Ei_coinc_energy, Ef_coinc_energy = None, None
                    for jdict in self.list:
                        if jdict["datasetID"] == "GG":
                            if jdict["decayMode"] == decay_mode and jdict["parentID"] == self.str2 and jdict["decayIndex"] == self.index:
                                
                                for each_n in jdict["normalizedBranchingRatios"]:
                                    if Ei_gate == int(each_n["levelIndexInitial"]) and Ef_gate == int(each_n["levelIndexFinal"]):
                                        gamma_gate = each_n["gammaEnergy"]
                                        Ei_gate_energy = each_n["levelEnergyInitial"]
                                        Ef_gate_energy = each_n["levelEnergyFinal"]
                    
                                    if Ei_coinc == int(each_n["levelIndexInitial"]) and Ef_coinc == int(each_n["levelIndexFinal"]):
                                        gamma_coinc = each_n["gammaEnergy"]
                                        Ei_coinc_energy = each_n["levelEnergyInitial"]
                                        Ef_coinc_energy = each_n["levelEnergyFinal"]
                                        
                    if quiet == False:
                        print("Cascade sequence between coincidence gammas: g({0} keV)-g({1} keV): \ng({2} [{3} keV] -> {4} [{5} keV]) - g({6} [{7} keV] -> {8} [{9} keV])\n".format(gamma_gate,gamma_coinc,Ei_gate,Ei_gate_energy,Ef_gate,Ef_gate_energy,Ei_coinc,Ei_coinc_energy,Ef_coinc,Ef_coinc_energy))
                    
                    for p,casc in enumerate(cascade):
                        #print(casc)
                        if quiet == False:
                            print("Path number {0}:".format(p+1))
                        list_gt = []
                        for i,v in enumerate(range(len(casc))):
                            #print(casc[v])
                            for j,u in enumerate(range(len(casc))):
                                if j == i+1:                                                    
                                    gamma_cascade = None
                                    Ei_cascade, Ef_cascade = None, None
                                    for jdict in self.list:
                                        if jdict["datasetID"] == "GG":
                                            if jdict["decayMode"] == decay_mode and jdict["parentID"] == self.str2 and jdict["decayIndex"] == self.index:
                                                
                                                for each_n in jdict["normalizedBranchingRatios"]:
                                                    if casc[v] == int(each_n["levelIndexInitial"]) and casc[u] == int(each_n["levelIndexFinal"]):
                                                        gamma_cascade = each_n["gammaEnergy"]
                                                        Ei_cascade = each_n["levelEnergyInitial"]
                                                        Ef_cascade = each_n["levelEnergyFinal"]

                                    if quiet == False:
                                        print("Transition sequence: {0} -> {1}: g({2} keV) [{3} keV -> {4} keV]".format(casc[v],casc[u],gamma_cascade,Ei_cascade,Ef_cascade))
                                    list_gt.append((casc[v],casc[u]))
                        list_gamma_tuples.append(list_gt)
                        if quiet == False:
                            print("\n")

                    if len(list_gamma_tuples) > 0:
                        return list_gamma_tuples
                    else:
                        print("No gamma cascades observed.")
                        return

                    
    def recalculate_ci(self, cdata_list, decay_mode, parent_id, decay_index, spath):
        """Re-calculates coincidence intensities based on a defined sequence of
        transitions.  For now, this method is intended for internal use only; 
        it is called by the function `get_gg_timecut`.

        Arguments:
            cdata_list: A list of coincidence-data JSON objects.
            decay_mode: A string object describing the decay mode:
                        "BM": Beta-minus decay;
                        "ECBP": Electron-capture/beta-plus decay;
                        "A": Alpha decay.
            parent_id: A string object describing the parent ID.
            decay_index: An integer object associated with the decay index of 
                         the parent state, where:
                         0: Ground-state decay;
                         >= 1: Isomer decay.
            spath: A list object corresponding to a sequence of 
                   transition-indexed tuples that satisfy the imposed timecut.

        Returns:
            A tuple object with elements corresponding to:

            [0]: The total coincidence intensity between a pair of gamma rays.
            [1]: The associated uncertainty on the coincidence intensity.

        Examples:
            Refer to the `get_gg_timecut` method to see how this function gets 
        invoked internally.
        """
        self.cdata_list = cdata_list
        self.decay_mode = decay_mode
        self.parent_id = parent_id
        self.decay_index = decay_index
        self.spath = spath
        if len(self.spath) > 0:
            abs_Ei, abs_Ef = None, None
            br_Ei, br_Ef = None, None
            total_intensity = []
            d_total_intensity = []
            for i,p in enumerate(self.spath):
                #print("Path number: {0}".format(i+1))
                coinc_intensity = 0.0
                d_coinc_intensity = 0.0
                abs_Ei = self.spath[i][0][0]
                abs_Ef = self.spath[i][0][1]
                br_Ei = self.spath[i][-1][0]
                br_Ef = self.spath[i][-1][1]

                for jdict in self.cdata_list:
                    if jdict["datasetID"] == "GG":
                        if jdict["decayMode"] == self.decay_mode and jdict["parentID"] == self.parent_id and jdict["decayIndex"] == self.decay_index:
                            for each_d in jdict["decaySingles"]:
                                if abs_Ei == int(each_d["levelIndexInitial"]) and abs_Ef == int(each_d["levelIndexFinal"]):
                                    coinc_intensity = each_d["absoluteGammaIntensity"]
                                    try:
                                        if each_d["dAbsoluteGammaIntensity"] is not None:
                                            d_coinc_intensity = (each_d["dAbsoluteGammaIntensity"]/each_d["absoluteGammaIntensity"])**2
                                        else:
                                            d_coinc_intensity = 0.0
                                    except ZeroDivisionError:
                                        d_coinc_intensity = 0.0
                                        
                            for each_n in jdict["normalizedBranchingRatios"]:
                                if br_Ei == int(each_n["levelIndexInitial"]) and br_Ef == int(each_n["levelIndexFinal"]):
                                    coinc_intensity *= each_n["gammaBR"]
                                    try:
                                        if each_n["dGammaBR"] is not None:
                                            d_coinc_intensity += (each_n["dGammaBR"]/each_n["gammaBR"])**2
                                        else:
                                            d_coinc_intensity += 0.0
                                    except ZeroDivisionError:
                                        d_coinc_intensity += 0.0

                            for sp in self.spath[i]:
                                Ei, Ef = None, None
                                if (sp[0] != abs_Ei and sp[1] != abs_Ef) and (sp[0] != br_Ei and sp[1] != br_Ef):
                                    Ei = sp[0]
                                    Ef = sp[1]
                            
                                    for each_n in jdict["normalizedBranchingRatios"]:
                                        if Ei == int(each_n["levelIndexInitial"]) and Ef == int(each_n["levelIndexFinal"]):
                                            coinc_intensity *= each_n["totalTransitionBR"]
                                            try:
                                                if each_n["dTotalTransitionBR"] is not None:
                                                    d_coinc_intensity += (each_n["dTotalTransitionBR"]/each_n["totalTransitionBR"])**2
                                                else:
                                                    d_coinc_intensity += 0.0
                                            except ZeroDivisionError:
                                                d_coinc_intensity += 0.0
                                    
                d_coinc_intensity = coinc_intensity*np.sqrt(d_coinc_intensity)
                total_intensity.append(coinc_intensity)
                d_total_intensity.append(d_coinc_intensity)
            #print("TI:",sum(total_intensity))
            #print("DTI:",np.sqrt(sum([df**2 for df in d_total_intensity])))
            
            return (sum(total_intensity),np.sqrt(sum([df**2 for df in d_total_intensity])))
