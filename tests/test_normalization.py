import pytest
import unittest
import numpy as np
import pandas as pd
from collections.abc import Iterable

import paceENSDF as pe
e = pe.ENSDF()
edata = e.load_ensdf()

class NormRecordTests(unittest.TestCase):

    __doc__="""Unit tests for `norm_record` method of the Normalization 
    class."""

    def test_norm_record_returns_dict_for_all_decays(self):
        ecbp_pairs = e.ensdf_pairs(edata,"ECBP")
        for parent, daughter in ecbp_pairs.items():
            ecbp = e.norm_record(edata, parent[0], parent[3], mode="ECBP")
            self.assertIsInstance(ecbp, dict)
            self.assertIsInstance(ecbp, Iterable)

        bm_pairs = e.ensdf_pairs(edata,"BM")
        for parent, daughter in bm_pairs.items():
            bm = e.norm_record(edata, parent[0], parent[3], mode="BM")
            self.assertIsInstance(bm, dict)
            self.assertIsInstance(bm, Iterable)

        a_pairs = e.ensdf_pairs(edata,"A")
        for parent, daughter in a_pairs.items():
            a = e.norm_record(edata, parent[0], parent[3], mode="A")
            self.assertIsInstance(a, dict)
            self.assertIsInstance(a, Iterable)

    def test_norm_record_returns_none_if_no_decay_norm_record(self):
        ecbp = e.norm_record(edata,"Xe200",0,mode="ECBP")
        self.assertIsNone(ecbp)
        bm = e.norm_record(edata,"Xe200",1,mode="BM")
        self.assertIsNone(bm)
        a = e.norm_record(edata,"Xe200",2,mode="A")
        self.assertIsNone(a)

    def test_norm_record_returns_none_if_illegal_string(self):
        ecbp = e.norm_record(edata,"Y86",0,mode="THisIsB@LL@CK$")
        self.assertIsNone(ecbp)
        ecbp = e.norm_record(edata,"THisIsB@LL@CK$",0,mode="ECBP")
        self.assertIsNone(ecbp)

    def test_norm_record_raises_TypeError_if_first_arg_not_list(self):
        with self.assertRaises(TypeError):
            ecbp = e.norm_record("Y86",edata,0,mode="ECBP")
        with self.assertRaises(TypeError):
            bm = e.norm_record("Co60",edata,0,mode="BM")
        with self.assertRaises(TypeError):
            a = e.norm_record("Ra226",edata,0,mode="A")
            
    def test_norm_record_raises_NameError_if_wrong_list(self):
        with self.assertRaises(NameError):
            ecbp = e.norm_record(XXXedataXXX,"Y86",0,mode="ECBP")
        with self.assertRaises(NameError):
            bm = e.norm_record(XXXedataXXX,"Co60",0,mode="BM")
        with self.assertRaises(NameError):
            a = e.norm_record(XXXedataXXX,"Ra226",0,mode="A")

    def test_norm_record_raises_KeyError_if_bad_dict_items_in_list(self):
        bad_dict_items_in_list = [{'a':0, 'b':1, 'c':2}]
        with self.assertRaises(KeyError):
           ecbp = e.norm_record(bad_dict_items_in_list,"Y86",0,mode="ECBP")
        with self.assertRaises(KeyError):
           bm = e.norm_record(bad_dict_items_in_list,"Co60",0,mode="BM")
        with self.assertRaises(KeyError):
           a = e.norm_record(bad_dict_items_in_list,"Ra226",0,mode="A")

    def test_norm_record_returned_contents_of_dict(self):
        ecbp_pairs = e.ensdf_pairs(edata,"ECBP")
        self.assertEqual(len(ecbp_pairs), 1279)
        for parent_key, daughter_value in ecbp_pairs.items():
            ecbp_norm = e.norm_record(edata, str(parent_key[0]), int(parent_key[3]), mode="ECBP")
            for norm_key, norm_value in ecbp_norm.items():
                self.assertIsInstance(norm_key, tuple)
                self.assertIsInstance(norm_key, Iterable)
                self.assertEqual(len(norm_key), 8)

                # Unpack the tuple key contents
                self.assertIsInstance(norm_key[0], str)
                self.assertIsInstance(norm_key[1], int)
                self.assertIsInstance(norm_key[2], int)
                self.assertIsInstance(norm_key[3], int)
                try:
                    self.assertIsInstance(norm_key[4], float)
                except AssertionError:
                    self.assertIsInstance(norm_key[4], str)
                self.assertIsInstance(norm_key[5], str)
                self.assertIsInstance(norm_key[6], int)
                self.assertIsInstance(norm_key[7], int)

                # Unpack the list value contents
                self.assertIsInstance(norm_value, list)
                self.assertIsInstance(norm_value, Iterable)
                self.assertEqual(len(norm_value), 5)

                for i,tuple_value in enumerate(norm_value):
                    self.assertEqual(len(tuple_value), 3)
                    try:
                        self.assertIsInstance(tuple_value[0], float)
                    except AssertionError:
                        self.assertIsNone(tuple_value[0])
                    try:
                        self.assertIsInstance(tuple_value[1], float)
                    except AssertionError:
                        self.assertIsNone(tuple_value[1])
                    self.assertIsInstance(tuple_value[2], bool)

        bm_pairs = e.ensdf_pairs(edata,"BM")
        self.assertEqual(len(bm_pairs), 1141)
        for parent_key, daughter_value in bm_pairs.items():
            bm_norm = e.norm_record(edata, str(parent_key[0]), int(parent_key[3]), mode="BM")
            for norm_key, norm_value in bm_norm.items():
                self.assertIsInstance(norm_key, tuple)
                self.assertIsInstance(norm_key, Iterable)
                self.assertEqual(len(norm_key), 8)

                # Unpack the tuple key contents
                self.assertIsInstance(norm_key[0], str)
                self.assertIsInstance(norm_key[1], int)
                self.assertIsInstance(norm_key[2], int)
                self.assertIsInstance(norm_key[3], int)
                try:
                    self.assertIsInstance(norm_key[4], float)
                except AssertionError:
                    self.assertIsInstance(norm_key[4], str)
                self.assertIsInstance(norm_key[5], str)
                self.assertIsInstance(norm_key[6], int)
                self.assertIsInstance(norm_key[7], int)

                # Unpack the list value contents
                self.assertIsInstance(norm_value, list)
                self.assertIsInstance(norm_value, Iterable)
                self.assertEqual(len(norm_value), 5)

                for i,tuple_value in enumerate(norm_value):
                    self.assertEqual(len(tuple_value), 3)
                    try:
                        self.assertIsInstance(tuple_value[0], float)
                    except AssertionError:
                        self.assertIsNone(tuple_value[0])
                    try:
                        self.assertIsInstance(tuple_value[1], float)
                    except AssertionError:
                        self.assertIsNone(tuple_value[1])
                    self.assertIsInstance(tuple_value[2], bool)


        a_pairs = e.ensdf_pairs(edata,"A")
        self.assertEqual(len(a_pairs), 834)
        for parent_key, daughter_value in a_pairs.items():
            a_norm = e.norm_record(edata, str(parent_key[0]), int(parent_key[3]), mode="A")
            for norm_key, norm_value in a_norm.items():
                self.assertIsInstance(norm_key, tuple)
                self.assertIsInstance(norm_key, Iterable)
                self.assertEqual(len(norm_key), 8)

                # Unpack the tuple key contents
                self.assertIsInstance(norm_key[0], str)
                self.assertIsInstance(norm_key[1], int)
                self.assertIsInstance(norm_key[2], int)
                self.assertIsInstance(norm_key[3], int)
                try:
                    self.assertIsInstance(norm_key[4], float)
                except AssertionError:
                    self.assertIsInstance(norm_key[4], str)
                self.assertIsInstance(norm_key[5], str)
                self.assertIsInstance(norm_key[6], int)
                self.assertIsInstance(norm_key[7], int)

                # Unpack the list value contents
                self.assertIsInstance(norm_value, list)
                self.assertIsInstance(norm_value, Iterable)
                self.assertEqual(len(norm_value), 5)

                for i,tuple_value in enumerate(norm_value):
                    self.assertEqual(len(tuple_value), 3)
                    try:
                        self.assertIsInstance(tuple_value[0], float)
                    except AssertionError:
                        self.assertIsNone(tuple_value[0])
                    try:
                        self.assertIsInstance(tuple_value[1], float)
                    except AssertionError:
                        self.assertIsNone(tuple_value[1])
                    self.assertIsInstance(tuple_value[2], bool)


class ProdNormRecordTests(unittest.TestCase):

    __doc__="""Unit tests for `prod_norm_record` method of the Normalization 
    class."""

    def test_prod_norm_record_returns_dict_for_all_decays(self):
        ecbp_pairs = e.ensdf_pairs(edata,"ECBP")
        for parent, daughter in ecbp_pairs.items():
            ecbp = e.prod_norm_record(edata, parent[0], parent[3], mode="ECBP")
            self.assertIsInstance(ecbp, dict)
            self.assertIsInstance(ecbp, Iterable)

        bm_pairs = e.ensdf_pairs(edata,"BM")
        for parent, daughter in bm_pairs.items():
            bm = e.prod_norm_record(edata, parent[0], parent[3], mode="BM")
            self.assertIsInstance(bm, dict)
            self.assertIsInstance(bm, Iterable)

        a_pairs = e.ensdf_pairs(edata,"A")
        for parent, daughter in a_pairs.items():
            a = e.prod_norm_record(edata, parent[0], parent[3], mode="A")
            self.assertIsInstance(a, dict)
            self.assertIsInstance(a, Iterable)

    def test_prod_norm_record_returns_none_if_no_decay_prod_norm_record(self):
        ecbp = e.prod_norm_record(edata,"Xe200",0,mode="ECBP")
        self.assertIsNone(ecbp)
        bm = e.prod_norm_record(edata,"Xe200",1,mode="BM")
        self.assertIsNone(bm)
        a = e.prod_norm_record(edata,"Xe200",2,mode="A")
        self.assertIsNone(a)

    def test_prod_norm_record_returns_none_if_illegal_string(self):
        ecbp = e.prod_norm_record(edata,"Y86",0,mode="THisIsB@LL@CK$")
        self.assertIsNone(ecbp)
        ecbp = e.prod_norm_record(edata,"THisIsB@LL@CK$",0,mode="ECBP")
        self.assertIsNone(ecbp)

    def test_prod_norm_record_raises_TypeError_if_first_arg_not_list(self):
        with self.assertRaises(TypeError):
            ecbp = e.prod_norm_record("Y86",edata,0,mode="ECBP")
        with self.assertRaises(TypeError):
            bm = e.prod_norm_record("Co60",edata,0,mode="BM")
        with self.assertRaises(TypeError):
            a = e.prod_norm_record("Ra226",edata,0,mode="A")
            
    def test_prod_norm_record_raises_NameError_if_wrong_list(self):
        with self.assertRaises(NameError):
            ecbp = e.prod_norm_record(XXXedataXXX,"Y86",0,mode="ECBP")
        with self.assertRaises(NameError):
            bm = e.prod_norm_record(XXXedataXXX,"Co60",0,mode="BM")
        with self.assertRaises(NameError):
            a = e.prod_norm_record(XXXedataXXX,"Ra226",0,mode="A")

    def test_prod_norm_record_raises_KeyError_if_bad_dict_items_in_list(self):
        bad_dict_items_in_list = [{'a':0, 'b':1, 'c':2}]
        with self.assertRaises(KeyError):
           ecbp = e.prod_norm_record(bad_dict_items_in_list,"Y86",0,mode="ECBP")
        with self.assertRaises(KeyError):
           bm = e.prod_norm_record(bad_dict_items_in_list,"Co60",0,mode="BM")
        with self.assertRaises(KeyError):
           a = e.prod_norm_record(bad_dict_items_in_list,"Ra226",0,mode="A")

    def test_prod_norm_record_returned_contents_of_dict(self):
        ecbp_pairs = e.ensdf_pairs(edata,"ECBP")
        self.assertEqual(len(ecbp_pairs), 1279)
        for parent_key, daughter_value in ecbp_pairs.items():
            ecbp_pnorm = e.prod_norm_record(edata, str(parent_key[0]), int(parent_key[3]), mode="ECBP")
            for pnorm_key, pnorm_value in ecbp_pnorm.items():
                self.assertIsInstance(pnorm_key, tuple)
                self.assertIsInstance(pnorm_key, Iterable)
                self.assertEqual(len(pnorm_key), 8)

                # Unpack the tuple key contents
                self.assertIsInstance(pnorm_key[0], str)
                self.assertIsInstance(pnorm_key[1], int)
                self.assertIsInstance(pnorm_key[2], int)
                self.assertIsInstance(pnorm_key[3], int)
                try:
                    self.assertIsInstance(pnorm_key[4], float)
                except AssertionError:
                    self.assertIsInstance(pnorm_key[4], str)
                self.assertIsInstance(pnorm_key[5], str)
                self.assertIsInstance(pnorm_key[6], int)
                self.assertIsInstance(pnorm_key[7], int)

                # Unpack the list value contents
                self.assertIsInstance(pnorm_value, list)
                self.assertIsInstance(pnorm_value, Iterable)
                self.assertEqual(len(pnorm_value), 4)

                for i,tuple_value in enumerate(pnorm_value):
                    self.assertEqual(len(tuple_value), 3)
                    try:
                        self.assertIsInstance(tuple_value[0], float)
                    except AssertionError:
                        self.assertIsNone(tuple_value[0])
                    try:
                        self.assertIsInstance(tuple_value[1], float)
                    except AssertionError:
                        self.assertIsNone(tuple_value[1])
                    self.assertIsInstance(tuple_value[2], bool)

        bm_pairs = e.ensdf_pairs(edata,"BM")
        self.assertEqual(len(bm_pairs), 1141)
        for parent_key, daughter_value in bm_pairs.items():
            bm_pnorm = e.prod_norm_record(edata, str(parent_key[0]), int(parent_key[3]), mode="BM")
            for pnorm_key, pnorm_value in bm_pnorm.items():
                self.assertIsInstance(pnorm_key, tuple)
                self.assertIsInstance(pnorm_key, Iterable)
                self.assertEqual(len(pnorm_key), 8)

                # Unpack the tuple key contents
                self.assertIsInstance(pnorm_key[0], str)
                self.assertIsInstance(pnorm_key[1], int)
                self.assertIsInstance(pnorm_key[2], int)
                self.assertIsInstance(pnorm_key[3], int)
                try:
                    self.assertIsInstance(pnorm_key[4], float)
                except AssertionError:
                    self.assertIsInstance(pnorm_key[4], str)
                self.assertIsInstance(pnorm_key[5], str)
                self.assertIsInstance(pnorm_key[6], int)
                self.assertIsInstance(pnorm_key[7], int)

                # Unpack the list value contents
                self.assertIsInstance(pnorm_value, list)
                self.assertIsInstance(pnorm_value, Iterable)
                self.assertEqual(len(pnorm_value), 4)

                for i,tuple_value in enumerate(pnorm_value):
                    self.assertEqual(len(tuple_value), 3)
                    try:
                        self.assertIsInstance(tuple_value[0], float)
                    except AssertionError:
                        self.assertIsNone(tuple_value[0])
                    try:
                        self.assertIsInstance(tuple_value[1], float)
                    except AssertionError:
                        self.assertIsNone(tuple_value[1])
                    self.assertIsInstance(tuple_value[2], bool)


        a_pairs = e.ensdf_pairs(edata,"A")
        self.assertEqual(len(a_pairs), 834)
        for parent_key, daughter_value in a_pairs.items():
            a_pnorm = e.prod_norm_record(edata, str(parent_key[0]), int(parent_key[3]), mode="A")
            for pnorm_key, pnorm_value in a_pnorm.items():
                self.assertIsInstance(pnorm_key, tuple)
                self.assertIsInstance(pnorm_key, Iterable)
                self.assertEqual(len(pnorm_key), 8)

                # Unpack the tuple key contents
                self.assertIsInstance(pnorm_key[0], str)
                self.assertIsInstance(pnorm_key[1], int)
                self.assertIsInstance(pnorm_key[2], int)
                self.assertIsInstance(pnorm_key[3], int)
                try:
                    self.assertIsInstance(pnorm_key[4], float)
                except AssertionError:
                    self.assertIsInstance(pnorm_key[4], str)
                self.assertIsInstance(pnorm_key[5], str)
                self.assertIsInstance(pnorm_key[6], int)
                self.assertIsInstance(pnorm_key[7], int)

                # Unpack the list value contents
                self.assertIsInstance(pnorm_value, list)
                self.assertIsInstance(pnorm_value, Iterable)
                self.assertEqual(len(pnorm_value), 4)

                for i,tuple_value in enumerate(pnorm_value):
                    self.assertEqual(len(tuple_value), 3)
                    try:
                        self.assertIsInstance(tuple_value[0], float)
                    except AssertionError:
                        self.assertIsNone(tuple_value[0])
                    try:
                        self.assertIsInstance(tuple_value[1], float)
                    except AssertionError:
                        self.assertIsNone(tuple_value[1])
                    self.assertIsInstance(tuple_value[2], bool)
                    
