import numpy as np
import pandas as pd
import json
import glob

import warnings
warnings.simplefilter('error', RuntimeWarning)

class BaseENSDF(object):
    __doc__="""Base class to handle ENSDF and coincidence-decay data sets."""

    def __init__(self,contents=None):
        self.contents = [] or None

    def load_ensdf(self):
        """Function to assign all 3226 JSON-formatted ENSDF-decay data sets 
        (alpha, beta-minus, electron-capture/beta-plus) to a list object 
        variable.
        
        Arguments:
            No arguments are passed to this function.
        
        Returns:
            A list object containing all 3226 JSON-formatted ENSDF-decay data 
            sets.

        Example:
            
            import paceENSDF as pe
            e = pe.ENSDF()
            edata = e.load_ensdf()
        """
        print("Loading ENSDF data sets, please wait...")
        from . import get_data
        ENSDF_JSON_PATH = get_data('ENSDF_JSON')
        json_ensdf_list = [j for j in glob.glob("%s/*.json"%ENSDF_JSON_PATH)]
        json_ensdf_data = []

        JSON_COUNT = 0
        for json_file in json_ensdf_list:
            JSON_COUNT += 1
            with open(json_file, mode='r') as jf:
                json_ensdf_dict = json.loads(jf.read())
                json_ensdf_data.append(json_ensdf_dict)
            jf.close()

        print("{0} JSON-formatted ENSDF-decay data sets loaded.".format(JSON_COUNT))
        return json_ensdf_data

    def load_pace(self):
        """Function to assign all JSON-formatted coincidence-decay data sets 
        (gamma/gamma and gamma/X-ray) to a list object variable.
        
        Arguments:
            No arguments are passed to this function.
        
        Returns:
            A list object containing all JSON-formatted coincidence-decay data 
            sets.

        Example:
            
            import paceENSDF as pe
            c = pe.ENSDF()
            cdata = c.load_pace()
        """
        print("Loading coincidence data sets, please wait...")
        from . import get_data
        PACE_JSON_PATH = get_data('PACE_JSON')
        json_gg_list = [j for j in glob.glob("%s/j_gg_*.json"%PACE_JSON_PATH)]
        json_gx_list = [j for j in glob.glob("%s/j_gx_*.json"%PACE_JSON_PATH)]
        #json_pg_list = [j for j in glob.glob("%s/j_pg_*.json"%PACE_JSON_PATH)]
                           
        json_coinc_data = []

        JSON_GG_COUNT = 0
        for json_file in json_gg_list:
            JSON_GG_COUNT += 1
            with open(json_file, mode='r') as jf:
                json_gg_dict = json.loads(jf.read())
                json_coinc_data.append(json_gg_dict)
            jf.close()

        JSON_GX_COUNT = 0
        for json_file in json_gx_list:
            JSON_GX_COUNT += 1
            with open(json_file, mode='r') as jf:
                json_gx_dict = json.loads(jf.read())
                json_coinc_data.append(json_gx_dict)
            jf.close()

        #JSON_PG_COUNT = 0
        #for json_file in json_pg_list:
        #    JSON_PG_COUNT += 1
        #    with open(json_file, mode='r') as jf:
        #        json_pg_dict = json.loads(jf.read())
        #        json_coinc_data.append(json_pg_dict)
        #    jf.close()               

        print("{0} JSON-formatted gamma/gamma coincidence-decay data sets loaded.".format(JSON_GG_COUNT))
        print("{0} JSON-formatted gamma/X-ray coincidence-decay data sets loaded.".format(JSON_GX_COUNT))
        #print("{0} JSON-formatted particle/gamma coincidence-decay data sets loaded.".format(JSON_PG_COUNT))
        return json_coinc_data
    
    def sort_by_json_key(list,str='parentID'):
        """Internal function: Sorts list by parent ID (alphabetical)."""
        return list['%s'%str]

    def sort_by_level_decay(list,str='levelEnergyParentDecay'):
        """Internal function: Sorts list by parent decay-level energy."""
        return list['%s'%str]

    def decay_datasets(self,list):
        """Parent IDs for all decay datasets.

        Arguments:
            list: A list of ENSDF-decay data JSON objects

        Returns: 
            A list of parent IDs for all decay datasets.  Each parent ID is a 
            string object.

        Example:
            decay_datasets(edata) 
        """
        self.list = list
        decay_parents = sorted(self.list, key=BaseENSDF.sort_by_json_key)
        list_of_parents = []
        for jdict in decay_parents:
            list_of_parents.append(jdict['parentID'])
        return list_of_parents

    def sorted_datasets(self,list,str):
        """Function to return list of sorted JSON dictionaries.

        Arguments:
            list: A list of ENSDF-decay data or coincidence-decay data JSON 
                  objects.
            str: A string argument according to decay-data preference:
                 "ENSDF": ENSDF-decay data;
                 "COINC": Coincidence-decay data.

        Returns: 
            A list of JSON dictionaries sorted by: (i) first, alphabetical 
            parent ID; (ii) second, parent decay-level energy.

        Examples:
            Assign sorted ENSDF-decay data to list variable using instance of
            the ENSDF class - see example using load_ensdf() method:

            edata_s = e.sorted_datasets(edata,"ensdf")

            Assign sorted coincidence-decay data to list variable using 
            instance of the ENSDF class - see example using load_pace() method:
        
            cdata_s = c.sorted_datasets(cdata,"coinc")
        """
        self.list = list
        self.str = str
        if str.lower() == 'ensdf':
            sorted_decay_data = sorted(self.list, key=lambda x: (x['parentID'], x['levelEnergyParentDecay']))
        elif str.lower() == 'coinc':
            #sorted_decay_data = sorted(self.list, key=lambda x: (x['parentID'], x['parentDecayLevelEnergy']))
            sorted_decay_data = sorted(self.list, key=lambda x: (x['parentID']))
        else:
            print("Wrong argument: Only 'ensdf' or 'coinc' are acceptable.")
            return
        return sorted_decay_data

    def check_time_units(str):
        """Internal function: Checks validity of halflife units.  Only 'best' 
        or 'seconds' are permitted agruments.

        Arguments:
            str: A string object corresponding to the desired halflife units.

        Returns:
            A string object if the required halflife units are valid.
        """
        if (str.lower() == 'best') or (str.lower() == 'seconds') or (str.lower() == 's'):
            return str
        else:
            print("Inavlid units for halflife.  The only arguements accepted are:")
            print("units='best'")
            print("units='seconds'")
            print("units='s'")
            return

    def check_decay(str):
        """Internal function: Checks to ensure validity of decay mode.

        Arguments:
            str: A string object corresponding to the appropriate decay mode.
                 Only the following arguments are valid:

                 'BM': Beta-minus decay
                 'ECBP': Electron-capture/beta-plus decay
                 'A': Alpha decay
                 'DBM': Double beta-minus decay        

        Returns:
            A string object if the decay mode is valid.
        """
        DECAY_MODE_INVALID = False
        decay_mode = None
        if str.upper() == "BM":
            decay_mode = "betaMinusDecay"
        elif str.upper() == "ECBP":
            decay_mode = "electronCaptureBetaPlusDecay"
        elif str.upper() == "A":
            decay_mode = "alphaDecay"
        elif str.upper() == "DBM":
            decay_mode = "doubleBetaMinusDecay"
        else:
            DECAY_MODE_INVALID = True
            pass

        if DECAY_MODE_INVALID == True:
            return None
        else:
            return decay_mode

    # This function isn't really needed - may remove?
    def decay_modes(self,list,**kwargs):
        """Decay-mode information and associated decay-scheme meta data.

        Arguments:
            list: A list of ENSDF-decay data JSON objects.
            kwargs: A keyword argument is needed for the appropriate 
                    radioactive-decay mode:

                    mode='A'    : Alpha decay
                    mode='BM'   : Beta-minus decay
                    mode='DBM'   : Double beta-minus decay
                    mode='ECBP' : Electron-capture/beta-plus decay
                    
                    Only the above keyword arguments (case insensitive) are 
                    acceptable.  

        Returns:
            A dictionary object with a key containing the parent information 
            in a tuple:

            [0]: Parent ID (str);
            [1]: Parent atomic (Z) number (int);
            [2]: Parent mass (A) number (int);
            [3]: Decay-level index of parent nucleus (int);
            [4]: Decay-level energy of parent nucleus (float/str);

            The corresponding dictionary value is a tuple containing the 
            associated daughter information:
        
            [0]: Daughter ID (str);
            [1]: Daughter atomic (Z) number (int);
            [2]: Daughter mass (A) number (int);
            [3]: Total number of levels in daughter decay scheme (int);
            [4]: Total number of gammas in daughter decay scheme (int);
            [5]: Total number of particle decays to levels in daughter (int).

        Examples:
            All alpha decay modes:

            decay_modes(edata,"A") 

            All beta-minus decay modes:

            decay_modes(edata,"BM") 

            All double-beta-minus decay modes:

            decay_modes(edata,"DBM") 

            All electron-capture/beta-plus decay modes:

            decay_modes(edata,"ECBP") 
        """
        self.list = list
        DECAY_MODE_INVALID = False
        decay_mode = None
        for mode in kwargs.values():
            if mode.upper() == "BM":
                decay_mode = "betaMinusDecay"
            elif mode.upper() == "ECBP":
                decay_mode = "electronCaptureBetaPlusDecay"
            elif mode.upper() == "A":
                decay_mode = "alphaDecay"
            elif mode.upper() == "DBM":
                decay_mode = "doubleBetaMinusDecay"
            else:
                DECAY_MODE_INVALID = True
                pass

        #decay_list = []
        decay_dict = {}
        for jdict in self.list:
            if decay_mode == jdict["decayMode"]:
                try:
                    decay_dict.update({(jdict['parentID'], jdict['parentAtomicNumber'], jdict['parentAtomicMass'], jdict['decayIndex'], float(jdict['levelEnergyParentDecay'])): (jdict['daughterID'], jdict['daughterAtomicNumber'], jdict['daughterAtomicMass'], jdict['totalNumberLevels'], jdict['totalNumberGammas'], jdict['totalNumberParticleDecays'])})
                except ValueError:
                    decay_dict.update({(jdict['parentID'], jdict['parentAtomicNumber'], jdict['parentAtomicMass'], jdict['decayIndex'], str(jdict['levelEnergyParentDecay'])): (jdict['daughterID'], jdict['daughterAtomicNumber'], jdict['daughterAtomicMass'], jdict['totalNumberLevels'], jdict['totalNumberGammas'], jdict['totalNumberParticleDecays'])})
        if DECAY_MODE_INVALID == False:
            print("{0} {1} data sets".format(len(decay_dict), decay_mode))
        if DECAY_MODE_INVALID == True:
            print("Invalid decay mode.")
            return None
        else:
            return decay_dict
    

    def ensdf_pairs(self,list,str):
        """Parent-daughter information from ENSDF-decay data sets for a 
        specified decay mode (alpha, beta-minus, or electron-capture/beta-plus 
        decay).

        Notes:
            Median-symmetrized values are adopted for the halflife whereupon
            asymmetric quantities are encountered in the source ENSDF data set.

        Arguments:
            list: A list of ENSDF-decay data JSON objects.
            str: A string object is needed for the appropriate radioactive-decay
                 mode:

                 mode='A'    : Alpha decay
                 mode='BM'   : Beta-minus decay
                 mode='ECBP' : Electron-capture/beta-plus decay
                    
                 Only the above arguments (case insensitive) are acceptable.  

        Returns:
            A dictionary object ordered by parent atomic number and mass.  The 
            returned key contains the parent information in a tuple:

            [0]: Parent ID (str);
            [1]: Parent atomic (Z) number (int);
            [2]: Parent mass (A) number (int);
            [3]: Decay-level index of parent nucleus (int);
            [4]: Decay-level energy of parent nucleus (float/str);
            [5]: Halflife in "best" units (float);
            [6]: Halflife unit (str);
            [7]: Q-value of decay in keV (float). 
        
            The corresponding dictionary value is a tuple containing the 
            associated daughter information:
        
            [0]: Daughter ID (str);
            [1]: Daughter atomic (Z) number (int);
            [2]: Daughter mass (A) number (int);
            [3]: Total number of levels in daughter decay scheme (int);
            [4]: Total number of gammas in daughter decay scheme (int);
            [5]: Total number of particle decays to levels in daughter (int).

        Examples:
            All alpha-decay parent-daughter pairs:

            ensdf_pairs(edata,"A") 

            All beta-minus decay parent-daughter pairs:

            ensdf_pairs(edata,"BM") 

            All electron-capture/beta-plus decay parent-daughter pairs:

            ensdf_pairs(edata,"ECBP") 
        """
        self.list = list
        self.str = str
        decay_mode = BaseENSDF.check_decay(self.str)
        if decay_mode == None:
            print("Invalid decay mode.")
        else:
            print(decay_mode)

            decay_pair_dict = {}
            for jdict in self.list:
                if decay_mode == jdict["decayMode"]:
                    pid = jdict["parentID"]
                    decay_index = jdict["decayIndex"]
                    pZ = jdict["parentAtomicNumber"]
                    pA = jdict["parentAtomicMass"]
                    did = jdict["daughterID"]
                    dZ = jdict["daughterAtomicNumber"]
                    dA = jdict["daughterAtomicMass"]
                    
                    decay_energy = None
                    halflife, unit_halflife = None, None
                    qvalue = None
                    for each_p in jdict["parentDecay"]:
                        decay_energy = each_p["parentDecayLevelEnergy"]
                        qvalue = each_p["valueQ"]
                        for each_t in each_p["halfLife"]:
                            halflife = each_t["halfLifeBest"]
                            unit_halflife = each_t["unitHalfLifeBest"]

                    # Meta data
                    tot_num_levels = jdict['totalNumberLevels']
                    tot_num_gammas = jdict['totalNumberGammas']
                    tot_num_particles = jdict['totalNumberParticleDecays']

                    decay_pair_dict.update({(pid,pZ,pA,decay_index,decay_energy,halflife,unit_halflife,qvalue):(did,dZ,dA,tot_num_levels,tot_num_gammas,tot_num_particles)})
            #return decay_pair_dict
            return dict(sorted(decay_pair_dict.items(), key = lambda x: (x[0][1], x[0][2])))
                

    def coinc_pairs(self,list, str):
        """Parent-daughter information from coincidence-decay data sets for a 
        specified decay mode (alpha, beta-minus, or electron-capture/beta-plus 
        decay).

        Notes:
            Median-symmetrized values are adopted for the halflife whereupon
            asymmetric quantities are encountered in the source ENSDF data set.

        Arguments:
            list: A list of coincidence-decay data JSON objects.
            str: A string object is needed for the appropriate radioactive-decay
                 mode:

                 mode='A'    : Alpha decay
                 mode='BM'   : Beta-minus decay
                 mode='ECBP' : Electron-capture/beta-plus decay
                    
                 Only the above arguments (case insensitive) are acceptable.  

        Returns:
            A dictionary object ordered by parent atomic number and mass.  The 
            returned key contains the parent information in a tuple:

            [0]: Parent ID (str);
            [1]: Parent atomic (Z) number (int);
            [2]: Parent mass (A) number (int);
            [3]: Decay-level index of parent nucleus (int);
            [4]: Decay-level energy of parent nucleus (float/str);
            [5]: Halflife in "best" units (float);
            [6]: Halflife unit (str);
            [7]: Q-value of decay in keV (float). 
        
            The corresponding dictionary value is a tuple containing the 
            associated daughter information:
        
            [0]: Daughter ID (str);
            [1]: Daughter atomic (Z) number (int);
            [2]: Daughter mass (A) number (int);
            [3]: Total number of levels in daughter decay scheme (int);
            [4]: Total number of gammas in daughter decay scheme (int);
            [5]: Total number of gamma/gamma coincidences in daughter (int).

        Examples:
            All alpha-decay parent-daughter pairs with coincident-gamma data:

            coinc_pairs(cdata,"A") 

            All beta-minus decay parent-daughter pairs with coincident-gamma 
            data:

            coinc_pairs(cdata,"BM") 

            All electron-capture/beta-plus decay parent-daughter pairs with 
            coincident-gamma data:

            coinc_pairs(cdata,"ECBP") 
        """        
        self.list = list
        self.str = str
        decay_mode = BaseENSDF.check_decay(self.str)
        if decay_mode == None:
            print("Invalid decay mode.")
        else:
            print(decay_mode)

            decay_pair_dict = {}
            for jdict in self.list:
                if decay_mode == jdict["decayMode"] and jdict["datasetID"] == "GG":
                    pid = jdict["parentID"]
                    decay_index = jdict["decayIndex"]
                    pZ = jdict["parentZ"]
                    pA = jdict["parentA"]
                    decay_energy = jdict["parentDecayLevelEnergy"]
                    qvalue = jdict["Qvalue"]

                    did = jdict["daughterID"]
                    dZ = jdict["daughterZ"]
                    dA = jdict["daughterA"]
                    nlevels = jdict["totalNumberLevels"]
                    ngammas = jdict["totalNumberGammas"]
                    ncoincs = jdict["totalNumberGammaCoincidences"]

                    halflife, unit_halflife = None, None
                    for each_t in jdict["halfLife"]:
                        halflife = each_t["halfLifeBest"]
                        unit_halflife = each_t["unitHalfLifeBest"]

                    decay_pair_dict.update({(pid,pZ,pA,decay_index,decay_energy,halflife,unit_halflife,qvalue):(did,dZ,dA,nlevels,ngammas,ncoincs)})
            #return decay_pair_dict
            return dict(sorted(decay_pair_dict.items(), key=lambda x: (x[0][1], x[0][2]) ))
        

    def quad_error(self,f,x,dx,y,dy):
        """Internal function: Combines errors in quadrature for calculations 
        of the type:

        f = x*y
        f = x/y

        Arguments:
            f: Result.
            x: First variable.
            dx: First variable uncertainty.
            x: Second variable.
            dx: Second variable uncertainty.
            
        Returns:
            Associated uncertainty.
        """
        self.f = f
        self.x, self.dx = x, dx
        self.y, self.dy = y, dy
        try:
            return float(self.f)*np.sqrt((float(self.dx)/float(self.x))**2+(float(self.dy)/float(self.y))**2)
        except TypeError:
            if self.f == None:
                return 0
            elif self.x == None and self.y == None:
                return 0
            elif self.x == None and float(self.y) > 0.0:
                return float(self.f)*float(self.dy)/float(self.y)
            elif float(self.x) > 0.0 and self.y == None:
                return float(self.f)*float(self.dx)/float(self.x)
        except ZeroDivisionError:
            if self.x != None and float(self.x) > 0:
                return float(self.f)*float(self.dx)/float(self.x)
            elif self.y != None and float(self.y) > 0:
                return float(self.f)*float(dy)/float(self.y)
            else:
                return 0

    def convert_width_or_halflife(self,W):
        """Internal function: Converts ENSDF-reported decay widths to halflife 
        values or vice versa.  This function assumes the decay widths in units 
        of [MeV] and returns a halflife in units of [s], or returns a decay 
        width in units of [MeV] assuming a halflife in units of [s].

        Notes:
            Primarily designated as an internal function to handle the 
            conversion between widths and halflives.  If called from the 
            interpretor or used in another program the decay widths and 
            halflives must be given in units of [MeV] and [s], respectively.

        Arguments:
            W: decay width value in units of [MeV], or halflife value in units 
               of [s].  When used internally the appropriate quantity is taken 
               from the corresponding JSON data structure.

        Returns:
            A float variable corresponding to the halflife in units of [s] or 
            the decay width in units of [MeV].

        Example:
            Assuming a width W = 3 keV, the halflife is calculated by passing 
            this width value as 0.003 MeV:
            
            convert_width_or_halflife(0.003)

            Assuming a halflife T1/2 = 1 h, the width is calculated by passing 
            this halflife value as 3600 s:
        
            convert_width_or_halflife(3600)
        """
        self.W = W
        
        #hbar_eV_s = 6.58217E-16 # eV.s
        #hbar_keV_s = 6.58217E-19 # keV.s
        hbar_MeV_s = 6.58217E-22 # MeV.s
        ln2 = np.log(2)

        # The method below still gives warning during the test phase even 
        # though the warning is already handled. 
        #try:
        #    halflife = hbar_MeV_s * ln2 / self.W
        #    return float(halflife)
        #except RuntimeWarning:
            # Return value as zero to handle division by zero scalar error
        #    return 0.0

        #To avoid test-run warnings, the following script will be used instead
        if self.W > 0:
            halflife = hbar_MeV_s * ln2 / self.W
            return float(halflife)
        else:
            return 0.0

