import pytest
import unittest
import numpy as np
import pandas as pd
from collections.abc import Iterable

import paceENSDF as pe
e = pe.ENSDF()
edata = e.load_ensdf()
cdata = e.load_pace()

class GetGG(unittest.TestCase):

    __doc__="""Unit tests for the `get_gg` method of the GammaGamma class."""

    ecbp_pairs = e.ensdf_pairs(edata,"ECBP")
    bm_pairs = e.ensdf_pairs(edata,"BM")
    a_pairs = e.ensdf_pairs(edata,"A")
    
    def test_get_gg_returns_list_or_none_for_all_coinc_decays(self):
        for parent, daughter in GetGG.ecbp_pairs.items():
            #for d in cdata:
            #    if d["datasetID"]=="GG" and d["parentID"]==str(parent[0]) and d["decayIndex"]==int(parent[3]):
            gg_ecbp = e.get_gg(cdata, "ECBP", str(parent[0]), int(parent[3]))
            try:
                self.assertIsInstance(gg_ecbp, list)
                self.assertIsInstance(gg_ecbp, Iterable)

                lot1 = []
                lot2 = []
                for coinc in gg_ecbp:
                    lot1.append((coinc[2], coinc[3]))
                    lot1.append((coinc[6], coinc[7]))
                lot1 = list(set(lot1))
                lot2 = list(set(lot2))

                for tc1 in lot1:
                    c1_gg = e.get_gg(cdata, "ECBP", str(parent[0]), int(parent[3]), int(tc1[0]), int(tc1[1]))
                    self.assertIsInstance(c1_gg, list)
                    self.assertIsInstance(c1_gg, Iterable)

                for tc2 in lot2:
                    c2_gg = e.get_gg(cdata, "ECBP", str(parent[0]), int(parent[3]), int(tc2[0]), int(tc2[1]))
                    self.assertIsInstance(c2_gg, list)
                    self.assertIsInstance(c2_gg, Iterable)
            except AssertionError:
                self.assertIsNone(gg_ecbp)

        for parent, daughter in GetGG.bm_pairs.items():
            #for d in cdata:
            #    if d["datasetID"]=="GG" and d["parentID"]==str(parent[0]) and d["decayIndex"]==int(parent[3]):
            gg_bm = e.get_gg(cdata, "BM", str(parent[0]), int(parent[3]))
            try:
                self.assertIsInstance(gg_bm, list)
                self.assertIsInstance(gg_bm, Iterable)

                lot1 = []
                lot2 = []
                for coinc in gg_bm:
                    lot1.append((coinc[2], coinc[3]))
                    lot1.append((coinc[6], coinc[7]))
                lot1 = list(set(lot1))
                lot2 = list(set(lot2))

                for tc1 in lot1:
                    c1_gg = e.get_gg(cdata, "BM", str(parent[0]), int(parent[3]), int(tc1[0]), int(tc1[1]))
                    self.assertIsInstance(c1_gg, list)
                    self.assertIsInstance(c1_gg, Iterable)

                for tc2 in lot2:
                    c2_gg = e.get_gg(cdata, "BM", str(parent[0]), int(parent[3]), int(tc2[0]), int(tc2[1]))
                    self.assertIsInstance(c2_gg, list)
                    self.assertIsInstance(c2_gg, Iterable)
            except AssertionError:
                self.assertIsNone(gg_bm)

        for parent, daughter in GetGG.a_pairs.items():
            #for d in cdata:
            #    if d["datasetID"]=="GG" and d["parentID"]==str(parent[0]) and d["decayIndex"]==int(parent[3]):
            gg_a = e.get_gg(cdata, "A", str(parent[0]), int(parent[3]))
            try:
                self.assertIsInstance(gg_a, list)
                self.assertIsInstance(gg_a, Iterable)

                lot1 = []
                lot2 = []
                for coinc in gg_a:
                    lot1.append((coinc[2], coinc[3]))
                    lot1.append((coinc[6], coinc[7]))
                lot1 = list(set(lot1))
                lot2 = list(set(lot2))

                for tc1 in lot1:
                    c1_gg = e.get_gg(cdata, "A", str(parent[0]), int(parent[3]), int(tc1[0]), int(tc1[1]))
                    self.assertIsInstance(c1_gg, list)
                    self.assertIsInstance(c1_gg, Iterable)

                for tc2 in lot2:
                    c2_gg = e.get_gg(cdata, "A", str(parent[0]), int(parent[3]), int(tc2[0]), int(tc2[1]))
                    self.assertIsInstance(c2_gg, list)
                    self.assertIsInstance(c2_gg, Iterable)
            except AssertionError:
                self.assertIsNone(gg_a)


    #def test_get_gg_returns_none_if_no_corresponding_coinc_decay(self):
    #    for parent, daughter in GetGG.ecbp_pairs.items():
    #        gg_ecbp = e.get_gg(cdata, "ECBP", str(parent[0]), int(parent[3]))
    #        try:
    #            self.assertIsInstance(gg_ecbp,list)
    #        except AssertionError:
    #            self.assertIsNone(gg_ecbp)

    #    for parent, daughter in GetGG.bm_pairs.items():
    #        gg_bm = e.get_gg(cdata, "ECBP", str(parent[0]), int(parent[3]))
    #        try:
    #            self.assertIsInstance(gg_bm,list)
    #        except AssertionError:
    #            self.assertIsNone(gg_bm)

    #    for parent, daughter in GetGG.a_pairs.items():
    #        gg_a = e.get_gg(cdata, "ECBP", str(parent[0]), int(parent[3]))
    #        try:
    #            self.assertIsInstance(gg_a,list)
    #        except AssertionError:
    #            self.assertIsNone(gg_a)

    def test_get_gg_returns_none_if_wrong_decay_mode(self):
        gg_ecbp = e.get_gg(cdata, "ECBP", "Co60", 0)
        self.assertIsNone(gg_ecbp)
        gg_ecbp = e.get_gg(cdata, "ECBP", "Co60", 0, 2, 1)
        self.assertIsNone(gg_ecbp)
        
        gg_bm = e.get_gg(cdata, "BM", "Y86", 0)
        self.assertIsNone(gg_bm)
        gg_bm = e.get_gg(cdata, "BM", "Y86", 0, 2, 1)
        self.assertIsNone(gg_bm)
        
        gg_a = e.get_gg(cdata, "A", "Na22", 0)
        self.assertIsNone(gg_a)
        gg_a = e.get_gg(cdata, "A", "Na22", 0, 2, 1)
        self.assertIsNone(gg_a)

    def test_get_gg_returns_none_if_missing_args(self):
        gg = e.get_gg(cdata, "BM", "Co60")
        self.assertIsNone(gg)
        gg = e.get_gg(cdata, "BM")
        self.assertIsNone(gg)
        gg = e.get_gg(cdata, "Co60", 0)
        self.assertIsNone(gg)
        gg = e.get_gg(cdata, "Co60")
        self.assertIsNone(gg)

    def test_get_gg_returns_none_if_wrong_number_args(self):
        gg = e.get_gg(cdata, "BM", "Co60", 0, 2)
        self.assertIsNone(gg)
        gg = e.get_gg(cdata, "BM", "Co60", 0, 2, 1, 2)
        self.assertIsNone(gg)

    def test_get_gg_returns_none_if_wrong_order_args(self):
        gg = e.get_gg(cdata, "Co60", "BM", 0)
        self.assertIsNone(gg)
        gg = e.get_gg(cdata, "Co60", "BM", 0, 2, 1)
        self.assertIsNone(gg)

        gg = e.get_gg(cdata, "Y86", "ECBP", 0)
        self.assertIsNone(gg)
        gg = e.get_gg(cdata, "Y86", "ECBP", 0, 2, 1)
        self.assertIsNone(gg)

        gg = e.get_gg(cdata, "Ra226", "A", 0)
        self.assertIsNone(gg)
        gg = e.get_gg(cdata, "Ra226", "A", 0, 2, 1)
        self.assertIsNone(gg)
        
    def test_get_gg_raises_TypeError_if_no_args(self):
        with self.assertRaises(TypeError):
            gg = e.get_gg(cdata)

    def test_get_gg_returns_none_if_illegal_string(self):
        gg = e.get_gg(cdata, "THisIsB@LL@CK$", "Co60", 0)
        self.assertIsNone(gg)
        gg = e.get_gg(cdata, "BM", "THisIsB@LL@CK$", 0)
        self.assertIsNone(gg)
        gg = e.get_gg(cdata, "THisIsB@LL@CK$", "THisIsB@LL@CK$", 0)
        self.assertIsNone(gg)

    def test_get_gg_raises_AttributeError_if_first_arg_not_list(self):
        with self.assertRaises(AttributeError):
            gg = e.get_gg("BM", cdata, "Co60", 0)
        with self.assertRaises(AttributeError):
            gg = e.get_gg("ECBP", cdata, "Y86", 0)
        with self.assertRaises(AttributeError):
            gg = e.get_gg("A", cdata, "Ra226", 0)

    def test_get_gg_raises_NameError_if_wrong_name_list(self):
        with self.assertRaises(NameError):
            gg = e.get_gg(XXXcdataXX, "BM", "Co60", 0)
        with self.assertRaises(NameError):
            gg = e.get_gg(XXXcdataXX, "ECBP", "Y86", 0)
        with self.assertRaises(NameError):
            gg = e.get_gg(XXXcdataXX, "A", "Ra226", 0)

    def test_get_gg_raises_KeyError_if_wrong_list(self):
        with self.assertRaises(KeyError):
            gg = e.get_gg(edata, "BM", "Co60", 0)
        with self.assertRaises(KeyError):
            gg = e.get_gg(edata, "BM", "Co60", 0, 2, 1)
            
        with self.assertRaises(KeyError):
            gg = e.get_gg(edata, "ECBP", "Y86", 0)
        with self.assertRaises(KeyError):
            gg = e.get_gg(edata, "ECBP", "Y86", 0, 2, 1)
            
        with self.assertRaises(KeyError):
            gg = e.get_gg(edata, "A", "Ra226", 0)
        with self.assertRaises(KeyError):
            gg = e.get_gg(edata, "A", "Ra226", 0, 2, 1)

    def test_get_gg_KeyError_if_bad_dict_items_in_list(self):
        bad_dict_items_in_list = [{'a':0, 'b':1, 'c':2}]
        with self.assertRaises(KeyError):
            gg = e.get_gg(bad_dict_items_in_list, "BM", "Co60", 0)
        with self.assertRaises(KeyError):
            gg = e.get_gg(bad_dict_items_in_list, "BM", "Co60", 0, 2, 1)

        with self.assertRaises(KeyError):
            gg = e.get_gg(bad_dict_items_in_list, "ECBP", "Y86", 0)
        with self.assertRaises(KeyError):
            gg = e.get_gg(bad_dict_items_in_list, "ECBP", "Y86", 0, 2, 1)

        with self.assertRaises(KeyError):
            gg = e.get_gg(bad_dict_items_in_list, "A", "Ra226", 0)
        with self.assertRaises(KeyError):
            gg = e.get_gg(bad_dict_items_in_list, "A", "Ra226", 0, 2, 1)

    def test_get_gg_returned_contents_of_list(self):
        for parent, daughter in GetGG.ecbp_pairs.items():
            gg_ecbp = e.get_gg(cdata, "ECBP", str(parent[0]), int(parent[3]))
            try:
                self.assertIsInstance(gg_ecbp, list)
                self.assertIsInstance(gg_ecbp, Iterable)

                for gg in gg_ecbp:
                    self.assertIsInstance(gg[0], float)
                    self.assertIsInstance(gg[1], float)
                    self.assertIsInstance(gg[2], int)
                    self.assertIsInstance(gg[3], int)
                    
                    try:
                        self.assertIsInstance(gg[4], float)
                    except AssertionError:
                        self.assertIsInstance(gg[4], str)

                    try:
                        self.assertIsInstance(gg[5], float)
                    except AssertionError:
                        self.assertIsInstance(gg[5], str)
                        
                    self.assertIsInstance(gg[6], int)
                    self.assertIsInstance(gg[7], int)

                    try:
                        self.assertIsInstance(gg[8], float)
                    except AssertionError:
                        self.assertIsInstance(gg[8], str)

                    try:
                        self.assertIsInstance(gg[9], float)
                    except AssertionError:
                        self.assertIsInstance(gg[9], str)
                        
                    self.assertIsInstance(gg[10], float)
                    self.assertIsInstance(gg[11], float)
            except AssertionError:
                self.assertIsNone(gg_ecbp)

        for parent, daughter in GetGG.bm_pairs.items():
            gg_bm = e.get_gg(cdata, "BM", str(parent[0]), int(parent[3]))
            try:
                self.assertIsInstance(gg_bm, list)
                self.assertIsInstance(gg_bm, Iterable)

                for gg in gg_bm:
                    self.assertIsInstance(gg[0], float)
                    self.assertIsInstance(gg[1], float)
                    self.assertIsInstance(gg[2], int)
                    self.assertIsInstance(gg[3], int)
                    
                    try:
                        self.assertIsInstance(gg[4], float)
                    except AssertionError:
                        self.assertIsInstance(gg[4], str)

                    try:
                        self.assertIsInstance(gg[5], float)
                    except AssertionError:
                        self.assertIsInstance(gg[5], str)
                        
                    self.assertIsInstance(gg[6], int)
                    self.assertIsInstance(gg[7], int)

                    try:
                        self.assertIsInstance(gg[8], float)
                    except AssertionError:
                        self.assertIsInstance(gg[8], str)

                    try:
                        self.assertIsInstance(gg[9], float)
                    except AssertionError:
                        self.assertIsInstance(gg[9], str)
                        
                    self.assertIsInstance(gg[10], float)
                    self.assertIsInstance(gg[11], float)
            except AssertionError:
                self.assertIsNone(gg_bm)

        for parent, daughter in GetGG.a_pairs.items():
            gg_a = e.get_gg(cdata, "A", str(parent[0]), int(parent[3]))
            try:
                self.assertIsInstance(gg_a, list)
                self.assertIsInstance(gg_a, Iterable)

                for gg in gg_a:
                    self.assertIsInstance(gg[0], float)
                    self.assertIsInstance(gg[1], float)
                    self.assertIsInstance(gg[2], int)
                    self.assertIsInstance(gg[3], int)
                    
                    try:
                        self.assertIsInstance(gg[4], float)
                    except AssertionError:
                        self.assertIsInstance(gg[4], str)

                    try:
                        self.assertIsInstance(gg[5], float)
                    except AssertionError:
                        self.assertIsInstance(gg[5], str)
                        
                    self.assertIsInstance(gg[6], int)
                    self.assertIsInstance(gg[7], int)

                    try:
                        self.assertIsInstance(gg[8], float)
                    except AssertionError:
                        self.assertIsInstance(gg[8], str)

                    try:
                        self.assertIsInstance(gg[9], float)
                    except AssertionError:
                        self.assertIsInstance(gg[9], str)
                        
                    self.assertIsInstance(gg[10], float)
                    self.assertIsInstance(gg[11], float)
            except AssertionError:
                self.assertIsNone(gg_a)
        

class GetGammaSingles(unittest.TestCase):

    __doc__="""Unit tests for the `get_gamma_singles` method of the GammaGamma 
    class."""

    ecbp_pairs = e.ensdf_pairs(edata,"ECBP")
    bm_pairs = e.ensdf_pairs(edata,"BM")
    a_pairs = e.ensdf_pairs(edata,"A")

    def test_get_gamma_singles_returns_list_for_all_coinc_decays(self):
        for parent, daughter in GetGammaSingles.ecbp_pairs.items():
            g_ecbp = e.get_gamma_singles(cdata, "ECBP", str(parent[0]), int(parent[3]))
            try:
                self.assertIsInstance(g_ecbp, list)
                self.assertIsInstance(g_ecbp, Iterable)
            except AssertionError:
                self.assertIsNone(g_ecbp)

        for parent, daughter in GetGammaSingles.bm_pairs.items():
            g_bm = e.get_gamma_singles(cdata, "BM", str(parent[0]), int(parent[3]))
            try:
                self.assertIsInstance(g_bm, list)
                self.assertIsInstance(g_bm, Iterable)
            except AssertionError:
                self.assertIsNone(g_bm)

        for parent, daughter in GetGammaSingles.a_pairs.items():
            g_a = e.get_gamma_singles(cdata, "A", str(parent[0]), int(parent[3]))
            try:
                self.assertIsInstance(g_a, list)
                self.assertIsInstance(g_a, Iterable)
            except AssertionError:
                self.assertIsNone(g_a)

    def test_get_gamma_singles_returns_none_if_wrong_decay_mode(self):
        g_ecbp = e.get_gamma_singles(cdata, "ECBP", "Co60", 0)
        self.assertIsNone(g_ecbp)
        g_bm = e.get_gamma_singles(cdata, "BM", "Y86", 0)
        self.assertIsNone(g_bm)
        g_a = e.get_gamma_singles(cdata, "A", "Na22", 0)
        self.assertIsNone(g_a)

    def test_get_gamma_singles_returns_none_if_wrong_order_string_args(self):
        g = e.get_gamma_singles(cdata, "Co60", "BM", 0)
        self.assertIsNone(g)
        g = e.get_gamma_singles(cdata, "Y86", 0, "ECBP")
        self.assertIsNone(g)
        g = e.get_gamma_singles(cdata, "Ra226", "A", 0)
        self.assertIsNone(g)

    def test_get_gamma_singles_raises_AttributeError_if_wrong_order_int_args(self):
        with self.assertRaises(AttributeError):
            g = e.get_gamma_singles(cdata, 0, "Ra226", "A")
        with self.assertRaises(AttributeError):
            g = e.get_gamma_singles(cdata, 1, "BM", "Co60")
        with self.assertRaises(AttributeError):
            g = e.get_gamma_singles(cdata, 0, "Y86", "ECBP")

    def test_get_gamma_singles_returns_none_if_illegal_string(self):
        g = e.get_gamma_singles(cdata, "THisIsB@LL@CK$", "Co60", 0)
        self.assertIsNone(g)
        g = e.get_gamma_singles(cdata, "BM", "THisIsB@LL@CK$", 0)
        self.assertIsNone(g)
        g = e.get_gamma_singles(cdata, "THisIsB@LL@CK$", "THisIsB@LL@CK$", 0)
        self.assertIsNone(g)

    def test_get_gamma_singles_raises_TypeError_if_wrong_number_args(self):
        with self.assertRaises(TypeError):
            g = e.get_gamma_singles(cdata)
        with self.assertRaises(TypeError):
            g = e.get_gamma_singles(cdata, "BM")
        with self.assertRaises(TypeError):
            g = e.get_gamma_singles(cdata, "BM", "Co60")
        with self.assertRaises(TypeError):
            g = e.get_gamma_singles(cdata, "BM", "Co60", 0, 2)
        with self.assertRaises(TypeError):
            g = e.get_gamma_singles(cdata, "BM", "Co60", 0, 3, True)

    def test_get_gamma_singles_raises_AttributeError_if_first_arg_not_list(self):
        with self.assertRaises(AttributeError):
            g = e.get_gamma_singles("BM", cdata, "Co60", 0)
        with self.assertRaises(AttributeError):
            g = e.get_gamma_singles("ECBP", cdata, "Y86", 0)
        with self.assertRaises(AttributeError):
            g = e.get_gamma_singles("A", cdata, "Ra226", 0)

    def test_get_gamma_singles_raises_NameError_if_wrong_name_list(self):
        with self.assertRaises(NameError):
            g = e.get_gamma_singles(XXXcdataXX, "BM", "Co60", 0)
        with self.assertRaises(NameError):
            g = e.get_gamma_singles(XXXcdataXX, "ECBP", "Y86", 0)
        with self.assertRaises(NameError):
            g = e.get_gamma_singles(XXXcdataXX, "A", "Ra226", 0)

    def test_get_gamma_singles_raises_KeyError_if_list_with_wrong_keys_gets_passed(self):
        with self.assertRaises(KeyError):
            g = e.get_gamma_singles(edata, "BM", "Co60", 0)
        with self.assertRaises(KeyError):
            g = e.get_gamma_singles(edata, "ECBP", "Y86", 0)
        with self.assertRaises(KeyError):
            g = e.get_gamma_singles(edata, "A", "Ra226", 0)

    def test_get_gamma_singles_KeyError_if_bad_dict_items_in_list(self):
        bad_dict_items_in_list = [{'a':0, 'b':1, 'c':2}]
        with self.assertRaises(KeyError):
            g = e.get_gamma_singles(bad_dict_items_in_list, "BM", "Co60", 0)
        with self.assertRaises(KeyError):
            g = e.get_gamma_singles(bad_dict_items_in_list, "ECBP", "Y86", 0)
        with self.assertRaises(KeyError):
            g = e.get_gamma_singles(bad_dict_items_in_list, "A", "Ra226", 0)

    def test_get_gamma_singles_returned_contents_of_list(self):
        for parent, daughter in GetGG.ecbp_pairs.items():
            g_ecbp = e.get_gamma_singles(cdata, "ECBP", str(parent[0]), int(parent[3]))
            try:
                self.assertIsInstance(g_ecbp, list)
                self.assertIsInstance(g_ecbp, Iterable)

                for g in g_ecbp:
                    self.assertIsInstance(g[0], float)
                    self.assertIsInstance(g[1], int)
                    self.assertIsInstance(g[2], int)
                    
                    try:
                        self.assertIsInstance(g[3], float)
                    except AssertionError:
                        self.assertIsInstance(g[3], str)

                    try:
                        self.assertIsInstance(g[4], float)
                    except AssertionError:
                        self.assertIsInstance(g[4], str)
                        
                    self.assertIsInstance(g[5], float)
                    self.assertIsInstance(g[6], float)
            except AssertionError:
                self.assertIsNone(g_ecbp)

        for parent, daughter in GetGG.bm_pairs.items():
            g_bm = e.get_gamma_singles(cdata, "BM", str(parent[0]), int(parent[3]))
            try:
                self.assertIsInstance(g_bm, list)
                self.assertIsInstance(g_bm, Iterable)

                for g in g_bm:
                    self.assertIsInstance(g[0], float)
                    self.assertIsInstance(g[1], int)
                    self.assertIsInstance(g[2], int)
                    
                    try:
                        self.assertIsInstance(g[3], float)
                    except AssertionError:
                        self.assertIsInstance(g[3], str)

                    try:
                        self.assertIsInstance(g[4], float)
                    except AssertionError:
                        self.assertIsInstance(g[4], str)
                        
                    self.assertIsInstance(g[5], float)
                    self.assertIsInstance(g[6], float)
            except AssertionError:
                self.assertIsNone(g_bm)

        for parent, daughter in GetGG.a_pairs.items():
            g_a = e.get_gamma_singles(cdata, "A", str(parent[0]), int(parent[3]))
            try:
                self.assertIsInstance(g_a, list)
                self.assertIsInstance(g_a, Iterable)

                for g in g_a:
                    self.assertIsInstance(g[0], float)
                    self.assertIsInstance(g[1], int)
                    self.assertIsInstance(g[2], int)
                    
                    try:
                        self.assertIsInstance(g[3], float)
                    except AssertionError:
                        self.assertIsInstance(g[3], str)

                    try:
                        self.assertIsInstance(g[4], float)
                    except AssertionError:
                        self.assertIsInstance(g[4], str)
                        
                    self.assertIsInstance(g[5], float)
                    self.assertIsInstance(g[6], float)
            except AssertionError:
                self.assertIsNone(g_a)


class FindGamma(unittest.TestCase):

    __doc__="""Unit tests for the `find_gamma` method of the GammaGamma 
    class."""

    def test_find_gamma_returns_DataFrame(self):
        df = e.find_gamma(cdata, 1173)
        self.assertIsInstance(df, pd.core.frame.DataFrame)
        df = e.find_gamma(cdata, 1173, 2)
        self.assertIsInstance(df, pd.core.frame.DataFrame)
        df = e.find_gamma(cdata, 1173.5, 0.2)
        self.assertIsInstance(df, pd.core.frame.DataFrame)

        df = e.find_gamma(cdata, 288, 1.9)
        assert type(df) is pd.core.frame.DataFrame
        df = e.find_gamma(cdata, 288.0, 1)
        assert type(df) is pd.core.frame.DataFrame
        df = e.find_gamma(cdata, 288.2, 3.9)
        assert type(df) is pd.core.frame.DataFrame

    def test_find_gamma_returns_none_if_doesnt_exist(self):
        df = e.find_gamma(cdata, 30000.0)
        self.assertIsNone(df)

        df = e.find_gamma(cdata, 30000.0, 15.9)
        self.assertIsNone(df)

    def test_find_gamma_raises_TypeError_if_missing_arguments(self):
        with self.assertRaises(TypeError):
            df = e.find_gamma(cdata)
        with self.assertRaises(TypeError):
            df = e.find_gamma()

    def test_find_gamma_raises_TypeError_if_wrong_argument_types(self):
        with self.assertRaises(TypeError):
            df = e.find_gamma(cdata, "1173.5")
        with self.assertRaises(TypeError):
            df = e.find_gamma(cdata, "1173.5", "0.1")
        with self.assertRaises(TypeError):
            df = e.find_gamma(cdata, 1173.5, "0.1")
        with self.assertRaises(TypeError):
            df = e.find_gamma(cdata, "1173.5", 0.1)
        with self.assertRaises(TypeError):
            df = e.find_gamma(cdata, "THisIsB@LL@CK$")

    def test_find_gamma_raises_TypeError_if_wrong_number_arguments_passed(self):
        with self.assertRaises(TypeError):
            df = e.find_gamma(cdata, 1173.5, 0.1, "THisIsB@LL@CK$")
        with self.assertRaises(TypeError):
            df = e.find_gamma(cdata, 1173.5, 0.1, 3)
        
    def test_find_gamma_raises_NameError_if_wrong_name_list_gets_passed(self):
        with self.assertRaises(NameError):
            df = e.find_gamma(XXXcdataXX, 1173.5, 0.1)
        with self.assertRaises(NameError):
            df = e.find_gamma(XXXcdataXX, 1173.5)

    def test_find_gamma_raises_KeyError_if_list_with_wrong_keys_gets_passed(self):
        with self.assertRaises(KeyError):
            df = e.find_gamma(edata, 1173.5, 0.1)
        with self.assertRaises(KeyError):
            df = e.find_gamma(edata, 1173.5)

    def test_find_gamma_raises_KeyError_if_bad_dict_items_in_list(self):
        bad_dict_items_in_list = [{'a':0, 'b':1, 'c':2}]
        with self.assertRaises(KeyError):
            df = e.find_gamma(bad_dict_items_in_list, 1173.5, 0.1)
        with self.assertRaises(KeyError):
            df = e.find_gamma(bad_dict_items_in_list, 1173.5)

    def test_find_gamma_returned_contents_of_DataFrame(self):
        df = e.find_gamma(cdata, 944.6, 0.1)
        self.assertIsInstance(df, pd.core.frame.DataFrame)
        self.assertIsInstance(df['Parent'], pd.core.series.Series)
        self.assertIsInstance(df['Decay Index'], pd.core.series.Series)
        self.assertIsInstance(df['Ex. Energy'], pd.core.series.Series)
        self.assertIsInstance(df['Daughter'], pd.core.series.Series)
        self.assertIsInstance(df['Decay Mode'], pd.core.series.Series)
        self.assertIsInstance(df['Gamma'], pd.core.series.Series)

        # Explore types after conversion of DataFrame to dictionary
        #df_dict = df.to_dict()

        for index, row in df.iterrows():
            self.assertIsInstance(row['Parent'], str)
            self.assertIsInstance(row['Decay Index'], int)
            self.assertIsInstance(row['Ex. Energy'], str)
            self.assertIsInstance(row['Daughter'], str)
            self.assertIsInstance(row['Decay Mode'], str)
            self.assertIsInstance(row['Gamma'], str)


class FindGammaCoinc(unittest.TestCase):

    __doc__="""Unit tests for the `find_gamma_coinc` method of the GammaGamma 
    class."""

    def test_find_gamma_coinc_returns_DataFrame(self):
        df = e.find_gamma_coinc(cdata, 1332, 1173)
        self.assertIsInstance(df, pd.core.frame.DataFrame)
        df = e.find_gamma_coinc(cdata, 1332, 1173, 2)
        self.assertIsInstance(df, pd.core.frame.DataFrame)
        df = e.find_gamma_coinc(cdata, 1332.5, 1173.2, 0.2)
        self.assertIsInstance(df, pd.core.frame.DataFrame)

        df = e.find_gamma_coinc(cdata, 288, 475, 1.9)
        assert type(df) is pd.core.frame.DataFrame
        df = e.find_gamma_coinc(cdata, 288.0, 475.5, 1)
        assert type(df) is pd.core.frame.DataFrame
        df = e.find_gamma_coinc(cdata, 288.2, 474.6, 3.9)
        assert type(df) is pd.core.frame.DataFrame

    def test_find_gamma_coinc_returns_none_if_doesnt_exist(self):
        df = e.find_gamma_coinc(cdata, 30000, 10000)
        self.assertIsNone(df)
        df = e.find_gamma_coinc(cdata, 30000, 10000, 100)
        self.assertIsNone(df)
        df = e.find_gamma_coinc(cdata, 10000.0, 30000.0, 500.0)
        self.assertIsNone(df)

    def test_find_gamma_coinc_raises_TypeError_if_missing_arguments(self):
        with self.assertRaises(TypeError):
            df = e.find_gamma_coinc(cdata)
        with self.assertRaises(TypeError):
            df = e.find_gamma_coinc()

    def test_find_gamma_coinc_raises_TypeError_if_wrong_argument_types(self):
        with self.assertRaises(TypeError):
            df = e.find_gamma_coinc(cdata, "1332.5", "1173.2")
        with self.assertRaises(TypeError):
            df = e.find_gamma_coinc(cdata, "1332.5", "1173.2", "0.1")
        with self.assertRaises(TypeError):
            df = e.find_gamma_coinc(cdata, 1332.5, 1173.2, "0.1")
        with self.assertRaises(TypeError):
            df = e.find_gamma_coinc(cdata, "1332.5", "1173.2", 0.1)
        with self.assertRaises(TypeError):
            df = e.find_gamma_coinc(cdata, 1332.5, "THisIsB@LL@CK$")

    def test_find_gamma_coinc_raises_TypeError_if_wrong_number_arguments_passed(self):
        with self.assertRaises(TypeError):
            df = e.find_gamma_coinc(cdata, 1332.5, 1173.2, 0.1, "THisIsB@LL@CK$")
        with self.assertRaises(TypeError):
            df = e.find_gamma_coinc(cdata, 1332.5, 1173.2, 0.1, 3)
        with self.assertRaises(TypeError):
            df = e.find_gamma_coinc(cdata, 1332.5)
        
    def test_find_gamma_coinc_raises_NameError_if_wrong_name_list_gets_passed(self):
        with self.assertRaises(NameError):
            df = e.find_gamma_coinc(XXXcdataXX, 1332.5, 1173.2, 0.1)
        with self.assertRaises(NameError):
            df = e.find_gamma_coinc(XXXcdataXX, 1332.5, 1173.5)

    def test_find_gamma_coinc_raises_KeyError_if_list_with_wrong_keys_gets_passed(self):
        with self.assertRaises(KeyError):
            df = e.find_gamma_coinc(edata, 1332.5, 1173.2, 0.1)
        with self.assertRaises(KeyError):
            df = e.find_gamma_coinc(edata, 1332.5, 1173.2)

    def test_find_gamma_coinc_raises_KeyError_if_bad_dict_items_in_list(self):
        bad_dict_items_in_list = [{'a':0, 'b':1, 'c':2}]
        with self.assertRaises(KeyError):
            df = e.find_gamma_coinc(bad_dict_items_in_list, 1332.5, 1173.2, 0.1)
        with self.assertRaises(KeyError):
            df = e.find_gamma_coinc(bad_dict_items_in_list, 1332.5, 1173.2)

    def test_find_gamma_coinc_returned_contents_of_DataFrame(self):
        df = e.find_gamma_coinc(cdata, 944.6, 656)
        self.assertIsInstance(df, pd.core.frame.DataFrame)
        self.assertIsInstance(df['Parent'], pd.core.series.Series)
        self.assertIsInstance(df['Decay Index'], pd.core.series.Series)
        self.assertIsInstance(df['Ex. Energy'], pd.core.series.Series)
        self.assertIsInstance(df['Daughter'], pd.core.series.Series)
        self.assertIsInstance(df['Decay Mode'], pd.core.series.Series)
        self.assertIsInstance(df['Gamma 1'], pd.core.series.Series)
        self.assertIsInstance(df['Gamma 2'], pd.core.series.Series)

        # Explore types after conversion of DataFrame to dictionary
        #df_dict = df.to_dict()

        for index, row in df.iterrows():
            self.assertIsInstance(row['Parent'], str)
            self.assertIsInstance(row['Decay Index'], int)
            self.assertIsInstance(row['Ex. Energy'], str)
            self.assertIsInstance(row['Daughter'], str)
            self.assertIsInstance(row['Decay Mode'], str)
            self.assertIsInstance(row['Gamma 1'], str)
            self.assertIsInstance(row['Gamma 2'], str)


