import pytest
import unittest
import numpy as np
import pandas as pd
from collections.abc import Iterable
import re

import paceENSDF as pe
e = pe.ENSDF()
edata = e.load_ensdf()
cdata = e.load_pace()

class GetGX(unittest.TestCase):

    __doc__="""Unit tests for the `get_gx` method of the GammaX class."""

    ecbp_pairs = e.ensdf_pairs(edata,"ECBP")
    bm_pairs = e.ensdf_pairs(edata,"BM")
    a_pairs = e.ensdf_pairs(edata,"A")
    
    def test_get_gx_returns_list_for_all_coinc_decays(self):
        for parent, daughter in GetGX.ecbp_pairs.items():
            gx_ecbp = e.get_gx(cdata, "ECBP", str(parent[0]), int(parent[3]))
            try:
                self.assertIsInstance(gx_ecbp, list)
                self.assertIsInstance(gx_ecbp, Iterable)

                lot1 = []
                for coinc in gx_ecbp:
                    lot1.append((coinc[1], coinc[2]))
                lot1 = list(set(lot1))

                for tc1 in lot1:
                    c1_gx = e.get_gx(cdata, "ECBP", str(parent[0]), int(parent[3]), int(tc1[0]), int(tc1[1]))
                    self.assertIsInstance(c1_gx, list)
                    self.assertIsInstance(c1_gx, Iterable)
            except AssertionError:
                self.assertIsNone(gx_ecbp)

        for parent, daughter in GetGX.bm_pairs.items():
            gx_bm = e.get_gx(cdata, "BM", str(parent[0]), int(parent[3]))
            try:
                self.assertIsInstance(gx_bm, list)
                self.assertIsInstance(gx_bm, Iterable)

                lot1 = []
                for coinc in gx_bm:
                    lot1.append((coinc[1], coinc[2]))
                lot1 = list(set(lot1))

                for tc1 in lot1:
                    c1_gx = e.get_gx(cdata, "BM", str(parent[0]), int(parent[3]), int(tc1[0]), int(tc1[1]))
                    self.assertIsInstance(c1_gx, list)
                    self.assertIsInstance(c1_gx, Iterable)
            except AssertionError:
                self.assertIsNone(gx_bm)

        for parent, daughter in GetGX.a_pairs.items():
            gx_a = e.get_gx(cdata, "A", str(parent[0]), int(parent[3]))
            try:
                self.assertIsInstance(gx_a, list)
                self.assertIsInstance(gx_a, Iterable)

                lot1 = []
                for coinc in gx_a:
                    lot1.append((coinc[1], coinc[2]))
                lot1 = list(set(lot1))

                for tc1 in lot1:
                    c1_gx = e.get_gx(cdata, "A", str(parent[0]), int(parent[3]), int(tc1[0]), int(tc1[1]))
                    self.assertIsInstance(c1_gx, list)
                    self.assertIsInstance(c1_gx, Iterable)
            except AssertionError:
                self.assertIsNone(gx_a)

    def test_get_gx_returns_none_if_wrong_decay_mode(self):
        gx_ecbp = e.get_gx(cdata, "ECBP", "Co60", 0)
        self.assertIsNone(gx_ecbp)
        gx_ecbp = e.get_gx(cdata, "ECBP", "Co60", 0, 2, 1)
        self.assertIsNone(gx_ecbp)
        
        gx_bm = e.get_gx(cdata, "BM", "Y86", 0)
        self.assertIsNone(gx_bm)
        gx_bm = e.get_gx(cdata, "BM", "Y86", 0, 2, 1)
        self.assertIsNone(gx_bm)
        
        gx_a = e.get_gx(cdata, "A", "Na22", 0)
        self.assertIsNone(gx_a)
        gx_a = e.get_gx(cdata, "A", "Na22", 0, 2, 1)
        self.assertIsNone(gx_a)

    def test_get_gx_returns_none_if_missing_args(self):
        gx = e.get_gx(cdata, "BM", "Co60")
        self.assertIsNone(gx)
        gx = e.get_gx(cdata, "BM")
        self.assertIsNone(gx)
        gx = e.get_gx(cdata, "Co60", 0)
        self.assertIsNone(gx)
        gx = e.get_gx(cdata, "Co60")
        self.assertIsNone(gx)

    def test_get_gx_returns_none_if_wrong_number_args(self):
        gx = e.get_gx(cdata, "BM", "Co60", 0, 2)
        self.assertIsNone(gx)
        gx = e.get_gx(cdata, "BM", "Co60", 0, 2, 1, 2)
        self.assertIsNone(gx)

    def test_get_gx_returns_none_if_wrong_order_args(self):
        gx = e.get_gx(cdata, "Co60", "BM", 0)
        self.assertIsNone(gx)
        gx = e.get_gx(cdata, "Co60", "BM", 0, 2, 1)
        self.assertIsNone(gx)

        gx = e.get_gx(cdata, "Y86", "ECBP", 0)
        self.assertIsNone(gx)
        gx = e.get_gx(cdata, "Y86", "ECBP", 0, 2, 1)
        self.assertIsNone(gx)

        gx = e.get_gx(cdata, "Ra226", "A", 0)
        self.assertIsNone(gx)
        gx = e.get_gx(cdata, "Ra226", "A", 0, 2, 1)
        self.assertIsNone(gx)
        
    def test_get_gx_raises_TypeError_if_no_args(self):
        with self.assertRaises(TypeError):
            gx = e.get_gx(cdata)

    def test_get_gx_returns_none_if_illegal_string(self):
        gx = e.get_gx(cdata, "THisIsB@LL@CK$", "Co60", 0)
        self.assertIsNone(gx)
        gx = e.get_gx(cdata, "BM", "THisIsB@LL@CK$", 0)
        self.assertIsNone(gx)
        gx = e.get_gx(cdata, "THisIsB@LL@CK$", "THisIsB@LL@CK$", 0)
        self.assertIsNone(gx)

    def test_get_gx_raises_AttributeError_if_first_arg_not_list(self):
        with self.assertRaises(AttributeError):
            gx = e.get_gx("BM", cdata, "Co60", 0)
        with self.assertRaises(AttributeError):
            gx = e.get_gx("ECBP", cdata, "Y86", 0)
        with self.assertRaises(AttributeError):
            gx = e.get_gx("A", cdata, "Ra226", 0)

    def test_get_gx_raises_NameError_if_wrong_name_list(self):
        with self.assertRaises(NameError):
            gx = e.get_gx(XXXcdataXX, "BM", "Co60", 0)
        with self.assertRaises(NameError):
            gx = e.get_gx(XXXcdataXX, "ECBP", "Y86", 0)
        with self.assertRaises(NameError):
            gx = e.get_gx(XXXcdataXX, "A", "Ra226", 0)

    def test_get_gx_raises_KeyError_if_wrong_list(self):
        with self.assertRaises(KeyError):
            gx = e.get_gx(edata, "BM", "Co60", 0)
        with self.assertRaises(KeyError):
            gx = e.get_gx(edata, "BM", "Co60", 0, 2, 1)
            
        with self.assertRaises(KeyError):
            gx = e.get_gx(edata, "ECBP", "Y86", 0)
        with self.assertRaises(KeyError):
            gx = e.get_gx(edata, "ECBP", "Y86", 0, 2, 1)
            
        with self.assertRaises(KeyError):
            gx = e.get_gx(edata, "A", "Ra226", 0)
        with self.assertRaises(KeyError):
            gx = e.get_gx(edata, "A", "Ra226", 0, 2, 1)

    def test_get_gx_KeyError_if_bad_dict_items_in_list(self):
        bad_dict_items_in_list = [{'a':0, 'b':1, 'c':2}]
        with self.assertRaises(KeyError):
            gx = e.get_gx(bad_dict_items_in_list, "BM", "Co60", 0)
        with self.assertRaises(KeyError):
            gx = e.get_gx(bad_dict_items_in_list, "BM", "Co60", 0, 2, 1)

        with self.assertRaises(KeyError):
            gx = e.get_gx(bad_dict_items_in_list, "ECBP", "Y86", 0)
        with self.assertRaises(KeyError):
            gx = e.get_gx(bad_dict_items_in_list, "ECBP", "Y86", 0, 2, 1)

        with self.assertRaises(KeyError):
            gx = e.get_gx(bad_dict_items_in_list, "A", "Ra226", 0)
        with self.assertRaises(KeyError):
            gx = e.get_gx(bad_dict_items_in_list, "A", "Ra226", 0, 2, 1)

    def test_get_gx_returned_contents_of_list(self):
        for parent, daughter in GetGX.ecbp_pairs.items():
            gx_ecbp = e.get_gx(cdata, "ECBP", str(parent[0]), int(parent[3]))
            try:
                self.assertIsInstance(gx_ecbp, list)
                self.assertIsInstance(gx_ecbp, Iterable)

                for gx in gx_ecbp:
                    self.assertIsInstance(gx[0], float)
                    self.assertIsInstance(gx[1], int)
                    self.assertIsInstance(gx[2], int)
                    self.assertIsInstance(gx[3], float)
                    self.assertIsInstance(gx[4], str)
                    self.assertIsInstance(gx[5], float)
                    self.assertIsInstance(gx[6], float)
            except AssertionError:
                self.assertIsNone(gx_ecbp)

        for parent, daughter in GetGX.bm_pairs.items():
            gx_bm = e.get_gx(cdata, "BM", str(parent[0]), int(parent[3]))
            try:
                self.assertIsInstance(gx_bm, list)
                self.assertIsInstance(gx_bm, Iterable)

                for gx in gx_bm:
                    self.assertIsInstance(gx[0], float)
                    self.assertIsInstance(gx[1], int)
                    self.assertIsInstance(gx[2], int)
                    self.assertIsInstance(gx[3], float)
                    self.assertIsInstance(gx[4], str)
                    self.assertIsInstance(gx[5], float)
                    self.assertIsInstance(gx[6], float)
            except AssertionError:
                self.assertIsNone(gx_bm)

        for parent, daughter in GetGX.a_pairs.items():
            gx_a = e.get_gx(cdata, "A", str(parent[0]), int(parent[3]))
            try:
                self.assertIsInstance(gx_a, list)
                self.assertIsInstance(gx_a, Iterable)

                for gx in gx_a:
                    self.assertIsInstance(gx[0], float)
                    self.assertIsInstance(gx[1], int)
                    self.assertIsInstance(gx[2], int)
                    self.assertIsInstance(gx[3], float)
                    self.assertIsInstance(gx[4], str)
                    self.assertIsInstance(gx[5], float)
                    self.assertIsInstance(gx[6], float)
            except AssertionError:
                self.assertIsNone(gx_a)


class GetXraySingles(unittest.TestCase):

    __doc__="""Unit tests for the `get_xray_singles` method of the GammaX 
    class."""

    ecbp_pairs = e.ensdf_pairs(edata,"ECBP")
    bm_pairs = e.ensdf_pairs(edata,"BM")
    a_pairs = e.ensdf_pairs(edata,"A")

    def test_get_xray_singles_returns_list_for_all_coinc_decays(self):
        for parent, daughter in GetXraySingles.ecbp_pairs.items():
            x_ecbp = e.get_xray_singles(cdata, "ECBP", str(parent[0]), int(parent[3]))
            try:
                self.assertIsInstance(x_ecbp, list)
                self.assertIsInstance(x_ecbp, Iterable)
                self.assertEqual(len(x_ecbp), 6)
            except AssertionError:
                self.assertIsNone(x_ecbp)

        for parent, daughter in GetXraySingles.bm_pairs.items():
            x_bm = e.get_xray_singles(cdata, "BM", str(parent[0]), int(parent[3]))
            try:
                self.assertIsInstance(x_bm, list)
                self.assertIsInstance(x_bm, Iterable)
                self.assertEqual(len(x_bm), 6)
            except AssertionError:
                self.assertIsNone(x_bm)

        for parent, daughter in GetXraySingles.a_pairs.items():
            x_a = e.get_xray_singles(cdata, "A", str(parent[0]), int(parent[3]))
            try:
                self.assertIsInstance(x_a, list)
                self.assertIsInstance(x_a, Iterable)
                self.assertEqual(len(x_a), 6)
            except AssertionError:
                self.assertIsNone(x_a)

    def test_get_xray_singles_returns_none_if_wrong_decay_mode(self):
        x_ecbp = e.get_xray_singles(cdata, "ECBP", "Co60", 0)
        self.assertIsNone(x_ecbp)
        x_bm = e.get_xray_singles(cdata, "BM", "Y86", 0)
        self.assertIsNone(x_bm)
        x_a = e.get_xray_singles(cdata, "A", "Na22", 0)
        self.assertIsNone(x_a)

    def test_get_xray_singles_returns_none_if_wrong_order_string_args(self):
        x = e.get_xray_singles(cdata, "Co60", "BM", 0)
        self.assertIsNone(x)
        x = e.get_xray_singles(cdata, "Y86", 0, "ECBP")
        self.assertIsNone(x)
        x = e.get_xray_singles(cdata, "Ra226", "A", 0)
        self.assertIsNone(x)

    def test_get_xray_singles_raises_AttributeError_if_wrong_order_int_args(self):
        with self.assertRaises(AttributeError):
            x = e.get_xray_singles(cdata, 0, "Ra226", "A")
        with self.assertRaises(AttributeError):
            x = e.get_xray_singles(cdata, 1, "BM", "Co60")
        with self.assertRaises(AttributeError):
            x = e.get_xray_singles(cdata, 0, "Y86", "ECBP")

    def test_get_xray_singles_returns_none_if_illegal_string(self):
        x = e.get_xray_singles(cdata, "THisIsB@LL@CK$", "Co60", 0)
        self.assertIsNone(x)
        x = e.get_xray_singles(cdata, "BM", "THisIsB@LL@CK$", 0)
        self.assertIsNone(x)
        x = e.get_xray_singles(cdata, "THisIsB@LL@CK$", "THisIsB@LL@CK$", 0)
        self.assertIsNone(x)

    def test_get_xray_singles_raises_TypeError_if_wrong_number_args(self):
        with self.assertRaises(TypeError):
            x = e.get_xray_singles(cdata)
        with self.assertRaises(TypeError):
            x = e.get_xray_singles(cdata, "BM")
        with self.assertRaises(TypeError):
            x = e.get_xray_singles(cdata, "BM", "Co60")
        with self.assertRaises(TypeError):
            x = e.get_xray_singles(cdata, "BM", "Co60", 0, 2)
        with self.assertRaises(TypeError):
            x = e.get_xray_singles(cdata, "BM", "Co60", 0, 3, True)

    def test_get_xray_singles_raises_AttributeError_if_first_arg_not_list(self):
        with self.assertRaises(AttributeError):
            x = e.get_xray_singles("BM", cdata, "Co60", 0)
        with self.assertRaises(AttributeError):
            x = e.get_xray_singles("ECBP", cdata, "Y86", 0)
        with self.assertRaises(AttributeError):
            x = e.get_xray_singles("A", cdata, "Ra226", 0)

    def test_get_xray_singles_raises_NameError_if_wrong_name_list(self):
        with self.assertRaises(NameError):
            x = e.get_xray_singles(XXXcdataXX, "BM", "Co60", 0)
        with self.assertRaises(NameError):
            x = e.get_xray_singles(XXXcdataXX, "ECBP", "Y86", 0)
        with self.assertRaises(NameError):
            x = e.get_xray_singles(XXXcdataXX, "A", "Ra226", 0)

    def test_get_xray_singles_raises_KeyError_if_list_with_wrong_keys_gets_passed(self):
        with self.assertRaises(KeyError):
            x = e.get_xray_singles(edata, "BM", "Co60", 0)
        with self.assertRaises(KeyError):
            x = e.get_xray_singles(edata, "ECBP", "Y86", 0)
        with self.assertRaises(KeyError):
            x = e.get_xray_singles(edata, "A", "Ra226", 0)

    def test_get_xray_singles_KeyError_if_bad_dict_items_in_list(self):
        bad_dict_items_in_list = [{'a':0, 'b':1, 'c':2}]
        with self.assertRaises(KeyError):
            x = e.get_xray_singles(bad_dict_items_in_list, "BM", "Co60", 0)
        with self.assertRaises(KeyError):
            x = e.get_xray_singles(bad_dict_items_in_list, "ECBP", "Y86", 0)
        with self.assertRaises(KeyError):
            x = e.get_xray_singles(bad_dict_items_in_list, "A", "Ra226", 0)

    def test_get_xray_singles_returned_contents_of_list(self):
        for parent, daughter in GetGX.ecbp_pairs.items():
            x_ecbp = e.get_xray_singles(cdata, "ECBP", str(parent[0]), int(parent[3]))
            try:
                self.assertIsInstance(x_ecbp, list)
                self.assertIsInstance(x_ecbp, Iterable)
                self.assertEqual(len(x_ecbp), 6)

                for x in x_ecbp:
                    self.assertIsInstance(x, list)
                    self.assertIsInstance(x, Iterable)
                    self.assertEqual(len(x), 3)
                    
                    self.assertIsInstance(x[0], float)
                    self.assertIsInstance(x[1], float)
                    self.assertIsInstance(x[2], float)
            except AssertionError:
                self.assertIsNone(x_ecbp)

        for parent, daughter in GetGX.ecbp_pairs.items():
            x_bm = e.get_xray_singles(cdata, "BM", str(parent[0]), int(parent[3]))
            try:
                self.assertIsInstance(x_bm, list)
                self.assertIsInstance(x_bm, Iterable)
                self.assertEqual(len(x_bm), 6)

                for x in x_bm:
                    self.assertIsInstance(x, list)
                    self.assertIsInstance(x, Iterable)
                    self.assertEqual(len(x), 3)
                    
                    self.assertIsInstance(x[0], float)
                    self.assertIsInstance(x[1], float)
                    self.assertIsInstance(x[2], float)
            except AssertionError:
                self.assertIsNone(x_bm)

        for parent, daughter in GetGX.ecbp_pairs.items():
            x_a = e.get_xray_singles(cdata, "A", str(parent[0]), int(parent[3]))
            try:
                self.assertIsInstance(x_a, list)
                self.assertIsInstance(x_a, Iterable)
                self.assertEqual(len(x_a), 6)

                for x in x_a:
                    self.assertIsInstance(x, list)
                    self.assertIsInstance(x, Iterable)
                    self.assertEqual(len(x), 3)

                    self.assertIsInstance(x[0], float)
                    self.assertIsInstance(x[1], float)
                    self.assertIsInstance(x[2], float)
            except AssertionError:
                self.assertIsNone(x_a)


class GetXrayContribution(unittest.TestCase):

    __doc__="""Unit tests for the `get_xray_contribution` method of the GammaX 
    class."""

    ecbp_pairs = e.ensdf_pairs(edata,"ECBP")
    bm_pairs = e.ensdf_pairs(edata,"BM")
    a_pairs = e.ensdf_pairs(edata,"A")

    def test_get_xray_contribution_returns_DataFrame(self):
        for parent, daughter in GetGX.ecbp_pairs.items():
            try:
                df = e.get_xray_contribution(cdata, "ECBP", str(parent[0]), int(parent[3]))
                self.assertIsInstance(df, pd.core.frame.DataFrame)
            except AssertionError:
                self.assertIsNone(df)

        for parent, daughter in GetGX.bm_pairs.items():
            try:
                df = e.get_xray_contribution(cdata, "BM", str(parent[0]), int(parent[3]))
                self.assertIsInstance(df, pd.core.frame.DataFrame)
            except AssertionError:
                self.assertIsNone(df)

        for parent, daughter in GetGX.a_pairs.items():
            try:
                df = e.get_xray_contribution(cdata, "A", str(parent[0]), int(parent[3]))
                self.assertIsInstance(df, pd.core.frame.DataFrame)
            except AssertionError:
                self.assertIsNone(df)

    def test_get_xray_contribution_returns_none_if_doesnt_exist(self):
        df = e.get_xray_contribution(cdata, "ECBP", "Co60", 0)
        self.assertIsNone(df)

    def test_get_xray_contribution_raises_TypeError_if_wrong_number_of_arguments(self):
        with self.assertRaises(TypeError):
            df = e.get_xray_contribution(cdata, "BM", "Co60")
        with self.assertRaises(TypeError):
            df = e.get_xray_contribution(cdata, "Co60", 0)
        with self.assertRaises(TypeError):
            df = e.get_xray_contribution(cdata, "BM")
        with self.assertRaises(TypeError):
            df = e.get_xray_contribution(cdata)
        with self.assertRaises(TypeError):
            df = e.get_xray_contribution()
        with self.assertRaises(TypeError):
            df = e.get_xray_contribution(cdata, "A", "Ra226", 0, True)
        with self.assertRaises(TypeError):
            df = e.get_xray_contribution(cdata, "A", "Ra226", 0, 3, False)
        with self.assertRaises(TypeError):
            df = e.get_xray_contribution(cdata, "A", "Ra226", 0, 3, False, "THisIsB@LL@CK$")

    def test_get_xray_contribution_returns_none_if_wrong_order_string_args(self):
        df = e.get_xray_contribution(cdata, "Co60", "BM", 0)
        self.assertIsNone(df)
        df = e.get_xray_contribution(cdata, "Y86", 0, "ECBP")
        self.assertIsNone(df)
        df = e.get_xray_contribution(cdata, "Ra226", "A", 0)
        self.assertIsNone(df)

    def test_get_xray_contribution_raises_AttributeError_if_wrong_order_int_args(self):
        with self.assertRaises(AttributeError):
            df = e.get_xray_contribution(cdata, 0, "Ra226", "A")
        with self.assertRaises(AttributeError):
            df = e.get_xray_contribution(cdata, 1, "BM", "Co60")
        with self.assertRaises(AttributeError):
            df = e.get_xray_contribution(cdata, 0, "Y86", "ECBP")

    def test_get_xray_contribution_returns_none_if_illegal_string(self):
        df = e.get_xray_contribution(cdata, "THisIsB@LL@CK$", "Co60", 0)
        self.assertIsNone(df)
        df = e.get_xray_contribution(cdata, "BM", "THisIsB@LL@CK$", 0)
        self.assertIsNone(df)
        df = e.get_xray_contribution(cdata, "THisIsB@LL@CK$", "THisIsB@LL@CK$", 0)
        self.assertIsNone(df)

    def test_get_xray_contribution_raises_AttributeError_if_first_arg_not_list(self):
        with self.assertRaises(AttributeError):
            df = e.get_xray_contribution("BM", cdata, "Co60", 0)
        with self.assertRaises(AttributeError):
            df = e.get_xray_contribution("ECBP", cdata, "Y86", 0)
        with self.assertRaises(AttributeError):
            df = e.get_xray_contribution("A", cdata, "Ra226", 0)

    def test_get_xray_contribution_raises_NameError_if_wrong_name_list(self):
        with self.assertRaises(NameError):
            df = e.get_xray_contribution(XXXcdataXX, "BM", "Co60", 0)
        with self.assertRaises(NameError):
            df = e.get_xray_contribution(XXXcdataXX, "ECBP", "Y86", 0)
        with self.assertRaises(NameError):
            df = e.get_xray_contribution(XXXcdataXX, "A", "Ra226", 0)

    def test_get_xray_contribution_raises_KeyError_if_list_with_wrong_keys_gets_passed(self):
        with self.assertRaises(KeyError):
            df = e.get_xray_contribution(edata, "BM", "Co60", 0)
        with self.assertRaises(KeyError):
            df = e.get_xray_contribution(edata, "ECBP", "Y86", 0)
        with self.assertRaises(KeyError):
            df = e.get_xray_contribution(edata, "A", "Ra226", 0)

    def test_get_xray_contribution_KeyError_if_bad_dict_items_in_list(self):
        bad_dict_items_in_list = [{'a':0, 'b':1, 'c':2}]
        with self.assertRaises(KeyError):
            df = e.get_xray_contribution(bad_dict_items_in_list, "BM", "Co60", 0)
        with self.assertRaises(KeyError):
            df = e.get_xray_contribution(bad_dict_items_in_list, "ECBP", "Y86", 0)
        with self.assertRaises(KeyError):
            df = e.get_xray_contribution(bad_dict_items_in_list, "A", "Ra226", 0)

    def test_get_xray_contribution_returned_contents_of_DataFrame(self):
        for parent, daughter in GetGX.ecbp_pairs.items():
            try:
                df = e.get_xray_contribution(cdata, "ECBP", str(parent[0]), int(parent[3]))
                self.assertIsInstance(df, pd.core.frame.DataFrame)
                self.assertIsInstance(df['Eg (keV)'], pd.core.series.Series)
                self.assertIsInstance(df['X-ray'], pd.core.series.Series)
                self.assertIsInstance(df['Ex (keV)'], pd.core.series.Series)
                self.assertIsInstance(df['Ix (%)'], pd.core.series.Series)
                self.assertIsInstance(df['dIx'], pd.core.series.Series)

                for index, row in df.iterrows():
                    self.assertIsInstance(row['Eg (keV)'], float)
                    self.assertIsInstance(row['X-ray'], str)
                    self.assertIsInstance(row['Ex (keV)'], float)
                    self.assertIsInstance(row['Ix (%)'], float)
                    self.assertIsInstance(row['dIx'], float)
                
            except AssertionError:
                self.assertIsNone(df)

        for parent, daughter in GetGX.bm_pairs.items():
            try:
                df = e.get_xray_contribution(cdata, "BM", str(parent[0]), int(parent[3]))
                self.assertIsInstance(df, pd.core.frame.DataFrame)
                self.assertIsInstance(df['Eg (keV)'], pd.core.series.Series)
                self.assertIsInstance(df['X-ray'], pd.core.series.Series)
                self.assertIsInstance(df['Ex (keV)'], pd.core.series.Series)
                self.assertIsInstance(df['Ix (%)'], pd.core.series.Series)
                self.assertIsInstance(df['dIx'], pd.core.series.Series)

                for index, row in df.iterrows():
                    self.assertIsInstance(row['Eg (keV)'], float)
                    self.assertIsInstance(row['X-ray'], str)
                    self.assertIsInstance(row['Ex (keV)'], float)
                    self.assertIsInstance(row['Ix (%)'], float)
                    self.assertIsInstance(row['dIx'], float)
                
            except AssertionError:
                self.assertIsNone(df)

        for parent, daughter in GetGX.a_pairs.items():
            try:
                df = e.get_xray_contribution(cdata, "A", str(parent[0]), int(parent[3]))
                self.assertIsInstance(df, pd.core.frame.DataFrame)
                self.assertIsInstance(df['Eg (keV)'], pd.core.series.Series)
                self.assertIsInstance(df['X-ray'], pd.core.series.Series)
                self.assertIsInstance(df['Ex (keV)'], pd.core.series.Series)
                self.assertIsInstance(df['Ix (%)'], pd.core.series.Series)
                self.assertIsInstance(df['dIx'], pd.core.series.Series)

                for index, row in df.iterrows():
                    self.assertIsInstance(row['Eg (keV)'], float)
                    self.assertIsInstance(row['X-ray'], str)
                    self.assertIsInstance(row['Ex (keV)'], float)
                    self.assertIsInstance(row['Ix (%)'], float)
                    self.assertIsInstance(row['dIx'], float)
                
            except AssertionError:
                self.assertIsNone(df)


class FindXray(unittest.TestCase):

    __doc__="""Unit tests for the `find_xray` method of the GammaX class."""

    def test_find_xray_returns_DataFrame(self):
        df = e.find_xray(cdata, 53)
        self.assertIsInstance(df, pd.core.frame.DataFrame)
        df = e.find_xray(cdata, 53, 2)
        self.assertIsInstance(df, pd.core.frame.DataFrame)
        df = e.find_xray(cdata, 53.5, 0.2)
        self.assertIsInstance(df, pd.core.frame.DataFrame)

        df = e.find_xray(cdata, 105, 1.9)
        assert type(df) is pd.core.frame.DataFrame
        df = e.find_xray(cdata, 105.0, 1)
        assert type(df) is pd.core.frame.DataFrame
        df = e.find_xray(cdata, 104.8, 3.5)
        assert type(df) is pd.core.frame.DataFrame

    def test_find_xray_returns_none_if_doesnt_exist(self):
        df = e.find_xray(cdata, 30000.0)
        self.assertIsNone(df)

        df = e.find_xray(cdata, 30000.0, 15.9)
        self.assertIsNone(df)

    def test_find_xray_raises_TypeError_if_missing_arguments(self):
        with self.assertRaises(TypeError):
            df = e.find_xray(cdata)
        with self.assertRaises(TypeError):
            df = e.find_xray()

    def test_find_xray_raises_TypeError_if_wrong_argument_types(self):
        with self.assertRaises(TypeError):
            df = e.find_xray(cdata, "53.5")
        with self.assertRaises(TypeError):
            df = e.find_xray(cdata, "53.5", "0.1")
        with self.assertRaises(TypeError):
            df = e.find_xray(cdata, 53.5, "0.1")
        with self.assertRaises(TypeError):
            df = e.find_xray(cdata, "53.5", 0.1)
        with self.assertRaises(TypeError):
            df = e.find_xray(cdata, "THisIsB@LL@CK$")

    def test_find_xray_raises_TypeError_if_wrong_number_arguments_passed(self):
        with self.assertRaises(TypeError):
            df = e.find_xray(cdata, 53.5, 0.1, "THisIsB@LL@CK$")
        with self.assertRaises(TypeError):
            df = e.find_xray(cdata, 53.5, 0.1, 3)
        
    def test_find_xray_raises_NameError_if_wrong_name_list_gets_passed(self):
        with self.assertRaises(NameError):
            df = e.find_xray(XXXcdataXX, 53.5, 0.1)
        with self.assertRaises(NameError):
            df = e.find_xray(XXXcdataXX, 53.5)

    def test_find_xray_raises_KeyError_if_list_with_wrong_keys_gets_passed(self):
        with self.assertRaises(KeyError):
            df = e.find_xray(edata, 53.5, 0.1)
        with self.assertRaises(KeyError):
            df = e.find_xray(edata, 53.5)

    def test_find_xray_raises_KeyError_if_bad_dict_items_in_list(self):
        bad_dict_items_in_list = [{'a':0, 'b':1, 'c':2}]
        with self.assertRaises(KeyError):
            df = e.find_xray(bad_dict_items_in_list, 53.5, 0.1)
        with self.assertRaises(KeyError):
            df = e.find_xray(bad_dict_items_in_list, 53.5)

    def test_find_xray_returned_contents_of_DataFrame(self):
        df = e.find_xray(cdata, 52.9, 0.1)
        self.assertIsInstance(df, pd.core.frame.DataFrame)
        self.assertIsInstance(df['Parent'], pd.core.series.Series)
        self.assertIsInstance(df['Decay Index'], pd.core.series.Series)
        self.assertIsInstance(df['Ex. Energy'], pd.core.series.Series)
        self.assertIsInstance(df['Daughter'], pd.core.series.Series)
        self.assertIsInstance(df['Decay Mode'], pd.core.series.Series)
        self.assertIsInstance(df['X-ray Label'], pd.core.series.Series)
        self.assertIsInstance(df['X-ray Energy'], pd.core.series.Series)

        # Explore types after conversion of DataFrame to dictionary
        #df_dict = df.to_dict()

        for index, row in df.iterrows():
            self.assertIsInstance(row['Parent'], str)
            self.assertIsInstance(row['Decay Index'], int)
            self.assertIsInstance(row['Ex. Energy'], str)
            self.assertIsInstance(row['Daughter'], str)
            self.assertIsInstance(row['Decay Mode'], str)
            self.assertIsInstance(row['X-ray Label'], str)
            self.assertIsInstance(row['X-ray Energy'], str)

class FindXrayCoinc(unittest.TestCase):

    __doc__="""Unit tests for the `find_xray_coinc` method of the GammaX 
    class."""

    def test_find_xray_coinc_returns_DataFrame(self):
        df = e.find_xray_coinc(cdata, 8, 1173)
        self.assertIsInstance(df, pd.core.frame.DataFrame)
        df = e.find_xray_coinc(cdata, 8, 1173, 2)
        self.assertIsInstance(df, pd.core.frame.DataFrame)
        df = e.find_xray_coinc(cdata, 8.5, 1173.2, 0.3)
        self.assertIsInstance(df, pd.core.frame.DataFrame)

        df = e.find_xray_coinc(cdata, 100, 475, 1.9)
        assert type(df) is pd.core.frame.DataFrame
        df = e.find_xray_coinc(cdata, 100.0, 475.5, 1)
        assert type(df) is pd.core.frame.DataFrame
        df = e.find_xray_coinc(cdata, 100.2, 474.6, 3.9)
        assert type(df) is pd.core.frame.DataFrame

    def test_find_xray_coinc_returns_none_if_doesnt_exist(self):
        df = e.find_xray_coinc(cdata, 30000, 10000)
        self.assertIsNone(df)
        df = e.find_xray_coinc(cdata, 30000, 10000, 100)
        self.assertIsNone(df)
        df = e.find_xray_coinc(cdata, 10000.0, 30000.0, 500.0)
        self.assertIsNone(df)

    def test_find_xray_coinc_raises_TypeError_if_missing_arguments(self):
        with self.assertRaises(TypeError):
            df = e.find_xray_coinc(cdata)
        with self.assertRaises(TypeError):
            df = e.find_xray_coinc()

    def test_find_xray_coinc_raises_TypeError_if_wrong_argument_types(self):
        with self.assertRaises(TypeError):
            df = e.find_xray_coinc(cdata, "8.5", "1173.2")
        with self.assertRaises(TypeError):
            df = e.find_xray_coinc(cdata, "8.5", "1173.2", "0.3")
        with self.assertRaises(TypeError):
            df = e.find_xray_coinc(cdata, 8.5, 1173.2, "0.3")
        with self.assertRaises(TypeError):
            df = e.find_xray_coinc(cdata, "8.5", "1173.2", 0.3)
        with self.assertRaises(TypeError):
            df = e.find_xray_coinc(cdata, 8.5, "THisIsB@LL@CK$")

    def test_find_xray_coinc_raises_TypeError_if_wrong_number_arguments_passed(self):
        with self.assertRaises(TypeError):
            df = e.find_xray_coinc(cdata, 8.5, 1173.2, 0.1, "THisIsB@LL@CK$")
        with self.assertRaises(TypeError):
            df = e.find_xray_coinc(cdata, 8.5, 1173.2, 0.1, 3)
        with self.assertRaises(TypeError):
            df = e.find_xray_coinc(cdata, 8.5)
        
    def test_find_xray_coinc_raises_NameError_if_wrong_name_list_gets_passed(self):
        with self.assertRaises(NameError):
            df = e.find_xray_coinc(XXXcdataXX, 8.5, 1173.2, 0.3)
        with self.assertRaises(NameError):
            df = e.find_xray_coinc(XXXcdataXX, 8.5, 1173.5)

    def test_find_xray_coinc_raises_KeyError_if_list_with_wrong_keys_gets_passed(self):
        with self.assertRaises(KeyError):
            df = e.find_xray_coinc(edata, 8.5, 1173.2, 0.3)
        with self.assertRaises(KeyError):
            df = e.find_xray_coinc(edata, 8.5, 1173.2)

    def test_find_xray_coinc_raises_KeyError_if_bad_dict_items_in_list(self):
        bad_dict_items_in_list = [{'a':0, 'b':1, 'c':2}]
        with self.assertRaises(KeyError):
            df = e.find_xray_coinc(bad_dict_items_in_list, 8.5, 1173.2, 0.3)
        with self.assertRaises(KeyError):
            df = e.find_xray_coinc(bad_dict_items_in_list, 8.5, 1173.2)

    def test_find_xray_coinc_returned_contents_of_DataFrame(self):
        df = e.find_xray_coinc(cdata, 12.5, 944.6)
        self.assertIsInstance(df, pd.core.frame.DataFrame)
        self.assertIsInstance(df['Parent'], pd.core.series.Series)
        self.assertIsInstance(df['Decay Index'], pd.core.series.Series)
        self.assertIsInstance(df['Ex. Energy'], pd.core.series.Series)
        self.assertIsInstance(df['Daughter'], pd.core.series.Series)
        self.assertIsInstance(df['Decay Mode'], pd.core.series.Series)
        self.assertIsInstance(df['X-ray Label'], pd.core.series.Series)
        self.assertIsInstance(df['Photon 1'], pd.core.series.Series)
        self.assertIsInstance(df['Photon 2'], pd.core.series.Series)

        # Explore types after conversion of DataFrame to dictionary
        #df_dict = df.to_dict()

        for index, row in df.iterrows():
            self.assertIsInstance(row['Parent'], str)
            self.assertIsInstance(row['Decay Index'], int)
            self.assertIsInstance(row['Ex. Energy'], str)
            self.assertIsInstance(row['Daughter'], str)
            self.assertIsInstance(row['Decay Mode'], str)
            self.assertIsInstance(row['X-ray Label'], str)
            self.assertIsInstance(row['Photon 1'], str)
            self.assertIsInstance(row['Photon 2'], str)


class GetBindingEnergies(unittest.TestCase):

    __doc__="""Unit tests for the `get_binding_energies ` method of the GammaX 
    class."""

    ecbp_pairs = e.ensdf_pairs(edata,"ECBP")
    bm_pairs = e.ensdf_pairs(edata,"BM")
    a_pairs = e.ensdf_pairs(edata,"A")

    pattern = re.compile('[A-Za-z]+')
    elements = []
    for k,v in ecbp_pairs.items():
        isotope = str(k[0])
        chem_symbol = pattern.findall(isotope)[0]
        elements.append(chem_symbol)

    for k,v in bm_pairs.items():
        isotope = str(k[0])
        chem_symbol = pattern.findall(isotope)[0]
        elements.append(chem_symbol)

    for k,v in a_pairs.items():
        isotope = str(k[0])
        chem_symbol = pattern.findall(isotope)[0]
        elements.append(chem_symbol)

    elements = sorted(list(set(elements)))

    def test_get_binding_energies_returns_DataFrame(self):
        for chemical in GetBindingEnergies.elements:
            try:
                df = e.get_binding_energies(cdata, chemical, shell='K')
                self.assertIsInstance(df, pd.core.frame.DataFrame)
                df = e.get_binding_energies(cdata, chemical, shell='L')
                self.assertIsInstance(df, pd.core.frame.DataFrame)
                df = e.get_binding_energies(cdata, chemical, shell='M')
                self.assertIsInstance(df, pd.core.frame.DataFrame)
                df = e.get_binding_energies(cdata, chemical, shell='all')
                self.assertIsInstance(df, pd.core.frame.DataFrame)
            except AssertionError:
                self.assertIsNone(df)

    def test_get_binding_energies_returns_none_if_doesnt_exist(self):
        df = e.get_binding_energies(cdata, "H", shell="all")
        self.assertIsNone(df)
        df = e.get_binding_energies(cdata, "He", shell="all")
        self.assertIsNone(df)
        df = e.get_binding_energies(cdata, 101, shell="all")
        self.assertIsNone(df)
        df = e.get_binding_energies(cdata, 103, shell="all")
        self.assertIsNone(df)
        df = e.get_binding_energies(cdata, 106, shell="all")
        self.assertIsNone(df)
        df = e.get_binding_energies(cdata, 110, shell="all")
        self.assertIsNone(df)

    def test_get_binding_energies_returns_none_if_missing_kwargs(self):
        df = e.get_binding_energies(cdata, "W")
        self.assertIsNone(df)

    def test_get_binding_energies_returns_none_if_illegal_kwargs(self):
        df = e.get_binding_energies(cdata, "W", shell="THisIsB@LL@CK$")
        self.assertIsNone(df)

    def test_get_binding_energies_raises_IndexError_if_missing_args_and_kwargs(self):
        with self.assertRaises(IndexError):
            df = e.get_binding_energies(cdata)

    def test_get_binding_energies_raises_TypeError_if_missing_function_arguments(self):
        with self.assertRaises(TypeError):
            df = e.get_binding_energies()

    def test_get_binding_energies_raises_NameError_if_wrong_name_list_gets_passed(self):
        with self.assertRaises(NameError):
            df = e.get_binding_energies(XXXcdataXX, "W", shell="K")
        with self.assertRaises(NameError):
            df = e.get_binding_energies(XXXcdataXX, "W", shell="L")
        with self.assertRaises(NameError):
            df = e.get_binding_energies(XXXcdataXX, "W", shell="M")
        with self.assertRaises(NameError):
            df = e.get_binding_energies(XXXcdataXX, "W", shell="all")

    def test_get_binding_energies_raises_KeyError_if_list_with_wrong_keys_gets_passed(self):
        with self.assertRaises(KeyError):
            df = e.get_binding_energies(edata, "W", shell="K")
        with self.assertRaises(KeyError):
            df = e.get_binding_energies(edata, "W", shell="L")
        with self.assertRaises(KeyError):
            df = e.get_binding_energies(edata, "W", shell="M")
        with self.assertRaises(KeyError):
            df = e.get_binding_energies(edata, "W", shell="all")

    def test_get_binding_energies_raises_KeyError_if_bad_dict_items_in_list(self):
        bad_dict_items_in_list = [{'a':0, 'b':1, 'c':2}]
        with self.assertRaises(KeyError):
            df = e.get_binding_energies(bad_dict_items_in_list, shell="K")
        with self.assertRaises(KeyError):
            df = e.get_binding_energies(bad_dict_items_in_list, shell="L")
        with self.assertRaises(KeyError):
            df = e.get_binding_energies(bad_dict_items_in_list, shell="M")
        with self.assertRaises(KeyError):
            df = e.get_binding_energies(bad_dict_items_in_list, shell="all")

    def test_find_gamma_coinc_returned_contents_of_DataFrame(self):
        for chemical in GetBindingEnergies.elements:
            df = e.get_binding_energies(cdata, chemical, shell='K')
            try:
                self.assertIsInstance(df, pd.core.frame.DataFrame)
                self.assertIsInstance(df['ID'], pd.core.series.Series)
                self.assertIsInstance(df['Z'], pd.core.series.Series)
                self.assertIsInstance(df['K'], pd.core.series.Series)

                for index, row in df.iterrows():
                    self.assertIsInstance(row['ID'], str)
                    self.assertIsInstance(row['Z'], int)
                    self.assertIsInstance(row['K'], float)

            except AssertionError:
                self.assertIsNone(df)

        for chemical in GetBindingEnergies.elements:
            df = e.get_binding_energies(cdata, chemical, shell='L')
            try:
                self.assertIsInstance(df, pd.core.frame.DataFrame)
                self.assertIsInstance(df['ID'], pd.core.series.Series)
                self.assertIsInstance(df['Z'], pd.core.series.Series)
                self.assertIsInstance(df['L1'], pd.core.series.Series)
                self.assertIsInstance(df['L2'], pd.core.series.Series)
                self.assertIsInstance(df['L3'], pd.core.series.Series)

                for index, row in df.iterrows():
                    self.assertIsInstance(row['ID'], str)
                    self.assertIsInstance(row['Z'], int)
                    self.assertIsInstance(row['L1'], float)
                    self.assertIsInstance(row['L2'], float)
                    self.assertIsInstance(row['L3'], float)

            except AssertionError:
                self.assertIsNone(df)

        for chemical in GetBindingEnergies.elements:
            df = e.get_binding_energies(cdata, chemical, shell='M')
            try:
                self.assertIsInstance(df, pd.core.frame.DataFrame)
                self.assertIsInstance(df['ID'], pd.core.series.Series)
                self.assertIsInstance(df['Z'], pd.core.series.Series)
                self.assertIsInstance(df['M1'], pd.core.series.Series)
                self.assertIsInstance(df['M2'], pd.core.series.Series)
                self.assertIsInstance(df['M3'], pd.core.series.Series)
                self.assertIsInstance(df['M4'], pd.core.series.Series)
                self.assertIsInstance(df['M5'], pd.core.series.Series)

                for index, row in df.iterrows():
                    self.assertIsInstance(row['ID'], str)
                    self.assertIsInstance(row['Z'], int)
                    self.assertIsInstance(row['M1'], float)
                    self.assertIsInstance(row['M2'], float)
                    self.assertIsInstance(row['M3'], float)
                    self.assertIsInstance(row['M4'], float)
                    self.assertIsInstance(row['M5'], float)

            except AssertionError:
                self.assertIsNone(df)

        for chemical in GetBindingEnergies.elements:
            df = e.get_binding_energies(cdata, chemical, shell='all')
            try:
                self.assertIsInstance(df, pd.core.frame.DataFrame)
                self.assertIsInstance(df['ID'], pd.core.series.Series)
                self.assertIsInstance(df['Z'], pd.core.series.Series)
                self.assertIsInstance(df['K'], pd.core.series.Series)
                self.assertIsInstance(df['L1'], pd.core.series.Series)
                self.assertIsInstance(df['L2'], pd.core.series.Series)
                self.assertIsInstance(df['L3'], pd.core.series.Series)
                self.assertIsInstance(df['M1'], pd.core.series.Series)
                self.assertIsInstance(df['M2'], pd.core.series.Series)
                self.assertIsInstance(df['M3'], pd.core.series.Series)
                self.assertIsInstance(df['M4'], pd.core.series.Series)
                self.assertIsInstance(df['M5'], pd.core.series.Series)

                for index, row in df.iterrows():
                    self.assertIsInstance(row['ID'], str)
                    self.assertIsInstance(row['Z'], int)
                    self.assertIsInstance(row['K'], float)
                    self.assertIsInstance(row['L1'], float)
                    self.assertIsInstance(row['L2'], float)
                    self.assertIsInstance(row['L3'], float)
                    self.assertIsInstance(row['M1'], float)
                    self.assertIsInstance(row['M2'], float)
                    self.assertIsInstance(row['M3'], float)
                    self.assertIsInstance(row['M4'], float)
                    self.assertIsInstance(row['M5'], float)

            except AssertionError:
                self.assertIsNone(df)


class GetValenceConfig(unittest.TestCase):

    __doc__="""Unit tests for the `get_valence_config` method of the GammaX 
    class."""

    ecbp_pairs = e.ensdf_pairs(edata,"ECBP")
    bm_pairs = e.ensdf_pairs(edata,"BM")
    a_pairs = e.ensdf_pairs(edata,"A")

    pattern = re.compile('[A-Za-z]+')
    elements = []
    for k,v in ecbp_pairs.items():
        isotope = str(k[0])
        chem_symbol = pattern.findall(isotope)[0]
        elements.append(chem_symbol)

    for k,v in bm_pairs.items():
        isotope = str(k[0])
        chem_symbol = pattern.findall(isotope)[0]
        elements.append(chem_symbol)

    for k,v in a_pairs.items():
        isotope = str(k[0])
        chem_symbol = pattern.findall(isotope)[0]
        elements.append(chem_symbol)

    elements = sorted(list(set(elements)))

    def test_get_valence_config_returns_list_for_all_parent_nuclides(self):
        for chemical in GetBindingEnergies.elements:
            try:
                conf = e.get_valence_config(cdata, chemical)
                self.assertIsInstance(conf, list)
                self.assertIsInstance(conf, Iterable)
            except AssertionError:
                self.assertIsNone(conf)

    def test_get_valence_config_returns_none_if_no_data(self):
        conf = e.get_valence_config(cdata, 1)
        self.assertIsNone(conf)
        conf = e.get_valence_config(cdata, 2)
        self.assertIsNone(conf)
        conf = e.get_valence_config(cdata, 101)
        self.assertIsNone(conf)
        conf = e.get_valence_config(cdata, 103)
        self.assertIsNone(conf)
        conf = e.get_valence_config(cdata, 106)
        self.assertIsNone(conf)
        conf = e.get_valence_config(cdata, 110)
        self.assertIsNone(conf)

    def test_get_valence_config_returns_none_if_illegal_string_is_passed(self):
        conf = e.get_valence_config(cdata, "THisIsB@LL@CK$")
        self.assertIsNone(conf)

    def test_get_valence_config_raises_IndexError_if_no_args_passed(self):
        with self.assertRaises(IndexError):
            conf = e.get_valence_config(cdata)

    def test_get_valence_config_raises_TypeError_if_no_arguments_passed_to_function(self):
        with self.assertRaises(TypeError):
            conf = e.get_valence_config()

    def test_get_valence_config_raises_TypeError_if_first_argument_not_list(self):
        with self.assertRaises(TypeError):
            conf = e.get_valence_config("W")

    def test_get_valence_config_raises_TypeError_if_wrong_order_arguments(self):
        with self.assertRaises(TypeError):
            conf = e.get_valence_config("W", cdata)

    def test_get_valence_config_raises_NameError_if_wrong_name_list(self):
        with self.assertRaises(NameError):
            conf = e.get_valence_config(XXXcdataXX, "W")

    def test_get_valence_config_raises_KeyError_if_list_with_wrong_keys_gets_passed(self):
        with self.assertRaises(KeyError):
            conf = e.get_valence_config(edata, "W")

    def test_get_valence_config_raises_KeyError_if_bad_dict_items_in_list(self):
        bad_dict_items_in_list = [{'a':0, 'b':1, 'c':2}]
        with self.assertRaises(KeyError):
            conf = e.get_valence_config(bad_dict_items_in_list, "W")

    def test_get_valence_config_returned_contents_of_list(self):
        for chemical in GetBindingEnergies.elements:
            try:
                conf = e.get_valence_config(cdata, chemical)
                self.assertIsInstance(conf, list)
                self.assertIsInstance(conf, Iterable)

                for i,c in enumerate(conf):
                    self.assertIsInstance(c, list)
                    self.assertIsInstance(c, Iterable)
                    self.assertEqual(len(c), 3)
                    self.assertIsInstance(c[0], str)
                    self.assertIsInstance(c[1], str)
                    self.assertIsInstance(c[2], int)

            except AssertionError:
                self.assertIsNone(conf)

    
