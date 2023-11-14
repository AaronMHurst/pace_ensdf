from .base_ensdf import *
from .normalization import Normalization
from .parent import Parent

class Daughter(Parent):
    __doc__="""Class to handle decay data corresponding to the daughter nucleus
    produced in a radioactive-decay process (alpha, beta-minus, 
    electron-capture/beta-plus decay)."""

    def __init__(self):
        BaseENSDF.__init__(self)
        Normalization.__init__(self)
        Parent.__init__(self)

    def get_levels(self, list, str, index, **kwargs):
        """Decay-scheme properties corresponding to levels populated in 
        radioactive-decay processes from alpha, beta-minus, and 
        electron-capture/beta-plus decay.

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
            A list object containing decay-scheme information associated with 
            the levels of the residual nucleus populated following radioactive 
            decay.  The list elements are:

            [0]: Level index corresponding to populated level (int);
            [1]: Associated level energy populated (float);
            [2]: Associated level energy uncertainty (float);           
            [3]: Isomer-decay flag (int).  Only permitted integers are:
                 0: False (i.e., not an isomeric level)
                 1: True (i.e., isomeric level)
            [4]: Number of spin-parity assignments for level (int);
            [5]: Spin assignment for level (float).  If more than one spin is 
                 permissable, the first permutation is given.
            [6]: Spin flag (int).  Only permitted integers are: 
                 1: Firm spin assignment; 
                 -1: Tentative spin assignment.
            [7]: Parity assignment for level (int).  If more than one parity is 
                 permissable, the first permutation is given.
            [8]: Parity flag (int).  Only permitted integers are: 
                 1: Firm parity assignment; 
                 -1: Tentative parity assignment.
            [9]: Number of gammas deexciting level (int).

        Examples:
            get_levels(edata,"Ra226",0,mode="A")
            get_levels(edata,"Co60",0,mode="BM")
            get_levels(edata,"V50",0,mode="ECBP")
        """
        self.list = list
        self.str = str
        self.index = int(index)
        
        decay_mode = BaseENSDF.check_decay([mode for mode in kwargs.values()][0])
        if decay_mode == None:
            print("Invalid decay mode.")
        else:
            #print(decay_mode)

            levels_list = []
            DAUGHTER_EXISTS = False
            for jdict in self.list:
                if decay_mode == jdict["decayMode"] and self.str == jdict["parentID"] and self.index == jdict["decayIndex"]:

                    DAUGHTER_EXISTS = True

                    pid = jdict["parentID"]
                    decay_index = jdict["decayIndex"]
                    pZ = jdict["parentAtomicNumber"]
                    pA = jdict["parentAtomicMass"]
                    did = jdict["daughterID"]
                    dZ = jdict["daughterAtomicNumber"]
                    dA = jdict["daughterAtomicMass"]

                    print("Daughter nucleus: {0} Z={1}, A={2}".format(did, dZ, dA))
                    for each_l in jdict["levelScheme"]:
                        level_index = each_l["levelIndex"]
                        level_energy = each_l["levelEnergy"]
                        d_level_energy = each_l["dLevelEnergy"]
                        isomer_flag = None
                        if each_l["levelIsIsomer"] == True:
                            isomer_flag = 1
                        elif each_l["levelIsIsomer"] == False:
                            isomer_flag = 0
                        num_jpi = each_l["numberOfSpins"]
                        spin, parity = None, None
                        spin_flag, parity_flag = None, None
                        for each_s in each_l["spins"]:
                            if each_s["spinIndex"] == 0:
                                spin = each_s["spinReal"]
                                parity = each_s["parity"]

                                if each_s["spinIsTentative"] == False:
                                    spin_flag = 1
                                else:
                                    spin_flag = -1

                                if each_s["parityIsTentative"] == False:
                                    parity_flag = 1
                                else:
                                    parity_flag = -1
                                    
                        num_gammas = each_l["numberOfGammas"]

                        levels_list.append([level_index, level_energy, d_level_energy, isomer_flag, num_jpi, spin, spin_flag, parity, parity_flag, num_gammas])
            if DAUGHTER_EXISTS == True:
                return levels_list
            else:
                return

    def get_levels_and_gammas(self, list, str, index, **kwargs):
        """Level energies, dexcitation gamma rays, and associated properties 
        observed in the residual daughter nucleus following radioactive-decay 
        processes according to alpha, beta-minus, and electron-capture/beta-plus
        decay.

        Notes:
            (i) Median-symmetrized values are adopted for gamma-ray mixing 
            ratios whereupon asymmetric quantities are encountered in the source
            ENSDF data set.  

            (ii) Gamma-ray intensities have not been normalized (i.e., these are
            the raw values from the RI field of the ENSDF Gamma record).  For 
            absolute intensities refer to methods from the Normalization class.

            (iii) Total internal-conversion coefficients (where given) are 
            calculated values obtained using the BrIcc code:

            [2008Ki07] - T.Kibedi et al., Nucl. Instrum. Methods Phys. Res. 
            Sect. A 589, 202 (2008).

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
            A list object containing levels, gammas, and associated decay-scheme
            properties of the residual nucleus populated following radioactive 
            decay.  The list elements are:

            [0]: Level index corresponding to initial level (int);
            [1]: Level index corresponding to final level (int);
            [2]: Associated initial level energy in keV (float);
            [3]: Associated final level energy in keV (float);
            [4]: Number of gammas associated with initial level (int);
            [5]: Index corresponding to gamma-ray number: 0 for first gamma, 
                 1 for second gamma, etc. (int);
            [6]: Deexcitation gamma-ray energy in keV (float);
            [7]: Deexcitation gamma-ray energy uncertainty (float);
            [8]: Raw gamma-ray intensity (float);
            [9]: Raw gamma-ray intensity uncertainty (float);
            [10]: Gamma-ray multipolarity (str);
            [11]: Gamma-ray mixing ratio (float).  The median symmetrized value 
                  is given where relevant.
            [12]: Gamma-ray mixing ratio uncertainty (float).  The median 
                  symmetrized value is given where relevant.
            [13]: Mixing-ratio flag to indicate its sign (int).  Only permitted
                  integers are:
                  0: No sign given for mixing ratio;
                  1: Positive-signed mixing ratio;
                  -1: Negative-signed mixing ratio.
            [14]: BrIcc-calculated total internal-conversion coefficient 
                  (float);
            [15]: Total internal-conversion coefficient uncertainty (float).

        Examples:
            get_levels_and_gammas(edata,"Ra226",0,mode="A")
            get_levels_and_gammas(edata,"Co60",0,mode="BM")
            get_levels_and_gammas(edata,"V50",0,mode="ECBP")
        """
        self.list = list
        self.str = str
        self.index = int(index)
        
        decay_mode = BaseENSDF.check_decay([mode for mode in kwargs.values()][0])
        if decay_mode == None:
            print("Invalid decay mode.")
        else:
            #print(decay_mode)

            gammas_list = []
            DAUGHTER_EXISTS = False
            for jdict in self.list:
                if decay_mode == jdict["decayMode"] and self.str == jdict["parentID"] and self.index == jdict["decayIndex"]:

                    DAUGHTER_EXISTS = True

                    pid = jdict["parentID"]
                    decay_index = jdict["decayIndex"]
                    pZ = jdict["parentAtomicNumber"]
                    pA = jdict["parentAtomicMass"]
                    did = jdict["daughterID"]
                    dZ = jdict["daughterAtomicNumber"]
                    dA = jdict["daughterAtomicMass"]

                    print("Daughter nucleus: {0} Z={1}, A={2}".format(did, dZ, dA))
                    for each_l in jdict["levelScheme"]:
                        num_gammas = each_l["numberOfGammas"]
                        if num_gammas > 0:
                            gamma_index = 0
                            for each_g in each_l["gammaDecay"]:
                                level_index_i = each_g["levelIndexInitial"]
                                level_energy_i = each_g["levelEnergyInitial"]
                                level_index_f = each_g["levelIndexFinal"]
                                level_energy_f = each_g["levelEnergyFinal"]

                                gamma_energy = each_g["gammaEnergy"]
                                d_gamma_energy = each_g["dGammaEnergy"]
                                gamma_intensity = each_g["gammaIntensity"]
                                d_gamma_intensity = each_g["dGammaIntensity"]

                                multipolarity = each_g["multipolarity"]
                                
                                mixing_ratio = each_g["mixingRatio"]
                                try:
                                    mixing_ratio = float(mixing_ratio)
                                except TypeError:
                                    if mixing_ratio is None:
                                        mixing_ratio = each_g["mixingRatio"]
                                
                                d_mixing_ratio = each_g["dMixingRatio"]
                                try:
                                    d_mixing_ratio = float(d_mixing_ratio)
                                except TypeError:
                                    if d_mixing_ratio is None:
                                        d_mixing_ratio = each_g["dMixingRatio"]
                                
                                mixing_flag = None
                                if each_g["mixingRatioSign"] == "positive":
                                    mixing_flag = 1
                                elif each_g["mixingRatioSign"] == "negative":
                                    mixing_flag = -1
                                else:
                                    mixing_flag = 0
                                alpha = each_g["calculatedTotalInternalConversionCoefficient"]
                                d_alpha = each_g["dCalculatedTotalInternalConversionCoefficient"]

                                gammas_list.append([level_index_i, level_index_f, level_energy_i, level_energy_f, num_gammas, gamma_index, gamma_energy, d_gamma_energy, gamma_intensity, d_gamma_intensity, multipolarity, mixing_ratio, d_mixing_ratio, mixing_flag, alpha, d_alpha])

                                gamma_index += 1
            if DAUGHTER_EXISTS == True:
                return gammas_list
            else:
                return

    def get_levels_and_gammas_subshells(self, list, str, index, **kwargs):
        """Level energies, dexcitation gamma rays, and associated properties
        including atomic subshell information, according to input keyword 
        argument, for the corresponding residual daughter nucleus produced 
        following radioactive-decay processes for alpha, beta-minus, and 
        electron-capture/beta-plus decay.

        Notes:
            (i) Median-symmetrized values are adopted for gamma-ray mixing 
            ratios whereupon asymmetric quantities are encountered in the source
            ENSDF data set.  

            (ii) Gamma-ray intensities have not been normalized (i.e., these are
            the raw values from the RI field of the ENSDF Gamma record).  For 
            absolute intensities refer to methods from the Normalization class.

            (iii) Total internal-conversion coefficients (where given) are 
            calculated values obtained using the BrIcc code:

            [2008Ki07] - T.Kibedi et al., Nucl. Instrum. Methods Phys. Res. 
            Sect. A 589, 202 (2008).

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

                    (ii) Atomic-subshell information

                    subshell='calc'    : Calculated atomic subshell internal 
                                         conversion coefficients (K to Q shell).
                    subshell='sumcalc' : Calculated atomic subshell summed 
                                         contribution L+ (sum over L shell to Q
                                         shell) to Q+.
                    subshell='ratio'   : Ratio of subshell electron intensity to
                                         total (K to Q shell).
                    subshell='expt'    : Measured atomic subshell internal 
                                         conversion coefficients (K to Q shell).
                    subshell='electron': Electron subshell intensities (K to Q 
                                         shell).

                    Only the above keyword arguments (case insensitive) are 
                    acceptable.  

        Returns: 
            A list object containing levels, gammas, and associated decay-scheme
            properties of the residual nucleus populated following radioactive 
            decay.  The first 16 list elements are the same as those from the 
            "get_levels_and_gammas()" method:

            [0]: Level index corresponding to initial level (int);
            [1]: Level index corresponding to final level (int);
            [2]: Associated initial level energy in keV (float);
            [3]: Associated final level energy in keV (float);
            [4]: Number of gammas associated with initial level (int);
            [5]: Index corresponding to gamma-ray number: 0 for first gamma, 
                 1 for second gamma, etc. (int);
            [6]: Deexcitation gamma-ray energy in keV (float);
            [7]: Deexcitation gamma-ray energy uncertainty (float);
            [8]: Raw gamma-ray intensity (float);
            [9]: Raw gamma-ray intensity uncertainty (float);
            [10]: Gamma-ray multipolarity (str);
            [11]: Gamma-ray mixing ratio (float).  The median symmetrized value 
                  is given where relevant.
            [12]: Gamma-ray mixing ratio uncertainty (float).  The median 
                  symmetrized value is given where relevant.
            [13]: Mixing-ratio flag to indicate its sign (int).  Only permitted
                  integers are:
                  0: No sign given for mixing ratio;
                  1: Positive-signed mixing ratio;
                  -1: Negative-signed mixing ratio.
            [14]: BrIcc-calculated total internal-conversion coefficient 
                  (float);
            [15]: Total internal-conversion coefficient uncertainty (float).

            The remaining elements depend upon the keyword argument provided.  
            The keyword arguments 'calc', 'ratio', 'expt', and 'electron' 
            provide the following atomic-subshell contributions:

            [16]: K-shell contribution (float).
            [17]: K-shell contribution uncertainty (float).
            [18]: L-shell contribution (float).
            [19]: L-shell contribution uncertainty (float).
            [20]: M-shell contribution (float).
            [21]: M-shell contribution uncertainty (float).
            [22]: N-shell contribution (float).
            [23]: N-shell contribution uncertainty (float).
            [24]: O-shell contribution (float).
            [25]: O-shell contribution uncertainty (float).
            [26]: P-shell contribution (float).
            [27]: P-shell contribution uncertainty (float).
            [28]: Q-shell contribution (float).
            [29]: Q-shell contribution uncertainty (float).

            The "subshell='sumcalc'" keyword argument produces the following 
            atomic subshell contributions:

            [16]: L+-shell (sum over L to Q) contribution (float).
            [17]: L+-shell contribution uncertainty (float).
            [18]: M+-shell (sum over M to Q) contribution (float).
            [19]: M+-shell contribution uncertainty (float).
            [20]: N+-shell (sum over N to Q) contribution (float).
            [21]: N+-shell contribution uncertainty (float).
            [22]: O+-shell (sum over O to Q) contribution (float).
            [23]: O+-shell contribution uncertainty (float).
            [24]: P+-shell (sum over P to Q) contribution (float).
            [25]: P+-shell contribution uncertainty (float).
            [26]: Q+-shell (sum over Q) contribution (float).
            [27]: Q+-shell contribution uncertainty (float).

        

        Examples:
            get_levels_and_gammas_subshells(edata,"Pu239",0,mode="A",subshell='calc')
            get_levels_and_gammas_subshells(edata,"Co60",0,mode="BM",subshell='sumcalc')
            get_levels_and_gammas_subshells(edata,"Re189",0,mode="BM",subshell='ratio') 
            get_levels_and_gammas_subshells(edata,"Au182",0,mode="ECBP",subshell='expt')
            get_levels_and_gammas_subshells(edata,"Nd136",0,mode="ECBP",subshell='electron') 
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
            #print(decay_mode)

            # Check for subshell keyword:
            SUBSHELL_TYPE = False
            SUBSHELL_CALC = False
            SUBSHELL_SUMCALC = False
            SUBSHELL_RATIO = False
            SUBSHELL_EXPT = False
            SUBSHELL_ELECTRON = False

            for subshell in kwargs.values():
                if subshell.lower()=='calc': 
                    SUBSHELL_TYPE = True
                    SUBSHELL_CALC = True
                elif subshell.lower()=='sumcalc': 
                    SUBSHELL_TYPE = True
                    SUBSHELL_SUMCALC = True
                elif subshell.lower()=='ratio': 
                    SUBSHELL_TYPE = True
                    SUBSHELL_RATIO = True
                elif subshell.lower()=='expt': 
                    SUBSHELL_TYPE = True
                    SUBSHELL_EXPT = True
                elif subshell.lower()=='electron': 
                    SUBSHELL_TYPE = True
                    SUBSHELL_ELECTRON = True
                #else:
            if SUBSHELL_TYPE == False:
                print("Inavlid atomic-subshell argument.  The only arguements accepted are:")
                print("subshell='calc'")
                print("subshell='sumcalc'")
                print("subshell='ratio'")
                print("subshell='expt'")
                print("subshell='electron'")

            elif SUBSHELL_TYPE == True:
                gammas_list = []
                DAUGHTER_EXISTS = False
                for jdict in self.list:
                    if decay_mode == jdict["decayMode"] and self.str == jdict["parentID"] and self.index == jdict["decayIndex"]:

                        DAUGHTER_EXISTS = True

                        pid = jdict["parentID"]
                        decay_index = jdict["decayIndex"]
                        pZ = jdict["parentAtomicNumber"]
                        pA = jdict["parentAtomicMass"]
                        did = jdict["daughterID"]
                        dZ = jdict["daughterAtomicNumber"]
                        dA = jdict["daughterAtomicMass"]

                        print("Daughter nucleus: {0} Z={1}, A={2}".format(did, dZ, dA))
                        for each_l in jdict["levelScheme"]:
                            num_gammas = each_l["numberOfGammas"]
                            if num_gammas > 0:
                                gamma_index = 0
                                for each_g in each_l["gammaDecay"]:
                                    level_index_i = each_g["levelIndexInitial"]
                                    level_energy_i = each_g["levelEnergyInitial"]
                                    level_index_f = each_g["levelIndexFinal"]
                                    level_energy_f = each_g["levelEnergyFinal"]

                                    gamma_energy = each_g["gammaEnergy"]
                                    d_gamma_energy = each_g["dGammaEnergy"]
                                    gamma_intensity = each_g["gammaIntensity"]
                                    d_gamma_intensity = each_g["dGammaIntensity"]

                                    multipolarity = each_g["multipolarity"]
                                    
                                    mixing_ratio = each_g["mixingRatio"]
                                    try:
                                        mixing_ratio = float(mixing_ratio)
                                    except TypeError:
                                        if mixing_ratio is None:
                                            mixing_ratio = each_g["mixingRatio"]
                                            
                                    d_mixing_ratio = each_g["dMixingRatio"]
                                    try:
                                        d_mixing_ratio = float(d_mixing_ratio)
                                    except TypeError:
                                        if d_mixing_ratio is None:
                                            d_mixing_ratio = each_g["dMixingRatio"]
                                    
                                    mixing_flag = None
                                    if each_g["mixingRatioSign"] == "positive":
                                        mixing_flag = 1
                                    elif each_g["mixingRatioSign"] == "negative":
                                        mixing_flag = -1
                                    else:
                                        mixing_flag = 0
                                    alpha = each_g["calculatedTotalInternalConversionCoefficient"]
                                    d_alpha = each_g["dCalculatedTotalInternalConversionCoefficient"]

                                    # Append list according to subshell keyword argument

                                    sub_K, d_sub_K = None, None
                                    sub_L, d_sub_L = None, None
                                    sub_M, d_sub_M = None, None
                                    sub_N, d_sub_N = None, None
                                    sub_O, d_sub_O = None, None
                                    sub_P, d_sub_P = None, None
                                    sub_Q, d_sub_Q = None, None

                                    if SUBSHELL_CALC == True:
                                        for each_ss in each_g["calculatedAtomicShellConversionCoefficients"]:
                                            sub_K = each_ss["calculatedInternalConversionCoefficientAtomicShellK"]
                                            d_sub_K = each_ss["dCalculatedInternalConversionCoefficientAtomicShellK"]
                                            sub_L = each_ss["calculatedInternalConversionCoefficientAtomicShellL"]
                                            d_sub_L = each_ss["dCalculatedInternalConversionCoefficientAtomicShellL"]
                                            sub_M = each_ss["calculatedInternalConversionCoefficientAtomicShellM"]
                                            d_sub_M = each_ss["dCalculatedInternalConversionCoefficientAtomicShellM"]
                                            sub_N = each_ss["calculatedInternalConversionCoefficientAtomicShellN"]
                                            d_sub_N = each_ss["dCalculatedInternalConversionCoefficientAtomicShellN"]
                                            sub_O = each_ss["calculatedInternalConversionCoefficientAtomicShellO"]
                                            d_sub_O = each_ss["dCalculatedInternalConversionCoefficientAtomicShellO"]
                                            sub_P = each_ss["calculatedInternalConversionCoefficientAtomicShellP"]
                                            d_sub_P = each_ss["dCalculatedInternalConversionCoefficientAtomicShellP"]
                                            sub_Q = each_ss["calculatedInternalConversionCoefficientAtomicShellQ"]
                                            d_sub_Q = each_ss["dCalculatedInternalConversionCoefficientAtomicShellQ"]

                                    elif SUBSHELL_SUMCALC == True:
                                        for each_ss in each_g["sumCalculatedAtomicShellConversionCoefficients"]:
                                            sub_L = each_ss["sumConversionCoefficientsAtomicShellPlusL"]
                                            d_sub_L = each_ss["dSumConversionCoefficientsAtomicShellPlusL"]
                                            sub_M = each_ss["sumConversionCoefficientsAtomicShellPlusM"]
                                            d_sub_M = each_ss["dSumConversionCoefficientsAtomicShellPlusM"]
                                            sub_N = each_ss["sumConversionCoefficientsAtomicShellPlusN"]
                                            d_sub_N = each_ss["dSumConversionCoefficientsAtomicShellPlusN"]
                                            sub_O = each_ss["sumConversionCoefficientsAtomicShellPlusO"]
                                            d_sub_O = each_ss["dSumConversionCoefficientsAtomicShellPlusO"]
                                            sub_P = each_ss["sumConversionCoefficientsAtomicShellPlusP"]
                                            d_sub_P = each_ss["dSumConversionCoefficientsAtomicShellPlusP"]
                                            sub_Q = each_ss["sumConversionCoefficientsAtomicShellPlusQ"]
                                            d_sub_Q = each_ss["doSumConversionCoefficientsAtomicShellPlusQ"]
                                            # Typo in syntax - fix source code and 'sed' the correct syntax

                                    elif SUBSHELL_RATIO == True:
                                        for each_ss in each_g["conversionElectronIntensityAtomicShellToTotalRatios"]:
                                            sub_K = each_ss["conversionElectronIntensityRatioAtomicShellKtoTotal"]
                                            d_sub_K = each_ss["dConversionElectronIntensityRatioAtomicShellKtoTotal"]
                                            sub_L = each_ss["conversionElectronIntensityRatioAtomicShellLtoTotal"]
                                            d_sub_L = each_ss["dConversionElectronIntensityRatioAtomicShellLtoTotal"]
                                            sub_M = each_ss["conversionElectronIntensityRatioAtomicShellMtoTotal"]
                                            d_sub_M = each_ss["dConversionElectronIntensityRatioAtomicShellMtoTotal"]
                                            sub_N = each_ss["conversionElectronIntensityRatioAtomicShellNtoTotal"]
                                            d_sub_N = each_ss["dConversionElectronIntensityRatioAtomicShellNtoTotal"]
                                            sub_O = each_ss["conversionElectronIntensityRatioAtomicShellOtoTotal"]
                                            d_sub_O = each_ss["dConversionElectronIntensityRatioAtomicShellOtoTotal"]
                                            sub_P = each_ss["conversionElectronIntensityRatioAtomicShellPtoTotal"]
                                            d_sub_P = each_ss["dConversionElectronIntensityRatioAtomicShellPtoTotal"]
                                            sub_Q = each_ss["conversionElectronIntensityRatioAtomicShellQtoTotal"]
                                            d_sub_Q = each_ss["dConversionElectronIntensityRatioAtomicShellQtoTotal"]

                                    elif SUBSHELL_EXPT == True:
                                        for each_ss in each_g["experimentalAtomicShellConversionCoefficients"]:
                                            sub_K = each_ss["experimentalInternalConversionCoefficientAtomicShellK"]
                                            d_sub_K = each_ss["dExperimentalInternalConversionCoefficientAtomicShellK"]
                                            sub_L = each_ss["experimentalInternalConversionCoefficientAtomicShellL"]
                                            d_sub_L = each_ss["dExperimentalInternalConversionCoefficientAtomicShellL"]
                                            sub_M = each_ss["experimentalInternalConversionCoefficientAtomicShellM"]
                                            d_sub_M = each_ss["dExperimentalInternalConversionCoefficientAtomicShellM"]
                                            sub_N = each_ss["experimentalInternalConversionCoefficientAtomicShellN"]
                                            d_sub_N = each_ss["dExperimentalInternalConversionCoefficientAtomicShellN"]
                                            sub_O = each_ss["experimentalInternalConversionCoefficientAtomicShellO"]
                                            d_sub_O = each_ss["dExperimentalInternalConversionCoefficientAtomicShellO"]
                                            sub_P = each_ss["experimentalInternalConversionCoefficientAtomicShellP"]
                                            d_sub_P = each_ss["dExperimentalInternalConversionCoefficientAtomicShellP"]
                                            sub_Q = each_ss["experimentalInternalConversionCoefficientAtomicShellQ"]
                                            d_sub_Q = each_ss["dExperimentalInternalConversionCoefficientAtomicShellQ"]

                                    elif SUBSHELL_ELECTRON == True:
                                        for each_ss in each_g["atomicShellConversionElectronIntensities"]:
                                            sub_K = each_ss["conversionElectronIntensityAtomicShellK"]
                                            d_sub_K = each_ss["dConversionElectronIntensityAtomicShellK"]
                                            sub_L = each_ss["conversionElectronIntensityAtomicShellL"]
                                            d_sub_L = each_ss["dConversionElectronIntensityAtomicShellL"]
                                            sub_M = each_ss["conversionElectronIntensityAtomicShellM"]
                                            d_sub_M = each_ss["dConversionElectronIntensityAtomicShellM"]
                                            sub_N = each_ss["conversionElectronIntensityAtomicShellN"]
                                            d_sub_N = each_ss["dConversionElectronIntensityAtomicShellN"]
                                            sub_O = each_ss["conversionElectronIntensityAtomicShellO"]
                                            d_sub_O = each_ss["dConversionElectronIntensityAtomicShellO"]
                                            sub_P = each_ss["conversionElectronIntensityAtomicShellP"]
                                            d_sub_P = each_ss["dConversionElectronIntensityAtomicShellP"]
                                            sub_Q = each_ss["conversionElectronIntensityAtomicShellQ"]
                                            d_sub_Q = each_ss["dConversionElectronIntensityAtomicShellQ"]

                                    else:
                                        pass

                                    if sub_K == None and d_sub_K == None:
                                        gammas_list.append([level_index_i, level_index_f, level_energy_i, level_energy_f, num_gammas, gamma_index, gamma_energy, d_gamma_energy, gamma_intensity, d_gamma_intensity, multipolarity, mixing_ratio, d_mixing_ratio, mixing_flag, alpha, d_alpha, sub_L, d_sub_L, sub_M, d_sub_M, sub_N, d_sub_N, sub_O, d_sub_O, sub_P, d_sub_P, sub_Q, d_sub_Q])

                                    else:
                                        gammas_list.append([level_index_i, level_index_f, level_energy_i, level_energy_f, num_gammas, gamma_index, gamma_energy, d_gamma_energy, gamma_intensity, d_gamma_intensity, multipolarity, mixing_ratio, d_mixing_ratio, mixing_flag, alpha, d_alpha, sub_K, d_sub_K, sub_L, d_sub_L, sub_M, d_sub_M, sub_N, d_sub_N, sub_O, d_sub_O, sub_P, d_sub_P, sub_Q, d_sub_Q])

                                    gamma_index += 1
                if DAUGHTER_EXISTS == True:
                    return gammas_list
                else:
                    return

    def find_multiple_jpi(self, list, str, index, **kwargs):
        """Finds all levels in decay-scheme of residual nucleus with multiple 
        spin-parity permutations.

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
            [4]: Decay-level energy of parent nucleus (float);
            [5]: Daughter ID (str);
            [6]: Daughter atomic (Z) number (int);
            [7]: Daughter mass (A) number (int);

            The corresponding dictionary values are lists containing all
            different permutations of the spin-parity assignments for each level
            with multiple assignments:

            [0]: Level index (int);
            [1]: Associated level energy (float);
            [2]: Associated level energy uncertainty (float);
            [3]: Number of spin-parity assignments for level (int);
            [4]: Spin-parity index (int):
                 0 for the first,
                 1 for the second, etc.
            [5]: Spin assignment for level (float);
            [6]: Parity assignment for level (int):
                 1: Positive parity;
                 -1: Negative parity;
                 0: No parity given.

        Example:
            find_multiple_jpi(edata, "Ar45", 0, mode="BM")
        """
        self.list = list
        self.str = str
        self.index = int(index)
        
        decay_mode = BaseENSDF.check_decay([mode for mode in kwargs.values()][0])
        if decay_mode == None:
            print("Invalid decay mode.")
        else:
            #print(decay_mode)
        
            mult_jpi_dict = {}
            level_scheme = []
            DAUGHTER_EXISTS = False
            for jdict in self.list:
                if decay_mode == jdict["decayMode"] and self.str == jdict["parentID"] and self.index == jdict["decayIndex"]:
                    
                    DAUGHTER_EXISTS = True
                    
                    pid = jdict["parentID"]
                    decay_index = jdict["decayIndex"]
                    pZ = jdict["parentAtomicNumber"]
                    pA = jdict["parentAtomicMass"]
                    did = jdict["daughterID"]
                    dZ = jdict["daughterAtomicNumber"]
                    dA = jdict["daughterAtomicMass"]

                    parent_decay_energy = None
                    for each_p in jdict["parentDecay"]:
                        parent_decay_energy = each_p["parentDecayLevelEnergy"]
                        
                    pd_pair_tuple = (pid,pZ,pA,decay_index,parent_decay_energy,did,dZ,dA)
                    
                    for each_l in jdict["levelScheme"]:
                        level_index = each_l["levelIndex"]
                        level_energy = each_l["levelEnergy"]
                        d_level_energy = each_l["dLevelEnergy"]
                        num_spins = each_l["numberOfSpins"]
                        if num_spins > 1:
                            for each_s in each_l["spins"]:
                                spin_index = each_s["spinIndex"]
                                spin = each_s["spinReal"]
                                parity = each_s["parity"]
                            
                                level_scheme.append([level_index, level_energy, d_level_energy, num_spins, spin_index, spin, parity])
                    mult_jpi_dict.update({pd_pair_tuple:level_scheme})
            if DAUGHTER_EXISTS == True:                
                return mult_jpi_dict
            else:
                return

    def find_unique_jpi(self, list, str, index, **kwargs):
        """Finds all levels in decay-scheme of residual nucleus with unique 
        spin-parity permutations, where both spin and parity are firmly 
        assigned.

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
            [4]: Decay-level energy of parent nucleus (float);
            [5]: Daughter ID (str);
            [6]: Daughter atomic (Z) number (int);
            [7]: Daughter mass (A) number (int);

            The corresponding dictionary values are lists corresponding to 
            levels with unique and firm assignments for both spin and parity:

            [0]: Level index (int);
            [1]: Associated level energy (float);
            [2]: Associated level energy uncertainty (float);
            [3]: Number of spin-parity assignments for level (int);
            [4]: Spin-parity index (int):
                 0 for the first,
                 1 for the second, etc.
            [5]: Spin assignment for level (float);
            [6]: Parity assignment for level (int):
                 1: Positive parity;
                 -1: Negative parity;
                 0: No parity given.

        Example:
            find_unique_jpi(edata, "Ar45", 0, mode="BM")
        """
        self.list = list
        self.str = str
        self.index = int(index)
        
        decay_mode = BaseENSDF.check_decay([mode for mode in kwargs.values()][0])
        if decay_mode == None:
            print("Invalid decay mode.")
        else:
            #print(decay_mode)
        
            unique_jpi_dict = {}
            level_scheme = []
            DAUGHTER_EXISTS = False
            for jdict in self.list:
                if decay_mode == jdict["decayMode"] and str == jdict["parentID"] and index == jdict["decayIndex"]:

                    DAUGHTER_EXISTS = True
                    
                    pid = jdict["parentID"]
                    decay_index = jdict["decayIndex"]
                    pZ = jdict["parentAtomicNumber"]
                    pA = jdict["parentAtomicMass"]
                    did = jdict["daughterID"]
                    dZ = jdict["daughterAtomicNumber"]
                    dA = jdict["daughterAtomicMass"]

                    parent_decay_energy = None
                    for each_p in jdict["parentDecay"]:
                        parent_decay_energy = each_p["parentDecayLevelEnergy"]
                        
                    pd_pair_tuple = (pid,pZ,pA,decay_index,parent_decay_energy,did,dZ,dA)
                    
                    for each_l in jdict["levelScheme"]:
                        level_index = each_l["levelIndex"]
                        level_energy = each_l["levelEnergy"]
                        d_level_energy = each_l["dLevelEnergy"]
                        num_spins = each_l["numberOfSpins"]
                        if num_spins == 1:
                            for each_s in each_l["spins"]:
                                if each_s["spinIsTentative"] == False and each_s["parityIsTentative"] == False:
                                    spin_index = each_s["spinIndex"]
                                    spin = each_s["spinReal"]
                                    parity = each_s["parity"]
                                    
                                    level_scheme.append([level_index, level_energy, d_level_energy, num_spins, spin_index, spin, parity])
                                    
                    unique_jpi_dict.update({pd_pair_tuple:level_scheme})
            if DAUGHTER_EXISTS == True:
                return unique_jpi_dict
            else:
                return

    def find_isomers(self, list, str, index, **kwargs):
        """Finds all isomeric levels in decay-scheme of residual nucleus.

        Notes:
            Median-symmetrized values are adopted for the halflife whereupon
            asymmetric quantities are encountered in the source ENSDF data set.
            
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

            The corresponding dictionary values are lists containing all  
            levels with associated halflife information:

            [0]: Level index (int);
            [1]: Associated level energy (float);
            [2]: Associated level energy uncertainty (float);
            [3]: Halflife in 'best' units or in 'seconds' (float);
            [4]: Halflife uncertainty (float);
            [5]: Halflife time units (str).

        Example:
            find_isomers(edata, "U237", 0, mode="BM", units="best")
            find_isomers(edata, "U237", 0, mode="BM", units="seconds")
        """
        self.list = list
        self.str = str
        self.index = int(index)
        
        if kwargs == {} or kwargs == None:
            print("Please pass keyword arguments for decay mode and halflife units:")
            print("'mode=<str>'")
            print("'units=<str>'")
            
        decay_mode = None
        #decay_mode = check_decay([mode for mode in kwargs.values() if mode != None][0])
        for kwarg in kwargs.values():
            decay_mode = BaseENSDF.check_decay(kwarg)
            if decay_mode != None:
                break
            
        if decay_mode == None:
            print("Invalid decay mode.")
            print("Please pass one of the following keyword arguments:")
            print("mode='A'")
            print("mode='BM'")
            print("mode='ECBP'")

        else:
            #print(decay_mode)
        
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
                print("Inavlid units for halflife.  The only arguments accepted are:")
                print("units='best'")
                print("units='seconds'")
                print("units='s'")
        
            if WRONG_UNITS == False:
                
                isomer_dict = {}
                level_scheme = []
                DAUGHTER_EXISTS = False
                for jdict in self.list:
                    if decay_mode == jdict["decayMode"] and self.str == jdict["parentID"] and self.index == jdict["decayIndex"]:

                        DAUGHTER_EXISTS = True
                        
                        pid = jdict["parentID"]
                        decay_index = jdict["decayIndex"]
                        pZ = jdict["parentAtomicNumber"]
                        pA = jdict["parentAtomicMass"]
                        did = jdict["daughterID"]
                        dZ = jdict["daughterAtomicNumber"]
                        dA = jdict["daughterAtomicMass"]

                        parent_decay_energy = None
                        for each_p in jdict["parentDecay"]:
                            parent_decay_energy = each_p["parentDecayLevelEnergy"]
                        pd_pair_tuple = (pid,pZ,pA,decay_index,parent_decay_energy,did,dZ,dA)
                        
                        for each_l in jdict["levelScheme"]:
                            level_index = each_l["levelIndex"]
                            level_energy = each_l["levelEnergy"]
                            d_level_energy = each_l["dLevelEnergy"]
                            
                            half_life, d_half_life, unit_half_life = None, None, None
                            if each_l["levelIsIsomer"] == True:
                                for each_i in each_l["isomerDecay"]:
                                    if BEST_UNITS == True:
                                        half_life = each_i["halfLifeBest"]
                                        d_half_life = each_i["dHalfLifeBest"]
                                        unit_half_life = each_i["unitHalfLifeBest"]
                                    else:
                                        half_life = each_i["halfLifeConverted"]
                                        d_half_life = each_i["dHalfLifeConverted"]
                                        unit_half_life = each_i["unitHalfLifeConverted"]

                                # Check for widths
                                if (half_life is None) and (d_half_life is None) and (unit_half_life is None):
                                    # Convert widths to T1/2
                                    if len(each_l["decayWidth"]) == 1:
                                        for each_w in each_l["decayWidth"]:
                                            width_MeV = each_w["decayWidthConverted"]
                                            d_width_MeV = each_w["dDecayWidthConverted"]
                                            
                                            half_life = BaseENSDF.convert_width_or_halflife(self,width_MeV)
                                            d_half_life = BaseENSDF.convert_width_or_halflife(self,d_width_MeV)
                                            unit_half_life = "s"
                                    
                                level_scheme.append([level_index, level_energy, d_level_energy, half_life, d_half_life, unit_half_life])
                                
                        isomer_dict.update({pd_pair_tuple: level_scheme})

                if DAUGHTER_EXISTS == True:
                    return isomer_dict
                else:
                    return


    def find_decay_widths(self, list, str, index, **kwargs):
        """Finds all decay widths in decay-scheme of residual nucleus.

        Notes:
            Median-symmetrized values are adopted for the halflife whereupon
            asymmetric quantities are encountered in the source ENSDF data set.
            
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

                    (ii) Decay-width units

                    units='best'     
                    units='MeV'  

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

            The corresponding dictionary values are lists containing all  
            levels with associated halflife information:

            [0]: Level index (int);
            [1]: Associated level energy (float);
            [2]: Associated level energy uncertainty (float);
            [3]: Decay width in 'best' units or in 'seconds' (float);
            [4]: Decay width uncertainty (float);
            [5]: Decay width time units (str).
            [6]: Flag to indicate source of decay width (bool):
                 True: Decay width parsed from ENSDF;
                 False: Decay width converted from halflife.

        Example:
            find_decay_widths(edata, "Ar32", 0, mode="ECBP", units="best")
            find_decay_widths(edata, "Ar32", 0, mode="ECBP", units="MeV")
        """
        self.list = list
        self.str = str
        self.index = int(index)
        
        if kwargs == {} or kwargs == None:
            print("Please pass keyword arguments for decay mode and halflife units:")
            print("'mode=<str>'")
            print("'units=<str>'")
            
        decay_mode = None
        #decay_mode = check_decay([mode for mode in kwargs.values() if mode != None][0])
        for kwarg in kwargs.values():
            decay_mode = BaseENSDF.check_decay(kwarg)
            if decay_mode != None:
                break
            
        if decay_mode == None:
            print("Invalid decay mode.")
            print("Please pass one of the following keyword arguments:")
            print("mode='A'")
            print("mode='BM'")
            print("mode='ECBP'")

        else:
            #print(decay_mode)
        
            BEST_UNITS = False
            WRONG_UNITS = True
            for unit in kwargs.values():
                if unit.lower()=='best': 
                    BEST_UNITS = True
                    WRONG_UNITS = False
                elif (unit=='MeV'):
                    BEST_UNITS = False
                    WRONG_UNITS = False
                #else:
            if WRONG_UNITS == True:
                print("Inavlid units for decay width.  The only arguments accepted are:")
                print("units='best'")
                print("units='MeV'")
        
            if WRONG_UNITS == False:
                
                width_dict = {}
                level_scheme = []
                DAUGHTER_EXISTS = False
                for jdict in self.list:
                    if decay_mode == jdict["decayMode"] and self.str == jdict["parentID"] and self.index == jdict["decayIndex"]:

                        DAUGHTER_EXISTS = True
                        
                        pid = jdict["parentID"]
                        decay_index = jdict["decayIndex"]
                        pZ = jdict["parentAtomicNumber"]
                        pA = jdict["parentAtomicMass"]
                        did = jdict["daughterID"]
                        dZ = jdict["daughterAtomicNumber"]
                        dA = jdict["daughterAtomicMass"]

                        parent_decay_energy = None
                        for each_p in jdict["parentDecay"]:
                            parent_decay_energy = each_p["parentDecayLevelEnergy"]
                        pd_pair_tuple = (pid,pZ,pA,decay_index,parent_decay_energy,did,dZ,dA)
                        
                        for each_l in jdict["levelScheme"]:
                            level_index = each_l["levelIndex"]
                            level_energy = each_l["levelEnergy"]
                            d_level_energy = each_l["dLevelEnergy"]
                            
                            #half_life, d_half_life, unit_half_life = None, None, None
                            decay_width, d_decay_width, unit_decay_width = None, None, None
                            CONVERTED_WIDTH = False
                            if each_l["levelIsIsomer"] == True:
                                if len(each_l["decayWidth"]) == 1:
                                    CONVERTED_WIDTH = False
                                    for each_w in each_l["decayWidth"]:
                                        if BEST_UNITS == True:
                                            decay_width = each_w["decayWidthBest"]
                                            d_decay_width = each_w["dDecayWidthBest"]
                                            unit_decay_width = each_w["unitDecayWidthBest"]
                                        else:
                                            decay_width = each_w["decayWidthConverted"]
                                            d_decay_width = each_w["dDecayWidthConverted"]
                                            unit_decay_width = each_w["unitDecayWidthConverted"]

                                elif len(each_l["isomerDecay"]) == 1:
                                    CONVERTED_WIDTH = True
                                    for each_i in each_l["isomerDecay"]:
                                        half_life = each_i["halfLifeConverted"]
                                        d_half_life = each_i["dHalfLifeConverted"]

                                        decay_width = BaseENSDF.convert_width_or_halflife(self,half_life)
                                        d_decay_width = BaseENSDF.convert_width_or_halflife(self,d_half_life)
                                        unit_decay_width = "MeV"
                                    
                                level_scheme.append([level_index, level_energy, d_level_energy, decay_width, d_decay_width, unit_decay_width, CONVERTED_WIDTH])
                                
                        width_dict.update({pd_pair_tuple: level_scheme})

                if DAUGHTER_EXISTS == True:
                    return width_dict
                else:
                    return                
