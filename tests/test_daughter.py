import pytest
import unittest
import numpy as np
import pandas as pd
from collections.abc import Iterable
import warnings
#warnings.simplefilter('error', RuntimeWarning)
warnings.simplefilter('ignore', RuntimeWarning)

import paceENSDF as pe
e = pe.ENSDF()
edata = e.load_ensdf()

class GetLevels(unittest.TestCase):

    __doc__="""Unit tests for the `get_levels` method of the Daughter class."""

    def test_get_levels_returns_list_for_all_decays(self):
        ecbp_pairs = e.ensdf_pairs(edata,"ECBP")
        for parent, daughter in ecbp_pairs.items():
            ecbp = e.get_levels(edata, str(parent[0]), int(parent[3]), mode="ECBP")
            self.assertIsInstance(ecbp, list)
            self.assertIsInstance(ecbp, Iterable)

        bm_pairs = e.ensdf_pairs(edata,"BM")
        for parent, daughter in bm_pairs.items():
            bm = e.get_levels(edata, str(parent[0]), int(parent[3]), mode="BM")
            self.assertIsInstance(bm, list)
            self.assertIsInstance(bm, Iterable)

        a_pairs = e.ensdf_pairs(edata,"A")
        for parent, daughter in a_pairs.items():
            a = e.get_levels(edata, str(parent[0]), int(parent[3]), mode="A")
            self.assertIsInstance(a, list)
            self.assertIsInstance(a, Iterable)

    def test_get_levels_returns_none_if_not_correct_decay_mode(self):
        ecbp = e.get_levels(edata,"Co60",0,mode="ECBP")
        self.assertIsNone(ecbp)
        bm = e.get_levels(edata,"Y86",0,mode="BM")
        self.assertIsNone(bm)
        a = e.get_levels(edata,"Na22",0,mode="A")
        self.assertIsNone(a)

    #def test_get_levels_returns_none_if_missing_kwargs(self):
    def test_get_levels_raises_IndexError_if_missing_kwargs(self):
        with self.assertRaises(IndexError):
            ecbp = e.get_levels(edata,"Y86",0)
        with self.assertRaises(IndexError):
            bm = e.get_levels(edata,"Co60",0)
        with self.assertRaises(IndexError):
            a = e.get_levels(edata,"Ra226",0)

    def test_get_levels_returns_none_if_illegal_string(self):
        levels = e.get_levels(edata,"Co60", 1, mode="THisIsB@LL@CK$")
        self.assertIsNone(levels)
        levels = e.get_levels(edata,"THisIsB@LL@CK$", 1, mode="BM")
        self.assertIsNone(levels)

    def test_get_levels_raises_TypeError_if_first_arg_not_list(self):
        with self.assertRaises(TypeError):
            ecbp = e.get_levels("Db258",edata,0,mode="ECBP")
        with self.assertRaises(TypeError):
            bm = e.get_levels("Co60",edata,1,mode="BM")
        with self.assertRaises(TypeError):
            a = e.get_levels("Ra226",edata,0,mode="A")

    def test_get_levels_raises_NameError_if_wrong_list(self):
        with self.assertRaises(NameError):
            ecbp = e.get_levels(XXXedataXXX,"Db258",0,mode="ECBP")
        with self.assertRaises(NameError):
            bm = e.get_levels(XXXedataXXX,"Co60",1,mode="BM")
        with self.assertRaises(NameError):
            a = e.get_levels(XXXedataXXX,"Ra226",0,mode="A")

    def test_get_levels_raises_KeyError_if_bad_dict_items_in_list(self):
        bad_dict_items_in_list = [{'a':0, 'b':1, 'c':2}]
        with self.assertRaises(KeyError):
           ecbp = e.get_levels(bad_dict_items_in_list,"Db258",0,mode="ECBP")
        with self.assertRaises(KeyError):
           bm = e.get_levels(bad_dict_items_in_list,"Co60",1,mode="BM")
        with self.assertRaises(KeyError):
           a = e.get_levels(bad_dict_items_in_list,"Ra226",0,mode="A")

    def test_get_levels_returned_contents_of_list(self):
        ecbp_pairs = e.ensdf_pairs(edata,"ECBP")
        for parent, daughter in ecbp_pairs.items():
            ecbp_levels = e.get_levels(edata, str(parent[0]), int(parent[3]), mode="ECBP")
            self.assertIsInstance(ecbp_levels, list)
            self.assertIsInstance(ecbp_levels, Iterable)
            #self.assertGreater(len(ecbp_levels), 0)
            for levels_value in ecbp_levels:
                # Unpack the list  contents
                self.assertIsInstance(levels_value[0], int)
                
                try:
                    self.assertIsInstance(levels_value[1], float)
                except AssertionError:
                    try:
                        # Sometimes <int>
                        self.assertIsInstance(levels_value[1], int)
                    except AssertionError:
                        # Sometimes <str>
                        self.assertIsInstance(levels_value[1], str)
                try:
                    self.assertIsInstance(levels_value[2], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[2], int)
                        
                self.assertIsInstance(levels_value[3], int)
                self.assertIsInstance(levels_value[4], int)
                try:
                    self.assertIsInstance(levels_value[5], float)
                except AssertionError:
                    if levels_value[6] == -1:
                        self.assertIsNone(levels_value[5])
                self.assertIsInstance(levels_value[6], int)
                self.assertIsInstance(levels_value[7], int)
                self.assertIsInstance(levels_value[8], int)
                self.assertIsInstance(levels_value[9], int)
                    

        bm_pairs = e.ensdf_pairs(edata,"BM")
        for parent, daughter in bm_pairs.items():
            bm_levels = e.get_levels(edata, str(parent[0]), int(parent[3]), mode="BM")
            self.assertIsInstance(bm_levels, list)
            self.assertIsInstance(bm_levels, Iterable)
            #self.assertGreater(len(bm_levels), 0)
            for levels_value in bm_levels:
                # Unpack the list  contents
                self.assertIsInstance(levels_value[0], int)
                
                try:
                    self.assertIsInstance(levels_value[1], float)
                except AssertionError:
                    try:
                        # Sometimes <int>
                        self.assertIsInstance(levels_value[1], int)
                    except AssertionError:
                        # Sometimes <str>
                        self.assertIsInstance(levels_value[1], str)
                try:
                    self.assertIsInstance(levels_value[2], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[2], int)
                        
                self.assertIsInstance(levels_value[3], int)
                self.assertIsInstance(levels_value[4], int)
                try:
                    self.assertIsInstance(levels_value[5], float)
                except AssertionError:
                    if levels_value[6] == -1:
                        self.assertIsNone(levels_value[5])
                self.assertIsInstance(levels_value[6], int)
                self.assertIsInstance(levels_value[7], int)
                self.assertIsInstance(levels_value[8], int)
                self.assertIsInstance(levels_value[9], int)


        a_pairs = e.ensdf_pairs(edata,"A")
        for parent, daughter in a_pairs.items():
            a_levels = e.get_levels(edata, str(parent[0]), int(parent[3]), mode="A")
            self.assertIsInstance(a_levels, list)
            self.assertIsInstance(a_levels, Iterable)
            #self.assertGreater(len(a_levels), 0)
            for levels_value in a_levels:
                # Unpack the list  contents
                self.assertIsInstance(levels_value[0], int)
                
                try:
                    self.assertIsInstance(levels_value[1], float)
                except AssertionError:
                    try:
                        # Sometimes <int>
                        self.assertIsInstance(levels_value[1], int)
                    except AssertionError:
                        # Sometimes <str>
                        self.assertIsInstance(levels_value[1], str)
                try:
                    self.assertIsInstance(levels_value[2], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[2], int)
                        
                self.assertIsInstance(levels_value[3], int)
                self.assertIsInstance(levels_value[4], int)
                try:
                    self.assertIsInstance(levels_value[5], float)
                except AssertionError:
                    if levels_value[6] == -1:
                        self.assertIsNone(levels_value[5])
                self.assertIsInstance(levels_value[6], int)
                self.assertIsInstance(levels_value[7], int)
                self.assertIsInstance(levels_value[8], int)
                self.assertIsInstance(levels_value[9], int)


class GetLevelsAndGammas(unittest.TestCase):

    __doc__="""Unit tests for the `get_levels_and_gammas` method of the 
    Daughter class."""

    def test_get_levels_and_gammas_returns_list_for_all_decays(self):
        ecbp_pairs = e.ensdf_pairs(edata,"ECBP")
        for parent, daughter in ecbp_pairs.items():
            ecbp = e.get_levels_and_gammas(edata, str(parent[0]), int(parent[3]), mode="ECBP")
            self.assertIsInstance(ecbp, list)
            self.assertIsInstance(ecbp, Iterable)

        bm_pairs = e.ensdf_pairs(edata,"BM")
        for parent, daughter in bm_pairs.items():
            bm = e.get_levels_and_gammas(edata, str(parent[0]), int(parent[3]), mode="BM")
            self.assertIsInstance(bm, list)
            self.assertIsInstance(bm, Iterable)

        a_pairs = e.ensdf_pairs(edata,"A")
        for parent, daughter in a_pairs.items():
            a = e.get_levels_and_gammas(edata, str(parent[0]), int(parent[3]), mode="A")
            self.assertIsInstance(a, list)
            self.assertIsInstance(a, Iterable)

    def test_get_levels_and_gammas_returns_none_if_not_correct_decay_mode(self):
        ecbp = e.get_levels_and_gammas(edata,"Co60",0,mode="ECBP")
        self.assertIsNone(ecbp)
        bm = e.get_levels_and_gammas(edata,"Y86",0,mode="BM")
        self.assertIsNone(bm)
        a = e.get_levels_and_gammas(edata,"Na22",0,mode="A")
        self.assertIsNone(a)

    #def test_get_levels_and_gammas_returns_none_if_missing_kwargs(self):
    def test_get_levels_and_gammas_raises_IndexError_if_missing_kwargs(self):
        with self.assertRaises(IndexError):
            ecbp = e.get_levels_and_gammas(edata,"Y86",0)
        with self.assertRaises(IndexError):
            bm = e.get_levels_and_gammas(edata,"Co60",0)
        with self.assertRaises(IndexError):
            a = e.get_levels_and_gammas(edata,"Ra226",0)

    def test_get_levels_and_gammas_returns_none_if_illegal_string(self):
        levels = e.get_levels_and_gammas(edata,"Co60", 1, mode="THisIsB@LL@CK$")
        self.assertIsNone(levels)
        levels = e.get_levels_and_gammas(edata,"THisIsB@LL@CK$", 1, mode="BM")
        self.assertIsNone(levels)

    def test_get_levels_and_gammas_raises_TypeError_if_first_arg_not_list(self):
        with self.assertRaises(TypeError):
            ecbp = e.get_levels_and_gammas("Db258",edata,0,mode="ECBP")
        with self.assertRaises(TypeError):
            bm = e.get_levels_and_gammas("Co60",edata,1,mode="BM")
        with self.assertRaises(TypeError):
            a = e.get_levels_and_gammas("Ra226",edata,0,mode="A")

    def test_get_levels_and_gammas_raises_NameError_if_wrong_list(self):
        with self.assertRaises(NameError):
            ecbp = e.get_levels_and_gammas(XXXedataXXX,"Db258",0,mode="ECBP")
        with self.assertRaises(NameError):
            bm = e.get_levels_and_gammas(XXXedataXXX,"Co60",1,mode="BM")
        with self.assertRaises(NameError):
            a = e.get_levels_and_gammas(XXXedataXXX,"Ra226",0,mode="A")

    def test_get_levels_and_gammas_raises_KeyError_if_bad_dict_items_in_list(self):
        bad_dict_items_in_list = [{'a':0, 'b':1, 'c':2}]
        with self.assertRaises(KeyError):
           ecbp = e.get_levels_and_gammas(bad_dict_items_in_list,"Db258",0,mode="ECBP")
        with self.assertRaises(KeyError):
           bm = e.get_levels_and_gammas(bad_dict_items_in_list,"Co60",1,mode="BM")
        with self.assertRaises(KeyError):
           a = e.get_levels_and_gammas(bad_dict_items_in_list,"Ra226",0,mode="A")

    def test_get_levels_and_gammas_returned_contents_of_list(self):
        ecbp_pairs = e.ensdf_pairs(edata,"ECBP")
        for parent, daughter in ecbp_pairs.items():
            ecbp_levels = e.get_levels_and_gammas(edata, str(parent[0]), int(parent[3]), mode="ECBP")
            self.assertIsInstance(ecbp_levels, list)
            self.assertIsInstance(ecbp_levels, Iterable)
            #self.assertGreater(len(ecbp_levels), 0)
            for levels_value in ecbp_levels:
                # Unpack the list  contents
                self.assertIsInstance(levels_value[0], int)
                self.assertIsInstance(levels_value[1], int)
                
                try:
                    self.assertIsInstance(levels_value[2], float)
                except AssertionError:
                    try:
                        # Sometimes <int>
                        self.assertIsInstance(levels_value[2], int)
                    except AssertionError:
                        # Sometimes <str>
                        self.assertIsInstance(levels_value[2], str)
                try:
                    self.assertIsInstance(levels_value[3], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[3], int)
                        
                self.assertIsInstance(levels_value[4], int)
                self.assertIsInstance(levels_value[5], int)
                
                try:
                    self.assertIsInstance(levels_value[6], float)
                except AssertionError:
                    try:
                        # Sometimes <int>
                        self.assertIsInstance(levels_value[6], int)
                    except AssertionError:
                        # Sometimes <str>
                        self.assertIsInstance(levels_value[6], str)
                try:
                    self.assertIsInstance(levels_value[7], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[7], int)

                try:
                    self.assertIsInstance(levels_value[8], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[8], int)
                try:
                    self.assertIsInstance(levels_value[9], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[9], int)

                try:
                    self.assertIsInstance(levels_value[10], str)
                except AssertionError:
                    self.assertIsNone(levels_value[10])
                    
                try:
                    self.assertIsInstance(levels_value[11], float)
                except AssertionError:
                    self.assertIsNone(levels_value[11])
                try:
                    self.assertIsInstance(levels_value[12], float)
                except AssertionError:
                    self.assertIsNone(levels_value[12])
                self.assertIsInstance(levels_value[13], int)
                
                try:
                    self.assertIsInstance(levels_value[14], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[14], int)
                try:
                    self.assertIsInstance(levels_value[15], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[15], int)
                    

        bm_pairs = e.ensdf_pairs(edata,"BM")
        for parent, daughter in bm_pairs.items():
            bm_levels = e.get_levels_and_gammas(edata, str(parent[0]), int(parent[3]), mode="BM")
            self.assertIsInstance(bm_levels, list)
            self.assertIsInstance(bm_levels, Iterable)
            #self.assertGreater(len(bm_levels), 0)
            for levels_value in bm_levels:
                # Unpack the list  contents
                self.assertIsInstance(levels_value[0], int)
                self.assertIsInstance(levels_value[1], int)
                
                try:
                    self.assertIsInstance(levels_value[2], float)
                except AssertionError:
                    try:
                        # Sometimes <int>
                        self.assertIsInstance(levels_value[2], int)
                    except AssertionError:
                        # Sometimes <str>
                        self.assertIsInstance(levels_value[2], str)
                try:
                    self.assertIsInstance(levels_value[3], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[3], int)
                        
                self.assertIsInstance(levels_value[4], int)
                self.assertIsInstance(levels_value[5], int)
                
                try:
                    self.assertIsInstance(levels_value[6], float)
                except AssertionError:
                    try:
                        # Sometimes <int>
                        self.assertIsInstance(levels_value[6], int)
                    except AssertionError:
                        # Sometimes <str>
                        self.assertIsInstance(levels_value[6], str)
                try:
                    self.assertIsInstance(levels_value[7], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[7], int)

                try:
                    self.assertIsInstance(levels_value[8], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[8], int)
                try:
                    self.assertIsInstance(levels_value[9], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[9], int)

                try:
                    self.assertIsInstance(levels_value[10], str)
                except AssertionError:
                    self.assertIsNone(levels_value[10])
                
                try:
                    self.assertIsInstance(levels_value[11], float)
                except AssertionError:
                    self.assertIsNone(levels_value[11])
                try:
                    self.assertIsInstance(levels_value[12], float)
                except AssertionError:
                    self.assertIsNone(levels_value[12])
                self.assertIsInstance(levels_value[13], int)
                
                try:
                    self.assertIsInstance(levels_value[14], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[14], int)
                try:
                    self.assertIsInstance(levels_value[15], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[15], int)


        a_pairs = e.ensdf_pairs(edata,"A")
        for parent, daughter in a_pairs.items():
            a_levels = e.get_levels_and_gammas(edata, str(parent[0]), int(parent[3]), mode="A")
            self.assertIsInstance(a_levels, list)
            self.assertIsInstance(a_levels, Iterable)
            #self.assertGreater(len(a_levels), 0)
            for levels_value in a_levels:
                # Unpack the list  contents
                self.assertIsInstance(levels_value[0], int)
                self.assertIsInstance(levels_value[1], int)
                
                try:
                    self.assertIsInstance(levels_value[2], float)
                except AssertionError:
                    try:
                        # Sometimes <int>
                        self.assertIsInstance(levels_value[2], int)
                    except AssertionError:
                        # Sometimes <str>
                        self.assertIsInstance(levels_value[2], str)
                try:
                    self.assertIsInstance(levels_value[3], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[3], int)
                        
                self.assertIsInstance(levels_value[4], int)
                self.assertIsInstance(levels_value[5], int)
                
                try:
                    self.assertIsInstance(levels_value[6], float)
                except AssertionError:
                    try:
                        # Sometimes <int>
                        self.assertIsInstance(levels_value[6], int)
                    except AssertionError:
                        # Sometimes <str>
                        self.assertIsInstance(levels_value[6], str)
                try:
                    self.assertIsInstance(levels_value[7], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[7], int)

                try:
                    self.assertIsInstance(levels_value[8], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[8], int)
                try:
                    self.assertIsInstance(levels_value[9], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[9], int)

                try:
                    self.assertIsInstance(levels_value[10], str)
                except AssertionError:
                    self.assertIsNone(levels_value[10])
                
                try:
                    self.assertIsInstance(levels_value[11], float)
                except AssertionError:
                    self.assertIsNone(levels_value[11])
                try:
                    self.assertIsInstance(levels_value[12], float)
                except AssertionError:
                    self.assertIsNone(levels_value[12])
                self.assertIsInstance(levels_value[13], int)
                
                try:
                    self.assertIsInstance(levels_value[14], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[14], int)
                try:
                    self.assertIsInstance(levels_value[15], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[15], int)


class GetLevelsAndGammasSubshells(unittest.TestCase):

    __doc__="""Unit tests for the `get_levels_and_gammas_subshells` method of 
    the Daughter class."""

    def test_get_levels_and_gammas_subshells_returns_list_for_all_decays(self):
        ecbp_pairs = e.ensdf_pairs(edata,"ECBP")
        for parent, daughter in ecbp_pairs.items():
            ecbp = e.get_levels_and_gammas_subshells(edata, str(parent[0]), int(parent[3]), mode="ECBP",subshell='calc')
            self.assertIsInstance(ecbp, list)
            self.assertIsInstance(ecbp, Iterable)
            ecbp = e.get_levels_and_gammas_subshells(edata, str(parent[0]), int(parent[3]), mode="ECBP",subshell='ratio')
            self.assertIsInstance(ecbp, list)
            self.assertIsInstance(ecbp, Iterable)
            ecbp = e.get_levels_and_gammas_subshells(edata, str(parent[0]), int(parent[3]), mode="ECBP",subshell='expt')
            self.assertIsInstance(ecbp, list)
            self.assertIsInstance(ecbp, Iterable)
            ecbp = e.get_levels_and_gammas_subshells(edata, str(parent[0]), int(parent[3]), mode="ECBP",subshell='electron')
            self.assertIsInstance(ecbp, list)
            self.assertIsInstance(ecbp, Iterable)
            ecbp = e.get_levels_and_gammas_subshells(edata, str(parent[0]), int(parent[3]), mode="ECBP",subshell='sumcalc')
            self.assertIsInstance(ecbp, list)
            self.assertIsInstance(ecbp, Iterable)

        bm_pairs = e.ensdf_pairs(edata,"BM")
        for parent, daughter in bm_pairs.items():
            bm = e.get_levels_and_gammas_subshells(edata, str(parent[0]), int(parent[3]), mode="BM",subshell='calc')
            self.assertIsInstance(bm, list)
            self.assertIsInstance(bm, Iterable)
            ecbp = e.get_levels_and_gammas_subshells(edata, str(parent[0]), int(parent[3]), mode="BM",subshell='ratio')
            self.assertIsInstance(ecbp, list)
            self.assertIsInstance(ecbp, Iterable)
            ecbp = e.get_levels_and_gammas_subshells(edata, str(parent[0]), int(parent[3]), mode="BM",subshell='expt')
            self.assertIsInstance(ecbp, list)
            self.assertIsInstance(ecbp, Iterable)
            ecbp = e.get_levels_and_gammas_subshells(edata, str(parent[0]), int(parent[3]), mode="BM",subshell='electron')
            self.assertIsInstance(ecbp, list)
            self.assertIsInstance(ecbp, Iterable)
            ecbp = e.get_levels_and_gammas_subshells(edata, str(parent[0]), int(parent[3]), mode="BM",subshell='sumcalc')
            self.assertIsInstance(ecbp, list)
            self.assertIsInstance(ecbp, Iterable)

        a_pairs = e.ensdf_pairs(edata,"A")
        for parent, daughter in a_pairs.items():
            a = e.get_levels_and_gammas_subshells(edata, str(parent[0]), int(parent[3]), mode="A",subshell='calc')
            self.assertIsInstance(a, list)
            self.assertIsInstance(a, Iterable)
            ecbp = e.get_levels_and_gammas_subshells(edata, str(parent[0]), int(parent[3]), mode="A",subshell='ratio')
            self.assertIsInstance(ecbp, list)
            self.assertIsInstance(ecbp, Iterable)
            ecbp = e.get_levels_and_gammas_subshells(edata, str(parent[0]), int(parent[3]), mode="A",subshell='expt')
            self.assertIsInstance(ecbp, list)
            self.assertIsInstance(ecbp, Iterable)
            ecbp = e.get_levels_and_gammas_subshells(edata, str(parent[0]), int(parent[3]), mode="A",subshell='electron')
            self.assertIsInstance(ecbp, list)
            self.assertIsInstance(ecbp, Iterable)
            ecbp = e.get_levels_and_gammas_subshells(edata, str(parent[0]), int(parent[3]), mode="A",subshell='sumcalc')
            self.assertIsInstance(ecbp, list)
            self.assertIsInstance(ecbp, Iterable)

    def test_get_levels_and_gammas_subshells_returns_none_if_not_correct_decay_mode(self):
        # 'calc'
        ecbp = e.get_levels_and_gammas_subshells(edata,"Co60",0,mode="ECBP",subshell='calc')
        self.assertIsNone(ecbp)
        bm = e.get_levels_and_gammas_subshells(edata,"Y86",0,mode="BM",subshell='calc')
        self.assertIsNone(bm)
        a = e.get_levels_and_gammas_subshells(edata,"Na22",0,mode="A",subshell='calc')
        self.assertIsNone(a)
        # 'ratio'
        ecbp = e.get_levels_and_gammas_subshells(edata,"Co60",0,mode="ECBP",subshell='ratio')
        self.assertIsNone(ecbp)
        bm = e.get_levels_and_gammas_subshells(edata,"Y86",0,mode="BM",subshell='ratio')
        self.assertIsNone(bm)
        a = e.get_levels_and_gammas_subshells(edata,"Na22",0,mode="A",subshell='ratio')
        self.assertIsNone(a)
        # 'expt'
        ecbp = e.get_levels_and_gammas_subshells(edata,"Co60",0,mode="ECBP",subshell='expt')
        self.assertIsNone(ecbp)
        bm = e.get_levels_and_gammas_subshells(edata,"Y86",0,mode="BM",subshell='expt')
        self.assertIsNone(bm)
        a = e.get_levels_and_gammas_subshells(edata,"Na22",0,mode="A",subshell='expt')
        self.assertIsNone(a)
        # 'electron'
        ecbp = e.get_levels_and_gammas_subshells(edata,"Co60",0,mode="ECBP",subshell='electron')
        self.assertIsNone(ecbp)
        bm = e.get_levels_and_gammas_subshells(edata,"Y86",0,mode="BM",subshell='electron')
        self.assertIsNone(bm)
        a = e.get_levels_and_gammas_subshells(edata,"Na22",0,mode="A",subshell='electron')
        self.assertIsNone(a)
        # 'sumcalc'
        ecbp = e.get_levels_and_gammas_subshells(edata,"Co60",0,mode="ECBP",subshell='sumcalc')
        self.assertIsNone(ecbp)
        bm = e.get_levels_and_gammas_subshells(edata,"Y86",0,mode="BM",subshell='sumcalc')
        self.assertIsNone(bm)
        a = e.get_levels_and_gammas_subshells(edata,"Na22",0,mode="A",subshell='sumcalc')
        self.assertIsNone(a)

    def test_get_levels_and_gammas_subshells_returns_none_if_missing_kwargs(self):
        ecbp = e.get_levels_and_gammas_subshells(edata,"Y86",0,subshell="expt")
        self.assertIsNone(ecbp)
        bm = e.get_levels_and_gammas_subshells(edata,"Co60",0,subshell="calc")
        self.assertIsNone(bm)
        a = e.get_levels_and_gammas_subshells(edata,"Ra226",0,mode="A")
        self.assertIsNone(a)

    def test_get_levels_and_gammas_subshells_returns_none_if_illegal_string(self):
        # 'calc'
        levels = e.get_levels_and_gammas_subshells(edata,"Co60", 1, mode="THisIsB@LL@CK$",subshell='calc')
        self.assertIsNone(levels)
        levels = e.get_levels_and_gammas_subshells(edata,"THisIsB@LL@CK$", 1, mode="BM",subshell='calc')
        self.assertIsNone(levels)
        # 'ratio'
        levels = e.get_levels_and_gammas_subshells(edata,"Co60", 1, mode="THisIsB@LL@CK$",subshell='ratio')
        self.assertIsNone(levels)
        levels = e.get_levels_and_gammas_subshells(edata,"THisIsB@LL@CK$", 1, mode="BM",subshell='ratio')
        self.assertIsNone(levels)
        # 'expt'
        levels = e.get_levels_and_gammas_subshells(edata,"Co60", 1, mode="THisIsB@LL@CK$",subshell='expt')
        self.assertIsNone(levels)
        levels = e.get_levels_and_gammas_subshells(edata,"THisIsB@LL@CK$", 1, mode="BM",subshell='expt')
        self.assertIsNone(levels)
        # 'electron'
        levels = e.get_levels_and_gammas_subshells(edata,"Co60", 1, mode="THisIsB@LL@CK$",subshell='electron')
        self.assertIsNone(levels)
        levels = e.get_levels_and_gammas_subshells(edata,"THisIsB@LL@CK$", 1, mode="BM",subshell='electron')
        self.assertIsNone(levels)
        # 'sumcalc'
        levels = e.get_levels_and_gammas_subshells(edata,"Co60", 1, mode="THisIsB@LL@CK$",subshell='sumcalc')
        self.assertIsNone(levels)
        levels = e.get_levels_and_gammas_subshells(edata,"THisIsB@LL@CK$", 1, mode="BM",subshell='sumcalc')
        self.assertIsNone(levels)
        # Wrong subshell
        levels = e.get_levels_and_gammas_subshells(edata,"Co60", 1, mode="BM",subshell='THisIsB@LL@CK$')

    def test_get_levels_and_gammas_subshells_raises_TypeError_if_first_arg_not_list(self):
        # 'calc'
        with self.assertRaises(TypeError):
            ecbp = e.get_levels_and_gammas_subshells("Db258",edata,0,mode="ECBP",subshell='calc')
        with self.assertRaises(TypeError):
            bm = e.get_levels_and_gammas_subshells("Co60",edata,1,mode="BM",subshell='calc')
        with self.assertRaises(TypeError):
            a = e.get_levels_and_gammas_subshells("Ra226",edata,0,mode="A",subshell='calc')
        # 'ratio'
        with self.assertRaises(TypeError):
            ecbp = e.get_levels_and_gammas_subshells("Db258",edata,0,mode="ECBP",subshell='ratio')
        with self.assertRaises(TypeError):
            bm = e.get_levels_and_gammas_subshells("Co60",edata,1,mode="BM",subshell='ratio')
        with self.assertRaises(TypeError):
            a = e.get_levels_and_gammas_subshells("Ra226",edata,0,mode="A",subshell='ratio')
        # 'expt'
        with self.assertRaises(TypeError):
            ecbp = e.get_levels_and_gammas_subshells("Db258",edata,0,mode="ECBP",subshell='expt')
        with self.assertRaises(TypeError):
            bm = e.get_levels_and_gammas_subshells("Co60",edata,1,mode="BM",subshell='calc')
        with self.assertRaises(TypeError):
            a = e.get_levels_and_gammas_subshells("Ra226",edata,0,mode="A",subshell='expt')
        # 'electron'
        with self.assertRaises(TypeError):
            ecbp = e.get_levels_and_gammas_subshells("Db258",edata,0,mode="ECBP",subshell='electron')
        with self.assertRaises(TypeError):
            bm = e.get_levels_and_gammas_subshells("Co60",edata,1,mode="BM",subshell='electron')
        with self.assertRaises(TypeError):
            a = e.get_levels_and_gammas_subshells("Ra226",edata,0,mode="A",subshell='electron')
        # 'sumcalc'
        with self.assertRaises(TypeError):
            ecbp = e.get_levels_and_gammas_subshells("Db258",edata,0,mode="ECBP",subshell='sumcalc')
        with self.assertRaises(TypeError):
            bm = e.get_levels_and_gammas_subshells("Co60",edata,1,mode="BM",subshell='sumcalc')
        with self.assertRaises(TypeError):
            a = e.get_levels_and_gammas_subshells("Ra226",edata,0,mode="A",subshell='sumcalc')

    def test_get_levels_and_gammas_subshells_raises_NameError_if_wrong_list(self):
        # 'calc'
        with self.assertRaises(NameError):
            ecbp = e.get_levels_and_gammas_subshells(XXXedataXXX,"Db258",0,mode="ECBP",subshell='calc')
        with self.assertRaises(NameError):
            bm = e.get_levels_and_gammas_subshells(XXXedataXXX,"Co60",1,mode="BM",subshell='calc')
        with self.assertRaises(NameError):
            a = e.get_levels_and_gammas_subshells(XXXedataXXX,"Ra226",0,mode="A",subshell='calc')
        # 'ratio'
        with self.assertRaises(NameError):
            ecbp = e.get_levels_and_gammas_subshells(XXXedataXXX,"Db258",0,mode="ECBP",subshell='ratio')
        with self.assertRaises(NameError):
            bm = e.get_levels_and_gammas_subshells(XXXedataXXX,"Co60",1,mode="BM",subshell='ratio')
        with self.assertRaises(NameError):
            a = e.get_levels_and_gammas_subshells(XXXedataXXX,"Ra226",0,mode="A",subshell='ratio')
        # 'expt'
        with self.assertRaises(NameError):
            ecbp = e.get_levels_and_gammas_subshells(XXXedataXXX,"Db258",0,mode="ECBP",subshell='expt')
        with self.assertRaises(NameError):
            bm = e.get_levels_and_gammas_subshells(XXXedataXXX,"Co60",1,mode="BM",subshell='expt')
        with self.assertRaises(NameError):
            a = e.get_levels_and_gammas_subshells(XXXedataXXX,"Ra226",0,mode="A",subshell='expt')
        # 'electron'
        with self.assertRaises(NameError):
            ecbp = e.get_levels_and_gammas_subshells(XXXedataXXX,"Db258",0,mode="ECBP",subshell='electron')
        with self.assertRaises(NameError):
            bm = e.get_levels_and_gammas_subshells(XXXedataXXX,"Co60",1,mode="BM",subshell='electron')
        with self.assertRaises(NameError):
            a = e.get_levels_and_gammas_subshells(XXXedataXXX,"Ra226",0,mode="A",subshell='electron')
        # 'sumcalc'
        with self.assertRaises(NameError):
            ecbp = e.get_levels_and_gammas_subshells(XXXedataXXX,"Db258",0,mode="ECBP",subshell='sumcalc')
        with self.assertRaises(NameError):
            bm = e.get_levels_and_gammas_subshells(XXXedataXXX,"Co60",1,mode="BM",subshell='sumcalc')
        with self.assertRaises(NameError):
            a = e.get_levels_and_gammas_subshells(XXXedataXXX,"Ra226",0,mode="A",subshell='sumcalc')

    def test_get_levels_and_gammas_subshells_raises_KeyError_if_bad_dict_items_in_list(self):
        bad_dict_items_in_list = [{'a':0, 'b':1, 'c':2}]
        # 'calc'
        with self.assertRaises(KeyError):
           ecbp = e.get_levels_and_gammas_subshells(bad_dict_items_in_list,"Db258",0,mode="ECBP",subshell='calc')
        with self.assertRaises(KeyError):
           bm = e.get_levels_and_gammas_subshells(bad_dict_items_in_list,"Co60",1,mode="BM",subshell='calc')
        with self.assertRaises(KeyError):
           a = e.get_levels_and_gammas_subshells(bad_dict_items_in_list,"Ra226",0,mode="A",subshell='calc')
        # 'ratio'
        with self.assertRaises(KeyError):
           ecbp = e.get_levels_and_gammas_subshells(bad_dict_items_in_list,"Db258",0,mode="ECBP",subshell='ratio')
        with self.assertRaises(KeyError):
           bm = e.get_levels_and_gammas_subshells(bad_dict_items_in_list,"Co60",1,mode="BM",subshell='ratio')
        with self.assertRaises(KeyError):
           a = e.get_levels_and_gammas_subshells(bad_dict_items_in_list,"Ra226",0,mode="A",subshell='ratio')
        # 'expt'
        with self.assertRaises(KeyError):
           ecbp = e.get_levels_and_gammas_subshells(bad_dict_items_in_list,"Db258",0,mode="ECBP",subshell='expt')
        with self.assertRaises(KeyError):
           bm = e.get_levels_and_gammas_subshells(bad_dict_items_in_list,"Co60",1,mode="BM",subshell='expt')
        with self.assertRaises(KeyError):
           a = e.get_levels_and_gammas_subshells(bad_dict_items_in_list,"Ra226",0,mode="A",subshell='expt')
        # 'electron'
        with self.assertRaises(KeyError):
           ecbp = e.get_levels_and_gammas_subshells(bad_dict_items_in_list,"Db258",0,mode="ECBP",subshell='electron')
        with self.assertRaises(KeyError):
           bm = e.get_levels_and_gammas_subshells(bad_dict_items_in_list,"Co60",1,mode="BM",subshell='electron')
        with self.assertRaises(KeyError):
           a = e.get_levels_and_gammas_subshells(bad_dict_items_in_list,"Ra226",0,mode="A",subshell='electron')
        # 'sumcalc'
        with self.assertRaises(KeyError):
           ecbp = e.get_levels_and_gammas_subshells(bad_dict_items_in_list,"Db258",0,mode="ECBP",subshell='sumcalc')
        with self.assertRaises(KeyError):
           bm = e.get_levels_and_gammas_subshells(bad_dict_items_in_list,"Co60",1,mode="BM",subshell='sumcalc')
        with self.assertRaises(KeyError):
           a = e.get_levels_and_gammas_subshells(bad_dict_items_in_list,"Ra226",0,mode="A",subshell='sumcalc')

    def test_get_levels_and_gammas_subshells_returned_contents_of_list(self):
        # 'calc'
        ecbp_pairs = e.ensdf_pairs(edata,"ECBP") 
        for parent, daughter in ecbp_pairs.items():
            ecbp_levels = e.get_levels_and_gammas_subshells(edata, str(parent[0]), int(parent[3]), mode="ECBP",subshell='calc')
            self.assertIsInstance(ecbp_levels, list)
            self.assertIsInstance(ecbp_levels, Iterable)
            #self.assertGreater(len(ecbp_levels), 0)
            for levels_value in ecbp_levels:
                # Unpack the list  contents
                self.assertIsInstance(levels_value[0], int)
                self.assertIsInstance(levels_value[1], int)
                
                try:
                    self.assertIsInstance(levels_value[2], float)
                except AssertionError:
                    try:
                        # Sometimes <int>
                        self.assertIsInstance(levels_value[2], int)
                    except AssertionError:
                        # Sometimes <str>
                        self.assertIsInstance(levels_value[2], str)
                try:
                    self.assertIsInstance(levels_value[3], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[3], int)
                        
                self.assertIsInstance(levels_value[4], int)
                self.assertIsInstance(levels_value[5], int)
                
                try:
                    self.assertIsInstance(levels_value[6], float)
                except AssertionError:
                    try:
                        # Sometimes <int>
                        self.assertIsInstance(levels_value[6], int)
                    except AssertionError:
                        # Sometimes <str>
                        self.assertIsInstance(levels_value[6], str)
                try:
                    self.assertIsInstance(levels_value[7], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[7], int)

                try:
                    self.assertIsInstance(levels_value[8], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[8], int)
                try:
                    self.assertIsInstance(levels_value[9], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[9], int)

                try:
                    self.assertIsInstance(levels_value[10], str)
                except AssertionError:
                    self.assertIsNone(levels_value[10])
                    
                try:
                    self.assertIsInstance(levels_value[11], float)
                except AssertionError:
                    self.assertIsNone(levels_value[11])
                try:
                    self.assertIsInstance(levels_value[12], float)
                except AssertionError:
                    self.assertIsNone(levels_value[12])
                self.assertIsInstance(levels_value[13], int)
                
                try:
                    self.assertIsInstance(levels_value[14], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[14], int)
                try:
                    self.assertIsInstance(levels_value[15], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[15], int)

                self.assertIsInstance(levels_value[16], float)
                self.assertIsInstance(levels_value[17], float)
                self.assertIsInstance(levels_value[18], float)
                self.assertIsInstance(levels_value[19], float)
                self.assertIsInstance(levels_value[20], float)
                self.assertIsInstance(levels_value[21], float)
                self.assertIsInstance(levels_value[22], float)
                self.assertIsInstance(levels_value[23], float)
                self.assertIsInstance(levels_value[24], float)
                self.assertIsInstance(levels_value[25], float)
                self.assertIsInstance(levels_value[26], float)
                self.assertIsInstance(levels_value[27], float)
                self.assertIsInstance(levels_value[28], float)
                self.assertIsInstance(levels_value[29], float)
                    

        bm_pairs = e.ensdf_pairs(edata,"BM")
        for parent, daughter in bm_pairs.items():
            bm_levels = e.get_levels_and_gammas_subshells(edata, str(parent[0]), int(parent[3]), mode="BM",subshell='calc')
            self.assertIsInstance(bm_levels, list)
            self.assertIsInstance(bm_levels, Iterable)
            #self.assertGreater(len(bm_levels), 0)
            for levels_value in bm_levels:
                # Unpack the list  contents
                self.assertIsInstance(levels_value[0], int)
                self.assertIsInstance(levels_value[1], int)
                
                try:
                    self.assertIsInstance(levels_value[2], float)
                except AssertionError:
                    try:
                        # Sometimes <int>
                        self.assertIsInstance(levels_value[2], int)
                    except AssertionError:
                        # Sometimes <str>
                        self.assertIsInstance(levels_value[2], str)
                try:
                    self.assertIsInstance(levels_value[3], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[3], int)
                        
                self.assertIsInstance(levels_value[4], int)
                self.assertIsInstance(levels_value[5], int)
                
                try:
                    self.assertIsInstance(levels_value[6], float)
                except AssertionError:
                    try:
                        # Sometimes <int>
                        self.assertIsInstance(levels_value[6], int)
                    except AssertionError:
                        # Sometimes <str>
                        self.assertIsInstance(levels_value[6], str)
                try:
                    self.assertIsInstance(levels_value[7], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[7], int)

                try:
                    self.assertIsInstance(levels_value[8], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[8], int)
                try:
                    self.assertIsInstance(levels_value[9], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[9], int)

                try:
                    self.assertIsInstance(levels_value[10], str)
                except AssertionError:
                    self.assertIsNone(levels_value[10])
                
                try:
                    self.assertIsInstance(levels_value[11], float)
                except AssertionError:
                    self.assertIsNone(levels_value[11])
                try:
                    self.assertIsInstance(levels_value[12], float)
                except AssertionError:
                    self.assertIsNone(levels_value[12])
                self.assertIsInstance(levels_value[13], int)
                
                try:
                    self.assertIsInstance(levels_value[14], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[14], int)
                try:
                    self.assertIsInstance(levels_value[15], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[15], int)

                self.assertIsInstance(levels_value[16], float)
                self.assertIsInstance(levels_value[17], float)
                self.assertIsInstance(levels_value[18], float)
                self.assertIsInstance(levels_value[19], float)
                self.assertIsInstance(levels_value[20], float)
                self.assertIsInstance(levels_value[21], float)
                self.assertIsInstance(levels_value[22], float)
                self.assertIsInstance(levels_value[23], float)
                self.assertIsInstance(levels_value[24], float)
                self.assertIsInstance(levels_value[25], float)
                self.assertIsInstance(levels_value[26], float)
                self.assertIsInstance(levels_value[27], float)
                self.assertIsInstance(levels_value[28], float)
                self.assertIsInstance(levels_value[29], float)

                
        a_pairs = e.ensdf_pairs(edata,"A")
        for parent, daughter in a_pairs.items():
            a_levels = e.get_levels_and_gammas_subshells(edata, str(parent[0]), int(parent[3]), mode="A",subshell='calc')
            self.assertIsInstance(a_levels, list)
            self.assertIsInstance(a_levels, Iterable)
            #self.assertGreater(len(a_levels), 0)
            for levels_value in a_levels:
                # Unpack the list  contents
                self.assertIsInstance(levels_value[0], int)
                self.assertIsInstance(levels_value[1], int)
                
                try:
                    self.assertIsInstance(levels_value[2], float)
                except AssertionError:
                    try:
                        # Sometimes <int>
                        self.assertIsInstance(levels_value[2], int)
                    except AssertionError:
                        # Sometimes <str>
                        self.assertIsInstance(levels_value[2], str)
                try:
                    self.assertIsInstance(levels_value[3], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[3], int)
                        
                self.assertIsInstance(levels_value[4], int)
                self.assertIsInstance(levels_value[5], int)
                
                try:
                    self.assertIsInstance(levels_value[6], float)
                except AssertionError:
                    try:
                        # Sometimes <int>
                        self.assertIsInstance(levels_value[6], int)
                    except AssertionError:
                        # Sometimes <str>
                        self.assertIsInstance(levels_value[6], str)
                try:
                    self.assertIsInstance(levels_value[7], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[7], int)

                try:
                    self.assertIsInstance(levels_value[8], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[8], int)
                try:
                    self.assertIsInstance(levels_value[9], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[9], int)

                try:
                    self.assertIsInstance(levels_value[10], str)
                except AssertionError:
                    self.assertIsNone(levels_value[10])
                
                try:
                    self.assertIsInstance(levels_value[11], float)
                except AssertionError:
                    self.assertIsNone(levels_value[11])
                try:
                    self.assertIsInstance(levels_value[12], float)
                except AssertionError:
                    self.assertIsNone(levels_value[12])
                self.assertIsInstance(levels_value[13], int)
                
                try:
                    self.assertIsInstance(levels_value[14], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[14], int)
                try:
                    self.assertIsInstance(levels_value[15], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[15], int)

                self.assertIsInstance(levels_value[16], float)
                self.assertIsInstance(levels_value[17], float)
                self.assertIsInstance(levels_value[18], float)
                self.assertIsInstance(levels_value[19], float)
                self.assertIsInstance(levels_value[20], float)
                self.assertIsInstance(levels_value[21], float)
                self.assertIsInstance(levels_value[22], float)
                self.assertIsInstance(levels_value[23], float)
                self.assertIsInstance(levels_value[24], float)
                self.assertIsInstance(levels_value[25], float)
                self.assertIsInstance(levels_value[26], float)
                self.assertIsInstance(levels_value[27], float)
                self.assertIsInstance(levels_value[28], float)
                self.assertIsInstance(levels_value[29], float)


        # 'ratio'
        ecbp_pairs = e.ensdf_pairs(edata,"ECBP") 
        for parent, daughter in ecbp_pairs.items():
            ecbp_levels = e.get_levels_and_gammas_subshells(edata, str(parent[0]), int(parent[3]), mode="ECBP",subshell='ratio')
            self.assertIsInstance(ecbp_levels, list)
            self.assertIsInstance(ecbp_levels, Iterable)
            #self.assertGreater(len(ecbp_levels), 0)
            for levels_value in ecbp_levels:
                # Unpack the list  contents
                self.assertIsInstance(levels_value[0], int)
                self.assertIsInstance(levels_value[1], int)
                
                try:
                    self.assertIsInstance(levels_value[2], float)
                except AssertionError:
                    try:
                        # Sometimes <int>
                        self.assertIsInstance(levels_value[2], int)
                    except AssertionError:
                        # Sometimes <str>
                        self.assertIsInstance(levels_value[2], str)
                try:
                    self.assertIsInstance(levels_value[3], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[3], int)
                        
                self.assertIsInstance(levels_value[4], int)
                self.assertIsInstance(levels_value[5], int)
                
                try:
                    self.assertIsInstance(levels_value[6], float)
                except AssertionError:
                    try:
                        # Sometimes <int>
                        self.assertIsInstance(levels_value[6], int)
                    except AssertionError:
                        # Sometimes <str>
                        self.assertIsInstance(levels_value[6], str)
                try:
                    self.assertIsInstance(levels_value[7], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[7], int)

                try:
                    self.assertIsInstance(levels_value[8], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[8], int)
                try:
                    self.assertIsInstance(levels_value[9], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[9], int)

                try:
                    self.assertIsInstance(levels_value[10], str)
                except AssertionError:
                    self.assertIsNone(levels_value[10])
                    
                try:
                    self.assertIsInstance(levels_value[11], float)
                except AssertionError:
                    self.assertIsNone(levels_value[11])
                try:
                    self.assertIsInstance(levels_value[12], float)
                except AssertionError:
                    self.assertIsNone(levels_value[12])
                self.assertIsInstance(levels_value[13], int)
                
                try:
                    self.assertIsInstance(levels_value[14], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[14], int)
                try:
                    self.assertIsInstance(levels_value[15], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[15], int)

                self.assertIsInstance(levels_value[16], float)
                self.assertIsInstance(levels_value[17], float)
                self.assertIsInstance(levels_value[18], float)
                self.assertIsInstance(levels_value[19], float)
                self.assertIsInstance(levels_value[20], float)
                self.assertIsInstance(levels_value[21], float)
                self.assertIsInstance(levels_value[22], float)
                self.assertIsInstance(levels_value[23], float)
                self.assertIsInstance(levels_value[24], float)
                self.assertIsInstance(levels_value[25], float)
                self.assertIsInstance(levels_value[26], float)
                self.assertIsInstance(levels_value[27], float)
                self.assertIsInstance(levels_value[28], float)
                self.assertIsInstance(levels_value[29], float)
                    

        bm_pairs = e.ensdf_pairs(edata,"BM")
        for parent, daughter in bm_pairs.items():
            bm_levels = e.get_levels_and_gammas_subshells(edata, str(parent[0]), int(parent[3]), mode="BM",subshell='ratio')
            self.assertIsInstance(bm_levels, list)
            self.assertIsInstance(bm_levels, Iterable)
            #self.assertGreater(len(bm_levels), 0)
            for levels_value in bm_levels:
                # Unpack the list  contents
                self.assertIsInstance(levels_value[0], int)
                self.assertIsInstance(levels_value[1], int)
                
                try:
                    self.assertIsInstance(levels_value[2], float)
                except AssertionError:
                    try:
                        # Sometimes <int>
                        self.assertIsInstance(levels_value[2], int)
                    except AssertionError:
                        # Sometimes <str>
                        self.assertIsInstance(levels_value[2], str)
                try:
                    self.assertIsInstance(levels_value[3], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[3], int)
                        
                self.assertIsInstance(levels_value[4], int)
                self.assertIsInstance(levels_value[5], int)
                
                try:
                    self.assertIsInstance(levels_value[6], float)
                except AssertionError:
                    try:
                        # Sometimes <int>
                        self.assertIsInstance(levels_value[6], int)
                    except AssertionError:
                        # Sometimes <str>
                        self.assertIsInstance(levels_value[6], str)
                try:
                    self.assertIsInstance(levels_value[7], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[7], int)

                try:
                    self.assertIsInstance(levels_value[8], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[8], int)
                try:
                    self.assertIsInstance(levels_value[9], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[9], int)

                try:
                    self.assertIsInstance(levels_value[10], str)
                except AssertionError:
                    self.assertIsNone(levels_value[10])
                
                try:
                    self.assertIsInstance(levels_value[11], float)
                except AssertionError:
                    self.assertIsNone(levels_value[11])
                try:
                    self.assertIsInstance(levels_value[12], float)
                except AssertionError:
                    self.assertIsNone(levels_value[12])
                self.assertIsInstance(levels_value[13], int)
                
                try:
                    self.assertIsInstance(levels_value[14], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[14], int)
                try:
                    self.assertIsInstance(levels_value[15], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[15], int)

                self.assertIsInstance(levels_value[16], float)
                self.assertIsInstance(levels_value[17], float)
                self.assertIsInstance(levels_value[18], float)
                self.assertIsInstance(levels_value[19], float)
                self.assertIsInstance(levels_value[20], float)
                self.assertIsInstance(levels_value[21], float)
                self.assertIsInstance(levels_value[22], float)
                self.assertIsInstance(levels_value[23], float)
                self.assertIsInstance(levels_value[24], float)
                self.assertIsInstance(levels_value[25], float)
                self.assertIsInstance(levels_value[26], float)
                self.assertIsInstance(levels_value[27], float)
                self.assertIsInstance(levels_value[28], float)
                self.assertIsInstance(levels_value[29], float)

                
        a_pairs = e.ensdf_pairs(edata,"A")
        for parent, daughter in a_pairs.items():
            a_levels = e.get_levels_and_gammas_subshells(edata, str(parent[0]), int(parent[3]), mode="A",subshell='ratio')
            self.assertIsInstance(a_levels, list)
            self.assertIsInstance(a_levels, Iterable)
            #self.assertGreater(len(a_levels), 0)
            for levels_value in a_levels:
                # Unpack the list  contents
                self.assertIsInstance(levels_value[0], int)
                self.assertIsInstance(levels_value[1], int)
                
                try:
                    self.assertIsInstance(levels_value[2], float)
                except AssertionError:
                    try:
                        # Sometimes <int>
                        self.assertIsInstance(levels_value[2], int)
                    except AssertionError:
                        # Sometimes <str>
                        self.assertIsInstance(levels_value[2], str)
                try:
                    self.assertIsInstance(levels_value[3], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[3], int)
                        
                self.assertIsInstance(levels_value[4], int)
                self.assertIsInstance(levels_value[5], int)
                
                try:
                    self.assertIsInstance(levels_value[6], float)
                except AssertionError:
                    try:
                        # Sometimes <int>
                        self.assertIsInstance(levels_value[6], int)
                    except AssertionError:
                        # Sometimes <str>
                        self.assertIsInstance(levels_value[6], str)
                try:
                    self.assertIsInstance(levels_value[7], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[7], int)

                try:
                    self.assertIsInstance(levels_value[8], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[8], int)
                try:
                    self.assertIsInstance(levels_value[9], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[9], int)

                try:
                    self.assertIsInstance(levels_value[10], str)
                except AssertionError:
                    self.assertIsNone(levels_value[10])
                
                try:
                    self.assertIsInstance(levels_value[11], float)
                except AssertionError:
                    self.assertIsNone(levels_value[11])
                try:
                    self.assertIsInstance(levels_value[12], float)
                except AssertionError:
                    self.assertIsNone(levels_value[12])
                self.assertIsInstance(levels_value[13], int)
                
                try:
                    self.assertIsInstance(levels_value[14], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[14], int)
                try:
                    self.assertIsInstance(levels_value[15], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[15], int)

                self.assertIsInstance(levels_value[16], float)
                self.assertIsInstance(levels_value[17], float)
                self.assertIsInstance(levels_value[18], float)
                self.assertIsInstance(levels_value[19], float)
                self.assertIsInstance(levels_value[20], float)
                self.assertIsInstance(levels_value[21], float)
                self.assertIsInstance(levels_value[22], float)
                self.assertIsInstance(levels_value[23], float)
                self.assertIsInstance(levels_value[24], float)
                self.assertIsInstance(levels_value[25], float)
                self.assertIsInstance(levels_value[26], float)
                self.assertIsInstance(levels_value[27], float)
                self.assertIsInstance(levels_value[28], float)
                self.assertIsInstance(levels_value[29], float)


        # 'expt'
        ecbp_pairs = e.ensdf_pairs(edata,"ECBP") 
        for parent, daughter in ecbp_pairs.items():
            ecbp_levels = e.get_levels_and_gammas_subshells(edata, str(parent[0]), int(parent[3]), mode="ECBP",subshell='expt')
            self.assertIsInstance(ecbp_levels, list)
            self.assertIsInstance(ecbp_levels, Iterable)
            #self.assertGreater(len(ecbp_levels), 0)
            for levels_value in ecbp_levels:
                # Unpack the list  contents
                self.assertIsInstance(levels_value[0], int)
                self.assertIsInstance(levels_value[1], int)
                
                try:
                    self.assertIsInstance(levels_value[2], float)
                except AssertionError:
                    try:
                        # Sometimes <int>
                        self.assertIsInstance(levels_value[2], int)
                    except AssertionError:
                        # Sometimes <str>
                        self.assertIsInstance(levels_value[2], str)
                try:
                    self.assertIsInstance(levels_value[3], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[3], int)
                        
                self.assertIsInstance(levels_value[4], int)
                self.assertIsInstance(levels_value[5], int)
                
                try:
                    self.assertIsInstance(levels_value[6], float)
                except AssertionError:
                    try:
                        # Sometimes <int>
                        self.assertIsInstance(levels_value[6], int)
                    except AssertionError:
                        # Sometimes <str>
                        self.assertIsInstance(levels_value[6], str)
                try:
                    self.assertIsInstance(levels_value[7], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[7], int)

                try:
                    self.assertIsInstance(levels_value[8], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[8], int)
                try:
                    self.assertIsInstance(levels_value[9], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[9], int)

                try:
                    self.assertIsInstance(levels_value[10], str)
                except AssertionError:
                    self.assertIsNone(levels_value[10])
                    
                try:
                    self.assertIsInstance(levels_value[11], float)
                except AssertionError:
                    self.assertIsNone(levels_value[11])
                try:
                    self.assertIsInstance(levels_value[12], float)
                except AssertionError:
                    self.assertIsNone(levels_value[12])
                self.assertIsInstance(levels_value[13], int)
                
                try:
                    self.assertIsInstance(levels_value[14], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[14], int)
                try:
                    self.assertIsInstance(levels_value[15], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[15], int)

                self.assertIsInstance(levels_value[16], float)
                self.assertIsInstance(levels_value[17], float)
                self.assertIsInstance(levels_value[18], float)
                self.assertIsInstance(levels_value[19], float)
                self.assertIsInstance(levels_value[20], float)
                self.assertIsInstance(levels_value[21], float)
                self.assertIsInstance(levels_value[22], float)
                self.assertIsInstance(levels_value[23], float)
                self.assertIsInstance(levels_value[24], float)
                self.assertIsInstance(levels_value[25], float)
                self.assertIsInstance(levels_value[26], float)
                self.assertIsInstance(levels_value[27], float)
                self.assertIsInstance(levels_value[28], float)
                self.assertIsInstance(levels_value[29], float)
                    

        bm_pairs = e.ensdf_pairs(edata,"BM")
        for parent, daughter in bm_pairs.items():
            bm_levels = e.get_levels_and_gammas_subshells(edata, str(parent[0]), int(parent[3]), mode="BM",subshell='expt')
            self.assertIsInstance(bm_levels, list)
            self.assertIsInstance(bm_levels, Iterable)
            #self.assertGreater(len(bm_levels), 0)
            for levels_value in bm_levels:
                # Unpack the list  contents
                self.assertIsInstance(levels_value[0], int)
                self.assertIsInstance(levels_value[1], int)
                
                try:
                    self.assertIsInstance(levels_value[2], float)
                except AssertionError:
                    try:
                        # Sometimes <int>
                        self.assertIsInstance(levels_value[2], int)
                    except AssertionError:
                        # Sometimes <str>
                        self.assertIsInstance(levels_value[2], str)
                try:
                    self.assertIsInstance(levels_value[3], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[3], int)
                        
                self.assertIsInstance(levels_value[4], int)
                self.assertIsInstance(levels_value[5], int)
                
                try:
                    self.assertIsInstance(levels_value[6], float)
                except AssertionError:
                    try:
                        # Sometimes <int>
                        self.assertIsInstance(levels_value[6], int)
                    except AssertionError:
                        # Sometimes <str>
                        self.assertIsInstance(levels_value[6], str)
                try:
                    self.assertIsInstance(levels_value[7], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[7], int)

                try:
                    self.assertIsInstance(levels_value[8], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[8], int)
                try:
                    self.assertIsInstance(levels_value[9], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[9], int)

                try:
                    self.assertIsInstance(levels_value[10], str)
                except AssertionError:
                    self.assertIsNone(levels_value[10])
                
                try:
                    self.assertIsInstance(levels_value[11], float)
                except AssertionError:
                    self.assertIsNone(levels_value[11])
                try:
                    self.assertIsInstance(levels_value[12], float)
                except AssertionError:
                    self.assertIsNone(levels_value[12])
                self.assertIsInstance(levels_value[13], int)
                
                try:
                    self.assertIsInstance(levels_value[14], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[14], int)
                try:
                    self.assertIsInstance(levels_value[15], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[15], int)

                self.assertIsInstance(levels_value[16], float)
                self.assertIsInstance(levels_value[17], float)
                self.assertIsInstance(levels_value[18], float)
                self.assertIsInstance(levels_value[19], float)
                self.assertIsInstance(levels_value[20], float)
                self.assertIsInstance(levels_value[21], float)
                self.assertIsInstance(levels_value[22], float)
                self.assertIsInstance(levels_value[23], float)
                self.assertIsInstance(levels_value[24], float)
                self.assertIsInstance(levels_value[25], float)
                self.assertIsInstance(levels_value[26], float)
                self.assertIsInstance(levels_value[27], float)
                self.assertIsInstance(levels_value[28], float)
                self.assertIsInstance(levels_value[29], float)

                
        a_pairs = e.ensdf_pairs(edata,"A")
        for parent, daughter in a_pairs.items():
            a_levels = e.get_levels_and_gammas_subshells(edata, str(parent[0]), int(parent[3]), mode="A",subshell='expt')
            self.assertIsInstance(a_levels, list)
            self.assertIsInstance(a_levels, Iterable)
            #self.assertGreater(len(a_levels), 0)
            for levels_value in a_levels:
                # Unpack the list  contents
                self.assertIsInstance(levels_value[0], int)
                self.assertIsInstance(levels_value[1], int)
                
                try:
                    self.assertIsInstance(levels_value[2], float)
                except AssertionError:
                    try:
                        # Sometimes <int>
                        self.assertIsInstance(levels_value[2], int)
                    except AssertionError:
                        # Sometimes <str>
                        self.assertIsInstance(levels_value[2], str)
                try:
                    self.assertIsInstance(levels_value[3], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[3], int)
                        
                self.assertIsInstance(levels_value[4], int)
                self.assertIsInstance(levels_value[5], int)
                
                try:
                    self.assertIsInstance(levels_value[6], float)
                except AssertionError:
                    try:
                        # Sometimes <int>
                        self.assertIsInstance(levels_value[6], int)
                    except AssertionError:
                        # Sometimes <str>
                        self.assertIsInstance(levels_value[6], str)
                try:
                    self.assertIsInstance(levels_value[7], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[7], int)

                try:
                    self.assertIsInstance(levels_value[8], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[8], int)
                try:
                    self.assertIsInstance(levels_value[9], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[9], int)

                try:
                    self.assertIsInstance(levels_value[10], str)
                except AssertionError:
                    self.assertIsNone(levels_value[10])
                
                try:
                    self.assertIsInstance(levels_value[11], float)
                except AssertionError:
                    self.assertIsNone(levels_value[11])
                try:
                    self.assertIsInstance(levels_value[12], float)
                except AssertionError:
                    self.assertIsNone(levels_value[12])
                self.assertIsInstance(levels_value[13], int)
                
                try:
                    self.assertIsInstance(levels_value[14], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[14], int)
                try:
                    self.assertIsInstance(levels_value[15], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[15], int)

                self.assertIsInstance(levels_value[16], float)
                self.assertIsInstance(levels_value[17], float)
                self.assertIsInstance(levels_value[18], float)
                self.assertIsInstance(levels_value[19], float)
                self.assertIsInstance(levels_value[20], float)
                self.assertIsInstance(levels_value[21], float)
                self.assertIsInstance(levels_value[22], float)
                self.assertIsInstance(levels_value[23], float)
                self.assertIsInstance(levels_value[24], float)
                self.assertIsInstance(levels_value[25], float)
                self.assertIsInstance(levels_value[26], float)
                self.assertIsInstance(levels_value[27], float)
                self.assertIsInstance(levels_value[28], float)
                self.assertIsInstance(levels_value[29], float)


        # 'electron'
        ecbp_pairs = e.ensdf_pairs(edata,"ECBP") 
        for parent, daughter in ecbp_pairs.items():
            ecbp_levels = e.get_levels_and_gammas_subshells(edata, str(parent[0]), int(parent[3]), mode="ECBP",subshell='electron')
            self.assertIsInstance(ecbp_levels, list)
            self.assertIsInstance(ecbp_levels, Iterable)
            #self.assertGreater(len(ecbp_levels), 0)
            for levels_value in ecbp_levels:
                # Unpack the list  contents
                self.assertIsInstance(levels_value[0], int)
                self.assertIsInstance(levels_value[1], int)
                
                try:
                    self.assertIsInstance(levels_value[2], float)
                except AssertionError:
                    try:
                        # Sometimes <int>
                        self.assertIsInstance(levels_value[2], int)
                    except AssertionError:
                        # Sometimes <str>
                        self.assertIsInstance(levels_value[2], str)
                try:
                    self.assertIsInstance(levels_value[3], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[3], int)
                        
                self.assertIsInstance(levels_value[4], int)
                self.assertIsInstance(levels_value[5], int)
                
                try:
                    self.assertIsInstance(levels_value[6], float)
                except AssertionError:
                    try:
                        # Sometimes <int>
                        self.assertIsInstance(levels_value[6], int)
                    except AssertionError:
                        # Sometimes <str>
                        self.assertIsInstance(levels_value[6], str)
                try:
                    self.assertIsInstance(levels_value[7], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[7], int)

                try:
                    self.assertIsInstance(levels_value[8], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[8], int)
                try:
                    self.assertIsInstance(levels_value[9], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[9], int)

                try:
                    self.assertIsInstance(levels_value[10], str)
                except AssertionError:
                    self.assertIsNone(levels_value[10])
                    
                try:
                    self.assertIsInstance(levels_value[11], float)
                except AssertionError:
                    self.assertIsNone(levels_value[11])
                try:
                    self.assertIsInstance(levels_value[12], float)
                except AssertionError:
                    self.assertIsNone(levels_value[12])
                self.assertIsInstance(levels_value[13], int)
                
                try:
                    self.assertIsInstance(levels_value[14], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[14], int)
                try:
                    self.assertIsInstance(levels_value[15], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[15], int)

                self.assertIsInstance(levels_value[16], float)
                self.assertIsInstance(levels_value[17], float)
                self.assertIsInstance(levels_value[18], float)
                self.assertIsInstance(levels_value[19], float)
                self.assertIsInstance(levels_value[20], float)
                self.assertIsInstance(levels_value[21], float)
                self.assertIsInstance(levels_value[22], float)
                self.assertIsInstance(levels_value[23], float)
                self.assertIsInstance(levels_value[24], float)
                self.assertIsInstance(levels_value[25], float)
                self.assertIsInstance(levels_value[26], float)
                self.assertIsInstance(levels_value[27], float)
                self.assertIsInstance(levels_value[28], float)
                self.assertIsInstance(levels_value[29], float)
                    

        bm_pairs = e.ensdf_pairs(edata,"BM")
        for parent, daughter in bm_pairs.items():
            bm_levels = e.get_levels_and_gammas_subshells(edata, str(parent[0]), int(parent[3]), mode="BM",subshell='electron')
            self.assertIsInstance(bm_levels, list)
            self.assertIsInstance(bm_levels, Iterable)
            #self.assertGreater(len(bm_levels), 0)
            for levels_value in bm_levels:
                # Unpack the list  contents
                self.assertIsInstance(levels_value[0], int)
                self.assertIsInstance(levels_value[1], int)
                
                try:
                    self.assertIsInstance(levels_value[2], float)
                except AssertionError:
                    try:
                        # Sometimes <int>
                        self.assertIsInstance(levels_value[2], int)
                    except AssertionError:
                        # Sometimes <str>
                        self.assertIsInstance(levels_value[2], str)
                try:
                    self.assertIsInstance(levels_value[3], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[3], int)
                        
                self.assertIsInstance(levels_value[4], int)
                self.assertIsInstance(levels_value[5], int)
                
                try:
                    self.assertIsInstance(levels_value[6], float)
                except AssertionError:
                    try:
                        # Sometimes <int>
                        self.assertIsInstance(levels_value[6], int)
                    except AssertionError:
                        # Sometimes <str>
                        self.assertIsInstance(levels_value[6], str)
                try:
                    self.assertIsInstance(levels_value[7], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[7], int)

                try:
                    self.assertIsInstance(levels_value[8], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[8], int)
                try:
                    self.assertIsInstance(levels_value[9], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[9], int)

                try:
                    self.assertIsInstance(levels_value[10], str)
                except AssertionError:
                    self.assertIsNone(levels_value[10])
                
                try:
                    self.assertIsInstance(levels_value[11], float)
                except AssertionError:
                    self.assertIsNone(levels_value[11])
                try:
                    self.assertIsInstance(levels_value[12], float)
                except AssertionError:
                    self.assertIsNone(levels_value[12])
                self.assertIsInstance(levels_value[13], int)
                
                try:
                    self.assertIsInstance(levels_value[14], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[14], int)
                try:
                    self.assertIsInstance(levels_value[15], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[15], int)

                self.assertIsInstance(levels_value[16], float)
                self.assertIsInstance(levels_value[17], float)
                self.assertIsInstance(levels_value[18], float)
                self.assertIsInstance(levels_value[19], float)
                self.assertIsInstance(levels_value[20], float)
                self.assertIsInstance(levels_value[21], float)
                self.assertIsInstance(levels_value[22], float)
                self.assertIsInstance(levels_value[23], float)
                self.assertIsInstance(levels_value[24], float)
                self.assertIsInstance(levels_value[25], float)
                self.assertIsInstance(levels_value[26], float)
                self.assertIsInstance(levels_value[27], float)
                self.assertIsInstance(levels_value[28], float)
                self.assertIsInstance(levels_value[29], float)

                
        a_pairs = e.ensdf_pairs(edata,"A")
        for parent, daughter in a_pairs.items():
            a_levels = e.get_levels_and_gammas_subshells(edata, str(parent[0]), int(parent[3]), mode="A",subshell='electron')
            self.assertIsInstance(a_levels, list)
            self.assertIsInstance(a_levels, Iterable)
            #self.assertGreater(len(a_levels), 0)
            for levels_value in a_levels:
                # Unpack the list  contents
                self.assertIsInstance(levels_value[0], int)
                self.assertIsInstance(levels_value[1], int)
                
                try:
                    self.assertIsInstance(levels_value[2], float)
                except AssertionError:
                    try:
                        # Sometimes <int>
                        self.assertIsInstance(levels_value[2], int)
                    except AssertionError:
                        # Sometimes <str>
                        self.assertIsInstance(levels_value[2], str)
                try:
                    self.assertIsInstance(levels_value[3], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[3], int)
                        
                self.assertIsInstance(levels_value[4], int)
                self.assertIsInstance(levels_value[5], int)
                
                try:
                    self.assertIsInstance(levels_value[6], float)
                except AssertionError:
                    try:
                        # Sometimes <int>
                        self.assertIsInstance(levels_value[6], int)
                    except AssertionError:
                        # Sometimes <str>
                        self.assertIsInstance(levels_value[6], str)
                try:
                    self.assertIsInstance(levels_value[7], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[7], int)

                try:
                    self.assertIsInstance(levels_value[8], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[8], int)
                try:
                    self.assertIsInstance(levels_value[9], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[9], int)

                try:
                    self.assertIsInstance(levels_value[10], str)
                except AssertionError:
                    self.assertIsNone(levels_value[10])
                
                try:
                    self.assertIsInstance(levels_value[11], float)
                except AssertionError:
                    self.assertIsNone(levels_value[11])
                try:
                    self.assertIsInstance(levels_value[12], float)
                except AssertionError:
                    self.assertIsNone(levels_value[12])
                self.assertIsInstance(levels_value[13], int)
                
                try:
                    self.assertIsInstance(levels_value[14], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[14], int)
                try:
                    self.assertIsInstance(levels_value[15], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[15], int)

                self.assertIsInstance(levels_value[16], float)
                self.assertIsInstance(levels_value[17], float)
                self.assertIsInstance(levels_value[18], float)
                self.assertIsInstance(levels_value[19], float)
                self.assertIsInstance(levels_value[20], float)
                self.assertIsInstance(levels_value[21], float)
                self.assertIsInstance(levels_value[22], float)
                self.assertIsInstance(levels_value[23], float)
                self.assertIsInstance(levels_value[24], float)
                self.assertIsInstance(levels_value[25], float)
                self.assertIsInstance(levels_value[26], float)
                self.assertIsInstance(levels_value[27], float)
                self.assertIsInstance(levels_value[28], float)
                self.assertIsInstance(levels_value[29], float)


        # 'sumcalc'
        ecbp_pairs = e.ensdf_pairs(edata,"ECBP") 
        for parent, daughter in ecbp_pairs.items():
            ecbp_levels = e.get_levels_and_gammas_subshells(edata, str(parent[0]), int(parent[3]), mode="ECBP",subshell='sumcalc')
            self.assertIsInstance(ecbp_levels, list)
            self.assertIsInstance(ecbp_levels, Iterable)
            #self.assertGreater(len(ecbp_levels), 0)
            for levels_value in ecbp_levels:
                # Unpack the list  contents
                self.assertIsInstance(levels_value[0], int)
                self.assertIsInstance(levels_value[1], int)
                
                try:
                    self.assertIsInstance(levels_value[2], float)
                except AssertionError:
                    try:
                        # Sometimes <int>
                        self.assertIsInstance(levels_value[2], int)
                    except AssertionError:
                        # Sometimes <str>
                        self.assertIsInstance(levels_value[2], str)
                try:
                    self.assertIsInstance(levels_value[3], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[3], int)
                        
                self.assertIsInstance(levels_value[4], int)
                self.assertIsInstance(levels_value[5], int)
                
                try:
                    self.assertIsInstance(levels_value[6], float)
                except AssertionError:
                    try:
                        # Sometimes <int>
                        self.assertIsInstance(levels_value[6], int)
                    except AssertionError:
                        # Sometimes <str>
                        self.assertIsInstance(levels_value[6], str)
                try:
                    self.assertIsInstance(levels_value[7], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[7], int)

                try:
                    self.assertIsInstance(levels_value[8], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[8], int)
                try:
                    self.assertIsInstance(levels_value[9], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[9], int)

                try:
                    self.assertIsInstance(levels_value[10], str)
                except AssertionError:
                    self.assertIsNone(levels_value[10])
                    
                try:
                    self.assertIsInstance(levels_value[11], float)
                except AssertionError:
                    self.assertIsNone(levels_value[11])
                try:
                    self.assertIsInstance(levels_value[12], float)
                except AssertionError:
                    self.assertIsNone(levels_value[12])
                self.assertIsInstance(levels_value[13], int)
                
                try:
                    self.assertIsInstance(levels_value[14], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[14], int)
                try:
                    self.assertIsInstance(levels_value[15], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[15], int)

                self.assertIsInstance(levels_value[16], float)
                self.assertIsInstance(levels_value[17], float)
                self.assertIsInstance(levels_value[18], float)
                self.assertIsInstance(levels_value[19], float)
                self.assertIsInstance(levels_value[20], float)
                self.assertIsInstance(levels_value[21], float)
                self.assertIsInstance(levels_value[22], float)
                self.assertIsInstance(levels_value[23], float)
                self.assertIsInstance(levels_value[24], float)
                self.assertIsInstance(levels_value[25], float)
                self.assertIsInstance(levels_value[26], float)
                self.assertIsInstance(levels_value[27], float)
                    

        bm_pairs = e.ensdf_pairs(edata,"BM")
        for parent, daughter in bm_pairs.items():
            bm_levels = e.get_levels_and_gammas_subshells(edata, str(parent[0]), int(parent[3]), mode="BM",subshell='sumcalc')
            self.assertIsInstance(bm_levels, list)
            self.assertIsInstance(bm_levels, Iterable)
            #self.assertGreater(len(bm_levels), 0)
            for levels_value in bm_levels:
                # Unpack the list  contents
                self.assertIsInstance(levels_value[0], int)
                self.assertIsInstance(levels_value[1], int)
                
                try:
                    self.assertIsInstance(levels_value[2], float)
                except AssertionError:
                    try:
                        # Sometimes <int>
                        self.assertIsInstance(levels_value[2], int)
                    except AssertionError:
                        # Sometimes <str>
                        self.assertIsInstance(levels_value[2], str)
                try:
                    self.assertIsInstance(levels_value[3], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[3], int)
                        
                self.assertIsInstance(levels_value[4], int)
                self.assertIsInstance(levels_value[5], int)
                
                try:
                    self.assertIsInstance(levels_value[6], float)
                except AssertionError:
                    try:
                        # Sometimes <int>
                        self.assertIsInstance(levels_value[6], int)
                    except AssertionError:
                        # Sometimes <str>
                        self.assertIsInstance(levels_value[6], str)
                try:
                    self.assertIsInstance(levels_value[7], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[7], int)

                try:
                    self.assertIsInstance(levels_value[8], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[8], int)
                try:
                    self.assertIsInstance(levels_value[9], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[9], int)

                try:
                    self.assertIsInstance(levels_value[10], str)
                except AssertionError:
                    self.assertIsNone(levels_value[10])
                
                try:
                    self.assertIsInstance(levels_value[11], float)
                except AssertionError:
                    self.assertIsNone(levels_value[11])
                try:
                    self.assertIsInstance(levels_value[12], float)
                except AssertionError:
                    self.assertIsNone(levels_value[12])
                self.assertIsInstance(levels_value[13], int)
                
                try:
                    self.assertIsInstance(levels_value[14], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[14], int)
                try:
                    self.assertIsInstance(levels_value[15], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[15], int)

                self.assertIsInstance(levels_value[16], float)
                self.assertIsInstance(levels_value[17], float)
                self.assertIsInstance(levels_value[18], float)
                self.assertIsInstance(levels_value[19], float)
                self.assertIsInstance(levels_value[20], float)
                self.assertIsInstance(levels_value[21], float)
                self.assertIsInstance(levels_value[22], float)
                self.assertIsInstance(levels_value[23], float)
                self.assertIsInstance(levels_value[24], float)
                self.assertIsInstance(levels_value[25], float)
                self.assertIsInstance(levels_value[26], float)
                self.assertIsInstance(levels_value[27], float)

                
        a_pairs = e.ensdf_pairs(edata,"A")
        for parent, daughter in a_pairs.items():
            a_levels = e.get_levels_and_gammas_subshells(edata, str(parent[0]), int(parent[3]), mode="A",subshell='sumcalc')
            self.assertIsInstance(a_levels, list)
            self.assertIsInstance(a_levels, Iterable)
            #self.assertGreater(len(a_levels), 0)
            for levels_value in a_levels:
                # Unpack the list  contents
                self.assertIsInstance(levels_value[0], int)
                self.assertIsInstance(levels_value[1], int)
                
                try:
                    self.assertIsInstance(levels_value[2], float)
                except AssertionError:
                    try:
                        # Sometimes <int>
                        self.assertIsInstance(levels_value[2], int)
                    except AssertionError:
                        # Sometimes <str>
                        self.assertIsInstance(levels_value[2], str)
                try:
                    self.assertIsInstance(levels_value[3], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[3], int)
                        
                self.assertIsInstance(levels_value[4], int)
                self.assertIsInstance(levels_value[5], int)
                
                try:
                    self.assertIsInstance(levels_value[6], float)
                except AssertionError:
                    try:
                        # Sometimes <int>
                        self.assertIsInstance(levels_value[6], int)
                    except AssertionError:
                        # Sometimes <str>
                        self.assertIsInstance(levels_value[6], str)
                try:
                    self.assertIsInstance(levels_value[7], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[7], int)

                try:
                    self.assertIsInstance(levels_value[8], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[8], int)
                try:
                    self.assertIsInstance(levels_value[9], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[9], int)

                try:
                    self.assertIsInstance(levels_value[10], str)
                except AssertionError:
                    self.assertIsNone(levels_value[10])
                
                try:
                    self.assertIsInstance(levels_value[11], float)
                except AssertionError:
                    self.assertIsNone(levels_value[11])
                try:
                    self.assertIsInstance(levels_value[12], float)
                except AssertionError:
                    self.assertIsNone(levels_value[12])
                self.assertIsInstance(levels_value[13], int)
                
                try:
                    self.assertIsInstance(levels_value[14], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[14], int)
                try:
                    self.assertIsInstance(levels_value[15], float)
                except AssertionError:
                    # Sometimes <int>
                    self.assertIsInstance(levels_value[15], int)

                self.assertIsInstance(levels_value[16], float)
                self.assertIsInstance(levels_value[17], float)
                self.assertIsInstance(levels_value[18], float)
                self.assertIsInstance(levels_value[19], float)
                self.assertIsInstance(levels_value[20], float)
                self.assertIsInstance(levels_value[21], float)
                self.assertIsInstance(levels_value[22], float)
                self.assertIsInstance(levels_value[23], float)
                self.assertIsInstance(levels_value[24], float)
                self.assertIsInstance(levels_value[25], float)
                self.assertIsInstance(levels_value[26], float)
                self.assertIsInstance(levels_value[27], float)


class FindMultipleJPi(unittest.TestCase):

    __doc__="""Unit tests for the `find_multiple_jpi` method of 
    the Daughter class."""

    def test_find_multiple_jpi_returns_dict_for_all_decays(self):
        ecbp_pairs = e.ensdf_pairs(edata,"ECBP")
        for parent, daughter in ecbp_pairs.items():
            ecbp = e.find_multiple_jpi(edata, str(parent[0]), int(parent[3]), mode="ECBP")
            self.assertIsInstance(ecbp, dict)
            self.assertIsInstance(ecbp, Iterable)

        bm_pairs = e.ensdf_pairs(edata,"BM")
        for parent, daughter in bm_pairs.items():
            bm = e.find_multiple_jpi(edata, str(parent[0]), int(parent[3]), mode="BM")
            self.assertIsInstance(bm, dict)
            self.assertIsInstance(bm, Iterable)

        a_pairs = e.ensdf_pairs(edata,"A")
        for parent, daughter in a_pairs.items():
            a = e.find_multiple_jpi(edata, str(parent[0]), int(parent[3]), mode="A")
            self.assertIsInstance(a, dict)
            self.assertIsInstance(a, Iterable)

    def test_find_multiple_jpi_returns_none_if_not_correct_decay_mode(self):
        ecbp = e.find_multiple_jpi(edata,"Co60",0,mode="ECBP")
        self.assertIsNone(ecbp)
        bm = e.find_multiple_jpi(edata,"Y86",0,mode="BM")
        self.assertIsNone(bm)
        a = e.find_multiple_jpi(edata,"Na22",0,mode="A")
        self.assertIsNone(a)

    def test_find_multiple_jpi_raises_IndexError_if_missing_kwargs(self):
        with self.assertRaises(IndexError):
            ecbp = e.find_multiple_jpi(edata,"Y86",0)
        with self.assertRaises(IndexError):
            bm = e.find_multiple_jpi(edata,"Co60",0)
        with self.assertRaises(IndexError):
            a = e.find_multiple_jpi(edata,"Ra226",0)

    def test_find_multiple_jpi_returns_none_if_illegal_string(self):
        levels = e.find_multiple_jpi(edata,"Co60", 1, mode="THisIsB@LL@CK$")
        self.assertIsNone(levels)
        levels = e.find_multiple_jpi(edata,"THisIsB@LL@CK$", 1, mode="BM")
        self.assertIsNone(levels)

    def test_find_multiple_jpi_raises_TypeError_if_first_arg_not_list(self):
        with self.assertRaises(TypeError):
            ecbp = e.find_multiple_jpi("Db258",edata,0,mode="ECBP")
        with self.assertRaises(TypeError):
            bm = e.find_multiple_jpi("Co60",edata,1,mode="BM")
        with self.assertRaises(TypeError):
            a = e.find_multiple_jpi("Ra226",edata,0,mode="A")

    def test_find_multiple_jpi_raises_NameError_if_wrong_list(self):
        with self.assertRaises(NameError):
            ecbp = e.find_multiple_jpi(XXXedataXXX,"Db258",0,mode="ECBP")
        with self.assertRaises(NameError):
            bm = e.find_multiple_jpi(XXXedataXXX,"Co60",1,mode="BM")
        with self.assertRaises(NameError):
            a = e.find_multiple_jpi(XXXedataXXX,"Ra226",0,mode="A")

    def test_find_multiple_jpi_raises_KeyError_if_bad_dict_items_in_list(self):
        bad_dict_items_in_list = [{'a':0, 'b':1, 'c':2}]
        with self.assertRaises(KeyError):
           ecbp = e.find_multiple_jpi(bad_dict_items_in_list,"Db258",0,mode="ECBP")
        with self.assertRaises(KeyError):
           bm = e.find_multiple_jpi(bad_dict_items_in_list,"Co60",1,mode="BM")
        with self.assertRaises(KeyError):
           a = e.find_multiple_jpi(bad_dict_items_in_list,"Ra226",0,mode="A")

    def test_find_multiple_jpi_returned_contents_of_dict(self):
        ecbp_pairs = e.ensdf_pairs(edata,"ECBP") 
        for parent, daughter in ecbp_pairs.items():
            ecbp_mjpi = e.find_multiple_jpi(edata, str(parent[0]), int(parent[3]), mode="ECBP")
            self.assertIsInstance(ecbp_mjpi, dict)
            self.assertIsInstance(ecbp_mjpi, Iterable)
            self.assertGreater(len(ecbp_mjpi), 0)
            for mjpi_key, mjpi_value in ecbp_mjpi.items():
                
                self.assertIsInstance(mjpi_key, tuple)
                self.assertIsInstance(mjpi_key, Iterable)
                self.assertEqual(len(mjpi_key), 8)
                self.assertIsInstance(mjpi_value, list)
                self.assertIsInstance(mjpi_value, Iterable)

                # Unpack the tuple key contents
                self.assertIsInstance(mjpi_key[0], str)
                self.assertIsInstance(mjpi_key[1], int)
                self.assertIsInstance(mjpi_key[2], int)
                self.assertIsInstance(mjpi_key[3], int)
                try:
                    self.assertIsInstance(mjpi_key[4], float)
                except AssertionError:
                    self.assertIsInstance(mjpi_key[4], str)
                self.assertIsInstance(mjpi_key[5], str)
                self.assertIsInstance(mjpi_key[6], int)
                self.assertIsInstance(mjpi_key[7], int)
                
                # Unpack the list value contents
                for value in mjpi_value:
                    self.assertIsInstance(value, list)
                    self.assertIsInstance(value, Iterable)
                    self.assertEqual(len(value), 7)
                
                    self.assertIsInstance(value[0], int)
                
                    try:
                        self.assertIsInstance(value[1], float)
                    except AssertionError:
                        try:
                            # Sometimes <int>
                            self.assertIsInstance(value[1], int)
                        except AssertionError:
                            # Sometimes <str>
                            self.assertIsInstance(value[1], str)
                    try:
                        self.assertIsInstance(value[2], float)
                    except AssertionError:
                        # Sometimes <int>
                        self.assertIsInstance(value[2], int)
                        
                    self.assertIsInstance(value[3], int)
                    self.assertIsInstance(value[4], int)
                    try:
                        self.assertIsInstance(value[5], float)
                    except AssertionError:
                        self.assertIsNone(value[5])
                    self.assertIsInstance(value[6], int)
                    

        bm_pairs = e.ensdf_pairs(edata,"BM")
        for parent, daughter in bm_pairs.items():
            bm_mjpi = e.find_multiple_jpi(edata, str(parent[0]), int(parent[3]), mode="BM")
            self.assertIsInstance(bm_mjpi, dict)
            self.assertIsInstance(bm_mjpi, Iterable)
            self.assertGreater(len(bm_mjpi), 0)
            for mjpi_key, mjpi_value in bm_mjpi.items():
                
                self.assertIsInstance(mjpi_key, tuple)
                self.assertIsInstance(mjpi_key, Iterable)
                self.assertEqual(len(mjpi_key), 8)
                self.assertIsInstance(mjpi_value, list)
                self.assertIsInstance(mjpi_value, Iterable)

                # Unpack the tuple key contents
                self.assertIsInstance(mjpi_key[0], str)
                self.assertIsInstance(mjpi_key[1], int)
                self.assertIsInstance(mjpi_key[2], int)
                self.assertIsInstance(mjpi_key[3], int)
                try:
                    self.assertIsInstance(mjpi_key[4], float)
                except AssertionError:
                    self.assertIsInstance(mjpi_key[4], str)
                self.assertIsInstance(mjpi_key[5], str)
                self.assertIsInstance(mjpi_key[6], int)
                self.assertIsInstance(mjpi_key[7], int)
                
                # Unpack the list value contents
                for value in mjpi_value:
                    self.assertIsInstance(value, list)
                    self.assertIsInstance(value, Iterable)
                    self.assertEqual(len(value), 7)
                    
                    self.assertIsInstance(value[0], int)
                
                    try:
                        self.assertIsInstance(value[1], float)
                    except AssertionError:
                        try:
                            # Sometimes <int>
                            self.assertIsInstance(value[1], int)
                        except AssertionError:
                            # Sometimes <str>
                            self.assertIsInstance(value[1], str)
                    try:
                        self.assertIsInstance(value[2], float)
                    except AssertionError:
                        # Sometimes <int>
                        self.assertIsInstance(value[2], int)
                        
                    self.assertIsInstance(value[3], int)
                    self.assertIsInstance(value[4], int)
                    try:
                        self.assertIsInstance(value[5], float)
                    except AssertionError:
                        self.assertIsNone(value[5])
                    self.assertIsInstance(value[6], int)


        a_pairs = e.ensdf_pairs(edata,"A")
        for parent, daughter in a_pairs.items():
            a_mjpi = e.find_multiple_jpi(edata, str(parent[0]), int(parent[3]), mode="A")
            self.assertIsInstance(a_mjpi, dict)
            self.assertIsInstance(a_mjpi, Iterable)
            self.assertGreater(len(a_mjpi), 0)
            for mjpi_key, mjpi_value in a_mjpi.items():
                
                self.assertIsInstance(mjpi_key, tuple)
                self.assertIsInstance(mjpi_key, Iterable)
                self.assertEqual(len(mjpi_key), 8)
                self.assertIsInstance(mjpi_value, list)
                self.assertIsInstance(mjpi_value, Iterable)

                # Unpack the tuple key contents
                self.assertIsInstance(mjpi_key[0], str)
                self.assertIsInstance(mjpi_key[1], int)
                self.assertIsInstance(mjpi_key[2], int)
                self.assertIsInstance(mjpi_key[3], int)
                try:
                    self.assertIsInstance(mjpi_key[4], float)
                except AssertionError:
                    self.assertIsInstance(mjpi_key[4], str)
                self.assertIsInstance(mjpi_key[5], str)
                self.assertIsInstance(mjpi_key[6], int)
                self.assertIsInstance(mjpi_key[7], int)
                
                # Unpack the list value contents
                for value in mjpi_value:
                    self.assertIsInstance(value, list)
                    self.assertIsInstance(value, Iterable)
                    self.assertEqual(len(value), 7)
                    
                    self.assertIsInstance(value[0], int)
                
                    try:
                        self.assertIsInstance(value[1], float)
                    except AssertionError:
                        try:
                            # Sometimes <int>
                            self.assertIsInstance(value[1], int)
                        except AssertionError:
                            # Sometimes <str>
                            self.assertIsInstance(value[1], str)
                    try:
                        self.assertIsInstance(value[2], float)
                    except AssertionError:
                        # Sometimes <int>
                        self.assertIsInstance(value[2], int)
                        
                    self.assertIsInstance(value[3], int)
                    self.assertIsInstance(value[4], int)
                    try:
                        self.assertIsInstance(value[5], float)
                    except AssertionError:
                        self.assertIsNone(value[5])
                    self.assertIsInstance(value[6], int)



class FindUniqueJPi(unittest.TestCase):

    __doc__="""Unit tests for the `find_unique_jpi` method of 
    the Daughter class."""

    def test_find_unique_jpi_returns_dict_for_all_decays(self):
        ecbp_pairs = e.ensdf_pairs(edata,"ECBP")
        for parent, daughter in ecbp_pairs.items():
            ecbp = e.find_unique_jpi(edata, str(parent[0]), int(parent[3]), mode="ECBP")
            self.assertIsInstance(ecbp, dict)
            self.assertIsInstance(ecbp, Iterable)

        bm_pairs = e.ensdf_pairs(edata,"BM")
        for parent, daughter in bm_pairs.items():
            bm = e.find_unique_jpi(edata, str(parent[0]), int(parent[3]), mode="BM")
            self.assertIsInstance(bm, dict)
            self.assertIsInstance(bm, Iterable)

        a_pairs = e.ensdf_pairs(edata,"A")
        for parent, daughter in a_pairs.items():
            a = e.find_unique_jpi(edata, str(parent[0]), int(parent[3]), mode="A")
            self.assertIsInstance(a, dict)
            self.assertIsInstance(a, Iterable)

    def test_find_unique_jpi_returns_none_if_not_correct_decay_mode(self):
        ecbp = e.find_unique_jpi(edata,"Co60",0,mode="ECBP")
        self.assertIsNone(ecbp)
        bm = e.find_unique_jpi(edata,"Y86",0,mode="BM")
        self.assertIsNone(bm)
        a = e.find_unique_jpi(edata,"Na22",0,mode="A")
        self.assertIsNone(a)

    def test_find_unique_jpi_raises_IndexError_if_missing_kwargs(self):
        with self.assertRaises(IndexError):
            ecbp = e.find_unique_jpi(edata,"Y86",0)
        with self.assertRaises(IndexError):
            bm = e.find_unique_jpi(edata,"Co60",0)
        with self.assertRaises(IndexError):
            a = e.find_unique_jpi(edata,"Ra226",0)

    def test_find_unique_jpi_returns_none_if_illegal_string(self):
        levels = e.find_unique_jpi(edata,"Co60", 1, mode="THisIsB@LL@CK$")
        self.assertIsNone(levels)
        levels = e.find_unique_jpi(edata,"THisIsB@LL@CK$", 1, mode="BM")
        self.assertIsNone(levels)

    def test_find_unique_jpi_raises_TypeError_if_first_arg_not_list(self):
        with self.assertRaises(TypeError):
            ecbp = e.find_unique_jpi("Db258",edata,0,mode="ECBP")
        with self.assertRaises(TypeError):
            bm = e.find_unique_jpi("Co60",edata,1,mode="BM")
        with self.assertRaises(TypeError):
            a = e.find_unique_jpi("Ra226",edata,0,mode="A")

    def test_find_unique_jpi_raises_NameError_if_wrong_list(self):
        with self.assertRaises(NameError):
            ecbp = e.find_unique_jpi(XXXedataXXX,"Db258",0,mode="ECBP")
        with self.assertRaises(NameError):
            bm = e.find_unique_jpi(XXXedataXXX,"Co60",1,mode="BM")
        with self.assertRaises(NameError):
            a = e.find_unique_jpi(XXXedataXXX,"Ra226",0,mode="A")

    def test_find_unique_jpi_raises_KeyError_if_bad_dict_items_in_list(self):
        bad_dict_items_in_list = [{'a':0, 'b':1, 'c':2}]
        with self.assertRaises(KeyError):
           ecbp = e.find_unique_jpi(bad_dict_items_in_list,"Db258",0,mode="ECBP")
        with self.assertRaises(KeyError):
           bm = e.find_unique_jpi(bad_dict_items_in_list,"Co60",1,mode="BM")
        with self.assertRaises(KeyError):
           a = e.find_unique_jpi(bad_dict_items_in_list,"Ra226",0,mode="A")

    def test_find_unique_jpi_returned_contents_of_dict(self):
        ecbp_pairs = e.ensdf_pairs(edata,"ECBP") 
        for parent, daughter in ecbp_pairs.items():
            ecbp_ujpi = e.find_unique_jpi(edata, str(parent[0]), int(parent[3]), mode="ECBP")
            self.assertIsInstance(ecbp_ujpi, dict)
            self.assertIsInstance(ecbp_ujpi, Iterable)
            self.assertGreater(len(ecbp_ujpi), 0)
            for ujpi_key, ujpi_value in ecbp_ujpi.items():
                
                self.assertIsInstance(ujpi_key, tuple)
                self.assertIsInstance(ujpi_key, Iterable)
                self.assertEqual(len(ujpi_key), 8)
                self.assertIsInstance(ujpi_value, list)
                self.assertIsInstance(ujpi_value, Iterable)

                # Unpack the tuple key contents
                self.assertIsInstance(ujpi_key[0], str)
                self.assertIsInstance(ujpi_key[1], int)
                self.assertIsInstance(ujpi_key[2], int)
                self.assertIsInstance(ujpi_key[3], int)
                try:
                    self.assertIsInstance(ujpi_key[4], float)
                except AssertionError:
                    self.assertIsInstance(ujpi_key[4], str)
                self.assertIsInstance(ujpi_key[5], str)
                self.assertIsInstance(ujpi_key[6], int)
                self.assertIsInstance(ujpi_key[7], int)
                
                # Unpack the list value contents
                for value in ujpi_value:
                    self.assertIsInstance(value, list)
                    self.assertIsInstance(value, Iterable)
                    self.assertEqual(len(value), 7)
                
                    self.assertIsInstance(value[0], int)
                
                    try:
                        self.assertIsInstance(value[1], float)
                    except AssertionError:
                        try:
                            # Sometimes <int>
                            self.assertIsInstance(value[1], int)
                        except AssertionError:
                            # Sometimes <str>
                            self.assertIsInstance(value[1], str)
                    try:
                        self.assertIsInstance(value[2], float)
                    except AssertionError:
                        # Sometimes <int>
                        self.assertIsInstance(value[2], int)
                        
                    self.assertIsInstance(value[3], int)
                    self.assertIsInstance(value[4], int)
                    try:
                        self.assertIsInstance(value[5], float)
                    except AssertionError:
                        self.assertIsNone(value[5])
                    self.assertIsInstance(value[6], int)
                    

        bm_pairs = e.ensdf_pairs(edata,"BM")
        for parent, daughter in bm_pairs.items():
            bm_ujpi = e.find_unique_jpi(edata, str(parent[0]), int(parent[3]), mode="BM")
            self.assertIsInstance(bm_ujpi, dict)
            self.assertIsInstance(bm_ujpi, Iterable)
            self.assertGreater(len(bm_ujpi), 0)
            for ujpi_key, ujpi_value in bm_ujpi.items():
                
                self.assertIsInstance(ujpi_key, tuple)
                self.assertIsInstance(ujpi_key, Iterable)
                self.assertEqual(len(ujpi_key), 8)
                self.assertIsInstance(ujpi_value, list)
                self.assertIsInstance(ujpi_value, Iterable)

                # Unpack the tuple key contents
                self.assertIsInstance(ujpi_key[0], str)
                self.assertIsInstance(ujpi_key[1], int)
                self.assertIsInstance(ujpi_key[2], int)
                self.assertIsInstance(ujpi_key[3], int)
                try:
                    self.assertIsInstance(ujpi_key[4], float)
                except AssertionError:
                    self.assertIsInstance(ujpi_key[4], str)
                self.assertIsInstance(ujpi_key[5], str)
                self.assertIsInstance(ujpi_key[6], int)
                self.assertIsInstance(ujpi_key[7], int)
                
                # Unpack the list value contents
                for value in ujpi_value:
                    self.assertIsInstance(value, list)
                    self.assertIsInstance(value, Iterable)
                    self.assertEqual(len(value), 7)
                    
                    self.assertIsInstance(value[0], int)
                
                    try:
                        self.assertIsInstance(value[1], float)
                    except AssertionError:
                        try:
                            # Sometimes <int>
                            self.assertIsInstance(value[1], int)
                        except AssertionError:
                            # Sometimes <str>
                            self.assertIsInstance(value[1], str)
                    try:
                        self.assertIsInstance(value[2], float)
                    except AssertionError:
                        # Sometimes <int>
                        self.assertIsInstance(value[2], int)
                        
                    self.assertIsInstance(value[3], int)
                    self.assertIsInstance(value[4], int)
                    try:
                        self.assertIsInstance(value[5], float)
                    except AssertionError:
                        self.assertIsNone(value[5])
                    self.assertIsInstance(value[6], int)


        a_pairs = e.ensdf_pairs(edata,"A")
        for parent, daughter in a_pairs.items():
            a_ujpi = e.find_unique_jpi(edata, str(parent[0]), int(parent[3]), mode="A")
            self.assertIsInstance(a_ujpi, dict)
            self.assertIsInstance(a_ujpi, Iterable)
            self.assertGreater(len(a_ujpi), 0)
            for ujpi_key, ujpi_value in a_ujpi.items():
                
                self.assertIsInstance(ujpi_key, tuple)
                self.assertIsInstance(ujpi_key, Iterable)
                self.assertEqual(len(ujpi_key), 8)
                self.assertIsInstance(ujpi_value, list)
                self.assertIsInstance(ujpi_value, Iterable)

                # Unpack the tuple key contents
                self.assertIsInstance(ujpi_key[0], str)
                self.assertIsInstance(ujpi_key[1], int)
                self.assertIsInstance(ujpi_key[2], int)
                self.assertIsInstance(ujpi_key[3], int)
                try:
                    self.assertIsInstance(ujpi_key[4], float)
                except AssertionError:
                    self.assertIsInstance(ujpi_key[4], str)
                self.assertIsInstance(ujpi_key[5], str)
                self.assertIsInstance(ujpi_key[6], int)
                self.assertIsInstance(ujpi_key[7], int)
                
                # Unpack the list value contents
                for value in ujpi_value:
                    self.assertIsInstance(value, list)
                    self.assertIsInstance(value, Iterable)
                    self.assertEqual(len(value), 7)
                    
                    self.assertIsInstance(value[0], int)
                
                    try:
                        self.assertIsInstance(value[1], float)
                    except AssertionError:
                        try:
                            # Sometimes <int>
                            self.assertIsInstance(value[1], int)
                        except AssertionError:
                            # Sometimes <str>
                            self.assertIsInstance(value[1], str)
                    try:
                        self.assertIsInstance(value[2], float)
                    except AssertionError:
                        # Sometimes <int>
                        self.assertIsInstance(value[2], int)
                        
                    self.assertIsInstance(value[3], int)
                    self.assertIsInstance(value[4], int)
                    try:
                        self.assertIsInstance(value[5], float)
                    except AssertionError:
                        self.assertIsNone(value[5])
                    self.assertIsInstance(value[6], int)



class FindIsomers(unittest.TestCase):

    __doc__="""Unit tests for the `find_isomers` method of the Daughter 
    class."""

    def test_find_isomers_returns_dict_for_all_decays(self):
        ecbp_pairs = e.ensdf_pairs(edata,"ECBP")
        for parent, daughter in ecbp_pairs.items():
            ecbp = e.find_isomers(edata, str(parent[0]), int(parent[3]), mode="ECBP", units='best')
            self.assertIsInstance(ecbp, dict)
            self.assertIsInstance(ecbp, Iterable)
            ecbp = e.find_isomers(edata, str(parent[0]), int(parent[3]), mode="ECBP", units='seconds')
            self.assertIsInstance(ecbp, dict)
            self.assertIsInstance(ecbp, Iterable)
            ecbp = e.find_isomers(edata, str(parent[0]), int(parent[3]), mode="ECBP", units='s')
            self.assertIsInstance(ecbp, dict)
            self.assertIsInstance(ecbp, Iterable)

        bm_pairs = e.ensdf_pairs(edata,"BM")
        for parent, daughter in bm_pairs.items():
            bm = e.find_isomers(edata, str(parent[0]), int(parent[3]), mode="BM", units='best')
            self.assertIsInstance(bm, dict)
            self.assertIsInstance(bm, Iterable)
            bm = e.find_isomers(edata, str(parent[0]), int(parent[3]), mode="BM", units='seconds')
            self.assertIsInstance(bm, dict)
            self.assertIsInstance(bm, Iterable)
            bm = e.find_isomers(edata, str(parent[0]), int(parent[3]), mode="BM", units='s')
            self.assertIsInstance(bm, dict)
            self.assertIsInstance(bm, Iterable)

        a_pairs = e.ensdf_pairs(edata,"A")
        for parent, daughter in a_pairs.items():
            a = e.find_isomers(edata, str(parent[0]), int(parent[3]), mode="A", units='best')
            self.assertIsInstance(a, dict)
            self.assertIsInstance(a, Iterable)
            a = e.find_isomers(edata, str(parent[0]), int(parent[3]), mode="A", units='seconds')
            self.assertIsInstance(a, dict)
            self.assertIsInstance(a, Iterable)
            a = e.find_isomers(edata, str(parent[0]), int(parent[3]), mode="A", units='s')
            self.assertIsInstance(a, dict)
            self.assertIsInstance(a, Iterable)

    def test_find_isomers_returns_none_if_not_correct_decay_mode(self):
        ecbp = e.find_isomers(edata,"Co60",0,mode="ECBP",units='best')
        self.assertIsNone(ecbp)
        bm = e.find_isomers(edata,"Y86",0,mode="BM",units='best')
        self.assertIsNone(bm)
        a = e.find_isomers(edata,"Na22",0,mode="A",units='best')
        self.assertIsNone(a)

    def test_find_isomers_returns_none_if_missing_kwargs(self):
        ecbp = e.find_isomers(edata,"Y86",0)
        self.assertIsNone(ecbp)
        ecbp = e.find_isomers(edata,"Y86",0,mode="ECBP")
        self.assertIsNone(ecbp)
        ecbp = e.find_isomers(edata,"Y86",0,units="best")
        self.assertIsNone(ecbp)
        
        bm = e.find_isomers(edata,"Co60",0)
        self.assertIsNone(bm)
        bm = e.find_isomers(edata,"Co60",0,mode="BM")
        self.assertIsNone(bm)
        bm = e.find_isomers(edata,"Co60",0,units="seconds")
        self.assertIsNone(bm)
        
        a = e.find_isomers(edata,"Ra226",0)
        self.assertIsNone(a)
        a = e.find_isomers(edata,"Ra226",0,mode="A")
        self.assertIsNone(a)
        a = e.find_isomers(edata,"Ra226",0,units="s")
        self.assertIsNone(a)

    def test_find_isomers_returns_none_if_illegal_string(self):
        isomers = e.find_isomers(edata,"Co60", 1, mode="THisIsB@LL@CK$", units="best")
        self.assertIsNone(isomers)
        isomers = e.find_isomers(edata,"Co60", 0, mode="BM", units="THisIsB@LL@CK$")
        self.assertIsNone(isomers)

    def test_find_isomers_raises_TypeError_if_first_arg_not_list(self):
        with self.assertRaises(TypeError):
            ecbp = e.find_isomers("Db258",edata,0,mode="ECBP",units="best")
        with self.assertRaises(TypeError):
            bm = e.find_isomers("Co60",edata,1,mode="BM",units="seconds")
        with self.assertRaises(TypeError):
            a = e.find_isomers("Ra226",edata,0,mode="A",units="s")

    def test_find_isomers_raises_NameError_if_wrong_list(self):
        with self.assertRaises(NameError):
            ecbp = e.find_isomers(XXXedataXXX,"Db258",0,mode="ECBP",units="s")
        with self.assertRaises(NameError):
            bm = e.find_isomers(XXXedataXXX,"Co60",1,mode="BM",units="seconds")
        with self.assertRaises(NameError):
            a = e.find_isomers(XXXedataXXX,"Ra226",0,mode="A",units="best")

    def test_find_isomers_raises_KeyError_if_bad_dict_items_in_list(self):
        bad_dict_items_in_list = [{'a':0, 'b':1, 'c':2}]
        with self.assertRaises(KeyError):
           ecbp = e.find_isomers(bad_dict_items_in_list,"Db258",0,mode="ECBP",units="best")
        with self.assertRaises(KeyError):
           bm = e.find_isomers(bad_dict_items_in_list,"Co60",1,mode="BM",units="s")
        with self.assertRaises(KeyError):
           a = e.find_isomers(bad_dict_items_in_list,"Ra226",0,mode="A",units="seconds")

    def test_find_isomers_returned_contents_of_dict(self):
        ecbp_pairs = e.ensdf_pairs(edata,"ECBP")
        for parent, daughter in ecbp_pairs.items():
            ecbp_isomers = e.find_isomers(edata, str(parent[0]), int(parent[3]), mode="ECBP", units="best")
            self.assertIsInstance(ecbp_isomers, dict)
            self.assertIsInstance(ecbp_isomers, Iterable)
            self.assertGreater(len(ecbp_isomers), 0)
            for isomers_key, isomers_value in ecbp_isomers.items():
                
                self.assertIsInstance(isomers_key, tuple)
                self.assertIsInstance(isomers_key, Iterable)
                self.assertEqual(len(isomers_key), 8)
                self.assertIsInstance(isomers_value, list)
                self.assertIsInstance(isomers_value, Iterable)

                # Unpack the tuple key contents
                self.assertIsInstance(isomers_key[0], str)
                self.assertIsInstance(isomers_key[1], int)
                self.assertIsInstance(isomers_key[2], int)
                self.assertIsInstance(isomers_key[3], int)
                try:
                    self.assertIsInstance(isomers_key[4], float)
                except AssertionError:
                    self.assertIsInstance(isomers_key[4], str)
                self.assertIsInstance(isomers_key[5], str)
                self.assertIsInstance(isomers_key[6], int)
                self.assertIsInstance(isomers_key[7], int)
                
                # Unpack the list value contents
                for value in isomers_value:
                    self.assertIsInstance(value, list)
                    self.assertIsInstance(value, Iterable)
                    self.assertEqual(len(value), 6)
                
                    self.assertIsInstance(value[0], int)
                
                    try:
                        self.assertIsInstance(value[1], float)
                    except AssertionError:
                        try:
                            # Sometimes <int>
                            self.assertIsInstance(value[1], int)
                        except AssertionError:
                            # Sometimes <str>
                            self.assertIsInstance(value[1], str)
                    try:
                        self.assertIsInstance(value[2], float)
                    except AssertionError:
                        # Sometimes <int>
                        self.assertIsInstance(value[2], int)
                        
                    try:
                        self.assertIsInstance(value[3], float)
                    except AssertionError:
                        # Sometimes an <int>
                        self.assertIsInstance(value[3], int)
                    try:
                        self.assertIsInstance(value[4], float)
                    except AssertionError:
                        # Sometimes an <int>
                        self.assertIsInstance(value[4], int)
                    self.assertIsInstance(value[5], str)
                    

        bm_pairs = e.ensdf_pairs(edata,"BM")
        for parent, daughter in bm_pairs.items():
            bm_isomers = e.find_isomers(edata, str(parent[0]), int(parent[3]), mode="BM", units="seconds")
            self.assertIsInstance(bm_isomers, dict)
            self.assertIsInstance(bm_isomers, Iterable)
            self.assertGreater(len(bm_isomers), 0)
            for isomers_key, isomers_value in bm_isomers.items():
                
                self.assertIsInstance(isomers_key, tuple)
                self.assertIsInstance(isomers_key, Iterable)
                self.assertEqual(len(isomers_key), 8)
                self.assertIsInstance(isomers_value, list)
                self.assertIsInstance(isomers_value, Iterable)

                # Unpack the tuple key contents
                self.assertIsInstance(isomers_key[0], str)
                self.assertIsInstance(isomers_key[1], int)
                self.assertIsInstance(isomers_key[2], int)
                self.assertIsInstance(isomers_key[3], int)
                try:
                    self.assertIsInstance(isomers_key[4], float)
                except AssertionError:
                    self.assertIsInstance(isomers_key[4], str)
                self.assertIsInstance(isomers_key[5], str)
                self.assertIsInstance(isomers_key[6], int)
                self.assertIsInstance(isomers_key[7], int)
                
                # Unpack the list value contents
                for value in isomers_value:
                    self.assertIsInstance(value, list)
                    self.assertIsInstance(value, Iterable)
                    self.assertEqual(len(value), 6)
                    
                    self.assertIsInstance(value[0], int)
                
                    try:
                        self.assertIsInstance(value[1], float)
                    except AssertionError:
                        try:
                            # Sometimes <int>
                            self.assertIsInstance(value[1], int)
                        except AssertionError:
                            # Sometimes <str>
                            self.assertIsInstance(value[1], str)
                    try:
                        self.assertIsInstance(value[2], float)
                    except AssertionError:
                        # Sometimes <int>
                        self.assertIsInstance(value[2], int)

                    try:
                        self.assertIsInstance(value[3], float)
                    except AssertionError:
                        # Sometimes an <int>
                        self.assertIsInstance(value[3], int)
                    try:
                        self.assertIsInstance(value[4], float)
                    except AssertionError:
                        # Sometimes an <int>
                        self.assertIsInstance(value[4], int)
                    self.assertIsInstance(value[5], str)


        a_pairs = e.ensdf_pairs(edata,"A")
        for parent, daughter in a_pairs.items():
            a_isomers = e.find_isomers(edata, str(parent[0]), int(parent[3]), mode="A", units="s")
            self.assertIsInstance(a_isomers, dict)
            self.assertIsInstance(a_isomers, Iterable)
            self.assertGreater(len(a_isomers), 0)
            for isomers_key, isomers_value in a_isomers.items():
                
                self.assertIsInstance(isomers_key, tuple)
                self.assertIsInstance(isomers_key, Iterable)
                self.assertEqual(len(isomers_key), 8)
                self.assertIsInstance(isomers_value, list)
                self.assertIsInstance(isomers_value, Iterable)

                # Unpack the tuple key contents
                self.assertIsInstance(isomers_key[0], str)
                self.assertIsInstance(isomers_key[1], int)
                self.assertIsInstance(isomers_key[2], int)
                self.assertIsInstance(isomers_key[3], int)
                try:
                    self.assertIsInstance(isomers_key[4], float)
                except AssertionError:
                    self.assertIsInstance(isomers_key[4], str)
                self.assertIsInstance(isomers_key[5], str)
                self.assertIsInstance(isomers_key[6], int)
                self.assertIsInstance(isomers_key[7], int)
                
                # Unpack the list value contents
                for value in isomers_value:
                    self.assertIsInstance(value, list)
                    self.assertIsInstance(value, Iterable)
                    self.assertEqual(len(value), 6)
                    
                    self.assertIsInstance(value[0], int)
                
                    try:
                        self.assertIsInstance(value[1], float)
                    except AssertionError:
                        try:
                            # Sometimes <int>
                            self.assertIsInstance(value[1], int)
                        except AssertionError:
                            # Sometimes <str>
                            self.assertIsInstance(value[1], str)
                    try:
                        self.assertIsInstance(value[2], float)
                    except AssertionError:
                        # Sometimes <int>
                        self.assertIsInstance(value[2], int)

                    try:
                        self.assertIsInstance(value[3], float)
                    except AssertionError:
                        # Sometimes an <int>
                        self.assertIsInstance(value[3], int)
                    try:
                        self.assertIsInstance(value[4], float)
                    except AssertionError:
                        # Sometimes an <int>
                        self.assertIsInstance(value[4], int)
                    self.assertIsInstance(value[5], str)


class FindDecayWidths(unittest.TestCase):

    __doc__="""Unit tests for the `find_decay_widths` method of the Daughter 
    class."""

    def test_find_decay_widths_returns_dict_for_all_decays(self):
        ecbp_pairs = e.ensdf_pairs(edata,"ECBP")
        for parent, daughter in ecbp_pairs.items():
            ecbp = e.find_decay_widths(edata, str(parent[0]), int(parent[3]), mode="ECBP", units='best')
            self.assertIsInstance(ecbp, dict)
            self.assertIsInstance(ecbp, Iterable)
            ecbp = e.find_decay_widths(edata, str(parent[0]), int(parent[3]), mode="ECBP", units='MeV')
            self.assertIsInstance(ecbp, dict)
            self.assertIsInstance(ecbp, Iterable)

        bm_pairs = e.ensdf_pairs(edata,"BM")
        for parent, daughter in bm_pairs.items():
            bm = e.find_decay_widths(edata, str(parent[0]), int(parent[3]), mode="BM", units='best')
            self.assertIsInstance(bm, dict)
            self.assertIsInstance(bm, Iterable)
            bm = e.find_decay_widths(edata, str(parent[0]), int(parent[3]), mode="BM", units='MeV')
            self.assertIsInstance(bm, dict)
            self.assertIsInstance(bm, Iterable)

        a_pairs = e.ensdf_pairs(edata,"A")
        for parent, daughter in a_pairs.items():
            a = e.find_decay_widths(edata, str(parent[0]), int(parent[3]), mode="A", units='best')
            self.assertIsInstance(a, dict)
            self.assertIsInstance(a, Iterable)
            a = e.find_decay_widths(edata, str(parent[0]), int(parent[3]), mode="A", units='MeV')
            self.assertIsInstance(a, dict)
            self.assertIsInstance(a, Iterable)

    def test_find_decay_widths_returns_none_if_not_correct_decay_mode(self):
        ecbp = e.find_decay_widths(edata,"Co60",0,mode="ECBP",units='best')
        self.assertIsNone(ecbp)
        bm = e.find_decay_widths(edata,"Y86",0,mode="BM",units='best')
        self.assertIsNone(bm)
        a = e.find_decay_widths(edata,"Na22",0,mode="A",units='best')
        self.assertIsNone(a)

    def test_find_decay_widths_returns_none_if_missing_kwargs(self):
        ecbp = e.find_decay_widths(edata,"Ar32",0)
        self.assertIsNone(ecbp)
        ecbp = e.find_decay_widths(edata,"Ar32",0,mode="ECBP")
        self.assertIsNone(ecbp)
        ecbp = e.find_decay_widths(edata,"Ar32",0,units="best")
        self.assertIsNone(ecbp)
        
        bm = e.find_decay_widths(edata,"Co60",0)
        self.assertIsNone(bm)
        bm = e.find_decay_widths(edata,"Co60",0,mode="BM")
        self.assertIsNone(bm)
        bm = e.find_decay_widths(edata,"Co60",0,units="MeV")
        self.assertIsNone(bm)
        
        a = e.find_decay_widths(edata,"Ra226",0)
        self.assertIsNone(a)
        a = e.find_decay_widths(edata,"Ra226",0,mode="A")
        self.assertIsNone(a)
        a = e.find_decay_widths(edata,"Ra226",0,units="best")
        self.assertIsNone(a)

    def test_find_decay_widths_returns_none_if_illegal_string(self):
        isomers = e.find_decay_widths(edata,"C9", 0, mode="THisIsB@LL@CK$", units="best")
        self.assertIsNone(isomers)
        isomers = e.find_decay_widths(edata,"C9", 0, mode="ECBP", units="THisIsB@LL@CK$")
        self.assertIsNone(isomers)

    def test_find_decay_widths_raises_TypeError_if_first_arg_not_list(self):
        with self.assertRaises(TypeError):
            ecbp = e.find_decay_widths("Db258",edata,0,mode="ECBP",units="best")
        with self.assertRaises(TypeError):
            bm = e.find_decay_widths("Co60",edata,1,mode="BM",units="MeV")
        with self.assertRaises(TypeError):
            a = e.find_decay_widths("Ra226",edata,0,mode="A",units="best")

    def test_find_decay_widths_raises_NameError_if_wrong_list(self):
        with self.assertRaises(NameError):
            ecbp = e.find_decay_widths(XXXedataXXX,"Ar32",0,mode="ECBP",units="s")
        with self.assertRaises(NameError):
            bm = e.find_decay_widths(XXXedataXXX,"Li9",0,mode="BM",units="seconds")
        with self.assertRaises(NameError):
            a = e.find_decay_widths(XXXedataXXX,"Ra226",0,mode="A",units="best")

    def test_find_decay_widths_raises_KeyError_if_bad_dict_items_in_list(self):
        bad_dict_items_in_list = [{'a':0, 'b':1, 'c':2}]
        with self.assertRaises(KeyError):
           ecbp = e.find_decay_widths(bad_dict_items_in_list,"Ar32",0,mode="ECBP",units="best")
        with self.assertRaises(KeyError):
           bm = e.find_decay_widths(bad_dict_items_in_list,"Li9",0,mode="BM",units="best")
        with self.assertRaises(KeyError):
           a = e.find_decay_widths(bad_dict_items_in_list,"Ra226",0,mode="A",units="MeV")

    def test_find_decay_widths_returned_contents_of_dict(self):
        ecbp_pairs = e.ensdf_pairs(edata,"ECBP")
        for parent, daughter in ecbp_pairs.items():
            ecbp_widths = e.find_decay_widths(edata, str(parent[0]), int(parent[3]), mode="ECBP", units="best")
            self.assertIsInstance(ecbp_widths, dict)
            self.assertIsInstance(ecbp_widths, Iterable)
            self.assertGreater(len(ecbp_widths), 0)
            for widths_key, widths_value in ecbp_widths.items():
                
                self.assertIsInstance(widths_key, tuple)
                self.assertIsInstance(widths_key, Iterable)
                self.assertEqual(len(widths_key), 8)
                self.assertIsInstance(widths_value, list)
                self.assertIsInstance(widths_value, Iterable)

                # Unpack the tuple key contents
                self.assertIsInstance(widths_key[0], str)
                self.assertIsInstance(widths_key[1], int)
                self.assertIsInstance(widths_key[2], int)
                self.assertIsInstance(widths_key[3], int)
                try:
                    self.assertIsInstance(widths_key[4], float)
                except AssertionError:
                    self.assertIsInstance(widths_key[4], str)
                self.assertIsInstance(widths_key[5], str)
                self.assertIsInstance(widths_key[6], int)
                self.assertIsInstance(widths_key[7], int)
                
                # Unpack the list value contents
                for value in widths_value:
                    self.assertIsInstance(value, list)
                    self.assertIsInstance(value, Iterable)
                    self.assertEqual(len(value), 7)
                
                    self.assertIsInstance(value[0], int)
                
                    try:
                        self.assertIsInstance(value[1], float)
                    except AssertionError:
                        try:
                            # Sometimes <int>
                            self.assertIsInstance(value[1], int)
                        except AssertionError:
                            # Sometimes <str>
                            self.assertIsInstance(value[1], str)
                    try:
                        self.assertIsInstance(value[2], float)
                    except AssertionError:
                        # Sometimes <int>
                        self.assertIsInstance(value[2], int)
                        
                    try:
                        self.assertIsInstance(value[3], float)
                    except AssertionError:
                        # Sometimes an <int>
                        self.assertIsInstance(value[3], int)
                    try:
                        self.assertIsInstance(value[4], float)
                    except AssertionError:
                        # Sometimes an <int>
                        self.assertIsInstance(value[4], int)
                    self.assertIsInstance(value[5], str)
                    self.assertIsInstance(value[6], bool)
                    

        bm_pairs = e.ensdf_pairs(edata,"BM")
        for parent, daughter in bm_pairs.items():
            bm_widths = e.find_decay_widths(edata, str(parent[0]), int(parent[3]), mode="BM", units="MeV")
            self.assertIsInstance(bm_widths, dict)
            self.assertIsInstance(bm_widths, Iterable)
            self.assertGreater(len(bm_widths), 0)
            for widths_key, widths_value in bm_widths.items():
                
                self.assertIsInstance(widths_key, tuple)
                self.assertIsInstance(widths_key, Iterable)
                self.assertEqual(len(widths_key), 8)
                self.assertIsInstance(widths_value, list)
                self.assertIsInstance(widths_value, Iterable)

                # Unpack the tuple key contents
                self.assertIsInstance(widths_key[0], str)
                self.assertIsInstance(widths_key[1], int)
                self.assertIsInstance(widths_key[2], int)
                self.assertIsInstance(widths_key[3], int)
                try:
                    self.assertIsInstance(widths_key[4], float)
                except AssertionError:
                    self.assertIsInstance(widths_key[4], str)
                self.assertIsInstance(widths_key[5], str)
                self.assertIsInstance(widths_key[6], int)
                self.assertIsInstance(widths_key[7], int)
                
                # Unpack the list value contents
                for value in widths_value:
                    self.assertIsInstance(value, list)
                    self.assertIsInstance(value, Iterable)
                    self.assertEqual(len(value), 7)
                    
                    self.assertIsInstance(value[0], int)
                
                    try:
                        self.assertIsInstance(value[1], float)
                    except AssertionError:
                        try:
                            # Sometimes <int>
                            self.assertIsInstance(value[1], int)
                        except AssertionError:
                            # Sometimes <str>
                            self.assertIsInstance(value[1], str)
                    try:
                        self.assertIsInstance(value[2], float)
                    except AssertionError:
                        # Sometimes <int>
                        self.assertIsInstance(value[2], int)

                    try:
                        self.assertIsInstance(value[3], float)
                    except AssertionError:
                        # Sometimes an <int>
                        self.assertIsInstance(value[3], int)
                    try:
                        self.assertIsInstance(value[4], float)
                    except AssertionError:
                        # Sometimes an <int>
                        self.assertIsInstance(value[4], int)
                    self.assertIsInstance(value[5], str)
                    self.assertIsInstance(value[6], bool)
                    

        a_pairs = e.ensdf_pairs(edata,"A")
        for parent, daughter in a_pairs.items():
            a_widths = e.find_decay_widths(edata, str(parent[0]), int(parent[3]), mode="A", units="MeV")
            self.assertIsInstance(a_widths, dict)
            self.assertIsInstance(a_widths, Iterable)
            self.assertGreater(len(a_widths), 0)
            for widths_key, widths_value in a_widths.items():
                
                self.assertIsInstance(widths_key, tuple)
                self.assertIsInstance(widths_key, Iterable)
                self.assertEqual(len(widths_key), 8)
                self.assertIsInstance(widths_value, list)
                self.assertIsInstance(widths_value, Iterable)

                # Unpack the tuple key contents
                self.assertIsInstance(widths_key[0], str)
                self.assertIsInstance(widths_key[1], int)
                self.assertIsInstance(widths_key[2], int)
                self.assertIsInstance(widths_key[3], int)
                try:
                    self.assertIsInstance(widths_key[4], float)
                except AssertionError:
                    self.assertIsInstance(widths_key[4], str)
                self.assertIsInstance(widths_key[5], str)
                self.assertIsInstance(widths_key[6], int)
                self.assertIsInstance(widths_key[7], int)
                
                # Unpack the list value contents
                for value in widths_value:
                    self.assertIsInstance(value, list)
                    self.assertIsInstance(value, Iterable)
                    self.assertEqual(len(value), 7)
                    
                    self.assertIsInstance(value[0], int)
                
                    try:
                        self.assertIsInstance(value[1], float)
                    except AssertionError:
                        try:
                            # Sometimes <int>
                            self.assertIsInstance(value[1], int)
                        except AssertionError:
                            # Sometimes <str>
                            self.assertIsInstance(value[1], str)
                    try:
                        self.assertIsInstance(value[2], float)
                    except AssertionError:
                        # Sometimes <int>
                        self.assertIsInstance(value[2], int)

                    try:
                        self.assertIsInstance(value[3], float)
                    except AssertionError:
                        # Sometimes an <int>
                        self.assertIsInstance(value[3], int)
                    try:
                        self.assertIsInstance(value[4], float)
                    except AssertionError:
                        # Sometimes an <int>
                        self.assertIsInstance(value[4], int)
                    self.assertIsInstance(value[5], str)
                    self.assertIsInstance(value[6], bool)

