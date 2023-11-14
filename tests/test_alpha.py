import pytest
import unittest
import numpy as np
import pandas as pd
from collections.abc import Iterable

import paceENSDF as pe
e = pe.ENSDF()
edata = e.load_ensdf()

class AlphaTests(unittest.TestCase):

    __doc__="""Unit tests for methods from the Alpha class."""

    def test_get_alpha_returns_dictionary_for_all_alpha_emitters(self):
        alpha_pairs = e.ensdf_pairs(edata,"A")
        for parent, daughter in alpha_pairs.items():
            a = e.get_alpha(edata, parent[0], parent[3], units="best")
            try:
                self.assertIsInstance(a, dict)
                self.assertIsInstance(a, Iterable)
            except AssertionError:
                self.assertIsNone(a)

    def test_get_alpha_returns_none_if_not_alpha_emitter(self):
        a = e.get_alpha(edata,"Se70",1,units="seconds")
        self.assertIsNone(a)
        a = e.get_alpha(edata,"Cs119",1,units="best")
        self.assertIsNone(a)

    def test_get_alpha_returns_none_if_illegal_string(self):
        a = e.get_alpha(edata,"Ra226",0,units="THisIsB@LL@CK$")
        self.assertIsNone(a)
        a = e.get_alpha(edata,"THisIsB@LL@CK$",0,units="best")
        self.assertIsNone(a)
        
    def test_get_alpha_raises_TypeError_if_first_arg_not_list(self):
        with self.assertRaises(TypeError):
            a = e.get_alpha("Ra226",edata,0,units="best")

    def test_get_alpha_raises_NameError_if_wrong_list(self):
        with self.assertRaises(NameError):
            a = e.get_alpha(XXXedataXXX,"Ra226",0,units="best")

    def test_get_alpha_raises_KeyError_if_bad_dict_items_in_list(self):
        bad_dict_items_in_list = [{'a':0, 'b':1, 'c':2}]
        with self.assertRaises(KeyError):
           a = e.get_alpha(bad_dict_items_in_list,"Ra226",0,units="best") 

    def test_get_alpha_returned_contents_of_dict(self):
        alpha_pairs = e.ensdf_pairs(edata,"A")
        for parent_key, daughter_value in alpha_pairs.items():
            a = e.get_alpha(edata, parent_key[0], parent_key[3], units="best")
            try:
                for a_key, a_value in a.items():
                    self.assertIsInstance(a_key, tuple)
                    self.assertIsInstance(a_key, Iterable)
                    self.assertEqual(len(a_key), 15)

                    # Unpack the key contents
                    self.assertIsInstance(a_key[0], str)
                    self.assertIsInstance(a_key[1], int)
                    self.assertIsInstance(a_key[2], int)
                    self.assertIsInstance(a_key[3], str)
                    self.assertIsInstance(a_key[4], int)
                    self.assertIsInstance(a_key[5], int)
                    try:
                        self.assertIsInstance(a_key[6], float)
                        self.assertIsInstance(a_key[7], float)
                    except AssertionError:
                        # Strings of the type '(0+X)' etc.
                        try:
                            self.assertIsInstance(a_key[6], str)
                            self.assertIsInstance(a_key[7], int)
                        except AssertionError:
                            try:
                                self.assertIsInstance(a_key[6], str)
                                # Sometimes it's an <int> or a <float>
                                self.assertIsInstance(a_key[7], float)
                            except AssertionError:
                                self.assertIsInstance(a_key[6], str)
                                # Associated strings may have `null`
                                # uncertainties in ENSDF archive: September 2023
                                self.assertIsNone(a_key[7])
                        
                    try:
                        self.assertIsInstance(a_key[8], float)
                        self.assertIsInstance(a_key[9], int)
                    except AssertionError:
                        # Null JPi
                        if a_key[9] == -1:
                            self.assertIsNone(a_key[8])
                            self.assertIsInstance(a_key[9], int)
                    self.assertIsInstance(a_key[10], int)
                    self.assertIsInstance(a_key[11], int)
                    try:
                        self.assertIsInstance(a_key[12], float)
                        self.assertIsInstance(a_key[13], float)
                        self.assertIsInstance(a_key[14], str)
                    except AssertionError:
                        # Null T1/2
                        self.assertIsNone(a_key[12])
                        self.assertIsNone(a_key[13])
                        self.assertIsNone(a_key[14])

                    # Unpack the value contents
                    self.assertIsInstance(a_value, list)
                    self.assertIsInstance(a_value, Iterable)
                    for v in a_value:
                        self.assertEqual(len(v), 13)

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
                            try:
                                # Sometimes numerical EA is an <int> or <float>
                                self.assertIsInstance(v[7], int)
                            except AssertionError:
                                self.assertIsNone(v[7])
                        try:
                            self.assertIsInstance(v[8], float)
                        except AssertionError:
                            try:
                                # Sometimes numerical dEA is an <int> or <float>
                                self.assertIsInstance(v[8], int)
                            except AssertionError:
                                self.assertIsNone(v[8])

                        try:
                            self.assertIsInstance(v[9], float)
                        except AssertionError:
                            try:
                                # Sometimes numerical IA is an <int> or <float>
                                self.assertIsInstance(v[9], int)
                            except AssertionError:
                                self.assertIsNone(v[9])
                        try:    
                            self.assertIsInstance(v[10], float)
                        except AssertionError:
                            try:
                                # Sometimes numerical dIA is an <int> or <float>
                                self.assertIsInstance(v[10], int)
                            except AssertionError:
                                self.assertIsNone(v[10])

                        try:
                            self.assertIsInstance(v[11], float)
                        except AssertionError:
                            try:
                                # Sometimes numerical HF is an <int> or <float>
                                self.assertIsInstance(v[11], int)
                            except AssertionError:
                                self.assertIsNone(v[11])
                        try:    
                            self.assertIsInstance(v[12], float)
                        except AssertionError:
                            try:
                                # Sometimes numerical dHF is an <int> or <float>
                                self.assertIsInstance(v[12], int)
                            except AssertionError:
                                self.assertIsNone(v[12])

                            
            except AttributeError:
                self.assertIsNone(a)
            
            
