import pytest
import unittest
import numpy as np
import pandas as pd
from collections.abc import Iterable

import paceENSDF as pe
e = pe.ENSDF()
edata = e.load_ensdf()

class GetBetaMinusTests(unittest.TestCase):

    __doc__="""Unit tests for the `get_beta_minus` method of the the BetaMinus 
    class."""

    def test_get_beta_minus_returns_dictionary_for_all_beta_minus_emitters(self):
        bm_pairs = e.ensdf_pairs(edata,"BM")
        for parent, daughter in bm_pairs.items():
            bm = e.get_beta_minus(edata, parent[0], parent[3], units="best")
            try:
                self.assertIsInstance(bm, dict)
                self.assertIsInstance(bm, Iterable)
            except AssertionError:
                self.assertIsNone(bm)

    def test_get_beta_minus_returns_none_if_not_beta_minus_emitter(self):
        bm = e.get_beta_minus(edata,"Se70",1,units="seconds")
        self.assertIsNone(bm)
        bm = e.get_beta_minus(edata,"Cs119",1,units="best")
        self.assertIsNone(bm)

    def test_get_beta_minus_returns_none_if_illegal_string(self):
        bm = e.get_beta_minus(edata,"Co60",0,units="THisIsB@LL@CK$")
        self.assertIsNone(bm)
        bm = e.get_beta_minus(edata,"THisIsB@LL@CK$",0,units="best")
        self.assertIsNone(bm)

    def test_get_beta_minus_raises_TypeError_if_first_arg_not_list(self):
        with self.assertRaises(TypeError):
            bm = e.get_beta_minus("Co60",edata,0,units="best")

    def test_get_beta_minus_raises_NameError_if_wrong_list(self):
        with self.assertRaises(NameError):
            bm = e.get_beta_minus(XXXedataXXX,"Co60",0,units="best")

    def test_get_beta_minus_raises_KeyError_if_bad_dict_items_in_list(self):
        bad_dict_items_in_list = [{'a':0, 'b':1, 'c':2}]
        with self.assertRaises(KeyError):
           bm = e.get_beta_minus(bad_dict_items_in_list,"Co60",0,units="best")

    def test_get_beta_minus_returned_contents_of_dict(self):
        bm_pairs = e.ensdf_pairs(edata,"BM")
        for parent_key, daughter_value in bm_pairs.items():
            bm = e.get_beta_minus(edata, parent_key[0], parent_key[3], units="best")
            try:
                for bm_key, bm_value in bm.items():
                    self.assertIsInstance(bm_key, tuple)
                    self.assertIsInstance(bm_key, Iterable)
                    self.assertEqual(len(bm_key), 15)

                    # Unpack the key contents
                    self.assertIsInstance(bm_key[0], str)
                    self.assertIsInstance(bm_key[1], int)
                    self.assertIsInstance(bm_key[2], int)
                    self.assertIsInstance(bm_key[3], str)
                    self.assertIsInstance(bm_key[4], int)
                    self.assertIsInstance(bm_key[5], int)
                    try:
                        self.assertIsInstance(bm_key[6], float)
                        self.assertIsInstance(bm_key[7], float)
                    except AssertionError:
                        # Strings of the type '(0+X)' etc.
                        try:
                            self.assertIsInstance(bm_key[6], str)
                            self.assertIsInstance(bm_key[7], int)
                        except AssertionError:
                            try:
                                self.assertIsInstance(bm_key[6], str)
                                # Sometimes it's an <int> or a <float>
                                self.assertIsInstance(bm_key[7], float)
                            except AssertionError:
                                self.assertIsInstance(bm_key[6], str)
                                # Associated strings may have `null`
                                # uncertainties in ENSDF archive: September 2023
                                self.assertIsNone(bm_key[7])
                                
                    try:
                        self.assertIsInstance(bm_key[8], float)
                        self.assertIsInstance(bm_key[9], int)
                    except AssertionError:
                        # Null JPi
                        if bm_key[9] == -1:
                            self.assertIsNone(bm_key[8])
                            self.assertIsInstance(bm_key[9], int)
                    self.assertIsInstance(bm_key[10], int)
                    self.assertIsInstance(bm_key[11], int)
                    try:
                        self.assertIsInstance(bm_key[12], float)
                        self.assertIsInstance(bm_key[13], float)
                        self.assertIsInstance(bm_key[14], str)
                    except AssertionError:
                        # Null T1/2
                        self.assertIsNone(bm_key[12])
                        self.assertIsNone(bm_key[13])
                        self.assertIsNone(bm_key[14])

                    # Unpack the value contents
                    self.assertIsInstance(bm_value, list)
                    self.assertIsInstance(bm_value, Iterable)
                    for v in bm_value:
                        self.assertEqual(len(v), 18)

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
                            self.assertIsInstance(v[15], str)
                        except AssertionError:
                            self.assertIsNone(v[15])
                        try:
                            self.assertIsInstance(v[16], str)
                        except AssertionError:
                            self.assertIsNone(v[16])

                        try:
                            self.assertIsInstance(v[17], int)
                        except AssertionError:
                            self.assertIsNone(v[17])
                            
                            
            except AttributeError:
                self.assertIsNone(bm)

                
class GetLogFTTests(unittest.TestCase):

    __doc__="""Unit tests for the `get_logft` method of the the BetaMinus 
    class."""

    def test_get_logft_returns_list_for_all_beta_minus_emitters(self):
        bm_pairs = e.ensdf_pairs(edata,"BM")
        for parent, daughter in bm_pairs.items():
            bm = e.get_logft(edata, parent[0], parent[3], mode="BM")
            try:
                self.assertIsInstance(bm, list)
                self.assertIsInstance(bm, Iterable)
            except AssertionError:
                self.assertIsNone(bm)

    def test_get_logft_returns_none_if_not_beta_minus_emitter(self):
        bm = e.get_logft(edata,"Se70",1,mode="BM")
        self.assertIsNone(bm)

    def test_get_logft_returns_none_if_illegal_string(self):
        bm = e.get_logft(edata,"Co60",0,mode="THisIsB@LL@CK$")
        self.assertIsNone(bm)
        bm = e.get_logft(edata,"THisIsB@LL@CK$",0,mode="BM")
        self.assertIsNone(bm)

    def test_get_logft_raises_TypeError_if_first_arg_not_list(self):
        with self.assertRaises(TypeError):
            bm = e.get_logft("Co60",edata,0,mode="BM")

    def test_get_logft_raises_NameError_if_wrong_list(self):
        with self.assertRaises(NameError):
            bm = e.get_logft(XXXedataXXX,"Co60",0,mode="BM")

    def test_get_logft_raises_KeyError_if_bad_dict_items_in_list(self):
        bad_dict_items_in_list = [{'a':0, 'b':1, 'c':2}]
        with self.assertRaises(KeyError):
            bm = e.get_logft(bad_dict_items_in_list,"Co60",0,mode="BM")

    def test_get_logft_returned_contents_of_list(self):
        bm_pairs = e.ensdf_pairs(edata,"BM")
        for parent_key, daughter_value in bm_pairs.items():
            bm = e.get_logft(edata, str(parent_key[0]), int(parent_key[3]), mode="BM")
            try:
                for bm_value in bm:
                    self.assertIsInstance(bm_value, list)
                    self.assertIsInstance(bm_value, Iterable)
                    self.assertEqual(len(bm_value), 9)

                    # Unpack the list contents
                    self.assertIsInstance(bm_value[0], int)
                    try:
                        self.assertIsInstance(bm_value[1], float)
                    except AssertionError:
                        # Handle levels of the type '0+X' etc.
                        self.assertIsInstance(bm_value[1], str)
                    self.assertIsInstance(bm_value[2], int)
                    try:
                        self.assertIsInstance(bm_value[3], float)
                    except AssertionError:
                        if bm_value[4] == -1:
                            self.assertIsNone(bm_value[3])
                    self.assertIsInstance(bm_value[4], int)
                    self.assertIsInstance(bm_value[5], int)
                    self.assertIsInstance(bm_value[6], int)
                    try:
                        self.assertIsInstance(bm_value[7], float)
                    except AssertionError:
                        self.assertIsNone(bm_value[7])
                    try:
                        self.assertIsInstance(bm_value[8], float)
                    except AssertionError:
                        self.assertIsNone(bm_value[8])
                        
            except TypeError:
                self.assertIsNone(bm)

class FindForbiddenTests(unittest.TestCase):

    __doc__="""Unit tests for the `find_forbidden` method of the the BetaMinus 
    class."""

    #Test parent-decay forbiddenness
    classification = ['0A','1F','1UF','2F','2UF','3F','3UF','4F','4UF','5F','5UF']

    def test_find_forbidden_returns_dictionary_for_all_beta_minus_emitters(self):
        # Test all forbiddenness classifications for beta-minus decay
        bm = e.find_forbidden(edata, "0A", mode="BM")
        try:
            self.assertIsInstance(bm, dict)
            self.assertIsInstance(bm, Iterable)
        except AssertionError:
            self.assertIsNone(bm)
        bm = e.find_forbidden(edata, "1F", mode="BM")
        try:
            self.assertIsInstance(bm, dict)
            self.assertIsInstance(bm, Iterable)
        except AssertionError:
            self.assertIsNone(bm)
        bm = e.find_forbidden(edata, "1UF", mode="BM")
        try:
            self.assertIsInstance(bm, dict)
            self.assertIsInstance(bm, Iterable)
        except AssertionError:
            self.assertIsNone(bm)
        bm = e.find_forbidden(edata, "2F", mode="BM")
        try:
            self.assertIsInstance(bm, dict)
            self.assertIsInstance(bm, Iterable)
        except AssertionError:
            self.assertIsNone(bm)
        bm = e.find_forbidden(edata, "2UF", mode="BM")
        try:
            self.assertIsInstance(bm, dict)
            self.assertIsInstance(bm, Iterable)
        except AssertionError:
            self.assertIsNone(bm)
        bm = e.find_forbidden(edata, "3F", mode="BM")
        try:
            self.assertIsInstance(bm, dict)
            self.assertIsInstance(bm, Iterable)
        except AssertionError:
            self.assertIsNone(bm)                
        bm = e.find_forbidden(edata, "3UF", mode="BM")
        try:
            self.assertIsInstance(bm, dict)
            self.assertIsInstance(bm, Iterable)
        except AssertionError:
            self.assertIsNone(bm)
        bm = e.find_forbidden(edata, "4F", mode="BM")
        try:
            self.assertIsInstance(bm, dict)
            self.assertIsInstance(bm, Iterable)
        except AssertionError:
            self.assertIsNone(bm)
        bm = e.find_forbidden(edata, "4UF", mode="BM")
        try:
            self.assertIsInstance(bm, dict)
            self.assertIsInstance(bm, Iterable)
        except AssertionError:
            self.assertIsNone(bm)
        bm = e.find_forbidden(edata, "5F", mode="BM")
        try:
            self.assertIsInstance(bm, dict)
            self.assertIsInstance(bm, Iterable)
        except AssertionError:
            self.assertIsNone(bm)
        bm = e.find_forbidden(edata, "5UF", mode="BM")
        try:
            self.assertIsInstance(bm, dict)
            self.assertIsInstance(bm, Iterable)
        except AssertionError:
            self.assertIsNone(bm)                

        #Test parent-decay forbiddenness
        classification = ['0A','1F','1UF','2F','2UF','3F','3UF','4F','4UF','5F','5UF']
        bm_pairs = e.ensdf_pairs(edata,"BM")
        for parent, daughter in bm_pairs.items():
            for forbidden in classification:
                bm = e.find_forbidden(edata, str(parent[0]), int(parent[3]), str(forbidden), mode="BM")
                try:
                    self.assertIsInstance(bm, dict)
                    self.assertIsInstance(bm, Iterable)
                except AssertionError:
                    self.assertIsNone(bm)

    def test_find_forbidden_returns_none_if_not_beta_minus_emitter(self):
        for forbidden in FindForbiddenTests.classification:
            bm = e.find_forbidden(edata,"Se70",1,forbidden,mode="BM")
            self.assertIsNone(bm)

    def test_find_forbidden_returns_none_if_illegal_string(self):
        for forbidden in FindForbiddenTests.classification:
            bm = e.find_forbidden(edata,"Co60",0,forbidden,mode="THisIsB@LL@CK$")
            self.assertIsNone

    def test_find_forbidden_returns_dict_or_none_depending_on_forbiddenness(self):
        bm_pairs = e.ensdf_pairs(edata,"BM")
        for parent, daughter in bm_pairs.items():
            for forbidden in FindForbiddenTests.classification:
                bm = e.find_forbidden(edata, str(parent[0]), int(parent[3]), str(forbidden), mode="BM")
            try:
                self.assertIsInstance(bm, dict)
                self.assertIsInstance(bm, Iterable)
            except AssertionError:
                self.assertIsNone(bm)

    def test_find_forbidden_raises_TypeError_if_first_arg_not_list(self):
        with self.assertRaises(TypeError):
            for forbidden in FindForbiddenTests.classification:
                bm = e.find_forbidden("Co60",edata,0,forbidden,mode="BM")

    def test_find_forbidden_raises_NameError_if_wrong_list(self):
        with self.assertRaises(NameError):
            for forbidden in FindForbiddenTests.classification:
                bm = e.find_forbidden(XXXedataXXX,"Co60",0,forbidden,mode="BM")

    def test_find_forbidden_raises_KeyError_if_bad_dict_items_in_list(self):
        bad_dict_items_in_list = [{'a':0, 'b':1, 'c':2}]
        with self.assertRaises(KeyError):
            for forbidden in FindForbiddenTests.classification:
                bm = e.find_forbidden(bad_dict_items_in_list,"Co60",0,forbidden,mode="BM")

    def test_find_forbidden_returned_contents_of_list(self):
        bm_pairs = e.ensdf_pairs(edata,"BM")
        # Search over all parents
        for parent_key, daughter_value in bm_pairs.items():
            for forbidden in FindForbiddenTests.classification:
                bm = e.find_forbidden(edata, str(parent_key[0]), int(parent_key[3]), str(forbidden), mode="BM")
                try:
                    for bm_key, bm_value in bm.items():
                        self.assertIsInstance(bm_key, tuple)
                        self.assertIsInstance(bm_key, Iterable)
                        self.assertIsInstance(bm_value, list)
                        self.assertIsInstance(bm_value, Iterable)

                        # Unpack the key contents
                        self.assertIsInstance(bm_key[0], str)
                        self.assertIsInstance(bm_key[1], int)
                        self.assertIsInstance(bm_key[2], int)
                        self.assertIsInstance(bm_key[3], int)
                        try:
                            self.assertIsInstance(bm_key[4], float)
                        except AssertionError:
                            self.assertIsInstance(bm_key[4], str)
                        try:
                            self.assertIsInstance(bm_key[5], float)
                        except AssertionError:
                            if bm_key[6] == -1:
                                self.assertIsNone(bm_key[5])
                        self.assertIsInstance(bm_key[6], int)
                        self.assertIsInstance(bm_key[7], int)
                        self.assertIsInstance(bm_key[8], int)
                        self.assertIsInstance(bm_key[9], str)
                        self.assertIsInstance(bm_key[10], int)
                        self.assertIsInstance(bm_key[11], int)
                        
                        # Unpack the value contents
                        for value in bm_value:
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
                    self.assertIsNone(bm)

        # Search over all forbidenness
        for forbidden in FindForbiddenTests.classification:
            bm = e.find_forbidden(edata, str(forbidden), mode="BM")
            try:
                for bm_key, bm_value in bm.items():
                    self.assertIsInstance(bm_key, tuple)
                    self.assertIsInstance(bm_key, Iterable)
                    self.assertIsInstance(bm_value, list)
                    self.assertIsInstance(bm_value, Iterable)

                    # Unpack the key contents
                    self.assertIsInstance(bm_key[0], str)
                    self.assertIsInstance(bm_key[1], int)
                    self.assertIsInstance(bm_key[2], int)
                    self.assertIsInstance(bm_key[3], int)
                    try:
                        self.assertIsInstance(bm_key[4], float)
                    except AssertionError:
                        self.assertIsInstance(bm_key[4], str)
                    try:
                        self.assertIsInstance(bm_key[5], float)
                    except AssertionError:
                        if bm_key[6] == -1:
                            self.assertIsNone(bm_key[5])
                    self.assertIsInstance(bm_key[6], int)
                    self.assertIsInstance(bm_key[7], int)
                    self.assertIsInstance(bm_key[8], int)
                    self.assertIsInstance(bm_key[9], str)
                    self.assertIsInstance(bm_key[10], int)
                    self.assertIsInstance(bm_key[11], int)

                    # Unpack the value contents
                    try:
                        for value in bm_value:
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
                        self.assertIsNone(bm_value)
                        
            except AttributeError:
                self.assertIsNone(bm)
