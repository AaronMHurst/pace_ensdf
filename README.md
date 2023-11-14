# paceENSDF: Python Archive of Coincident Emissions from ENSDF

This project [[1]](#1) is a Python package enabling access, manipulation, analysis and visualization of the radioactive-decay data from the Evaluated Nuclear Structure Data File (ENSDF) library [[2]](#2).  A total of 3254 data sets encompassing &alpha; (834), &beta;<sup>-</sup> (1141), and &epsilon;/&beta;<sup>+</sup> (1279) have been extracted from the ENSDF archive [[2]](#2), parsed and translated into a representative JavaScript Object Notation (JSON) format (descibed below).  The JSON-formatted data sets constitute a total of 92,264 deexcitation &gamma; rays associated with 41,094 levels.  Additionally, we also provide a Reference Input Parameter Library [[3]](#3) RIPL-translated format of the corresponding decay-scheme data.  These data sets are bundled together with the analysis toolkit.  A schematic illustrating the portion of the nuclear chart of relevance to the aforementioned decay data from ENSDF is shown in the figure below.

![ENSDF Nuclides](decay_nuclides.png?raw=true "Schematic showing portion of nuclear chart of relevance to the ENSDF-decay data sets")

The `paceENSDF` package provides users with a convenient means to access and manipulate the decay data from ENSDF [[2]](#2) with various methods to return all associated nuclear structure decay-scheme data including levels, spins, parities, &gamma;-rays information, etc.  The `Jupyter Notebooks` distributed with this package in the `notebook` folder provide an overview of some of the available methods.

All ENSDF decay-scheme data sets containing &gamma;-ray information have also been used to generate coincidence &gamma;-&gamma; and &gamma;-*X*-ray JSON data structures from the corresponding decay data set [[1]](#1).  In addition to the coincidence energies and absolute intensities, together with uncertainties, these data structures contain additional meta data parsed from the original ENSDF data structure allowing users to search for single energies (both &gamma; and *X*-ray) as well as coincidence pairs.  Refer to the corresponding `Jupyter Notebooks` provided with this project to see example use cases.

### Notes on ENSDF quantities

Although most quantities in ENSDF are normally-distributed symmetrical quantities associated with the equality `=` operator, the following exceptions (frequent in many cases) are also accounted for:

* All asymmetric quantities parsed in the original ENSDF dataset are symmetrized and their associated median-symmertized values and uncertainties are reported in the derived JSON data structures.
* All approximate `AP` values parsed in the original ENSDF dataset are reported with an assumed 50% uncertainty.
* All values parsed as limits (i.e., `LT`, `GT`, `GE`, `GE`) in the original ENSDF dataset are reported with an assumed 100% uncertainty.

# Building and installation

This project should be built and installed by executing the `installation.sh` script at the terminal command line of the project directory:

```Bash
$ git clone https://github.com/AaronMHurst/pace_ensdf.git
$ cd pace_ensdf
$ sh installation.sh
```

# Testing

A suite of Python modules containing 283 unit tests have been written for this project and are located in the `tests` folder.  To run the test suite and ensure they work with the Python environment, run `tox` in the project directory where the `tox.ini` file is also located:

```Bash
$ tox -r
```

This project has the following Python-package dependencies: `numpy`, `pandas`, and `pytest`.  The test session is automatically started after building against the required Python environment.

# Running the software

After the installation the `paceENSDF` scripts can be ran from any location by importing the package and making an instance of the `ENSDF` class:

```Bash
$ python
```
```python
>>> import paceENSDF as pe
>>> e = pe.ENSDF()
```

Most methods also require passing the `JSON`-formatted source data set as a list object.  To use the ENSDF decay-data sets:

```python
>>> edata = e.load_ensdf()
```

A `Jupyter Notebook` is provided illustrating use of the various methods for access and manipulation of the ENSDF data.  To run the notebook from the terminal command line:

```Bash
$ cd notebook
$ jupyter notebook decay_paceENSDF.ipynb
```

Alternatively, To use the coincidence &gamma;-&gamma; and &gamma;-*X*-ray data sets:

```python
>>> cdata = e.load_pace()
```

Again, a `Jupyter Notebook` is also provided illustrating use of the various methods for access and manipulation of the coincidence data:

```Bash
$ cd notebook
$ jupyter notebook coinc_paceENSDF.ipynb
```

Inline plotting methods are supported in the notebooks using the `matplotlib` Python package.

# Docstrings

All `paceENSDF` classes and functions have supporting docstrings.  Please refer to the individual dosctrings for more information on any particular function including how to use it.  The dosctrings for each method generally have the following structure:

* A short explanation of the function.
* A list and description of arguments that need to be passed to the function.
* The return value of the function.
* An example(s) invoking use of the function.

To retrieve a list of all available methods simply execute the following command in a Python interpreter:

```python
>>> help(e)
```

Or, to retrieve the docstring for a particular method, e.g., the callable `get_gg`:

```python
>>> help(e.get_gg)
```

## RIPL format

Because many nuclear reaction codes source decay-scheme information in a particular Reference Input Parameter Library (RIPL) [[3]](#3) format, representative RIPL-translated data sets have also been generated for each corresponding ENSDF-decay data set and these files are also bundled with the software.  The RIPL-formatted ENSDF-decay data sets are located in their respective `pace_ensdf/paceENSDF/ENSDF_RIPL/<decay_mode>` directories, where `<decay_mode>` corresponds to `alpha`, `beta_minus`, `beta_plus`, or `ecbp`.


## JSON format

All original ENSDF radioactive-decay data sets have been translated into a representative JavaScript Object Notation (JSON) format using an intuitive syntax to describe the quantities sourced from the primary and continuation records of the ENSDF-formatted data sets [[2]](#2).  The corresponding JSON-formatted radioative-decay data sets are bundled with this software package together with JSON-formatted coincidence $\gamma-\gamma$ and $\gamma-X$-ray data sets derived from the respective decay information in the original ENSDF library.  These JSON data structures are located in project folders:
```Bash
pace_ensdf/paceENSDF/ENSDF_JSON
```
for the radioactive-decay data sets, and
```Bash
pace_ensdf/paceENSDF/COINC_JSON
```
for the coincidence data sets.

The JSON data structures support the following data types:

* *string*
* *number*
* *boolean*
* *null*
* *object* (JSON object)
* *array*

The JSON-formatted schemas for (1) the interpretted [ENSDF decay](https://github.com/AaronMHurst/pace_ensdf#1-json-formatted-ensdf-decay-schema) datasets, and (2) the derived coincidence [&gamma;-&gamma;](https://github.com/AaronMHurst/pace_ensdf#2-json-formatted-coincidence-%CE%B3-%CE%B3-schema) and (3) [&gamma;-*X*-ray](https://github.com/AaronMHurst/pace_ensdf#3-json-formatted-coincidence-%CE%B3-x-ray-schema) datasets are described below.

## (1) JSON-formatted ENSDF-decay schema

| JSON key | Explanation |
| --- | --- |
| `"parentAtomicNumber"` | A number type denoting the atomic number of the parent nucleus.|
| `"parentAtomicMass"` | A number type denoting the mass number of the parent nucleus.|
| `"parentNeutronNumber"` | A number type denoting the neutron number of the parent nucleus.|
| `"daughterAtomicNumber"` | A number type denoting the atomic number of the daughter nucleus.|
| `"daughterAtomicMass"` | A number type denoting the mass number of the daughter nucleus.|
| `"daughterNeutronNumber"` | A number type denoting the neutron number of the daughter nucleus.|
| `"levelEnergyParentDecay"` | Usually a number type (float or integer) representing the decay-level energy of the parent.  String types are also acceptable, e.g., 'X', to indicate an unknown or imprecise value.  Values greater than zero are isomer decays.|
| `"parentID"` | A string type identification value of the parent nucleus `<symbol><mass>`.|
| `"daughterID"` | A string type identification value of the daughter nucleus `<symbol><mass>`.|
| `"decayMode"` | A string type representation of the decay mode: `"alphaDecay"`, `"betaMinusDecay"`, and `"electronCaptureBetaPusDecay"` values are acceptable.|
| `"totalNumberLevels"` | A number type value (integer) denoting the total number of levels observed in the daughter nucleus.|
| `"totalNumberGammas"` | A number type value (integer) denoting the total number of gammas observed in the daughter nucleus.|
| `"totalNumberParticleDecays` | A number type value (integer) denoting the number of particle decays observed to levels the daughter nucleus.|
| `"decaySchemeNormalization"` | An array type containing the two normalization arrays from ENSDF.|
| `"parentDecay"` | An array type containing several JSON objects related to the decay properties of the parent nucleus.|
| `"levelScheme"` | An array type containing several JSON objects related to the level scheme properties of the daughter nucleus populated following radioactive decay.|
| `"decayIndex"` | A number type value (integer) to indicate whether the parent nucleus decays from its ground state (0) or from an isomeric level (>0).|

The JSON arrays are described below:

### 1.1 `"decaySchemeNormalization"` array

| JSON key | Explanation |
| --- | --- |
| `"normalizationRecord"` | An array type containing all the information from the ENSDF primary *Normalization Record*.|
| `"productionNormalizationRecord"` | An array type containing all the information from the ENSDF primary *Production Normalization Record*.|

##### 1.1.1 `"normalizationRecord"` array
| JSON key | Explanation |
| --- | --- |
| `"recordExists"`| A boolean type to indicate whether the *Normalization Record* is present in the original ENSDF document.|
| `"multiplerPhotonIntensity"`| A number type representing the photon-intensity multiplier.|
| `"dMultiplerPhotonIntensity"`| A number type representing the associated uncertainty of the photon-intensity multiplier.|
| `"recordExistsNR"`| A boolean type to indicate whether the photon-intensity multiplier is parsed from the original ENSDF document.|
| `"multiplerTransitionIntensity"`| A number type representing the transition-intensity multiplier.|
| `"dMultiplerTransitionIntensity"`| A number type representing the associated uncertainty of the transition-intensity multiplier.|
| `"recordExistsNT"`| A boolean type to indicate whether the transition-intensity multiplier is parsed from the original ENSDF document.|
| `"multiplerBranchingRatio"`| A number type representing the branching-ratio multiplier.|
| `"dMultiplerBranchingRatio"`| A number type representing the associated uncertainty of the branching-ratio multiplier.|
| `"recordExistsBR"`| A boolean type to indicate whether the branching-ratio multiplier is parsed from the original ENSDF document.|
| `"multiplerLeptonIntensity"`| A number type representing the lepton-intensity multiplier.|
| `"dMultiplerLeptonIntensity"`| A number type representing the associated uncertainty of the lepton-intensity multiplier.|
| `"recordExistsNB"`| A boolean type to indicate whether the lepton-intensity multiplier is parsed from the original ENSDF document.|
| `"multiplierDelayedParticleIntensity"`| A number type representing the delayed-particle intensity multiplier.|
| `"dMultiplierDelayedParticleIntensity"`| A number type representing the associated uncertainty of the delayed-particle intensity multiplier.|
| `"recordExistsNP"`| A boolean type to indicate whether the delayed-particle intensity multiplier is parsed from the original ENSDF document.|

#### 1.1.2 `"productionNormalizationRecord"` array
| JSON key | Explanation |
| --- | --- |
| `"recordExists"`| A boolean type to indicate whether the *Production Normalization Record* is present in the original ENSDF document.|
| `"multiplierPhotonIntensityBranchingRatioCorrected"`| A number type representing the branching-ratio corrected photon-intensity multiplier.|
| `"dMultiplierPhotonIntensityBranchingRatioCorrected"`| A number type representing the associated uncertainty of the branching-ratio corrected photon-intensity multiplier.|
| `"recordExistsPNR"`| A boolean type to indicate whether the branching-ratio corrected photon-intensity multiplier is parsed from the original ENSDF document.|
| `"multiplierTransitionIntensityBranchingRatioCorrected"`| A number type representing the branching-ratio corrected transition-intensity multiplier.|
| `"dMultiplierTransitionIntensityBranchingRatioCorrected"`| A number type representing the associated uncertainty of the branching-ratio corrected transition-intensity multiplier.|
| `"recordExistsPNT"`| A boolean type to indicate whether the branching-ratio corrected transition-intensity multiplier is parsed from the original ENSDF document.|
| `"multiplierLeptonIntensityBranchingRatioCorrected"`| A number type representing the branching-ratio corrected lepton-intensity multiplier.|
| `"dMultiplierLeptonIntensityBranchingRatioCorrected"`| A number type representing the associated uncertainty of the branching-ratio corrected lepton-intensity multiplier.|
| `"recordExistsPNB"`| A boolean type to indicate whether the branching-ratio corrected lepton-intensity multiplier is parsed from the original ENSDF document.|
| `"multiplierDelayedParticleIntensity"`| A number type representing the delayed-particle intensity multiplier.  This quantity should be identical to that given in the corresponding `normalizationRecord`.|
| `"dMultiplierDelayedParticleIntensity"`| A number type representing the associated uncertainty of the delayed-particle intensity multiplier.  This quantity should be identical to that given in the corresponding `normalizationRecord`.|
| `"recordExistsPNP"`| A boolean type to indicate whether the delayed-particle intensity multiplier is parsed from the original ENSDF document.  This quantity should be identical to that given in the corresponding `normalizationRecord`.|

### 1.2 `"parentDecay"` array
| JSON key | Explanation |
| --- | --- |
| `"parentIsIsomer"`| A boolean type to indicate isomeric decay.|
| `"parentDecayLevelEnergy"`| A number type<sup>*</sup> (float or integer) corresponding to the excitation energy associated with the decay of the parent.|
| `"dParentDecayLevelEnergy"`| A number type (float or integer) corresponding to the associated uncertainty of parent-decay excitation energy.|
| `"parentDecayLevelEnergyIsKnown"`| A boolean type<sup>**</sup> to indicate whether or not the parent-decay level energy is known.|
| `"parentDecayLevelEnergyThreshold"`| If `"parentDecayLevelEnergyIsKnown": true` the corresponding value is a `null` type.  Otherwise number or string type values are allowed.|
| `"parentDecayLevelEnergyOffset"`| If `"parentDecayLevelEnergyIsKnown": true` the corresponding value is a `null` type.  Otherwise number or string type values are allowed.|
| `"parentDecayLevelEnergyOffsetDirection"`| If `"parentDecayLevelEnergyIsKnown": true` the corresponding value is a `null` type.  Otherwise `"positive"` (e.g., in the case of `"parentDecayLevelEnergy": "0.0 + X"`) or `"negative"` values are acceptable to denote the offset direction.|
| `"valueQ"`| A number type (float or integer) corresponding to the ground-state *Q* value, i.e., the total energy available for the ground-state to ground-state transition.|
| `"dValueQ"`| A number type (float or integer) corresponding to the associated uncertainty of the ground-state *Q* value.|
| `"atomicIonizationState"`| If given it will be a signed number type (integer) describing the ionization state for ionized-atomic decay, otherwise it will be a `null` type.|
| `"halfLife"`| An array type containing the half-life information for the parent isotope or isomer.|
| `"decayWidth"`| An array type containing the decay-width information for the parent isotope or isomer.|
| `"numberOfSpins"`| A number type (integer) corresponding to the number of spin-parity permutations of the level.|
| `"spins"`| An array type corresponding to the spin-parity information associated with the level.|

<sup>*</sup> For real numerical data the value will be a number type (float or integer); level energies expressed as, e.g., `0.0 + X` or similar, will be represented as a string type.

<sup>**</sup> If `"parentDecayLevelEnergy" : <number>`: `"parentDecayLevelEnergyIsKnown" : true`, else if `"parentDecayLevelEnergy" : <string>`: `"parentDecayLevelEnergyIsKnown" : false`.

#### 1.2.1 `"halfLife"` array

| JSON key | Explanation |
| --- | --- |
| `"halfLifeBest"` | A number type representing the halflife in *best* units from original data set.|
| `"dHalfLifeBest"` | A number type representing the associated uncertainty on the halflife in *best* units. |
| `"unitHalfLifeBest"` | A string type to indicate the *best* halflife units.|
| `"halfLifeConverted"` | A number type representing the halflife *converted* to units of seconds.|
| `"dHalfLifeConverted"` | A number type representing the associated uncertainty on the halflife *converted* to seconds.|
| `"unitHalfLifeConverted"` | A string type to indicate the *converted* halflife units.|

#### 1.2.2 `"spins"` array

| JSON key | Explanation |
| --- | --- |
|  `"spinIndex"`| A number type (integer) associated with the indexed sequence of the spin-parity permutations.|
|  `"spinReal"`| A number type (float) corresponding to the real spin value of the level. |
|  `"spinIsTentative"` | A boolean type to flag tentative spin assignments. |
|  `"spinIsLimit"` | A boolean type to flag levels with spin values expressed as limits. |
|  `"spinLimits"` | A string type representing the associated spin limits of the level; a `null` value is given if the level does not have any spin limits. |
|  `"parity"` | A number type (integer) that represents the parity of the level: -1 (negative &pi;), 1 (positive &pi;), 0 (no &pi; assignment). |
|  `"paritySign"` | A string type referring to the parity (*"negative"*, *"positive"*, or *null*) of the level. |
|  `"parityIsTentative"` | A boolean type to flag tentative parity assignments. |

### 1.3 `"levelScheme"` array

| JSON key | Explanation |
| --- | --- |
| `"levelIndex"` | A number type (integer) corresponding to unique index associated with an energy level. |
| `"levelEnergy"` | A number type<sup>*</sup> (float) corresponding to the level excitation energy. |
| `"dLevelEnergy"` | A number type (float) corresponding to the uncertainty of the level excitation energy. |
| `"levelEnergyIsKnown"` | A boolean type<sup>**</sup> to indicate whether or not the level energy is known.|
| `"levelEnergyThreshold"` | If `"levelEnergyIsKnown": true` the corresponding value is a `null` type.  Otherwise number or string type values are allowed.|
| `"levelEnergyOffset"` | If `"levelEnergyIsKnown": true` the corresponding value is a `null` type.  Otherwise number or string type values are allowed.|
| `"levelEnergyOffsetDirection"` | If `"levelEnergyIsKnown": true` the corresponding value is a `null` type.  Otherwise `"positive"` (e.g., in the case of `"levelEnergy": "0.0 + X"`) or `"negative"` values are acceptable to denote the offset direction.|
| `"levelIsIsomer"` | A boolean type to flag levels with isomeric properties. |
| `"isomerDecay"` | An array type corresponding to the isomer-decay properties of the level. |
| `"decayWidth"` | An array type corresponding to the decay-width properties of the level. |
| `"numberOfSpins"` | A number type (integer) corresponding to the number of spin-parity permutations of the level. |
| `"spins"` | An array type corresponding to the spin-parity information associated with the level. |
| `"numberOfGammas"` | A number type (integer) corresponding to the number of deexcitation &gamma; rays belonging to the levels. |
| `"gammaDecay"` | An array type corresponding to the &gamma;-decay properties of the level. |
| `"alphaDecay"` | An array type containing JSON objects associated with the &alpha;-decay properties of the level.  *Only populated in &alpha;-decay datasets.* |
| `"betaMinusDecay"` | An array type containing JSON objects associated with the &beta;<sup>-</sup>-decay properties of the level.  *Only populated in &beta;<sup>-</sup>-decay datasets.* |
| `"betaPlusDecay"` | An array type containing JSON objects associated with the &epsilon;/&beta;<sup>+</sup>-decay properties of the level.  *Only populated in &epsilon;/&beta;<sup>+</sup>-decay datasets.* |

<sup>*</sup> For real numerical data the value will be a number type (float or integer); level energies expressed as, e.g., `0.0 + X` or similar, will be represented as a string type.

<sup>**</sup> If `"levelEnergy" : <number>`: `"levelEnergyIsKnown" : true`, else if `"levelEnergy" : <string>`: `"levelEnergyIsKnown" : false`.

#### 1.3.1 `"isomerDecay"` array

An empty array will be present in the JSON structure for key-value pairs given by `"levelIsIsomer": false`.  Levels with `true` values, however, contain the following information:

| JSON key | Explanation |
| --- | --- |
| `"halfLifeBest"` | A number type representing the halflife in *best* units taken from original data set.|
| `"dHalfLifeBest"` | A number type representing the associated uncertainty on the halflife in *best* units. |
| `"unitHalfLifeBest"` | A string type to indicate the *best* halflife units.|
| `"halfLifeConverted"` | A number type representing the halflife *converted* to units of seconds.|
| `"dHalfLifeConverted"` | A number type representing the associated uncertainty on the halflife *converted* to seconds.|
| `"unitHalfLifeConverted"` | A string type to indicate the *converted* halflife units.|


#### 1.3.2 `"decayWidth"` array

Generally, the JSON structures for each level contain an empty `"decayWidth"` array.  However, the decay width of the level can be calculated from the corresponding halflife (or vice-versa, whenever one or the other is known) upon invoking the callable method `convert_width_or_halflife` of the `BaseENSDF` class (see appropriate docstring).  Alternatively, in the few cases where decay widths have been parsed directly from the source ENSDF-decay dataset, the array has the following structure:

| JSON key | Explanation |
| --- | --- |
| `"decayWidthBest"` | A number type representing the decay width of the level in *best* units taken from original dataset.|
| `"dDecayWidthBest"` | A number type representing the associated uncertainty on the decay width in *best* units. |
| `"unitDecayWidthBest"` | A string type to indicate the *best* decay-width units.|
| `"decayWidthConverted"` | A number type representing the decay width *converted* to units of MeV.|
| `"dDecayWidthConverted"` | A number type representing the associated uncertainty on the decay width *converted* to MeV.|
| `"unitDecayWidthConverted"` | A string type to indicate the *converted* decay-width units.|

#### 1.3.3 `"spins"` array

The same JSON keys in the [`"spins"`](https://github.com/AaronMHurst/pace_ensdf#122-spins-array) array belonging to the `"parentDecay"` array are used to describe the `"spins"` array for each level.  These keys are again described explicitly as:

| JSON key | Explanation |
| --- | --- |
|  `"spinIndex"`| A number type (integer) associated with the indexed sequence of the spin-parity permutations.|
|  `"spinReal"`| A number type (float) corresponding to the real spin value of the level. |
|  `"spinIsTentative"` | A boolean type to flag tentative spin assignments. |
|  `"spinIsLimit"` | A boolean type to flag levels with spin values expressed as limits. |
|  `"spinLimits"` | A string type representing the associated spin limits of the level; a `null` value is given if the level does not have any spin limits. |
|  `"parity"` | A number type (integer) that represents the parity of the level: -1 (negative &pi;), 1 (positive &pi;), 0 (no &pi; assignment). |
|  `"paritySign"` | A string type referring to the parity (*"negative"*, *"positive"*, or *null*) of the level. |
|  `"parityIsTentative"` | A boolean type to flag tentative parity assignments. |


#### 1.3.4 `"gammaDecay"` array

The calculated internal-conversion coefficients in this array were determined using the Band-Raman internal-conversion coefficient calculator BrIcc [[4]](#4).

| JSON key | Explanation |
| --- | --- |
| `"gammaEnergy"` | A number type<sup>*</sup> (float) corresponding to the &gamma;-ray energy.|
| `"dGammaEnergy"` | A number type (float) corresponding to the associated uncertainty of the &gamma;-ray energy.|
| `"gammaEnergyIsKnown"` | A boolean type<sup>**</sup> to indicate whether or not the &gamma;-ray energy is known.|
| `"gammaEnergyThreshold"` | If `"gammaEnergyIsKnown": true` the corresponding value is a `null` type.  Otherwise number or string type values are allowed.|
| `"gammaEnergyOffset"` | If `"gammaEnergyIsKnown": true` the corresponding value is a `null` type.  Otherwise number or string type values are allowed.|
| `"gammaEnergyOffsetDirection"` | If `"gammaEnergyIsKnown": true` the corresponding value is a `null` type.  Otherwise `"positive"` (e.g., in the case of `"gammaEnergy": "0.0 + X"`) or `"negative"` values are acceptable to denote the offset direction.|
| `"levelIndexInitial"` | A number type (integer) corresponding to the index of the initial level associated with the &gamma;-ray transition.|
| `"levelIndexFinal"` | A number type (integer) corresponding to the index of the final level associated with the &gamma;-ray transition.|
| `"levelEnergyInitial"` | A number type (float) corresponding to the excitation energy of the initial level associated with the &gamma;-ray transition.|
| `"levelEnergyFinal"` | A number type (float) corresponding to the excitation energy of the final level associated with the &gamma;-ray transition.|
| `"gammaIntensity"` | A number type (float) corresponding to the *raw* &gamma;-ray intensity parsed from the ENSDF file, i.e., the &gamma;-ray intensity prior to any application of [normalization](https://github.com/AaronMHurst/pace_ensdf#11-decayschemenormalization-array) factors.|
| `"dGammaIntensity"` | A number type (float) corresponding to the associated uncertainty of the &gamma;-ray intensity.|
|  `"multipolarity"` | A string type (or *null*) describing the multipolarity (*"M1", "E1", "M2", "E2", "M1+E2",* etc.) of the &gamma;-ray transition.|
|  `"multipolarityIsTentative"`| A boolean type to flag tentative multipolarity assignments.|
|  `"multipolarityIsAssumed"`| A boolean type to indicate evaluator-assumed multipolarity assignments.|
|  `"mixingRatio"`| A number type (or *null*) corresponding to the &gamma;-ray mixing ratio where known.|
|  `"dMixingRatio"`| A number type (or *null*) corresponding to the associated uncertainty of the &gamma;-ray mixing ratio.|
|  `"mixingRatioSign"`| A string type (or *null*) corresponding to the sign (*"positive"* or *"negative"*) of the &gamma;-ray mixing ratio.
|  `"calculatedTotalInternalConversionCoefficient"`| A number type corresponding to the calculated total internal-conversion coefficient associated with the &gamma;-ray transition; deduced using BrIcc[[4]](#4).|
|  `"dCalculatedTotalInternalConversionCoefficient"`| A number type corresponding to the associated uncertainty of the calculated total internal-conversion coefficient; deduced using BrIcc[[4]](#4)|
|  `"calculatedAtomicShellConversionCoefficients"` | An array type containing the calculated atomic subshell internal-conversion coefficient data.|
| `"sumCalculatedAtomicShellConversionCoefficients"` | An array type containing the calculated summed atomic subshell internal-conversion coefficient data.|
| `"conversionElectronIntensityAtomicShellToTotalRatios"` | An array type containing the atomic subshell internal-conversion electron intensity to total ratios.|
| `"experimentalAtomicShellConversionCoefficients"` | An array type containing the experimental atomic subshell internal-conversion coefficient data.|
| `"atomicShellConversionElectronIntensities"` | An array type containing the atomic subshell internal-conversion electron intensities.|

<sup>*</sup> For real numerical data the value will be a number type (float or integer); &gamma;-ray energies expressed as, e.g., `0.0 + X` or similar, will be represented as a string type.

<sup>**</sup> If `"gammaEnergy" : <number>`: `"gammaEnergyIsKnown" : true`, else if `"gammaEnergy" : <string>`: `"gammaEnergyIsKnown" : false`.

##### 1.3.4.1 `"calculatedAtomicShellConversionCoefficients"` array

The calculated internal-conversion coefficient contributions from the individual atomic shells in this array were determined using the Band-Raman internal-conversion coefficient calculator BrIcc [[4]](#4).

| JSON key | Explanation |
| --- | --- |
|  `"calculatedInternalConversionCoefficientAtomicShellK"`| A number type (float) corresponding to the calculated *K*-shell internal-conversion coefficient.|
|  `"dCalculatedInternalConversionCoefficientAtomicShellK"`| A number type (float) corresponding to the associated uncertainty of the calculated *K*-shell internal-conversion coefficient.|
|  `"calculatedInternalConversionCoefficientAtomicShellL"`| A number type (float) corresponding to the calculated *L*-shell internal-conversion coefficient.|
|  `"dCalculatedInternalConversionCoefficientAtomicShellL"`| A number type (float) corresponding to the associated uncertainty of the calculated *L*-shell internal-conversion coefficient.|
|  `"calculatedInternalConversionCoefficientAtomicShellM"`| A number type (float) corresponding to the calculated *M*-shell internal-conversion coefficient.|
|  `"dCalculatedInternalConversionCoefficientAtomicShellM"`| A number type (float) corresponding to the associated uncertainty of the calculated *M*-shell internal-conversion coefficient.|
|  `"calculatedInternalConversionCoefficientAtomicShellN"`| A number type (float) corresponding to the calculated *N*-shell internal-conversion coefficient.|
|  `"dCalculatedInternalConversionCoefficientAtomicShellN"`| A number type (float) corresponding to the associated uncertainty of the calculated *N*-shell internal-conversion coefficient.|
|  `"calculatedInternalConversionCoefficientAtomicShellO"`| A number type (float) corresponding to the calculated *O*-shell internal-conversion coefficient.|
|  `"dCalculatedInternalConversionCoefficientAtomicShellO"`| A number type (float) corresponding to the associated uncertainty of the calculated *O*-shell internal-conversion coefficient.|
|  `"calculatedInternalConversionCoefficientAtomicShellP"`| A number type (float) corresponding to the calculated *P*-shell internal-conversion coefficient.|
|  `"dCalculatedInternalConversionCoefficientAtomicShellP"`| A number type (float) corresponding to the associated uncertainty of the calculated *P*-shell internal-conversion coefficient.|
|  `"calculatedInternalConversionCoefficientAtomicShellQ"`| A number type (float) corresponding to the calculated *Q*-shell internal-conversion coefficient.|
|  `"dCalculatedInternalConversionCoefficientAtomicShellQ"`| A number type (float) corresponding to the associated uncertainty of the calculated *Q*-shell internal-conversion coefficient.|


##### 1.3.4.2 `"sumCalculatedAtomicShellConversionCoefficients"` array

The calculated internal-conversion coefficient contributions in this array were determined using the Band-Raman internal-conversion coefficient calculator BrIcc [[4]](#4).

| JSON key | Explanation |
| --- | --- |
|  `"sumConversionCoefficientsAtomicShellPlusL"`| A number type (float) corresponding to the sum of calculated internal-conversion coefficients from *L*-shell contributions and higher (i.e., *L+*).|
|  `"dSumConversionCoefficientsAtomicShellPlusL"`| A number type (float) corresponding to the associated uncertainty of the sum of calculated internal-conversion coefficients from *L*-shell contributions and higher (i.e., *L+*).|
|  `"sumConversionCoefficientsAtomicShellPlusM"`| A number type (float) corresponding to the sum of calculated internal-conversion coefficients from *M*-shell contributions and higher (i.e., *M+*).|
|  `"dSumConversionCoefficientsAtomicShellPlusM"`| A number type (float) corresponding to the associated uncertainty of the sum of calculated internal-conversion coefficients from *M*-shell contributions and higher (i.e., *M+*).|
|  `"sumConversionCoefficientsAtomicShellPlusN"`| A number type (float) corresponding to the sum of calculated internal-conversion coefficients from *N*-shell contributions and higher (i.e., *N+*).|
|  `"dSumConversionCoefficientsAtomicShellPlusN"`| A number type (float) corresponding to the associated uncertainty of the sum of calculated internal-conversion coefficients from *N*-shell contributions and higher (i.e., *N+*).| 
|  `"sumConversionCoefficientsAtomicShellPlusO"`| A number type (float) corresponding to the sum of calculated internal-conversion coefficients from *O*-shell contributions and higher (i.e., *O+*).|
|  `"dSumConversionCoefficientsAtomicShellPlusO"`| A number type (float) corresponding to the associated uncertainty of the sum of calculated internal-conversion coefficients from *O*-shell contributions and higher (i.e., *O+*).| 
|  `"sumConversionCoefficientsAtomicShellPlusP"`| A number type (float) corresponding to the sum of calculated internal-conversion coefficients from *P*-shell contributions and higher (i.e., *P+*).|
|  `"dSumConversionCoefficientsAtomicShellPlusP"`| A number type (float) corresponding to the associated uncertainty of the sum of calculated internal-conversion coefficients from *P*-shell contributions and higher (i.e., *P+*).| 
|  `"sumConversionCoefficientsAtomicShellPlusQ"`| A number type (float) corresponding to the sum of calculated internal-conversion coefficients from *Q*-shell contributions and higher (i.e., *Q+*).|
|  `"dSumConversionCoefficientsAtomicShellPlusQ"`| A number type (float) corresponding to the associated uncertainty of the sum of calculated internal-conversion coefficients from *Q*-shell contributions and higher (i.e., *Q+*).| 

##### 1.3.4.3 `"conversionElectronIntensityAtomicShellToTotalRatios"` array

The quantities in this structure are the ratios of the atomic-subshell internal-conversion electron intensities to the total transition intensity, e.g., for the $K$ shell:

```math
R_{K} = \frac{\Gamma_{e_{K}} }{\Gamma_{\gamma} + \Gamma_{e}}, \quad\quad\quad (1)
```

where $\Gamma_{\gamma}$ is the $\gamma$-ray transition intensity, $\Gamma_{e}$ is the total conversion-electron transition intensity, and $\Gamma_{e_{K}}$ is the $K$-shell conversion-electron intensity.  However, because $\alpha = \Gamma_{e}/\Gamma_{\gamma}$, it follows that $\Gamma_{\text{tot}} = \Gamma_{\gamma} + \Gamma_{e} = \Gamma_{\gamma} (1+\alpha).$  Accordingly, the value of $\alpha_{K}$ can be deduced from the ratio $R_{K}$ and the total internal-conversion coefficient $\alpha$

```math
\frac{\Gamma_{e_{K}} }{\Gamma_{\gamma}(1+\alpha)} = \frac{\alpha_{K} \Gamma_{\gamma}}{\Gamma_{\gamma}(1+\alpha)}, \quad\quad\quad
```

```math
\alpha_{K} = \left[\frac{\Gamma_{e_{K}} }{\Gamma_{\gamma}(1+\alpha)}\right](1+\alpha). \quad\quad\quad (2)
```

Provided that both the ratio in Eq. (2) above along with  $\alpha$ are available we can also use this information to deduce $\alpha_{i}$ values where $i$ represents the $K, L, M,\dots$ atomic subshell.  In certain cases where this ratio is parsed from the source ENSDF dataset we have used this method deduce the corresponding $\alpha_{i}$ and populate the [`"calculatedAtomicShellConversionCoefficients"`](https://github.com/AaronMHurst/pace_ensdf#1341-calculatedatomicshellconversioncoefficients-array) array.


| JSON key | Explanation |
| --- | --- |
| `"conversionElectronIntensityRatioAtomicShellKtoTotal"` | A number type (float) corresponding to the $R_{K}$ ratio given by Eq. (1). |
| `"dConversionElectronIntensityRatioAtomicShellKtoTotal"` | A number type (float) corresponding to the associated uncertainty on the $R_{K}$ ratio. |
| `"conversionElectronIntensityRatioAtomicShellLtoTotal"` | A number type (float) corresponding to the $R_{L}$ ratio given by Eq. (1). |
| `"dConversionElectronIntensityRatioAtomicShellLtoTotal"` | A number type (float) corresponding to the associated uncertainty on the $R_{L}$ ratio. |
| `"conversionElectronIntensityRatioAtomicShellMtoTotal"` | A number type (float) corresponding to the $R_{M}$ ratio given by Eq. (1). |
| `"dConversionElectronIntensityRatioAtomicShellMtoTotal"` | A number type (float) corresponding to the associated uncertainty on the $R_{M}$ ratio. |
| `"conversionElectronIntensityRatioAtomicShellNtoTotal"` | A number type (float) corresponding to the $R_{N}$ ratio given by Eq. (1). |
| `"dConversionElectronIntensityRatioAtomicShellNtoTotal"` | A number type (float) corresponding to the associated uncertainty on the $R_{N}$ ratio. |
| `"conversionElectronIntensityRatioAtomicShellOtoTotal"` | A number type (float) corresponding to the $R_{O}$ ratio given by Eq. (1). |
| `"dConversionElectronIntensityRatioAtomicShellOtoTotal"` | A number type (float) corresponding to the associated uncertainty on the $R_{O}$ ratio. |
| `"conversionElectronIntensityRatioAtomicShellPtoTotal"` | A number type (float) corresponding to the $R_{P}$ ratio given by Eq. (1). |
| `"dConversionElectronIntensityRatioAtomicShellPtoTotal"` | A number type (float) corresponding to the associated uncertainty on the $R_{P}$ ratio. |
| `"conversionElectronIntensityRatioAtomicShellQtoTotal"` | A number type (float) corresponding to the $R_{Q}$ ratio given by Eq. (1). |
| `"dConversionElectronIntensityRatioAtomicShellQtoTotal"` | A number type (float) corresponding to the associated uncertainty on the $R_{Q}$ ratio. |


##### 1.3.4.4 `"experimentalAtomicShellConversionCoefficients"` array

| JSON key | Explanation |
| --- | --- |
| `"experimentalInternalConversionCoefficientAtomicShellK"` | A number type (float) corresponding to the experimental *K*-shell internal-conversion coefficient.|
| `"dExperimentalInternalConversionCoefficientAtomicShellK"` | A number type (float) corresponding to the associated uncertainty of the experimental *K*-shell internal-conversion coefficient.|
| `"experimentalInternalConversionCoefficientAtomicShellL"` | A number type (float) corresponding to the experimental *L*-shell internal-conversion coefficient.|
| `"dExperimentalInternalConversionCoefficientAtomicShellL"` | A number type (float) corresponding to the associated uncertainty of the experimental *L*-shell internal-conversion coefficient.|
| `"experimentalInternalConversionCoefficientAtomicShellM"` | A number type (float) corresponding to the experimental *M*-shell internal-conversion coefficient.|
| `"dExperimentalInternalConversionCoefficientAtomicShellM"` | A number type (float) corresponding to the associated uncertainty of the experimental *M*-shell internal-conversion coefficient.|
| `"experimentalInternalConversionCoefficientAtomicShellN"` | A number type (float) corresponding to the experimental *N*-shell internal-conversion coefficient.|
| `"dExperimentalInternalConversionCoefficientAtomicShellN"` | A number type (float) corresponding to the associated uncertainty of the experimental *N*-shell internal-conversion coefficient.|
| `"experimentalInternalConversionCoefficientAtomicShellO"` | A number type (float) corresponding to the experimental *O*-shell internal-conversion coefficient.|
| `"dExperimentalInternalConversionCoefficientAtomicShellO"` | A number type (float) corresponding to the associated uncertainty of the experimental *O*-shell internal-conversion coefficient.|
| `"experimentalInternalConversionCoefficientAtomicShellP"` | A number type (float) corresponding to the experimental *P*-shell internal-conversion coefficient.|
| `"dExperimentalInternalConversionCoefficientAtomicShellP"` | A number type (float) corresponding to the associated uncertainty of the experimental *P*-shell internal-conversion coefficient.|
| `"experimentalInternalConversionCoefficientAtomicShellQ"` | A number type (float) corresponding to the experimental *Q*-shell internal-conversion coefficient.|
| `"dExperimentalInternalConversionCoefficientAtomicShellQ"` | A number type (float) corresponding to the associated uncertainty of the experimental *Q*-shell internal-conversion coefficient.|


##### 1.3.4.5 `"atomicShellConversionElectronIntensities"` array

| JSON key | Explanation |
| --- | --- |
| `"conversionElectronIntensityAtomicShellK"` | A number type (float) corresponding to the atomic *K*-shell internal-conversion electron intensity.|
| `"dConversionElectronIntensityAtomicShellK"` | A number type (float) corresponding to the associated uncertainty for the atomic *K*-shell internal-conversion electron intensity.|
| `"conversionElectronIntensityAtomicShellL"` | A number type (float) corresponding to the atomic *L*-shell internal-conversion electron intensity.|
| `"dConversionElectronIntensityAtomicShellL"` | A number type (float) corresponding to the associated uncertainty for the atomic *L*-shell internal-conversion electron intensity.|
| `"conversionElectronIntensityAtomicShellM"` | A number type (float) corresponding to the atomic *M*-shell internal-conversion electron intensity.|
| `"dConversionElectronIntensityAtomicShellM"` | A number type (float) corresponding to the associated uncertainty for the atomic *M*-shell internal-conversion electron intensity.|
| `"conversionElectronIntensityAtomicShellN"` | A number type (float) corresponding to the atomic *N*-shell internal-conversion electron intensity.|
| `"dConversionElectronIntensityAtomicShellN"` | A number type (float) corresponding to the associated uncertainty for the atomic *N*-shell internal-conversion electron intensity.|
| `"conversionElectronIntensityAtomicShellO"` | A number type (float) corresponding to the atomic *O*-shell internal-conversion electron intensity.|
| `"dConversionElectronIntensityAtomicShellO"` | A number type (float) corresponding to the associated uncertainty for the atomic *O*-shell internal-conversion electron intensity.|
| `"conversionElectronIntensityAtomicShellP"` | A number type (float) corresponding to the atomic *P*-shell internal-conversion electron intensity.|
| `"dConversionElectronIntensityAtomicShellP"` | A number type (float) corresponding to the associated uncertainty for the atomic *P*-shell internal-conversion electron intensity.|
| `"conversionElectronIntensityAtomicShellQ"` | A number type (float) corresponding to the atomic *Q*-shell internal-conversion electron intensity.|
| `"dConversionElectronIntensityAtomicShellQ"` | A number type (float) corresponding to the associated uncertainty for the atomic *Q*-shell internal-conversion electron intensity.|


#### 1.3.5 `"alphaDecay"` array

This array will only be present in the data structure and populated when `"decayMode": "alphaDecay"`.

| JSON key | Explanation |
| --- | --- |
| `"alphaEnergy"`      | A number type (float) corresponding to the &alpha;-particle energy in units of keV.|
| `"dAlphaEnergy"`     | A number type (float) corresponding to the associated uncertainty on the &alpha;-particle energy.|
| `"alphaIntensity"`   | A number type (float) corresponding to the &alpha;-particle intensity.|
| `"dAlphaIntensity"`  | A number type (float) corresponding to the associated uncertainty on the &alpha;-particle intensity.|
| `"hindranceFactor"`  | A number type (float) corresponding to the hindrance factor for &alpha; decay.|
| `"dHindranceFactor"` | A number type (float) corresponding to the associated uncertainty on the hindrance factor.|


#### 1.3.6 `"betaMinusDecay"` array

This array will only be present in the data structure and populated when `"decayMode": "betaMinusDecay"`.

| JSON key | Explanation |
| --- | --- |
| `"endPointBetaMinusEnergy"`     | A number type (float) corresponding to the &beta;<sup>-</sup>-decay end-point energy in keV.|
| `"dEndPointBetaMinusEnergy"`    | A number type (float) corresponding to the associated uncertainty on the &beta;<sup>-</sup>-decay end-point energy.|
| `"betaMinusIntensity"`          | A number type (float) corresponding to the intensity of the &beta;<sup>-</sup>-decay branch.|
| `"dBetaMinusIntensity"`         | A number type (float) corresponding to the associated uncertainty on the intensity of the &beta;<sup>-</sup>-decay branch.|
| `"logFT"`                       | A number type (float) corresponding to the log(*ft*) value of the &beta;<sup>-</sup> transition.|
| `"dLogFT"`                      | A number type (float) corresponding to the associated uncertainty on the log(*ft*) value.|
| `"averageBetaMinusEnergy"`      | A number type (float) corresponding to the average energy of the &beta;<sup>-</sup> spectrum.|
| `"dAverageBetaMinusEnergy"`     | A number type (float) corresponding to the associated uncertainty on the average energy of the &beta;<sup>-</sup> spectrum.|
| `"betaMinusDose"`               |
| `"dBetaMinusDose"`              |
| `"selectionRulesDeltaJ"`        | A number type (integer) corresponding to the difference in spin values between initial and final states associated with the &beta;<sup>-</sup> transition; $\Delta J = \|J_{i} - J_{f}\|$.|
| `"selectionRulesDeltaPi"`       | A number type (integer) to indicate parity changes between initial and final states associated with the &beta;<sup>-</sup> transition; $\Delta \pi = \pi_{i} \pi_{f}$.  Change in parity $\pi = -1$; no change in parity $\pi = 1$.|
| `"forbiddennessDegree"`         | A string type representing the forbiddenness degree associated with the &beta;<sup>-</sup> transition.  Refer to [table](https://github.com/AaronMHurst/pace_ensdf#allowed-and-forbidden-transitions-in-%CE%B2-decay) of forbidden/allowed classifications.|
| `"forbiddennessClassification"` | A string type representing the forbiddenness classification associated with the &beta;<sup>-</sup> transition.  Refer to [table](https://github.com/AaronMHurst/pace_ensdf#allowed-and-forbidden-transitions-in-%CE%B2-decay) of forbidden/allowed classifications.|
| `"orbitalAngularMomentum"`      | A number type (integer) representing the orbital angular momentum quantum number associated with the &beta;<sup>-</sup> transition.  Refer to [table](https://github.com/AaronMHurst/pace_ensdf#allowed-and-forbidden-transitions-in-%CE%B2-decay) of forbidden/allowed classifications.|



#### 1.3.7 `"betaPlusDecay"` array

This array will only be present in the data structure and populated when `"decayMode": "electronCaptureBetaPlusDecay"`.

| JSON key | Explanation |
| --- | --- |
| `"electronCaptureEnergy"`  | A number type (float) corresponding to the &epsilon; energy in keV.|
| `"dElectronCaptureEnergy"` | A number type (float) corresponding to the associated uncertainty on the &epsilon; energy.|
| `"electronCaptureIntensity"`  | A number type (float) corresponding to the intensity of the &epsilon;-decay branch.|
| `"dElectronCaptureIntensity"` | A number type (float) corresponding to the associated uncertainty on the intensity of the &epsilon;-decay branch.|
| `"averageBetaPlusEnergy"`  | A number type (float) corresponding to the average energy of the &beta;<sup>+</sup> spectrum.|
| `"dAverageBetaPlusEnergy"` | A number type (float) corresponding to the associated uncertainty on the average energy of the &beta;<sup>+</sup> spectrum.|
| `"betaPlusIntensity"`  | A number type (float) corresponding to the intensity of the &beta;<sup>+</sup>-decay branch.|
| `"dBetaPlusIntensity"` | A number type (float) corresponding to the associated uncertainty on the intensity of the &beta;<sup>+</sup>-decay branch.|
| `"totalElectronCaptureBetaPlusIntensity"`  | A number type (float) corresponding to the total &epsilon; + &beta;<sup>+</sup> intensity.|
| `"dTotalElectronCaptureBetaPlusIntensity"` | A number type (float) corresponding to the associated uncertainty on the total &epsilon; + &beta;<sup>+</sup> intensity.|
| `"logFT"`  | A number type (float) corresponding to the log(*ft*) value of the &epsilon; + &beta;<sup>+</sup> transition.|
| `"dLogFT"` | A number type (float) corresponding to the associated uncertainty on the log(*ft*) value.|
| `"endPointBetaPlusEnergy"`  | A number type (float) corresponding to the &beta;<sup>+</sup>-decay end-point energy in keV.|
| `"dEndPointBetaPlusEnergy"` | A number type (float) corresponding to the associated uncertainty on the &beta;<sup>+</sup>-decay end-point energy.|
| `"calculatedAtomicShellElectronCaptureFractions"`    | An array type containing the calculated fraction of decay by electron capture for the atomic subshell.|
| `"sumCalculatedAtomicShellElectronCaptureFractions"` | An array type containing the calculated fraction of decay by electron capture for the summed contributions from the atomic subshells.|
| `"experimentalAtomicShellElectronCaptureFractions"`  | An array type containing the experimentally-measured fraction of decay by electron capture for the atomic subshells.|
| `"selectionRulesDeltaJ"` | A number type (integer) corresponding to the difference in spin values between initial and final states associated with the &beta;<sup>-</sup> transition; $\Delta J = \|J_{i} - J_{f}\|$.|
| `"selectionRulesDeltaPi"` | A number type (integer) to indicate parity changes between initial and final states associated with the &beta;<sup>-</sup> transition; $\Delta \pi = \pi_{i} \pi_{f}$.  Change in parity $\pi = -1$; no change in parity $\pi = 1$.|
| `"forbiddennessDegree"` | A string type representing the forbiddenness degree associated with the &beta;<sup>-</sup> transition.  Refer to [table](https://github.com/AaronMHurst/pace_ensdf#allowed-and-forbidden-transitions-in-%CE%B2-decay) of forbidden/allowed classifications.|
| `"forbiddennessClassification"` | A string type representing the forbiddenness classification associated with the &beta;<sup>-</sup> transition.  Refer to [table](https://github.com/AaronMHurst/pace_ensdf#allowed-and-forbidden-transitions-in-%CE%B2-decay) of forbidden/allowed classifications.|
| `"orbitalAngularMomentum"` | A number type (integer) representing the orbital angular momentum quantum number associated with the &beta;<sup>-</sup> transition.  Refer to [table](https://github.com/AaronMHurst/pace_ensdf#allowed-and-forbidden-transitions-in-%CE%B2-decay) of forbidden/allowed classifications.|

##### 1.3.7.1 `"calculatedAtomicShellElectronCaptureFractions"` array

| JSON key | Explanation |
| --- | --- |
| `"calculatedElectronCaptureFractionAtomicShellK"` | A number type (float) corresponding to the calculated fraction of decay by &epsilon; from the atomic *K* shell. |
| `"dCalculatedElectronCaptureFractionAtomicShellK"` | A number type (float) corresponding to the associated uncertainty of the calculated fraction of decay by &epsilon; from the atomic *K* shell. |
| `"calculatedElectronCaptureFractionAtomicShellL"` | A number type (float) corresponding to the calculated fraction of decay by &epsilon; from the atomic *L* shell. |
| `"dCalculatedElectronCaptureFractionAtomicShellL"` | A number type (float) corresponding to the associated uncertainty of the calculated fraction of decay by &epsilon; from the atomic *L* shell. |
| `"calculatedElectronCaptureFractionAtomicShellM"` | A number type (float) corresponding to the calculated fraction of decay by &epsilon; from the atomic *M* shell. |
| `"dCalculatedElectronCaptureFractionAtomicShellM"` | A number type (float) corresponding to the associated uncertainty of the calculated fraction of decay by &epsilon; from the atomic *M* shell. |
| `"calculatedElectronCaptureFractionAtomicShellN"` | A number type (float) corresponding to the calculated fraction of decay by &epsilon; from the atomic *N* shell. |
| `"dCalculatedElectronCaptureFractionAtomicShellN"` | A number type (float) corresponding to the associated uncertainty of the calculated fraction of decay by &epsilon; from the atomic *N* shell. |
| `"calculatedElectronCaptureFractionAtomicShellO"` | A number type (float) corresponding to the calculated fraction of decay by &epsilon; from the atomic *O* shell. |
| `"dCalculatedElectronCaptureFractionAtomicShellO"` | A number type (float) corresponding to the associated uncertainty of the calculated fraction of decay by &epsilon; from the atomic *O* shell. |
| `"calculatedElectronCaptureFractionAtomicShellP"` | A number type (float) corresponding to the calculated fraction of decay by &epsilon; from the atomic *P* shell. |
| `"dCalculatedElectronCaptureFractionAtomicShellP"` | A number type (float) corresponding to the associated uncertainty of the calculated fraction of decay by &epsilon; from the atomic *P* shell. |
| `"calculatedElectronCaptureFractionAtomicShellQ"` | A number type (float) corresponding to the calculated fraction of decay by &epsilon; from the atomic *Q* shell. |
| `"dCalculatedElectronCaptureFractionAtomicShellQ"` | A number type (float) corresponding to the associated uncertainty of the calculated fraction of decay by &epsilon; from the atomic *Q* shell. |


##### 1.3.7.2 `"sumCalculatedAtomicShellElectronCaptureFractions"` array

| JSON key | Explanation |
| --- | --- |
| `"sumElectronCaptureFractionAtomicShellPlusL"` | A number type (float) corresponding to the sum of contributions to the calculated fraction of decay by &epsilon; from the atomic *L* shell and above (i.e., *L+*).|
| `"dSumElectronCaptureFractionAtomicShellPlusL"` | A number type (float) corresponding to the associated uncertainty on the sum of contributions to the calculated fraction of decay by &epsilon; from the atomic *L* shell and above (i.e., *L+*).|
| `"sumElectronCaptureFractionAtomicShellPlusM"` | A number type (float) corresponding to the sum of contributions to the calculated fraction of decay by &epsilon; from the atomic *M* shell and above (i.e., *M+*).|
| `"dSumElectronCaptureFractionAtomicShellPlusM"` | A number type (float) corresponding to the associated uncertainty on the sum of contributions to the calculated fraction of decay by &epsilon; from the atomic *M* shell and above (i.e., *M+*).|
| `"sumElectronCaptureFractionAtomicShellPlusN"` | A number type (float) corresponding to the sum of contributions to the calculated fraction of decay by &epsilon; from the atomic *N* shell and above (i.e., *N+*).|
| `"dSumElectronCaptureFractionAtomicShellPlusN"` | A number type (float) corresponding to the associated uncertainty on the sum of contributions to the calculated fraction of decay by &epsilon; from the atomic *N* shell and above (i.e., *N+*).|
| `"sumElectronCaptureFractionAtomicShellPlusO"` | A number type (float) corresponding to the sum of contributions to the calculated fraction of decay by &epsilon; from the atomic *O* shell and above (i.e., *O+*).|
| `"dSumElectronCaptureFractionAtomicShellPlusO"` | A number type (float) corresponding to the associated uncertainty on the sum of contributions to the calculated fraction of decay by &epsilon; from the atomic *O* shell and above (i.e., *O+*).|
| `"sumElectronCaptureFractionAtomicShellPlusP"` | A number type (float) corresponding to the sum of contributions to the calculated fraction of decay by &epsilon; from the atomic *P* shell and above (i.e., *P+*).|
| `"dSumElectronCaptureFractionAtomicShellPlusP"` | A number type (float) corresponding to the associated uncertainty on the sum of contributions to the calculated fraction of decay by &epsilon; from the atomic *P* shell and above (i.e., *P+*).|
| `"sumElectronCaptureFractionAtomicShellPlusQ"` | A number type (float) corresponding to the sum of contributions to the calculated fraction of decay by &epsilon; from the atomic *Q* shell and above (i.e., *Q+*).|
| `"dSumElectronCaptureFractionAtomicShellPlusQ"` | A number type (float) corresponding to the associated uncertainty on the sum of contributions to the calculated fraction of decay by &epsilon; from the atomic *Q* shell and above (i.e., *Q+*).|


##### 1.3.7.3 `"experimentalAtomicShellElectronCaptureFractions"` array

| JSON key | Explanation |
| --- | --- |
| `"experimentalElectronCaptureFractionAtomicShellK"` | A number type (float) corresponding to the experimentally-measured fraction of decay by &epsilon; from the atomic *K* shell. |
| `"dExperimentalElectronCaptureFractionAtomicShellK"` | A number type (float) corresponding to the associated uncertainty of the experimentally-measured fraction of decay by &epsilon; from the atomic *K* shell. |
| `"experimentalElectronCaptureFractionAtomicShellL"` | A number type (float) corresponding to the experimentally-measured fraction of decay by &epsilon; from the atomic *L* shell. |
| `"dExperimentalElectronCaptureFractionAtomicShellL"` | A number type (float) corresponding to the associated uncertainty of the experimentally-measured fraction of decay by &epsilon; from the atomic *L* shell. |
| `"experimentalElectronCaptureFractionAtomicShellM"` | A number type (float) corresponding to the experimentally-measured fraction of decay by &epsilon; from the atomic *M* shell. |
| `"dExperimentalElectronCaptureFractionAtomicShellM"` | A number type (float) corresponding to the associated uncertainty of the experimentally-measured fraction of decay by &epsilon; from the atomic *M* shell. |
| `"experimentalElectronCaptureFractionAtomicShellN"` | A number type (float) corresponding to the experimentally-measured fraction of decay by &epsilon; from the atomic *N* shell. |
| `"dExperimentalElectronCaptureFractionAtomicShellN"` | A number type (float) corresponding to the associated uncertainty of the experimentally-measured fraction of decay by &epsilon; from the atomic *N* shell. |


## Allowed and forbidden transitions in &beta; decay

The following table is based on the selection rules in $\beta$ decay and can be used to help classify allowed and forbidden transitions together with their degree of fobiddenness in $\beta^{-} / \beta^{+}$ decay.  For the allowed `A` transitions the preceding number is used to indicate the spin coupling, i.e., anti-parallel $S=0$ and paralled $S=1$.  In the case of forbidden `F` and forbidden unique `UF` transitions the preceding number indicates the degree of fobiddenness.  Values of $\Delta \pi = 1$ indicate no change in parity and $\Delta \pi = -1$ indicate a change in parity associated with the $\beta$-decay transition.

| $\Delta J$ | $\Delta \pi$ | Degree | $l$ | Classification |
| --- | --- | --- | --- | --- |
| 0 | 1 | `0A` | 0 | Allowed ($S = 0$) |
| 1 | 1 | `1A` | 0 | Allowed ($S = 1$) |
| 0 | -1 | `1F` | 1 | First Forbidden |
| 1 | -1 | `1F` | 1 | First Forbidden |
| 2 | -1 | `1UF` | 1 | First Forbidden Unique |
| 2 | 1 | `2F` | 2 | Second Forbidden |
| 3 | 1 | `2UF` | 2 | Second Forbidden Unique |
| 3 | -1 | `3F` | 3 | Third Forbidden |
| 4 | -1 | `3UF` | 3 | Third Forbidden Unique |
| 4 | 1 | `4F` | 4 | Fourth Forbidden |
| 5 | 1 | `4UF` | 4 | Fourth Forbidden Unique |
| 5 | -1 | `5F` | 5 | Fifth Forbidden |
| 6 | -1 | `5UF` | 5 | Fifth Forbidden Unique |

Here, $\Delta J = \|J_{i} - J_{f}\|$ and $\Delta \pi = \pi_{i} \pi_{f}$, where $i$ and $f$ denote initial and final states, respectively, associated with the $\beta$-decay transition.  A conservative approach has been adopted in the assignment of allowed/forbidden transitions whereupon only states where both $J$ and $\pi$ are firmly established, in both the initial and final state, have been used to make any such assignments.  Unless all of these conditions are met the values of the corresponding keys in the $\beta$-decay JSON structures will all be set to `null`.  However, because boolean flags have been used to indicate the nature of firm/tentative $J^{\pi}$ assignments throughout the database, together with interpreted values for all permutations of $J$ and $\pi$, it is straightforward for the user to relax this condition to establish assignments that meet their criteria.

## (2) JSON-formatted coincidence &gamma;-&gamma; schema

| JSON key | Explanation |
| --- | --- |
| `"parentID"` | A string type value corresponding to the identification of the parent nucleus `<symbol><mass>`.|
| `"parentZ"` | A number type (integer) corresponding to the atomic number of the parent nucleus.|
| `"parentA"` | A number type (integer) corresponding to the mass number of the parent nucleus.|
| `"daughterID"` | A string type value corresponding to the identification of the daughter nucleus `<symbol><mass>`.|
| `"daughterZ"` | A number type (integer) corresponding to the atomic number of the daughter nucleus.|
| `"daughterA"` | A number type (integer) corresponding to the mass number of the daughter nucleus.|
| `"decayMode"` | A string type to indicate the radioactive decay mode; acceptable values are `"alphaDecay"`, `"betaMinusDecay"`, or `"electronCaptureBetaPlus"` decay.|
| `"isomer"` | A boolean type to indicate isomeric `"true"` or ground-state `"false"` decay.|
| `"parentDecayLevelEnergy"` | A number type (float) corresponding to the energy level parent nucleus undergoing decay: 0 keV if `"isomer": false` or > 0 keV if `"isomer": true`.
| `"Qvalue"` | A number type (float or integer) corresponding to the ground-state *Q* value, i.e., the total energy available for the ground-state to ground-state transition.|
| `"dQvalue"` | A number type (float or integer) corresponding to the associated uncertainty of the ground-state *Q* value.|
| `"unitEnergy"` | A string type representing the units for the energy data types in the structure; The value should be units of `"keV"`. |
| `"totalNumberLevels"` | A number type (integer) denoting the total number of levels in the decay scheme of the daughter nucleus. |
| `"totalNumberGammas"` | A number type (integer) denoting the total number of &gamma; rays in the decay scheme of the daughter nucleus. |
| `"totalNumberGammaCoincidences"` | A number type (integer) denoting the total number of coincident &gamma;-&gamma; pairs in the decay scheme of the daughter nucleus. |
| `"checkNumberGammaCoincidences"` | A number type (integer) denoting the total number of coincident &gamma;-&gamma; pairs in the decay scheme of the daughter nucleus.  This is a check to esnure `"totalNumberGammaCoincidences" == "checkNumberGammaCoincidences"`). |
| `"halfLife"` | An array type containing the half-life information for the parent isotope or isomer.|
| `"normalizedBranchingRatios"` | An array type containing normalized branching ratios associated with the &gamma;-ray and internal-conversion electron transitions.|
| `"decaySingles"` | An array type containing information associated with the singles &gamma;-ray and internal-conversion electron transitions.| 
| `"decayCoincidences"` | An array type containing information associated with the coincidence &gamma;-&gamma; transitions.|
| `"decayIndex"` | A number type value (integer) to indicate whether the parent nucleus decays from its ground state (0) or from an isomeric level (>0).|
|``"datasetID"` | A string type defining the dataset; for the &gamma;-&gamma; datasets this value should be `"GG"`.|

### 2.1 `"halfLife"` array

This array contains the same data types as described for other parts in the schema in [1.2.1 `"halfLife"` array](https://github.com/AaronMHurst/pace_ensdf/tree/main#121-halflife-array) and [1.3.1 `"isomerDecay"` array](https://github.com/AaronMHurst/pace_ensdf/tree/main#131-isomerdecay-array), explicitly:

| JSON key | Explanation |
| --- | --- |
| `"halfLifeBest"` | A number type (float) representing the halflife in *best* units from original data set.|
| `"dHalfLifeBest"` | A number type (float) representing the associated uncertainty on the halflife in *best* units. |
| `"unitHalfLifeBest"` | A string type to indicate the *best* halflife units.|
| `"halfLifeConverted"` | A number type (float) representing the halflife *converted* to units of seconds.|
| `"dHalfLifeConverted"` | A number type (float) representing the associated uncertainty on the halflife *converted* to seconds.|
| `"unitHalfLifeConverted"` | A string type to indicate the *converted* halflife units.|



### 2.2 `"normalizedBranchingRatios"` array

The normalized branching ratios presented in this data structure are defined and explained in Ref. [[1]](#1) which is distributed with this software package.

| JSON key | Explanation |
| --- | --- |
| `"gammaEnergy"` | A number type (float) corresponding to the &gamma;-ray energy.|
| `"unitEnergy"` | A string type representing the units for the energy data types in the structure; The value should be units of `"keV"`. | 
| `"levelIndexInitial"` | A number type (integer) corresponding to the index of the initial level associated with the &gamma;-ray transition. |
| `"levelIndexFinal"` | A number type (integer) corresponding to the index of the final level associated with the &gamma;-ray transition.|
| `"levelEnergyInitial"` | A number type (float) corresponding to the excitation energy of the initial level associated with the &gamma;-ray transition.|
| `"levelEnergyFinal"` | A number type (float) corresponding to the excitation energy of the final level associated with the &gamma;-ray transition.|
| `"gammaBR"` | A number type (float) corresponding to the normalized &gamma-ray; intensity branching ratio. |
| `"dGammaBR"` | A number type (float) corresponding to the associated uncertainty of the normalized &gamma-ray; intensity ratio. |
| `"conversionElectronBR"` | A number type (float) corresponding to the normalized conversion-electron intensity branching ratio. |
| `"dConversionElectronBR"` | A number type (float) corresponding to the associated uncertainty of the normalized conversion-electron intensity branching ratio. |
| `"totalTransitionBR"` | A number type (float) corresponding to the normalized total transition intensity (&Gamma;<sub>&gamma;</sub> + &Gamma;<sub>*e*</sub>) branching ratio. |
| `"dTotalTransitionBR"` | A number type (float) corresponding to the associated uncertainty of the normalized total transition intensity branching ratio. |


### 2.3 `"decaySingles"` array

This array contains [normalized](https://github.com/AaronMHurst/pace_ensdf/tree/main#11-decayschemenormalization-array) absolute intensities associated with the &gamma;-ray and conversion-electron transitions.

| JSON key | Explanation |
| --- | --- |
| `"gammaEnergy"` | A number type (float) corresponding to the &gamma;-ray energy.|
| `"unitEnergy"` | A string type representing the units for the energy data types in the structure; The value should be units of `"keV"`. |
| `"levelIndexInitial"` | A number type (integer) corresponding to the index of the initial level associated with the &gamma;-ray transition.|
| `"levelIndexFinal"` | A number type (integer) corresponding to the index of the final level associated with the &gamma;-ray transition.|
| `"levelEnergyInitial"` | A number type (float) corresponding to the excitation energy of the initial level associated with the &gamma;-ray transition.|
| `"levelEnergyFinal"` | A number type (float) corresponding to the excitation energy of the final level associated with the &gamma;-ray transition.|
| `"absoluteGammaIntensity"` | A number type (float) corresponding to the absolute &gamma-ray intensity in percentage units.|
| `"dAbsoluteGammaIntensity"` | A number type (float) corresponding to the associated uncertainty of the &gamma;-ray intensity.|
| `"internalConversionCoefficient"` | A number type (float) corresponding to the BrIcc-calculated [[4]](#4) internal-conversion coefficient.|
| `"dInternalConversionCoefficient"` | A number type (float) corresponding to associated uncertainty of the BrIcc-calculated [[4]](#4) internal-conversion coefficient.|
| `"absoluteElectronIntensity"` | A number type (float) corresponding to the absolute conversion-electron intensity in percentage units.|
| `"dAbsoluteElectronIntensity"` | A number type (float) corresponding to the associated uncertainty of the conversion-electron intensity.|
| `"totalConvertedIntensity"` | A number type (float) corresponding to the total transition intensity (&Gamma;<sub>&gamma;</sub> + &Gamma;<sub>*e*</sub>) in percentage units.|
| `"dTotalConvertedIntensity"` | A number type (float) corresponding to the associated uncertainty of the total transition intensity in percentage units.|
| `"unitIntensity"` | A string type defining the intensity units: The value should be units of `"percent"`.|
| `"levelIsomer"` | A boolean type to indicate whether level is an isomer `"true"` or not `"false"`.|
| `"levelHalfLifeBest"` | A number type (float) representing the halflife in *best* units from original data set associated with the *initial level* of the &gamma;-ray transition.|
| `"dLevelHalfLifeBest"` | A number type (float) representing the associated uncertainty on the halflife in *best* units associated with the *initial level* of the &gamma;-ray transition. |
| `"unitLevelHalfLifeBest"` | A string type to indicate the *best* halflife units associated with the *initial level* of the &gamma;-ray transition.|
| `"levelHalfLifeConverted"` | A number type (float) representing the halflife *converted* to units of seconds associated with the *initial level* of the &gamma;-ray transition.|
| `"dLevelHalfLifeConverted"` | A number type (float) representing the associated uncertainty on the halflife *converted* to seconds associated with the *initial level* of the &gamma;-ray transition.|
| `"unitLevelHalfLifeConverted"` | A string type to indicate the *converted* halflife units associated with the *initial level* of the &gamma;-ray transition.|


### 2.4 `"decayCoincidences"` array

| JSON key | Explanation |
| --- | --- |
| `"gammaEnergyGate"` | A number type (float) corresponding to the &gamma;-ray energy of the gating transition.|
| `"gammaEnergyCoincidence"` | A number type (float) corresponding to the &gamma;-ray energy of the coincidence transition.|
| `"unitEnergy"` | A string type representing the units for the energy data types in the structure; The value should be units of `"keV"`. |
| `"gammaGateLevelIndexInitial"` | A number type (integer) corresponding to the index of the initial level associated with the &gamma;-ray gating transition.|
| `"gammaGateLevelIndexFinal"` | A number type (integer) corresponding to the index of the final level associated with the &gamma;-ray gating transition.| 
| `"gammaGateLevelEnergyInitial"` | A number type (float) corresponding to the excitation energy of the initial level associated with the &gamma;-ray gating transition.|
| `"gammaGateLevelEnergyFinal"` | A number type (float) corresponding to the excitation energy of the final level associated with the &gamma;-ray gating transition.|
| `"gammaCoincidenceLevelIndexInitial"` | A number type (integer) corresponding to the index of the initial level associated with the &gamma;-ray coincidence transition.|
| `"gammaCoincidenceLevelIndexFinal"` | A number type (integer) corresponding to the index of the final level associated with the &gamma;-ray coincidence transition.|
| `"gammaCoincidenceLevelEnergyInitial"` | A number type (float) corresponding to the excitation energy of the initial level associated with the &gamma;-ray coincidence transition.|
| `"gammaCoincidenceLevelEnergyFinal"` | A number type (float) corresponding to the excitation energy of the final level associated with the &gamma;-ray coincidence transition.|
| `"absoluteCoincidenceIntensity"` | A number type (float) correponding to the &gamma;-&gamma; coincidence intensity.|
| `"dAbsoluteCoincidenceIntensity"` | A number type (float) correponding to the associated uncertainty of the &gamma;-&gamma; coincidence intensity.|
| `"unitIntensity"` | A string type defining the intensity units: The value should be units of `"percent"`.|
| `"numberParallelCascadePaths"` | A number type (integer) representing the total number of parallel paths between gate-coincidence &gamma;-&gamma; pair.|
| `"coincidenceCascadeSequences"` | An array type containing information on the cascades for each parallel path.|
| `"gammaGateLevelIsomer"` | A boolean type to indicate whether level associated with the &gamma;-ray gating transition is an isomer `"true"` or not `"false"`.|
| `"gammaGateLevelHalfLifeBest"` | A number type (float) representing the halflife in *best* units from original data set associated with the *initial level* of the &gamma;-ray gate transition.|
| `"dGammaGateLevelHalfLifeBest"` | A number type (float) representing the associated uncertainty on the halflife in *best* units associated with the *initial level* of the &gamma;-ray gate transition. |
| `"unitGammaGateLevelHalfLifeBest"` | A string type to indicate the *best* halflife units associated with the *initial level* of the &gamma;-ray gate transition.|
| `"gammaGateLevelHalfLifeConverted"` | A number type (float) representing the halflife *converted* to units of seconds associated with the *initial level* of the &gamma;-ray gate transition.|
| `"dGammaGateLevelHalfLifeConverted"` | A number type (float) representing the associated uncertainty on the halflife *converted* to seconds associated with the *initial level* of the &gamma;-ray gate transition.|
| `"unitGammaGateLevelHalfLifeConverted"` | A string type to indicate the *converted* halflife units associated with the *initial level* of the &gamma;-ray gate transition.|

#### 2.4.1 `"coincidenceCascadeSequences"` array

| JSON key | Explanation |
| --- | --- |
| `"pathNumber"` | A number type (integer) representing the parallel path index number associated with the cascade.|
| `"indexedTransitionSequence"` | An array type containing integers associated with levels in the corresponding cascade.|

##### 2.4.1.1 `"indexedTransitionSequence"` array



## (3) JSON-formatted coincidence &gamma;-*X*-ray schema

Many of the data types are common to both the &gamma;-&gamma; and &gamma;-*X*-ray schemas.  However, all data types will be explicitly explained again here where relevant.

| JSON key | Explanation |
| --- | --- |
| `"parentID"` | A string type value corresponding to the identification of the parent nucleus `<symbol><mass>`.|
| `"parentZ"` | A number type (integer) corresponding to the atomic number of the parent nucleus.|
| `"parentA"` | A number type (integer) corresponding to the mass number of the parent nucleus.|
| `"daughterID"` | A string type value corresponding to the identification of the daughter nucleus `<symbol><mass>`.|
| `"daughterZ"` | A number type (integer) corresponding to the atomic number of the daughter nucleus.|
| `"daughterA"` | A number type (integer) corresponding to the mass number of the daughter nucleus.|
| `"decayMode"` | A string type to indicate the radioactive decay mode; acceptable values are `"alphaDecay"`, `"betaMinusDecay"`, or `"electronCaptureBetaPlus"` decay.|
| `"isomer"` | A boolean type to indicate isomeric `"true"` or ground-state `"false"` decay.|
| `"parentDecayLevelEnergy"` | A number type (float) corresponding to the energy level parent nucleus undergoing decay: 0 keV if `"isomer": false` or > 0 keV if `"isomer": true`.
| `"Qvalue"` | A number type (float or integer) corresponding to the ground-state *Q* value, i.e., the total energy available for the ground-state to ground-state transition.|
| `"dQvalue"` | A number type (float or integer) corresponding to the associated uncertainty of the ground-state *Q* value.|
| `"unitEnergy"` | A string type representing the units for the energy data types in the structure; The value should be units of `"keV"`. |
| `"totalNumberLevels"` | A number type (integer) denoting the total number of levels in the decay scheme of the daughter nucleus. |
| `"totalNumberGammas"` | A number type (integer) denoting the total number of &gamma; rays in the decay scheme of the daughter nucleus. |
| `totalNumberKshellXrays"` | A number type (integer) denoting the total number of *K*-shell *X* rays in the decay scheme of the daughter nucleus. |
| `"totalNumberKshellXrayCoincidences"` | A number type (integer) denoting the total number of coincident &gamma;-*X*-ray (*K* shell) pairs in the decay scheme of the daughter nucleus. |
| `"totalNumberKshellElectronCoincidences"` | A number type (integer) denoting the total number of coincident &gamma;-*e<sub>K</sub>*; (*K*-shell electrons) pairs in the decay scheme of the daughter nucleus.  |
| `"halfLife"` | An array type containing the half-life information for the parent isotope or isomer.|
| `"bindingEnergies"` | An array type containing the binding energies taken from Ref. [[4]](#4) for the subshells in the daughter nucleus. |
| `"valenceElectronicConfiguration"` | An array type containing information associated with the valence electronic subshell configuration associated with the daughter nucleus. |
| `"XrayBranchingRatios"` | An array type containing the *X*-ray branching ratios taken from the Table of Isotopes [[5]](#5) for the daughter nucleus.|
| `"totalProjectionXrays"` | An array type containing information associated with the total projection of the *K*-shell *X* rays corresponding to the daughter nucleus. |
| `"gammaXraySingles"` | An array type containing information associated with the individual-transition contributions to the singles *X*-ray spectrum for the daughter nucleus.|
| `"gammaXrayCoincidences"` | An array type containing information associated with the coincidence &gamma;-*X*-ray (*K* shell) transitions.|
| `"KshellElectronCoincidences"` | An array type containing information associated with the *K*-shell electron-&gamma; coincidences.|
| `"decayIndex"` | A number type value (integer) to indicate whether the parent nucleus decays from its ground state (0) or from an isomeric level (>0).|
|``"datasetID"` | A string type defining the dataset; for the &gamma;-*X*-ray datasets this value should be `"GX"`.|


### 3.1 `"halfLife"` array

This array contains identical key-value pairs to those in the corresponding [&gamma;-&gamma; JSON data structure](https://github.com/AaronMHurst/pace_ensdf/tree/main#21-halflife-array).

| JSON key | Explanation |
| --- | --- |
| `"halfLifeBest"` | A number type (float) representing the halflife in *best* units from original data set.|
| `"dHalfLifeBest"` | A number type (float) representing the associated uncertainty on the halflife in *best* units. |
| `"unitHalfLifeBest"` | A string type to indicate the *best* halflife units.|
| `"halfLifeConverted"` | A number type (float) representing the halflife *converted* to units of seconds.|
| `"dHalfLifeConverted"` | A number type (float) representing the associated uncertainty on the halflife *converted* to seconds.|
| `"unitHalfLifeConverted"` | A string type to indicate the *converted* halflife units.|

### 3.2 `"bindingEnergies"` array

| JSON key | Explanation |
| --- | --- |
| `"elementID"` | A string type value corresponding to the checmical-symbol identification of the daughter nucleus.|
| `"atomicNumber"` | A number type (integer) corresponding to the atomic number (*Z*) of the daughter nucleus.|
| `"unitEnergy"` | A string type representing the units for the energy data types in the structure; The value should be units of `"keV"`. |
| `"valenceElectronicConfigurationLatexString"` | A string type corresponding to a LaTex representation of the valence electronic subshell configuration of the element associated with the radioactive-decay product. |
| `"KsubshellBindingEnergy"` | A number type (float) corresponding to the binding energy of the *K* shell.|
| `"L1subshellBindingEnergy"` | A number type (float) corresponding to the binding energy of the *L<sub>1</sub>* subshell.|
| `"L2subshellBindingEnergy"` | A number type (float) corresponding to the binding energy of the *L<sub>2</sub>* subshell.|
| `"L3subshellBindingEnergy"` | A number type (float) corresponding to the binding energy of the *L<sub>3</sub>* subshell.|
| `"M1subshellBindingEnergy"` | A number type (float) corresponding to the binding energy of the *M<sub>1</sub>* subshell.|
| `"M2subshellBindingEnergy"` | A number type (float) corresponding to the binding energy of the *M<sub>2</sub>* subshell.|
| `"M3subshellBindingEnergy"` | A number type (float) corresponding to the binding energy of the *M<sub>3</sub>* subshell.|
| `"M4subshellBindingEnergy"` | A number type (float) corresponding to the binding energy of the *M<sub>4</sub>* subshell.|
| `"M5subshellBindingEnergy"` | A number type (float) corresponding to the binding energy of the *M<sub>5</sub>* subshell.|


### 3.3 `"valenceElectronicConfiguration"` array

| JSON key | Explanation |
| --- | --- |
| `"numberValenceSubshells"` | A number type (integer) corresponding to the number of valence subshells. |
| `"numberValenceElectrons"` | A number type (integer) corresponding to the number of valence electrons. |
| `"valenceSubshells"` | An array type containing valence-subshell electronic information. |

#### 3.3.1 `"valenceSubshells"` array

| JSON key | Explanation |
| --- | --- |
| "electronicSubshell"` | A string type denoting the valence electronic subshell. |
| `"orbitalAngularMomentum"` | A number type (integer) corresponding to the orbital angular momentum. |
| `"spinAngularMomentum"` | A number type (integer) corresponding to the spin angular momentum. |
| `"totalAngularMomentumRealLS"` | A string type denoting the real value of total angular momentum.|
| `"particleNumberOccupancy"` | A number type (integer) referring to the number of particles (electrons) occupying the orbital.|
| `"particleNumberVacancies"` | A number type (integer) referring to the number of particles-vacanices available the orbital.|
| `"maximumOrbitalOccupancy"` | A number type (integer) referring to the maximum number of particles permitted to occupy the orbital: This value should be equivalent to `"particleNumberOccupancy"` + `"maximumOrbitalOccupancy"`.|


### 3.4 `"XrayBranchingRatios"` array

The energies and branching ratios in this data structure have been extracted from the Table of Isotopes [[5]](#5).

| JSON key | Explanation |
| --- | --- |
| `"elementID"` | A string type value corresponding to the checmical-symbol identification of the daughter nucleus.|
| `"atomicNumber"` | A number type (integer) corresponding to the atomic number (*Z*) of the daughter nucleus.|
| `"unitEnergy"` | A string type representing the units for the energy data types in the structure; The value should be units of `"keV"`. |
| `"energyKalpha1"` | A number type (float) corresponding to the energy of the $K_{\alpha_{1}}$ $X$ ray. |
| `"Kalpha1BR"` | A number type (float) corresponding to the branching ratio for the $K_{\alpha_{1}}$ $X$ ray. |
| `"dKalpha1BR"` | A number type (float) corresponding to the associated uncertainty on the branching ratio for the $K_{\alpha_{1}}$ $X$ ray. |
| `"energyKalpha2"` | A number type (float) corresponding to the energy of the $K_{\alpha_{2}}$ $X$ ray. |
| `"Kalpha2BR"` | A number type (float) corresponding to the branching ratio for the $K_{\alpha_{2}}$ $X$ ray. |
| `"dKalpha2BR"` | A number type (float) corresponding to the associated uncertainty on the branching ratio for the $K_{\alpha_{2}}$ $X$ ray. |
| `"energyKalpha3"` | A number type (float) corresponding to the energy of the $K_{\alpha_{3}}$ $X$ ray. |
| `"Kalpha3BR"` | A number type (float) corresponding to the branching ratio for the $K_{\alpha_{3}}$ $X$ ray. |
| `"dKalpha3BR"` | A number type (float) corresponding to the associated uncertainty on the branching ratio for the $K_{\alpha_{3}}$ $X$ ray. |
| `"energyKbeta1"` | A number type (float) corresponding to the energy of the $K_{\beta_{1}}$ $X$ ray. |
| `"Kbeta1BR"` |A number type (float) corresponding to the branching ratio for the $K_{\beta_{1}}$ $X$ ray. |
| `"dKbeta1BR"` | A number type (float) corresponding to the associated uncertainty on the branching ratio for the $K_{\beta_{1}}$ $X$ ray. |
| `"energyKbeta2"` | A number type (float) corresponding to the energy of the $K_{\beta_{2}}$ $X$ ray. |
| `"Kbeta2BR"` |A number type (float) corresponding to the branching ratio for the $K_{\beta_{2}}$ $X$ ray. |
| `"dKbeta2BR"` | A number type (float) corresponding to the associated uncertainty on the branching ratio for the $K_{\beta_{2}}$ $X$ ray. |
| `"energyKbeta3"` | A number type (float) corresponding to the energy of the $K_{\beta_{3}}$ $X$ ray. |
| `"Kbeta3BR"` | A number type (float) corresponding to the branching ratio for the $K_{\beta_{3}}$ $X$ ray. |
| `"dKbeta3BR"` | A number type (float) corresponding to the associated uncertainty on the branching ratio for the $K_{\beta_{3}}$ $X$ ray. |


### 3.5 `"totalProjectionXrays"` array

The total intensities are calculated using calculated internal-conversion coefficients from Ref. [[4]](#4) and *X*-ray branching ratios from the *Table of Isotopes* [[5]](#5).  See Ref. [[1]](#1) for an overview of the calculation methodology.

| JSON key | Explanation |
| --- | --- |
| `"energyKalpha1"` | A number type (float) corresponding to the energy of the $K_{\alpha_{1}}$ $X$ ray. |
| `"intensityKalpha1"` | A number type (float) corresponding to the absolute intensity of the $K_{\alpha_{1}}$ $X$ ray. |
| `"dIntensityKalpha1"` | A number type (float) corresponding to the associated uncertainty on the absolute intensity of the $K_{\alpha_{1}}$ $X$ ray. |
| `"energyKalpha2"` | A number type (float) corresponding to the energy of the $K_{\alpha_{2}}$ $X$ ray. |
| `"intensityKalpha2"` | A number type (float) corresponding to the absolute intensity of the $K_{\alpha_{2}}$ $X$ ray. |
| `"dIntensityKalpha2"` | A number type (float) corresponding to the associated uncertainty on the absolute intensity of the $K_{\alpha_{2}}$ $X$ ray. |
| `"energyKalpha3"` | A number type (float) corresponding to the energy of the $K_{\alpha_{3}}$ $X$ ray. |
| `"intensityKalpha3"` | A number type (float) corresponding to the absolute intensity of the $K_{\alpha_{3}}$ $X$ ray. |
| `"dIntensityKalpha3"` | A number type (float) corresponding to the associated uncertainty on the absolute intensity of the $K_{\alpha_{3}}$ $X$ ray. |
| `"energyKbeta1"` | A number type (float) corresponding to the energy of the $K_{\beta_{1}}$ $X$ ray. |
| `"intensityKbeta1"` | A number type (float) corresponding to the absolute intensity of the $K_{\beta_{1}}$ $X$ ray. |
| `"dIntensityKbeta1"` | A number type (float) corresponding to the associated uncertainty on the absolute intensity of the $K_{\beta_{1}}$ $X$ ray. |
| `"energyKbeta2"` | A number type (float) corresponding to the energy of the $K_{\beta_{2}}$ $X$ ray. |
| `"intensityKbeta2"` | A number type (float) corresponding to the absolute intensity of the $K_{\beta_{2}}$ $X$ ray. |
| `"dIntensityKbeta2"` | A number type (float) corresponding to the associated uncertainty on the absolute intensity of the $K_{\beta_{2}}$ $X$ ray. |
| `"energyKbeta3"` | A number type (float) corresponding to the energy of the $K_{\beta_{3}}$ $X$ ray. |
| `"intensityKbeta3"` | A number type (float) corresponding to the absolute intensity of the $K_{\beta_{3}}$ $X$ ray. |
| `"dIntensityKbeta3"` | A number type (float) corresponding to the associated uncertainty on the absolute intensity of the $K_{\beta_{3}}$ $X$ ray. |
| `"unitEnergy"` | A string type representing the units for the energy data types in the structure; The value should be units of `"keV"`. | 
| `"unitIntensity"` | A string type defining the intensity units: The value should be units of `"percent"`.|



### 3.6 `"gammaXraySingles"` array

| JSON key | Explanation |
| --- | --- |
| `"gammaEnergy"` | A number type (float) corresponding to the &gamma;-ray transition energy.|
| `"levelIndexInitial"` | A number type (integer) corresponding to the index of the initial level associated with the &gamma;-ray transition. |
| `"levelIndexFinal"` | A number type (integer) corresponding to the index of the final level associated with the &gamma;-ray transition.|
| `"XrayEnergy"` | A number type (float) corresponding to the *K*-shell *X*-ray energy.|
| `"labelXrayTransition"` | A string type denoting the *X*-ray label, e.g., `"Kalpha1"` for the $K_{\alpha_{1}}$ *X* ray. |
| `"absoluteSingleIntensityContributionGammaXray"` | A number type (float) corresponding to the absolute *X*-ray intensity contribution associated with the transition energy.|
| `"dAbsoluteSingleIntensityContributionGammaXray"` | A number type (float) corresponding to the associated uncertainty on the absolute *X*-ray intensity contribution.|
| `"unitEnergy"` | A string type representing the units for the energy data types in the structure; The value should be units of `"keV"`. | 
| `"unitIntensity"` | A string type defining the intensity units: The value should be units of `"percent"`.|



### 3.7 `"gammaXrayCoincidences"` array

| JSON key | Explanation |
| --- | --- |
| `"gammaEnergy"` | A number type (float) corresponding to the &gamma;-ray transition energy.|
| `"levelIndexInitial"` | A number type (integer) corresponding to the index of the initial level associated with the &gamma;-ray transition. |
| `"levelIndexFinal"` | A number type (integer) corresponding to the index of the final level associated with the &gamma;-ray transition.|
| `"XrayEnergy"` | A number type (float) corresponding to the *K*-shell *X*-ray energy.|
| `"labelXrayTransition"` | A string type denoting the *X*-ray label, e.g., `"Kalpha1"` for the $K_{\alpha_{1}}$ *X* ray. |
| `"absoluteCoincidenceIntensityGammaXray"` | A number type (float) correponding to the &gamma;-*X*-ray coincidence intensity.|
| `"dAbsoluteCoincidenceIntensityGammaXray"` | A number type (float) correponding to the associated uncertainty of the &gamma;-*X*-ray coincidence intensity.|
| `"unitEnergy"` | A string type representing the units for the energy data types in the structure; The value should be units of `"keV"`. | 
| `"unitIntensity"` | A string type defining the intensity units: The value should be units of `"percent"`.|


### 3.8 `"KshellElectronCoincidences"` array

| JSON key | Explanation |
| --- | --- |
| `"transitionEnergy"` | A number type (float) corresponding to the &gamma;-ray transition energy.|
| `"levelIndexInitial"` | A number type (integer) corresponding to the index of the initial level associated with the &gamma;-ray transition. | 
| `"levelIndexFinal"` | A number type (integer) corresponding to the index of the final level associated with the &gamma;-ray transition.|
| `"electronEnergy"` | A number type (float) corresponding to the electron energy associated with the transition: $E_{e} = E_{\gamma} - B_{K}$, where $B_{K}$ is the binding energy of the *K* shell `"KsubshellBindingEnergy"`.|
| `"intensityContributionTransition"` | A number type (float) representing the intensity contribution associated with transitions in coincidence.| 
| `"dIntensityContributionTransition"` | A number type (float) representing the associated uncertainty on the intensity contribution corresponding to transitions in coincidence.| 
| `"intensityContributionParticle"` | A number type (float) representing the intensity contribution associated with particle feeding; only non-zero if `"decayMode": "electronCaptureBetaPlus"`. | 
| `"dIntensityContributionParticle"` | A number type (float) representing the associated uncertainty on the intensity contribution corresponding to particle feeding. | 
| `"intensityContributionTotal"` | A number type corresponding to the total *K*-shell *e*-&gamma; coincidence intensity, i.e., `"intensityContributionTransition"` + `"intensityContributionParticle"`.|
| `"dIntensityContributionTotal"` | A number type corresponding to the associated uncertainty on the total *K*-shell *e*-&gamma; coincidence intensity. |
| `"unitEnergy"` | A string type representing the units for the energy data types in the structure; The value should be units of `"keV"`. | 
| `"unitIntensity"` | A string type defining the intensity units: The value should be units of `"percent"`.|



## References

<a id="1">[1]</a>
A.M. Hurst, B.D. Pierson, B.C. Archambault, L.A. Bernstein, S.M. Tannous,
*"A decay datababase of coincident &gamma;-&gamma; and &gamma;-X-ray branching ratios for in-field spectroscopy applications"*,
Eur. Phys. J. (Web of Conf.) **284**, 18002 (2023);
https://doi.org/10.1051/epjconf/202328418002

<a id="2">[2]</a>
J.K. Tuli,
*"Evaluated Nuclear Structure Data File"*, BNL-NCS-51655-01/02-Rev (2001);
https://www.nndc.bnl.gov/ensdf/

<a id="3">[3]</a>
R. Capote *et al*.,
*"RIPL - Reference Input Parameter Library for Calculation of Nuclear Reactions and Nuclear Data Evaluations"*,
Nucl. Data Sheets **110**, 3107 (2009).

<a id="4">[4]</a>
T. Kibedi, T.W. Burrows, M.B. Trzhaskovskaya, P.M. Davidson, C.W. Nestor Jr.,
*Evaluation of theoretical conversion coefficients using BrIcc*,
Nucl. Instrum. Methods Phys. Res. Sect. A **589**, 202 (2008).

<a id="5">[5]</a>
R.B. Firestone, V.S. Shirley, C.M. Baglin, S.Y.F. Chu, J. Zipkin,
*"Table of Isotopes"*,
8th Ed. John Wiley and Sons, Inc., New York, Vols. 1 and 2 (1996).
