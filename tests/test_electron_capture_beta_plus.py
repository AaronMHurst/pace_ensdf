import pytest
import unittest
import numpy as np
import pandas as pd
from collections.abc import Iterable

import paceENSDF as pe
e = pe.ENSDF()
edata = e.load_ensdf()

class GetLogFTTests(unittest.TestCase):

    __doc__="""Unit tests for the `get_logft` method of the the BetaMinus 
    class.  This class contains an identical set of testing methods to those  
    in the `test_beta_minus` module, other than passing the string 'ECBP' to 
    the methods to define the appropriate decay mode."""

    def test_get_logft_returns_list_for_all_ecbp_emitters(self):
        ecbp_pairs = e.ensdf_pairs(edata,"ECBP")
        for parent, daughter in ecbp_pairs.items():
            ecbp = e.get_logft(edata, parent[0], parent[3], mode="ECBP")
            try:
                self.assertIsInstance(ecbp, list)
                self.assertIsInstance(ecbp, Iterable)
            except AssertionError:
                self.assertIsNone(ecbp)

    def test_get_logft_returns_none_if_not_ecbp_emitter(self):
        ecbp = e.get_logft(edata,"Se70",1,mode="ECBP")
        self.assertIsNone(ecbp)
        ecbp = e.get_logft(edata,"Cs119",1,mode="ECBP")
        self.assertIsNone(ecbp)

    def test_get_logft_returns_none_if_illegal_string(self):
        ecbp = e.get_logft(edata,"Y86",0,mode="THisIsB@LL@CK$")
        self.assertIsNone(ecbp)
        ecbp = e.get_logft(edata,"THisIsB@LL@CK$",0,mode="ECBP")
        self.assertIsNone(ecbp)

    def test_get_logft_raises_TypeError_if_first_arg_not_list(self):
        with self.assertRaises(TypeError):
            ecbp = e.get_logft("Y86",edata,0,mode="ECBP")

    def test_get_logft_raises_NameError_if_wrong_list(self):
        with self.assertRaises(NameError):
            ecbp = e.get_logft(XXXedataXXX,"Y86",0,mode="ECBP")

    def test_get_logft_raises_KeyError_if_bad_dict_items_in_list(self):
        bad_dict_items_in_list = [{'a':0, 'b':1, 'c':2}]
        with self.assertRaises(KeyError):
           ecbp = e.get_logft(bad_dict_items_in_list,"Y86",0,mode="ECBP")

    def test_get_logft_returned_contents_of_list(self):
        ecbp_pairs = e.ensdf_pairs(edata,"ECBP")
        for parent_key, daughter_value in ecbp_pairs.items():
            ecbp = e.get_logft(edata, str(parent_key[0]), int(parent_key[3]), mode="ECBP")
            try:
                for ecbp_value in ecbp:
                    self.assertIsInstance(ecbp_value, list)
                    self.assertIsInstance(ecbp_value, Iterable)
                    self.assertEqual(len(ecbp_value), 9)

                    # Unpack the list contents
                    self.assertIsInstance(ecbp_value[0], int)
                    try:
                        self.assertIsInstance(ecbp_value[1], float)
                    except AssertionError:
                        # Handle levels of the type '0+X' etc.
                        self.assertIsInstance(ecbp_value[1], str)
                    self.assertIsInstance(ecbp_value[2], int)
                    try:
                        self.assertIsInstance(ecbp_value[3], float)
                    except AssertionError:
                        if ecbp_value[4] == -1:
                            self.assertIsNone(ecbp_value[3])
                    self.assertIsInstance(ecbp_value[4], int)
                    self.assertIsInstance(ecbp_value[5], int)
                    self.assertIsInstance(ecbp_value[6], int)
                    try:
                        self.assertIsInstance(ecbp_value[7], float)
                    except AssertionError:
                        self.assertIsNone(ecbp_value[7])
                    try:
                        self.assertIsInstance(ecbp_value[8], float)
                    except AssertionError:
                        self.assertIsNone(ecbp_value[8])
                        
            except TypeError:
                self.assertIsNone(ecbp)


class FindForbiddenTests(unittest.TestCase):

    __doc__="""Unit tests for the `find_forbidden` method of the the BetaMinus 
    class.  This class contains an identical set of testing methods to those  
    in the `test_beta_minus` module, other than passing the string 'ECBP' to 
    the methods to define the appropriate decay mode."""

    #Test parent-decay forbiddenness
    classification = ['0A','1F','1UF','2F','2UF','3F','3UF','4F','4UF','5F','5UF']

    def test_find_forbidden_returns_dictionary_for_all_ecbp_emitters(self):
        # Test all forbiddenness classifications for beta-minus decay
        ecbp = e.find_forbidden(edata, "0A", mode="ECBP")
        try:
            self.assertIsInstance(ecbp, dict)
            self.assertIsInstance(ecbp, Iterable)
        except AssertionError:
            self.assertIsNone(ecbp)
        ecbp = e.find_forbidden(edata, "1F", mode="ECBP")
        try:
            self.assertIsInstance(ecbp, dict)
            self.assertIsInstance(ecbp, Iterable)
        except AssertionError:
            self.assertIsNone(ecbp)
        ecbp = e.find_forbidden(edata, "1UF", mode="ECBP")
        try:
            self.assertIsInstance(ecbp, dict)
            self.assertIsInstance(ecbp, Iterable)
        except AssertionError:
            self.assertIsNone(ecbp)
        ecbp = e.find_forbidden(edata, "2F", mode="ECBP")
        try:
            self.assertIsInstance(ecbp, dict)
            self.assertIsInstance(ecbp, Iterable)
        except AssertionError:
            self.assertIsNone(ecbp)
        ecbp = e.find_forbidden(edata, "2UF", mode="ECBP")
        try:
            self.assertIsInstance(ecbp, dict)
            self.assertIsInstance(ecbp, Iterable)
        except AssertionError:
            self.assertIsNone(ecbp)
        ecbp = e.find_forbidden(edata, "3F", mode="ECBP")
        try:
            self.assertIsInstance(ecbp, dict)
            self.assertIsInstance(ecbp, Iterable)
        except AssertionError:
            self.assertIsNone(ecbp)                
        ecbp = e.find_forbidden(edata, "3UF", mode="ECBP")
        try:
            self.assertIsInstance(ecbp, dict)
            self.assertIsInstance(ecbp, Iterable)
        except AssertionError:
            self.assertIsNone(ecbp)
        ecbp = e.find_forbidden(edata, "4F", mode="ECBP")
        try:
            self.assertIsInstance(ecbp, dict)
            self.assertIsInstance(ecbp, Iterable)
        except AssertionError:
            self.assertIsNone(ecbp)
        ecbp = e.find_forbidden(edata, "4UF", mode="ECBP")
        try:
            self.assertIsInstance(ecbp, dict)
            self.assertIsInstance(ecbp, Iterable)
        except AssertionError:
            self.assertIsNone(ecbp)
        ecbp = e.find_forbidden(edata, "5F", mode="ECBP")
        try:
            self.assertIsInstance(ecbp, dict)
            self.assertIsInstance(ecbp, Iterable)
        except AssertionError:
            self.assertIsNone(ecbp)
        ecbp = e.find_forbidden(edata, "5UF", mode="ECBP")
        try:
            self.assertIsInstance(ecbp, dict)
            self.assertIsInstance(ecbp, Iterable)
        except AssertionError:
            self.assertIsNone(ecbp)                

        #Test parent-decay forbiddenness
        classification = ['0A','1F','1UF','2F','2UF','3F','3UF','4F','4UF','5F','5UF']
        ecbp_pairs = e.ensdf_pairs(edata,"ECBP")
        for parent, daughter in ecbp_pairs.items():
            for forbidden in classification:
                ecbp = e.find_forbidden(edata, str(parent[0]), int(parent[3]), str(forbidden), mode="ECBP")
                try:
                    self.assertIsInstance(ecbp, dict)
                    self.assertIsInstance(ecbp, Iterable)
                except AssertionError:
                    self.assertIsNone(ecbp)

    def test_find_forbidden_returns_none_if_not_ecbp_emitter(self):
        for forbidden in FindForbiddenTests.classification:
            ecbp = e.find_forbidden(edata,"Se70",1,forbidden,mode="ECBP")
            self.assertIsNone(ecbp)

    def test_find_forbidden_returns_none_if_illegal_string(self):
        for forbidden in FindForbiddenTests.classification:
            ecbp = e.find_forbidden(edata,"Y86",0,forbidden,mode="THisIsB@LL@CK$")
            self.assertIsNone

    def test_find_forbidden_returns_dict_or_none_depending_on_forbiddenness(self):
        ecbp_pairs = e.ensdf_pairs(edata,"ECBP")
        for parent, daughter in ecbp_pairs.items():
            for forbidden in FindForbiddenTests.classification:
                ecbp = e.find_forbidden(edata, str(parent[0]), int(parent[3]), str(forbidden), mode="ECBP")
            try:
                self.assertIsInstance(ecbp, dict)
                self.assertIsInstance(ecbp, Iterable)
            except AssertionError:
                self.assertIsNone(ecbp)

    def test_find_forbidden_raises_TypeError_if_first_arg_not_list(self):
        with self.assertRaises(TypeError):
            for forbidden in FindForbiddenTests.classification:
                ecbp = e.find_forbidden("Y86",edata,0,forbidden,mode="ECBP")

    def test_find_forbidden_raises_NameError_if_wrong_list(self):
        with self.assertRaises(NameError):
            for forbidden in FindForbiddenTests.classification:
                ecbp = e.find_forbidden(XXXedataXXX,"Y86",0,forbidden,mode="ECBP")

    def test_find_forbidden_raises_KeyError_if_bad_dict_items_in_list(self):
        bad_dict_items_in_list = [{'a':0, 'b':1, 'c':2}]
        with self.assertRaises(KeyError):
            for forbidden in FindForbiddenTests.classification:
                ecbp = e.find_forbidden(bad_dict_items_in_list,"Y86",0,forbidden,mode="ECBP")

    def test_find_forbidden_returned_contents_of_list(self):
        ecbp_pairs = e.ensdf_pairs(edata,"ECBP")
        # Search over all parents
        for parent_key, daughter_value in ecbp_pairs.items():
            for forbidden in FindForbiddenTests.classification:
                ecbp = e.find_forbidden(edata, str(parent_key[0]), int(parent_key[3]), str(forbidden), mode="ECBP")
                try:
                    for ecbp_key, ecbp_value in ecbp.items():
                        self.assertIsInstance(ecbp_key, tuple)
                        self.assertIsInstance(ecbp_key, Iterable)
                        self.assertIsInstance(ecbp_value, list)
                        self.assertIsInstance(ecbp_value, Iterable)

                        # Unpack the key contents
                        self.assertIsInstance(ecbp_key[0], str)
                        self.assertIsInstance(ecbp_key[1], int)
                        self.assertIsInstance(ecbp_key[2], int)
                        self.assertIsInstance(ecbp_key[3], int)
                        try:
                            self.assertIsInstance(ecbp_key[4], float)
                        except AssertionError:
                            self.assertIsInstance(ecbp_key[4], str)
                        try:
                            self.assertIsInstance(ecbp_key[5], float)
                        except AssertionError:
                            if ecbp_key[6] == -1:
                                self.assertIsNone(ecbp_key[5])
                        self.assertIsInstance(ecbp_key[6], int)
                        self.assertIsInstance(ecbp_key[7], int)
                        self.assertIsInstance(ecbp_key[8], int)
                        self.assertIsInstance(ecbp_key[9], str)
                        self.assertIsInstance(ecbp_key[10], int)
                        self.assertIsInstance(ecbp_key[11], int)
                        
                        # Unpack the value contents
                        for value in ecbp_value:
                            self.assertIsInstance(value[0], int)
                            try:
                                self.assertIsInstance(value[1], float)
                            except AssertionError:
                                self.assertIsInstance(value[1], str)
                            self.assertIsInstance(value[2], int)
                            try:
                                self.assertIsInstance(value[3], float)
                            except AssertionError:
                                if value[4] == -1:
                                    self.assertIsNone(value[3])
                            self.assertIsInstance(value[4], int)
                            self.assertIsInstance(value[5], int)
                            self.assertIsInstance(value[6], int)
                            try:
                                self.assertIsInstance(value[7], float)
                            except AssertionError:
                                self.assertIsNone(value[7])
                            try:
                                self.assertIsInstance(value[8], float)
                            except AssertionError:
                                self.assertIsNone(value[8])
                            self.assertIsInstance(value[9], str)
                            self.assertIsInstance(value[10], str)
                            self.assertIsInstance(value[11], int)
                            self.assertIsInstance(value[12], int)
                            self.assertIsInstance(value[13], int)
                            

                except TypeError:
                    self.assertIsNone(ecbp)

        # Search over all forbidenness
        for forbidden in FindForbiddenTests.classification:
            ecbp = e.find_forbidden(edata, str(forbidden), mode="ECBP")
            try:
                for ecbp_key, ecbp_value in ecbp.items():
                    self.assertIsInstance(ecbp_key, tuple)
                    self.assertIsInstance(ecbp_key, Iterable)
                    self.assertIsInstance(ecbp_value, list)
                    self.assertIsInstance(ecbp_value, Iterable)

                    # Unpack the key contents
                    self.assertIsInstance(ecbp_key[0], str)
                    self.assertIsInstance(ecbp_key[1], int)
                    self.assertIsInstance(ecbp_key[2], int)
                    self.assertIsInstance(ecbp_key[3], int)
                    try:
                        self.assertIsInstance(ecbp_key[4], float)
                    except AssertionError:
                        self.assertIsInstance(ecbp_key[4], str)
                    try:
                        self.assertIsInstance(ecbp_key[5], float)
                    except AssertionError:
                        if ecbp_key[6] == -1:
                            self.assertIsNone(ecbp_key[5])
                    self.assertIsInstance(ecbp_key[6], int)
                    self.assertIsInstance(ecbp_key[7], int)
                    self.assertIsInstance(ecbp_key[8], int)
                    self.assertIsInstance(ecbp_key[9], str)
                    self.assertIsInstance(ecbp_key[10], int)
                    self.assertIsInstance(ecbp_key[11], int)

                    # Unpack the value contents
                    try:
                        for value in ecbp_value:
                            self.assertIsInstance(value[0], int)
                            try:
                                self.assertIsInstance(value[1], float)
                            except AssertionError:
                                self.assertIsInstance(value[1], str)
                            self.assertIsInstance(value[2], int)
                            try:
                                self.assertIsInstance(value[3], float)
                            except AssertionError:
                                if value[4] == -1:
                                    self.assertIsNone(value[3])
                            self.assertIsInstance(value[4], int)
                            self.assertIsInstance(value[5], int)
                            self.assertIsInstance(value[6], int)
                            try:
                                self.assertIsInstance(value[7], float)
                            except AssertionError:
                                self.assertIsNone(value[7])
                            try:
                                self.assertIsInstance(value[8], float)
                            except AssertionError:
                                self.assertIsNone(value[8])
                            self.assertIsInstance(value[9], str)
                            self.assertIsInstance(value[10], str)
                            self.assertIsInstance(value[11], int)
                            self.assertIsInstance(value[12], int)
                            self.assertIsInstance(value[13], int)
                            
                    except AssertionError:
                        self.assertIsNone(ecbp_value)
                        
            except AttributeError:
                self.assertIsNone(ecbp)                

                
class GetElectronCaptureBetaPlus(unittest.TestCase):

    __doc__="""Unit tests for the `get_ecbp` method of the 
    ElectronCaptureBetaPlus class."""

    def test_get_ecbp_returns_dict_for_all_ecbp_emitters(self):
        ecbp_pairs = e.ensdf_pairs(edata,"ECBP")
        for parent, daughter in ecbp_pairs.items():
            ecbp = e.get_ecbp(edata, parent[0], parent[3], units="best")
            try:
                self.assertIsInstance(ecbp, dict)
                self.assertIsInstance(ecbp, Iterable)
            except AssertionError:
                self.assertIsNone(ecbp)
            ecbp = e.get_ecbp(edata, parent[0], parent[3], units="seconds")
            try:
                self.assertIsInstance(ecbp, dict)
                self.assertIsInstance(ecbp, Iterable)
            except AssertionError:
                self.assertIsNone(ecbp)

    def test_get_ecbp_returns_none_if_not_ecbp_emitter(self):
        ecbp = e.get_ecbp(edata,"Fe68",0,units="seconds")
        self.assertIsNone(ecbp)
        ecbp = e.get_ecbp(edata,"Co70",1,units="best")
        self.assertIsNone(ecbp)

    def test_get_ecbp_returns_none_if_illegal_string(self):
        ecbp = e.get_ecbp(edata,"Na22",0,units="THisIsB@LL@CK$")
        self.assertIsNone(ecbp)
        ecbp = e.get_ecbp(edata,"THisIsB@LL@CK$",0,units="best")
        self.assertIsNone(ecbp)

    def test_get_ecbp_raises_TypeError_if_first_arg_not_list(self):
        with self.assertRaises(TypeError):
            ecbp = e.get_ecbp("Na22",edata,0,units="best")

    def test_get_ecbp_raises_NameError_if_wrong_list(self):
        with self.assertRaises(NameError):
            ecbp = e.get_ecbp(XXXedataXXX,"Na22",0,units="best")

    def test_get_ecbp_raises_KeyError_if_bad_dict_items_in_list(self):
        bad_dict_items_in_list = [{'a':0, 'b':1, 'c':2}]
        with self.assertRaises(KeyError):
           ecbp = e.get_ecbp(bad_dict_items_in_list,"Na22",0,units="best")

    def test_get_ecbp_returned_contents_of_dict(self):
        ecbp_pairs = e.ensdf_pairs(edata,"ECBP")
        for parent_key, daughter_value in ecbp_pairs.items():
            ecbp = e.get_ecbp(edata, parent_key[0], parent_key[3], units="best")
            try:
                for ecbp_key, ecbp_value in ecbp.items():
                    self.assertIsInstance(ecbp_key, tuple)
                    self.assertIsInstance(ecbp_key, Iterable)
                    self.assertEqual(len(ecbp_key), 15)

                    # Unpack the key contents
                    self.assertIsInstance(ecbp_key[0], str)
                    self.assertIsInstance(ecbp_key[1], int)
                    self.assertIsInstance(ecbp_key[2], int)
                    self.assertIsInstance(ecbp_key[3], str)
                    self.assertIsInstance(ecbp_key[4], int)
                    self.assertIsInstance(ecbp_key[5], int)
                    try:
                        self.assertIsInstance(ecbp_key[6], float)
                        self.assertIsInstance(ecbp_key[7], float)
                    except AssertionError:
                        # Strings of the type '(0+X)' etc.
                        try:
                            self.assertIsInstance(ecbp_key[6], str)
                            self.assertIsInstance(ecbp_key[7], int)
                        except AssertionError:
                            # Sometimes it's an <int> or a <float>
                            try:
                                self.assertIsInstance(ecbp_key[7], float)
                            except AssertionError:
                                # Sometimes it's a <str>, e.g., 'AP'
                                self.assertIsInstance(ecbp_key[7], str)
                    try:
                        self.assertIsInstance(ecbp_key[8], float)
                        self.assertIsInstance(ecbp_key[9], int)
                    except AssertionError:
                        # Null JPi
                        if ecbp_key[9] == -1:
                            self.assertIsNone(ecbp_key[8])
                            self.assertIsInstance(ecbp_key[9], int)
                    self.assertIsInstance(ecbp_key[10], int)
                    self.assertIsInstance(ecbp_key[11], int)
                    try:
                        self.assertIsInstance(ecbp_key[12], float)
                        self.assertIsInstance(ecbp_key[13], float)
                        self.assertIsInstance(ecbp_key[14], str)
                    except AssertionError:
                        # Null T1/2
                        self.assertIsNone(ecbp_key[12])
                        self.assertIsNone(ecbp_key[13])
                        self.assertIsNone(ecbp_key[14])

                    # Unpack the value contents
                    self.assertIsInstance(ecbp_value, list)
                    self.assertIsInstance(ecbp_value, Iterable)
                    for v in ecbp_value:
                        self.assertEqual(len(v), 24)

                        self.assertIsInstance(v[0], int)
                        try:
                            self.assertIsInstance(v[1], float)
                        except AssertionError:
                            # Level energies of the type '0+X' etc
                            self.assertIsInstance(v[1], str)
                        self.assertIsInstance(v[2], int)
                        try:
                            self.assertIsInstance(v[3], float)
                        except AssertionError:
                            # Null JPi
                            if v[4] == -1:
                                self.assertIsNone(v[3])
                                
                        self.assertIsInstance(v[4], int)
                        self.assertIsInstance(v[5], int)
                        self.assertIsInstance(v[6], int)

                        try:
                            self.assertIsInstance(v[7], float)
                        except AssertionError:
                            self.assertIsNone(v[7])
                        try:
                            self.assertIsInstance(v[8], float)
                        except AssertionError:
                            self.assertIsNone(v[8])

                        try:
                            self.assertIsInstance(v[9], float)
                        except AssertionError:
                            self.assertIsNone(v[9])
                        try:
                            self.assertIsInstance(v[10], float)
                        except AssertionError:
                            self.assertIsNone(v[10])

                        try:
                            self.assertIsInstance(v[11], float)
                        except AssertionError:
                            self.assertIsNone(v[11])
                        try:
                            self.assertIsInstance(v[12], float)
                        except AssertionError:
                            self.assertIsNone(v[12])

                        try:
                            self.assertIsInstance(v[13], float)
                        except AssertionError:
                            self.assertIsNone(v[13])
                        try:
                            self.assertIsInstance(v[14], float)
                        except AssertionError:
                            self.assertIsNone(v[14])

                        try:
                            self.assertIsInstance(v[15], float)
                        except AssertionError:
                            self.assertIsNone(v[15])
                        try:
                            self.assertIsInstance(v[16], float)
                        except AssertionError:
                            self.assertIsNone(v[16])

                        try:
                            self.assertIsInstance(v[17], float)
                        except AssertionError:
                            self.assertIsNone(v[17])
                        try:
                            self.assertIsInstance(v[18], float)
                        except AssertionError:
                            self.assertIsNone(v[18])

                        try:
                            self.assertIsInstance(v[19], float)
                        except AssertionError:
                            self.assertIsNone(v[19])
                        try:
                            self.assertIsInstance(v[20], float)
                        except AssertionError:
                            self.assertIsNone(v[20])

                        try:
                            self.assertIsInstance(v[21], str)
                        except AssertionError:
                            self.assertIsNone(v[21])
                        try:
                            self.assertIsInstance(v[22], str)
                        except AssertionError:
                            self.assertIsNone(v[22])
                        try:
                            self.assertIsInstance(v[23], int)
                        except AssertionError:
                            self.assertIsNone(v[23])
                        
            except AttributeError:
                self.assertIsNone(ecbp)

        

class GetElectronCaptureFractions(unittest.TestCase):

    __doc__="""Unit tests for the `get_ec_fractions` method of the 
    ElectronCaptureBetaPlus class."""

    def test_get_ec_fractions_returns_list_for_all_ecbp_emitters(self):
        ecbp_pairs = e.ensdf_pairs(edata,"ECBP")
        for parent, daughter in ecbp_pairs.items():
            ec_fractions = e.get_ec_fractions(edata, parent[0], parent[3], subshell="calc")
            try:
                self.assertIsInstance(ec_fractions, list)
                self.assertIsInstance(ec_fractions, Iterable)
            except AssertionError:
                self.assertIsNone(ec_fractions)
            ec_fractions = e.get_ec_fractions(edata, parent[0], parent[3], subshell="sumcalc")
            try:
                self.assertIsInstance(ec_fractions, list)
                self.assertIsInstance(ec_fractions, Iterable)
            except AssertionError:
                self.assertIsNone(ec_fractions)
            ec_fractions = e.get_ec_fractions(edata, parent[0], parent[3], subshell="expt")
            try:
                self.assertIsInstance(ec_fractions, list)
                self.assertIsInstance(ec_fractions, Iterable)
            except AssertionError:
                self.assertIsNone(ec_fractions)

    def test_get_ec_fractions_returns_none_if_not_ec_fractions(self):
        ec_fractions = e.get_ec_fractions(edata,"Fe68",0,subshell="calc")
        self.assertIsNone(ec_fractions)
        ec_fractions = e.get_ec_fractions(edata,"Co70",0,subshell="sumcalc")
        self.assertIsNone(ec_fractions)
        ec_fractions = e.get_ec_fractions(edata,"Co70",0,subshell="expt")
        self.assertIsNone(ec_fractions)

    def test_get_ec_fractions_returns_none_if_illegal_string(self):
        ec_fractions = e.get_ec_fractions(edata,"Na22",0,subshell="THisIsB@LL@CK$")
        self.assertIsNone(ec_fractions)
        ec_fractions = e.get_ec_fractions(edata,"THisIsB@LL@CK$",0,subshell="calc")
        self.assertIsNone(ec_fractions)

    def test_get_ec_fractions_raises_TypeError_if_first_arg_not_list(self):
        with self.assertRaises(TypeError):
            ec_fractions = e.get_ec_fractions("Na22",edata,0,subshell="calc")

    def test_get_ec_fractions_raises_NameError_if_wrong_list(self):
        with self.assertRaises(NameError):
            ec_fractions = e.get_ec_fractions(XXXedataXXX,"Na22",0,subshell="calc")

    def test_get_ec_fractions_raises_KeyError_if_bad_dict_items_in_list(self):
        bad_dict_items_in_list = [{'a':0, 'b':1, 'c':2}]
        with self.assertRaises(KeyError):
           ec_fractions = e.get_ec_fractions(bad_dict_items_in_list,"Na22",0,subshell="calc")


    def test_get_ec_fractions_returned_contents_of_list(self):
        ecbp_pairs = e.ensdf_pairs(edata,"ECBP")
        for parent_key, daughter_value in ecbp_pairs.items():
            # 'calc' subshell contributions
            ec_fractions = e.get_ec_fractions(edata, parent_key[0], parent_key[3], subshell="calc")
            try:
                self.assertIsInstance(ec_fractions, list)
                self.assertIsInstance(ec_fractions, Iterable)
                for ecbp_value in ec_fractions:
                    self.assertEqual(len(ecbp_value), 16)

                    # Unpack the key contents
                    self.assertIsInstance(ecbp_value[0], int)
                    try:
                        self.assertIsInstance(ecbp_value[1], float)
                    except AssertionError:
                        self.assertIsInstance(ecbp_value[1], str)
                    except AssertionError:
                        self.assertIsNone(ecbp_value[1])

                    try:
                        self.assertIsInstance(ecbp_value[2], float)
                    except AssertionError:
                        self.assertIsNone(ecbp_value[2])
                    try:
                        self.assertIsInstance(ecbp_value[3], float)
                    except AssertionError:
                        self.assertIsNone(ecbp_value[3])
                    try:
                        self.assertIsInstance(ecbp_value[4], float)
                    except AssertionError:
                        self.assertIsNone(ecbp_value[4])
                    try:
                        self.assertIsInstance(ecbp_value[5], float)
                    except AssertionError:
                        self.assertIsNone(ecbp_value[5])
                    try:
                        self.assertIsInstance(ecbp_value[6], float)
                    except AssertionError:
                        self.assertIsNone(ecbp_value[6])
                    try:
                        self.assertIsInstance(ecbp_value[7], float)
                    except AssertionError:
                        self.assertIsNone(ecbp_value[7])
                    try:
                        self.assertIsInstance(ecbp_value[8], float)
                    except AssertionError:
                        self.assertIsNone(ecbp_value[8])
                    try:
                        self.assertIsInstance(ecbp_value[9], float)
                    except AssertionError:
                        self.assertIsNone(ecbp_value[9])
                    try:
                        self.assertIsInstance(ecbp_value[10], float)
                    except AssertionError:
                        self.assertIsNone(ecbp_value[10])
                    try:
                        self.assertIsInstance(ecbp_value[11], float)
                    except AssertionError:
                        self.assertIsNone(ecbp_value[11])
                    try:
                        self.assertIsInstance(ecbp_value[12], float)
                    except AssertionError:
                        self.assertIsNone(ecbp_value[12])
                    try:
                        self.assertIsInstance(ecbp_value[13], float)
                    except AssertionError:
                        self.assertIsNone(ecbp_value[13])
                    try:
                        self.assertIsInstance(ecbp_value[14], float)
                    except AssertionError:
                        self.assertIsNone(ecbp_value[14])
                    try:
                        self.assertIsInstance(ecbp_value[15], float)
                    except AssertionError:
                        self.assertIsNone(ecbp_value[15])

            except AssertionError:
                self.assertIsNone(ec_fractions)

            # 'sumcalc' subshell contributions
            ec_fractions = e.get_ec_fractions(edata, parent_key[0], parent_key[3], subshell="sumcalc")
            try:
                self.assertIsInstance(ec_fractions, list)
                self.assertIsInstance(ec_fractions, Iterable)
                for ecbp_value in ec_fractions:
                    self.assertEqual(len(ecbp_value), 14)

                    # Unpack the key contents
                    self.assertIsInstance(ecbp_value[0], int)
                    try:
                        self.assertIsInstance(ecbp_value[1], float)
                    except AssertionError:
                        self.assertIsInstance(ecbp_value[1], str)
                    except AssertionError:
                        self.assertIsNone(ecbp_value[1])

                    try:
                        self.assertIsInstance(ecbp_value[2], float)
                    except AssertionError:
                        self.assertIsNone(ecbp_value[2])
                    try:
                        self.assertIsInstance(ecbp_value[3], float)
                    except AssertionError:
                        self.assertIsNone(ecbp_value[3])
                    try:
                        self.assertIsInstance(ecbp_value[4], float)
                    except AssertionError:
                        self.assertIsNone(ecbp_value[4])
                    try:
                        self.assertIsInstance(ecbp_value[5], float)
                    except AssertionError:
                        self.assertIsNone(ecbp_value[5])
                    try:
                        self.assertIsInstance(ecbp_value[6], float)
                    except AssertionError:
                        self.assertIsNone(ecbp_value[6])
                    try:
                        self.assertIsInstance(ecbp_value[7], float)
                    except AssertionError:
                        self.assertIsNone(ecbp_value[7])
                    try:
                        self.assertIsInstance(ecbp_value[8], float)
                    except AssertionError:
                        self.assertIsNone(ecbp_value[8])
                    try:
                        self.assertIsInstance(ecbp_value[9], float)
                    except AssertionError:
                        self.assertIsNone(ecbp_value[9])
                    try:
                        self.assertIsInstance(ecbp_value[10], float)
                    except AssertionError:
                        self.assertIsNone(ecbp_value[10])
                    try:
                        self.assertIsInstance(ecbp_value[11], float)
                    except AssertionError:
                        self.assertIsNone(ecbp_value[11])
                    try:
                        self.assertIsInstance(ecbp_value[12], float)
                    except AssertionError:
                        self.assertIsNone(ecbp_value[12])
                    try:
                        self.assertIsInstance(ecbp_value[13], float)
                    except AssertionError:
                        self.assertIsNone(ecbp_value[13])

            except AssertionError:
                self.assertIsNone(ec_fractions)

            # 'expt' subshell contributions
            ec_fractions = e.get_ec_fractions(edata, parent_key[0], parent_key[3], subshell="expt")
            try:
                self.assertIsInstance(ec_fractions, list)
                self.assertIsInstance(ec_fractions, Iterable)
                for ecbp_value in ec_fractions:
                    self.assertEqual(len(ecbp_value), 10)

                    # Unpack the key contents
                    self.assertIsInstance(ecbp_value[0], int)
                    try:
                        self.assertIsInstance(ecbp_value[1], float)
                    except AssertionError:
                        self.assertIsInstance(ecbp_value[1], str)
                    except AssertionError:
                        self.assertIsNone(ecbp_value[1])

                    try:
                        self.assertIsInstance(ecbp_value[2], float)
                    except AssertionError:
                        self.assertIsNone(ecbp_value[2])
                    try:
                        self.assertIsInstance(ecbp_value[3], float)
                    except AssertionError:
                        self.assertIsNone(ecbp_value[3])
                    try:
                        self.assertIsInstance(ecbp_value[4], float)
                    except AssertionError:
                        self.assertIsNone(ecbp_value[4])
                    try:
                        self.assertIsInstance(ecbp_value[5], float)
                    except AssertionError:
                        self.assertIsNone(ecbp_value[5])
                    try:
                        self.assertIsInstance(ecbp_value[6], float)
                    except AssertionError:
                        self.assertIsNone(ecbp_value[6])
                    try:
                        self.assertIsInstance(ecbp_value[7], float)
                    except AssertionError:
                        self.assertIsNone(ecbp_value[7])
                    try:
                        self.assertIsInstance(ecbp_value[8], float)
                    except AssertionError:
                        self.assertIsNone(ecbp_value[8])
                    try:
                        self.assertIsInstance(ecbp_value[9], float)
                    except AssertionError:
                        self.assertIsNone(ecbp_value[9])

            except AssertionError:
                self.assertIsNone(ec_fractions)
