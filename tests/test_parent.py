import pytest
import unittest
import numpy as np
import pandas as pd
from collections.abc import Iterable

import paceENSDF as pe
e = pe.ENSDF()
edata = e.load_ensdf()

class FindParentsMultipleJPi(unittest.TestCase):

    __doc__="""Unit tests for the `find_parents_multiple_jpi` method of the 
    Parent class."""

    def test_find_parents_multiple_jpi_returns_dict_for_all_decays(self):
        ecbp = e.find_parents_multiple_jpi(edata, mode="ECBP")
        self.assertIsInstance(ecbp, dict)
        self.assertIsInstance(ecbp, Iterable)

        bm = e.find_parents_multiple_jpi(edata, mode="BM")
        self.assertIsInstance(bm, dict)
        self.assertIsInstance(bm, Iterable)

        a = e.find_parents_multiple_jpi(edata, mode="A")
        self.assertIsInstance(a, dict)
        self.assertIsInstance(a, Iterable)

    def test_find_parents_multiple_jpi_returns_none_if_illegal_string(self):
        mjpi = e.find_parents_multiple_jpi(edata,mode="THisIsB@LL@CK$")
        self.assertIsNone(mjpi)

    def test_find_parents_multiple_jpi_raises_TypeError_if_first_arg_not_list(self):
        with self.assertRaises(TypeError):
            ecbp = e.find_parents_multiple_jpi("ECBP",edata)
        with self.assertRaises(TypeError):
            bm = e.find_parents_multiple_jpi("BM",edata)
        with self.assertRaises(TypeError):
            a = e.find_parents_multiple_jpi("A",edata)

    def test_find_parents_multiple_jpi_raises_NameError_if_wrong_list(self):
        with self.assertRaises(NameError):
            ecbp = e.find_parents_multiple_jpi(XXXedataXXX,mode="ECBP")
        with self.assertRaises(NameError):
            bm = e.find_parents_multiple_jpi(XXXedataXXX,mode="BM")
        with self.assertRaises(NameError):
            a = e.find_parents_multiple_jpi(XXXedataXXX,mode="A")

    def test_find_parents_multiple_jpi_raises_KeyError_if_bad_dict_items_in_list(self):
        bad_dict_items_in_list = [{'a':0, 'b':1, 'c':2}]
        with self.assertRaises(KeyError):
           ecbp = e.find_parents_multiple_jpi(bad_dict_items_in_list,mode="ECBP")
        with self.assertRaises(KeyError):
           bm = e.find_parents_multiple_jpi(bad_dict_items_in_list,mode="BM")
        with self.assertRaises(KeyError):
           a = e.find_parents_multiple_jpi(bad_dict_items_in_list,mode="A")

    def test_find_parents_multiple_jpi_returned_contents_of_dict(self):
        ecbp_mjpi = e.find_parents_multiple_jpi(edata, mode="ECBP")
        for mjpi_key, mjpi_value in ecbp_mjpi.items():
            self.assertIsInstance(mjpi_key, tuple)
            self.assertIsInstance(mjpi_key, Iterable)
            self.assertEqual(len(mjpi_key), 4)

            # Unpack the tuple key contents
            self.assertIsInstance(mjpi_key[0], str)
            self.assertIsInstance(mjpi_key[1], int)
            try:
                self.assertIsInstance(mjpi_key[2], float)
            except AssertionError:
                self.assertIsInstance(mjpi_key[2], str)
            self.assertIsInstance(mjpi_key[3], int)

            # Unpack the list value contents
            self.assertIsInstance(mjpi_value, list)
            self.assertIsInstance(mjpi_value, Iterable)
            self.assertGreater(len(mjpi_value), 1)
            for v in mjpi_value:
                self.assertIsInstance(v[0], float)
                self.assertIsInstance(v[1], int)

        bm_mjpi = e.find_parents_multiple_jpi(edata, mode="BM")
        for mjpi_key, mjpi_value in bm_mjpi.items():
            self.assertIsInstance(mjpi_key, tuple)
            self.assertIsInstance(mjpi_key, Iterable)
            self.assertEqual(len(mjpi_key), 4)

            # Unpack the tuple key contents
            self.assertIsInstance(mjpi_key[0], str)
            self.assertIsInstance(mjpi_key[1], int)
            try:
                self.assertIsInstance(mjpi_key[2], float)
            except AssertionError:
                self.assertIsInstance(mjpi_key[2], str)
            self.assertIsInstance(mjpi_key[3], int)

            # Unpack the list value contents
            self.assertIsInstance(mjpi_value, list)
            self.assertIsInstance(mjpi_value, Iterable)
            self.assertGreater(len(mjpi_value), 1)
            for v in mjpi_value:
                self.assertIsInstance(v[0], float)
                self.assertIsInstance(v[1], int)

        a_mjpi = e.find_parents_multiple_jpi(edata, mode="A")
        for mjpi_key, mjpi_value in a_mjpi.items():
            self.assertIsInstance(mjpi_key, tuple)
            self.assertIsInstance(mjpi_key, Iterable)
            self.assertEqual(len(mjpi_key), 4)

            # Unpack the tuple key contents
            self.assertIsInstance(mjpi_key[0], str)
            self.assertIsInstance(mjpi_key[1], int)
            try:
                self.assertIsInstance(mjpi_key[2], float)
            except AssertionError:
                self.assertIsInstance(mjpi_key[2], str)
            self.assertIsInstance(mjpi_key[3], int)

            # Unpack the list value contents
            self.assertIsInstance(mjpi_value, list)
            self.assertIsInstance(mjpi_value, Iterable)
            self.assertGreater(len(mjpi_value), 1)
            for v in mjpi_value:
                self.assertIsInstance(v[0], float)
                self.assertIsInstance(v[1], int)


class GetParentJPi(unittest.TestCase):

    __doc__="""Unit tests for the `get_parent_jpi` method of the Parent 
    class."""

    def test_get_parent_jpi_returns_list_for_all_decays(self):
        ecbp_pairs = e.ensdf_pairs(edata,"ECBP")
        for parent, daughter in ecbp_pairs.items():
            ecbp = e.get_parent_jpi(edata, str(parent[0]), int(parent[3]), mode="ECBP")
            self.assertIsInstance(ecbp, list)
            self.assertIsInstance(ecbp, Iterable)

        bm_pairs = e.ensdf_pairs(edata,"BM")
        for parent, daughter in bm_pairs.items():
            bm = e.get_parent_jpi(edata, str(parent[0]), int(parent[3]), mode="BM")
            self.assertIsInstance(bm, list)
            self.assertIsInstance(bm, Iterable)

        a_pairs = e.ensdf_pairs(edata,"A")
        for parent, daughter in a_pairs.items():
            a = e.get_parent_jpi(edata, str(parent[0]), int(parent[3]), mode="A")
            self.assertIsInstance(a, list)
            self.assertIsInstance(a, Iterable)

    def test_get_parent_jpi_returns_none_if_not_correct_decay_mode(self):
        ecbp = e.get_parent_jpi(edata,"Co60",0,mode="ECBP")
        self.assertIsNone(ecbp)
        bm = e.get_parent_jpi(edata,"Y86",0,mode="BM")
        self.assertIsNone(bm)
        a = e.get_parent_jpi(edata,"Na22",0,mode="A")
        self.assertIsNone(a)

    def test_get_parent_jpi_returns_none_if_illegal_string(self):
        jpi = e.get_parent_jpi(edata,"Co60", 1, mode="THisIsB@LL@CK$")
        self.assertIsNone(jpi)
        jpi = e.get_parent_jpi(edata,"THisIsB@LL@CK$", 1, mode="BM")
        self.assertIsNone(jpi)

    def test_get_parent_jpi_raises_TypeError_if_first_arg_not_list(self):
        with self.assertRaises(TypeError):
            ecbp = e.get_parent_jpi("Db258",edata,0,mode="ECBP")
        with self.assertRaises(TypeError):
            bm = e.get_parent_jpi("Co60",edata,1,mode="BM")
        with self.assertRaises(TypeError):
            a = e.get_parent_jpi("Ra226",edata,0,mode="A")

    def test_get_parent_jpi_raises_NameError_if_wrong_list(self):
        with self.assertRaises(NameError):
            ecbp = e.get_parent_jpi(XXXedataXXX,"Db258",0,mode="ECBP")
        with self.assertRaises(NameError):
            bm = e.get_parent_jpi(XXXedataXXX,"Co60",1,mode="BM")
        with self.assertRaises(NameError):
            a = e.get_parent_jpi(XXXedataXXX,"Ra226",0,mode="A")

    def test_get_parent_jpi_raises_KeyError_if_bad_dict_items_in_list(self):
        bad_dict_items_in_list = [{'a':0, 'b':1, 'c':2}]
        with self.assertRaises(KeyError):
           ecbp = e.get_parent_jpi(bad_dict_items_in_list,"Db258",0,mode="ECBP")
        with self.assertRaises(KeyError):
           bm = e.get_parent_jpi(bad_dict_items_in_list,"Co60",1,mode="BM")
        with self.assertRaises(KeyError):
           a = e.get_parent_jpi(bad_dict_items_in_list,"Ra226",0,mode="A")

    def test_get_parent_jpi_returned_contents_of_list(self):
        ecbp_pairs = e.ensdf_pairs(edata,"ECBP")
        for parent, daughter in ecbp_pairs.items():
            ecbp_jpi = e.get_parent_jpi(edata, str(parent[0]), int(parent[3]), mode="ECBP")
            self.assertIsInstance(ecbp_jpi, list)
            self.assertIsInstance(ecbp_jpi, Iterable)
            self.assertGreater(len(ecbp_jpi), 0)
            for jpi_value in ecbp_jpi:
                # Unpack the list  contents
                try:
                    self.assertIsInstance(jpi_value[0], float)
                except AssertionError:
                    if int(jpi_value[1]) == 0:
                        self.assertIsNone(jpi_value[0])
                self.assertIsInstance(jpi_value[1], int)

        bm_pairs = e.ensdf_pairs(edata,"BM")
        for parent, daughter in bm_pairs.items():
            bm_jpi = e.get_parent_jpi(edata, str(parent[0]), int(parent[3]), mode="BM")
            self.assertIsInstance(bm_jpi, list)
            self.assertIsInstance(bm_jpi, Iterable)
            self.assertGreater(len(bm_jpi), 0)
            for jpi_value in bm_jpi:
                # Unpack the list  contents
                try:
                    self.assertIsInstance(jpi_value[0], float)
                except AssertionError:
                    if int(jpi_value[1]) == 0:
                        self.assertIsNone(jpi_value[0])
                self.assertIsInstance(jpi_value[1], int)

        a_pairs = e.ensdf_pairs(edata,"A")
        for parent, daughter in a_pairs.items():
            a_jpi = e.get_parent_jpi(edata, str(parent[0]), int(parent[3]), mode="A")
            self.assertIsInstance(a_jpi, list)
            self.assertIsInstance(a_jpi, Iterable)
            self.assertGreater(len(a_jpi), 0)
            for jpi_value in a_jpi:
                # Unpack the list  contents
                try:
                    self.assertIsInstance(jpi_value[0], float)
                except AssertionError:
                    if int(jpi_value[1]) == 0:
                        self.assertIsNone(jpi_value[0])
                self.assertIsInstance(jpi_value[1], int)
                

class FindAllParentIsomers(unittest.TestCase):

    __doc__="""Unit tests for the `find_all_parent_isomers` method of the 
    Parent class."""

    def test_find_all_parent_isomers_returns_list_for_all_decays(self):
        ecbp = e.find_all_parent_isomers(edata, mode="ECBP")
        self.assertIsInstance(ecbp, list)
        self.assertIsInstance(ecbp, Iterable)

        bm = e.find_all_parent_isomers(edata, mode="BM")
        self.assertIsInstance(bm, list)
        self.assertIsInstance(bm, Iterable)

        a = e.find_all_parent_isomers(edata, mode="A")
        self.assertIsInstance(a, list)
        self.assertIsInstance(a, Iterable)

    def test_find_all_parent_isomers_returns_none_if_not_correct_decay_mode(self):
        p = e.find_all_parent_isomers(edata, mode="2P")
        self.assertIsNone(p)

    def test_find_all_parent_isomers_returns_none_if_illegal_string(self):
        iso = e.find_all_parent_isomers(edata, mode="THisIsB@LL@CK$")
        self.assertIsNone(iso)

    def test_find_all_parent_isomers_raises_TypeError_if_first_arg_not_list(self):
        with self.assertRaises(TypeError):
            ecbp = e.find_all_parent_isomers("ECBP",edata)
        with self.assertRaises(TypeError):
            bm = e.find_all_parent_isomers("Co60",edata)
        with self.assertRaises(TypeError):
            a = e.find_all_parent_isomers("A",edata)

    def test_find_all_parent_isomers_raises_NameError_if_wrong_list(self):
        with self.assertRaises(NameError):
            ecbp = e.find_all_parent_isomers(XXXedataXXX,mode="ECBP")
        with self.assertRaises(NameError):
            bm = e.find_all_parent_isomers(XXXedataXXX,mode="BM")
        with self.assertRaises(NameError):
            a = e.find_all_parent_isomers(XXXedataXXX,mode="A")

    def test_find_all_parent_isomers_raises_KeyError_if_bad_dict_items_in_list(self):
        bad_dict_items_in_list = [{'a':0, 'b':1, 'c':2}]
        with self.assertRaises(KeyError):
           ecbp = e.find_all_parent_isomers(bad_dict_items_in_list,mode="ECBP")
        with self.assertRaises(KeyError):
           bm = e.find_all_parent_isomers(bad_dict_items_in_list,mode="BM")
        with self.assertRaises(KeyError):
           a = e.find_all_parent_isomers(bad_dict_items_in_list,mode="A")

    def test_find_all_parent_isomers_returned_contents_of_list(self):
        ecbp_iso = e.find_all_parent_isomers(edata, mode="ECBP")
        self.assertIsInstance(ecbp_iso, list)
        self.assertIsInstance(ecbp_iso, Iterable)
        self.assertEqual(len(ecbp_iso), 267)
        for iso_value in ecbp_iso:
            # Unpack the list  contents
            self.assertIsInstance(iso_value[0], str)
            self.assertIsInstance(iso_value[1], int)
            try:
                self.assertIsInstance(iso_value[2], float)
            except AssertionError:
                self.assertIsInstance(iso_value[2], str)
            self.assertIsInstance(iso_value[3], int)
            self.assertIsInstance(iso_value[4], int)
            self.assertIsInstance(iso_value[5], str)
            self.assertIsInstance(iso_value[6], int)
            self.assertIsInstance(iso_value[7], int)

        bm_iso = e.find_all_parent_isomers(edata, mode="BM")
        self.assertIsInstance(bm_iso, list)
        self.assertIsInstance(bm_iso, Iterable)
        self.assertEqual(len(bm_iso), 186)
        for iso_value in bm_iso:
            # Unpack the list  contents
            self.assertIsInstance(iso_value[0], str)
            self.assertIsInstance(iso_value[1], int)
            try:
                self.assertIsInstance(iso_value[2], float)
            except AssertionError:
                self.assertIsInstance(iso_value[2], str)
            self.assertIsInstance(iso_value[3], int)
            self.assertIsInstance(iso_value[4], int)
            self.assertIsInstance(iso_value[5], str)
            self.assertIsInstance(iso_value[6], int)
            self.assertIsInstance(iso_value[7], int)
                
        a_iso = e.find_all_parent_isomers(edata, mode="A")
        self.assertIsInstance(a_iso, list)
        self.assertIsInstance(a_iso, Iterable)
        self.assertEqual(len(a_iso), 177)
        for iso_value in a_iso:
            # Unpack the list  contents
            self.assertIsInstance(iso_value[0], str)
            self.assertIsInstance(iso_value[1], int)
            try:
                self.assertIsInstance(iso_value[2], float)
            except AssertionError:
                self.assertIsInstance(iso_value[2], str)
            self.assertIsInstance(iso_value[3], int)
            self.assertIsInstance(iso_value[4], int)
            self.assertIsInstance(iso_value[5], str)
            self.assertIsInstance(iso_value[6], int)
            self.assertIsInstance(iso_value[7], int)


class GetParentDecay(unittest.TestCase):

    __doc__="""Unit tests for the `get_parent_decay` method of the Parent 
    class."""

    def test_get_parent_decay_returns_dict_for_all_decays(self):
        ecbp_pairs = e.ensdf_pairs(edata,"ECBP")
        for parent, daughter in ecbp_pairs.items():
            ecbp = e.get_parent_decay(edata, str(parent[0]), int(parent[3]), mode="ECBP")
            self.assertIsInstance(ecbp, dict)
            self.assertIsInstance(ecbp, Iterable)

        bm_pairs = e.ensdf_pairs(edata,"BM")
        for parent, daughter in bm_pairs.items():
            bm = e.get_parent_decay(edata, str(parent[0]), int(parent[3]), mode="BM")
            self.assertIsInstance(bm, dict)
            self.assertIsInstance(bm, Iterable)

        a_pairs = e.ensdf_pairs(edata,"A")
        for parent, daughter in a_pairs.items():
            a = e.get_parent_decay(edata, str(parent[0]), int(parent[3]), mode="A")
            self.assertIsInstance(a, dict)
            self.assertIsInstance(a, Iterable)

    def test_get_parent_decay_returns_none_if_not_correct_decay_mode(self):
        ecbp = e.get_parent_decay(edata,"Co60",0,mode="ECBP")
        self.assertIsNone(ecbp)
        bm = e.get_parent_decay(edata,"Y86",0,mode="BM")
        self.assertIsNone(bm)
        a = e.get_parent_decay(edata,"Na22",0,mode="A")
        self.assertIsNone(a)

    def test_get_parent_decay_returns_none_if_illegal_string(self):
        decay = e.get_parent_decay(edata,"Co60", 1, mode="THisIsB@LL@CK$")
        self.assertIsNone(decay)
        decay = e.get_parent_decay(edata,"THisIsB@LL@CK$", 1, mode="BM")
        self.assertIsNone(decay)

    def test_get_parent_decay_raises_TypeError_if_first_arg_not_list(self):
        with self.assertRaises(TypeError):
            ecbp = e.get_parent_decay("Db258",edata,0,mode="ECBP")
        with self.assertRaises(TypeError):
            bm = e.get_parent_decay("Co60",edata,1,mode="BM")
        with self.assertRaises(TypeError):
            a = e.get_parent_decay("Ra226",edata,0,mode="A")

    def test_get_parent_decay_raises_NameError_if_wrong_list(self):
        with self.assertRaises(NameError):
            ecbp = e.get_parent_decay(XXXedataXXX,"Db258",0,mode="ECBP")
        with self.assertRaises(NameError):
            bm = e.get_parent_decay(XXXedataXXX,"Co60",1,mode="BM")
        with self.assertRaises(NameError):
            a = e.get_parent_decay(XXXedataXXX,"Ra226",0,mode="A")

    def test_get_parent_decay_raises_KeyError_if_bad_dict_items_in_list(self):
        bad_dict_items_in_list = [{'a':0, 'b':1, 'c':2}]
        with self.assertRaises(KeyError):
           ecbp = e.get_parent_decay(bad_dict_items_in_list,"Db258",0,mode="ECBP")
        with self.assertRaises(KeyError):
           bm = e.get_parent_decay(bad_dict_items_in_list,"Co60",1,mode="BM")
        with self.assertRaises(KeyError):
           a = e.get_parent_decay(bad_dict_items_in_list,"Ra226",0,mode="A")

    def test_get_parent_decay_returned_contents_of_dict(self):
        ecbp_pairs = e.ensdf_pairs(edata,"ECBP")
        for parent, daughter in ecbp_pairs.items():
            ecbp_decay = e.get_parent_decay(edata, str(parent[0]), int(parent[3]), mode="ECBP")
            self.assertIsInstance(ecbp_decay, dict)
            self.assertIsInstance(ecbp_decay, Iterable)
            self.assertEqual(len(ecbp_decay), 1)
            for decay_key, decay_value in ecbp_decay.items():
                self.assertIsInstance(decay_key, tuple)
                self.assertIsInstance(decay_key, Iterable)
                self.assertEqual(len(decay_key), 7)

                # Unpack the tuple key contents
                self.assertIsInstance(decay_key[0], str)
                self.assertIsInstance(decay_key[1], int)
                self.assertIsInstance(decay_key[2], int)
                self.assertIsInstance(decay_key[3], int)
                self.assertIsInstance(decay_key[4], str)
                self.assertIsInstance(decay_key[5], int)
                self.assertIsInstance(decay_key[6], int)
                
                # Unpack the list value contents
                self.assertIsInstance(decay_value, list)
                self.assertIsInstance(decay_value, Iterable)
                self.assertEqual(len(decay_value), 2)
                for v_tup in decay_value:
                    self.assertIsInstance(v_tup, tuple)
                    self.assertIsInstance(v_tup, Iterable)
                    self.assertEqual(len(v_tup), 2)
                    try:
                        self.assertIsInstance(v_tup[0], float)
                    except AssertionError:
                        # Maybe an <int>
                        try:
                            self.assertIsInstance(v_tup[0], int)
                        except AssertionError:
                            # Or a <str>
                            self.assertIsInstance(v_tup[0], str)

                    try:
                        self.assertIsInstance(v_tup[1], float)
                    except AssertionError:
                        # Maybe an <int>
                        try:
                            self.assertIsInstance(v_tup[1], int)
                        except AssertionError:
                            # Or a <str> for 'AP' error types
                            try:
                                self.assertIsInstance(v_tup[1], str)
                            except AssertionError:
                                # Null error types
                                self.assertIsNone(v_tup[1])

        bm_pairs = e.ensdf_pairs(edata,"BM")
        for parent, daughter in bm_pairs.items():
            bm_decay = e.get_parent_decay(edata, str(parent[0]), int(parent[3]), mode="BM")
            self.assertIsInstance(bm_decay, dict)
            self.assertIsInstance(bm_decay, Iterable)
            self.assertEqual(len(bm_decay), 1)
            for decay_key, decay_value in bm_decay.items():
                self.assertIsInstance(decay_key, tuple)
                self.assertIsInstance(decay_key, Iterable)
                self.assertEqual(len(decay_key), 7)

                # Unpack the tuple key contents
                self.assertIsInstance(decay_key[0], str)
                self.assertIsInstance(decay_key[1], int)
                self.assertIsInstance(decay_key[2], int)
                self.assertIsInstance(decay_key[3], int)
                self.assertIsInstance(decay_key[4], str)
                self.assertIsInstance(decay_key[5], int)
                self.assertIsInstance(decay_key[6], int)
                
                # Unpack the list value contents
                self.assertIsInstance(decay_value, list)
                self.assertIsInstance(decay_value, Iterable)
                self.assertEqual(len(decay_value), 2)
                for v_tup in decay_value:
                    self.assertIsInstance(v_tup, tuple)
                    self.assertIsInstance(v_tup, Iterable)
                    self.assertEqual(len(v_tup), 2)
                    try:
                        self.assertIsInstance(v_tup[0], float)
                    except AssertionError:
                        # Maybe an <int>
                        try:
                            self.assertIsInstance(v_tup[0], int)
                        except AssertionError:
                            # Or a <str>
                            self.assertIsInstance(v_tup[0], str)

                    try:
                        self.assertIsInstance(v_tup[1], float)
                    except AssertionError:
                        # Maybe an <int>
                        try:
                            self.assertIsInstance(v_tup[1], int)
                        except AssertionError:
                            # Or a <str> for 'AP' error types
                            try:
                                self.assertIsInstance(v_tup[1], str)
                            except AssertionError:
                                # Null error types
                                self.assertIsNone(v_tup[1])

        a_pairs = e.ensdf_pairs(edata,"A")
        for parent, daughter in a_pairs.items():
            a_decay = e.get_parent_decay(edata, str(parent[0]), int(parent[3]), mode="A")
            self.assertIsInstance(a_decay, dict)
            self.assertIsInstance(a_decay, Iterable)
            self.assertEqual(len(a_decay), 1)
            for decay_key, decay_value in a_decay.items():
                self.assertIsInstance(decay_key, tuple)
                self.assertIsInstance(decay_key, Iterable)
                self.assertEqual(len(decay_key), 7)

                # Unpack the tuple key contents
                self.assertIsInstance(decay_key[0], str)
                self.assertIsInstance(decay_key[1], int)
                self.assertIsInstance(decay_key[2], int)
                self.assertIsInstance(decay_key[3], int)
                self.assertIsInstance(decay_key[4], str)
                self.assertIsInstance(decay_key[5], int)
                self.assertIsInstance(decay_key[6], int)
                
                # Unpack the list value contents
                self.assertIsInstance(decay_value, list)
                self.assertIsInstance(decay_value, Iterable)
                self.assertEqual(len(decay_value), 2)
                for v_tup in decay_value:
                    self.assertIsInstance(v_tup, tuple)
                    self.assertIsInstance(v_tup, Iterable)
                    self.assertEqual(len(v_tup), 2)
                    try:
                        self.assertIsInstance(v_tup[0], float)
                    except AssertionError:
                        # Maybe an <int>
                        try:
                            self.assertIsInstance(v_tup[0], int)
                        except AssertionError:
                            # Or a <str>
                            self.assertIsInstance(v_tup[0], str)

                    try:
                        self.assertIsInstance(v_tup[1], float)
                    except AssertionError:
                        # Maybe an <int>
                        try:
                            self.assertIsInstance(v_tup[1], int)
                        except AssertionError:
                            # Or a <str> for 'AP' error types
                            try:
                                self.assertIsInstance(v_tup[1], str)
                            except AssertionError:
                                # Null error types
                                self.assertIsNone(v_tup[1])


class GetParentHalflife(unittest.TestCase):

    __doc__="""Unit tests for the `get_parent_halflife` method of the Parent 
    class."""

    def test_get_parent_halflife_returns_dict_for_all_decays(self):
        ecbp_pairs = e.ensdf_pairs(edata,"ECBP")
        for parent, daughter in ecbp_pairs.items():
            ecbp = e.get_parent_halflife(edata, str(parent[0]), int(parent[3]), mode="ECBP", units="best")
            self.assertIsInstance(ecbp, dict)
            self.assertIsInstance(ecbp, Iterable)

        ecbp_pairs = e.ensdf_pairs(edata,"ECBP")
        for parent, daughter in ecbp_pairs.items():
            ecbp = e.get_parent_halflife(edata, str(parent[0]), int(parent[3]), mode="ECBP", units="seconds")
            self.assertIsInstance(ecbp, dict)
            self.assertIsInstance(ecbp, Iterable)

        ecbp_pairs = e.ensdf_pairs(edata,"ECBP")
        for parent, daughter in ecbp_pairs.items():
            ecbp = e.get_parent_halflife(edata, str(parent[0]), int(parent[3]), mode="ECBP", units="s")
            self.assertIsInstance(ecbp, dict)
            self.assertIsInstance(ecbp, Iterable)

        bm_pairs = e.ensdf_pairs(edata,"BM")
        for parent, daughter in bm_pairs.items():
            bm = e.get_parent_halflife(edata, str(parent[0]), int(parent[3]), mode="BM", units="BEST")
            self.assertIsInstance(bm, dict)
            self.assertIsInstance(bm, Iterable)

        bm_pairs = e.ensdf_pairs(edata,"BM")
        for parent, daughter in bm_pairs.items():
            bm = e.get_parent_halflife(edata, str(parent[0]), int(parent[3]), mode="BM", units="SECONDS")
            self.assertIsInstance(bm, dict)
            self.assertIsInstance(bm, Iterable)

        bm_pairs = e.ensdf_pairs(edata,"BM")
        for parent, daughter in bm_pairs.items():
            bm = e.get_parent_halflife(edata, str(parent[0]), int(parent[3]), mode="BM", units="S")
            self.assertIsInstance(bm, dict)
            self.assertIsInstance(bm, Iterable)

        a_pairs = e.ensdf_pairs(edata,"a")
        for parent, daughter in a_pairs.items():
            a = e.get_parent_halflife(edata, str(parent[0]), int(parent[3]), mode="a", units="best")
            self.assertIsInstance(a, dict)
            self.assertIsInstance(a, Iterable)

        a_pairs = e.ensdf_pairs(edata,"a")
        for parent, daughter in a_pairs.items():
            a = e.get_parent_halflife(edata, str(parent[0]), int(parent[3]), mode="a", units="seconds")
            self.assertIsInstance(a, dict)
            self.assertIsInstance(a, Iterable)

        a_pairs = e.ensdf_pairs(edata,"a")
        for parent, daughter in a_pairs.items():
            a = e.get_parent_halflife(edata, str(parent[0]), int(parent[3]), mode="a", units="s")
            self.assertIsInstance(a, dict)
            self.assertIsInstance(a, Iterable)

    def test_get_parent_halflife_returns_none_if_not_correct_decay_mode(self):
        ecbp = e.get_parent_halflife(edata,"Co60",0,mode="ECBP",units='best')
        self.assertIsNone(ecbp)
        bm = e.get_parent_halflife(edata,"Y86",0,mode="BM",units="s")
        self.assertIsNone(bm)
        a = e.get_parent_halflife(edata,"Na22",0,mode="A",units="seconds")
        self.assertIsNone(a)

    def test_get_parent_halflife_returns_none_if_missing_kwargs(self):
        bm = e.get_parent_halflife(edata,"Co60",0,mode="BM")
        self.assertIsNone(bm)
        bm = e.get_parent_halflife(edata,"Co60",0,units='best')
        self.assertIsNone(bm)
        bm = e.get_parent_halflife(edata,"Co60",0)
        self.assertIsNone(bm)
        
    def test_get_parent_halflife_returns_none_if_illegal_string(self):
        decay = e.get_parent_halflife(edata,"Co60", 1, mode="THisIsB@LL@CK$",units="s")
        self.assertIsNone(decay)
        decay = e.get_parent_halflife(edata,"THisIsB@LL@CK$", 1, mode="BM",units="best")
        self.assertIsNone(decay)

    def test_get_parent_halflife_raises_TypeError_if_first_arg_not_list(self):
        with self.assertRaises(TypeError):
            ecbp = e.get_parent_halflife("Db258",edata,0,mode="ECBP",units="best")
        with self.assertRaises(TypeError):
            bm = e.get_parent_halflife("Co60",edata,1,mode="BM",units="best")
        with self.assertRaises(TypeError):
            a = e.get_parent_halflife("Ra226",edata,0,mode="A",units="best")

    def test_get_parent_halflife_raises_NameError_if_wrong_list(self):
        with self.assertRaises(NameError):
            ecbp = e.get_parent_halflife(XXXedataXXX,"Db258",0,mode="ECBP",units="best")
        with self.assertRaises(NameError):
            bm = e.get_parent_halflife(XXXedataXXX,"Co60",1,mode="BM",units="best")
        with self.assertRaises(NameError):
            a = e.get_parent_halflife(XXXedataXXX,"Ra226",0,mode="A",units="best")

    def test_get_parent_halflife_raises_KeyError_if_bad_dict_items_in_list(self):
        bad_dict_items_in_list = [{'a':0, 'b':1, 'c':2}]
        with self.assertRaises(KeyError):
           ecbp = e.get_parent_halflife(bad_dict_items_in_list,"Db258",0,mode="ECBP",units="best")
        with self.assertRaises(KeyError):
           bm = e.get_parent_halflife(bad_dict_items_in_list,"Co60",1,mode="BM",units="best")
        with self.assertRaises(KeyError):
           a = e.get_parent_halflife(bad_dict_items_in_list,"Ra226",0,mode="A",units="best")

           
    def test_get_parent_halflife_returned_contents_of_dict(self):
        ecbp_pairs = e.ensdf_pairs(edata,"ECBP")
        for parent, daughter in ecbp_pairs.items():
            ecbp_decay = e.get_parent_halflife(edata, str(parent[0]), int(parent[3]), mode="ECBP", units="best")
            self.assertIsInstance(ecbp_decay, dict)
            self.assertIsInstance(ecbp_decay, Iterable)
            self.assertEqual(len(ecbp_decay), 1)
            for decay_key, decay_value in ecbp_decay.items():
                self.assertIsInstance(decay_key, tuple)
                self.assertIsInstance(decay_key, Iterable)
                self.assertEqual(len(decay_key), 8)

                # Unpack the tuple key contents
                self.assertIsInstance(decay_key[0], str)
                self.assertIsInstance(decay_key[1], int)
                self.assertIsInstance(decay_key[2], int)
                self.assertIsInstance(decay_key[3], int)
                try:
                    self.assertIsInstance(decay_key[4], float)
                except AssertionError:
                    self.assertIsInstance(decay_key[4], str)
                self.assertIsInstance(decay_key[5], str)
                self.assertIsInstance(decay_key[6], int)
                self.assertIsInstance(decay_key[7], int)
                
                # Unpack the list value contents
                self.assertIsInstance(decay_value, list)
                self.assertIsInstance(decay_value, Iterable)
                self.assertEqual(len(decay_value), 3)
                self.assertIsInstance(decay_value[0], float)
                self.assertIsInstance(decay_value[1], float)
                self.assertIsInstance(decay_value[2], str)

        bm_pairs = e.ensdf_pairs(edata,"BM")
        for parent, daughter in bm_pairs.items():
            bm_decay = e.get_parent_halflife(edata, str(parent[0]), int(parent[3]), mode="BM", units="seconds")
            self.assertIsInstance(bm_decay, dict)
            self.assertIsInstance(bm_decay, Iterable)
            self.assertEqual(len(bm_decay), 1)
            for decay_key, decay_value in bm_decay.items():
                self.assertIsInstance(decay_key, tuple)
                self.assertIsInstance(decay_key, Iterable)
                self.assertEqual(len(decay_key), 8)

                # Unpack the tuple key contents
                self.assertIsInstance(decay_key[0], str)
                self.assertIsInstance(decay_key[1], int)
                self.assertIsInstance(decay_key[2], int)
                self.assertIsInstance(decay_key[3], int)
                try:
                    self.assertIsInstance(decay_key[4], float)
                except AssertionError:
                    self.assertIsInstance(decay_key[4], str)
                self.assertIsInstance(decay_key[5], str)
                self.assertIsInstance(decay_key[6], int)
                self.assertIsInstance(decay_key[7], int)
                
                # Unpack the list value contents
                self.assertIsInstance(decay_value, list)
                self.assertIsInstance(decay_value, Iterable)
                self.assertEqual(len(decay_value), 3)
                try:
                    self.assertIsInstance(decay_value[0], float)
                    self.assertIsInstance(decay_value[1], float)
                    self.assertIsInstance(decay_value[2], str)
                except AssertionError:
                    # Account for 'mixed source' 122Ag(E=X) and
                    # 124Ag (E=0.0+X) beta-minus datasets from ENSDF
                    if decay_value[0] is None:
                        self.assertIsNone(decay_value[0])
                        self.assertIsNone(decay_value[1])
                        self.assertIsNone(decay_value[2])
                

        a_pairs = e.ensdf_pairs(edata,"A")
        for parent, daughter in a_pairs.items():
            a_decay = e.get_parent_halflife(edata, str(parent[0]), int(parent[3]), mode="A", units="s")
            self.assertIsInstance(a_decay, dict)
            self.assertIsInstance(a_decay, Iterable)
            self.assertEqual(len(a_decay), 1)
            for decay_key, decay_value in a_decay.items():
                self.assertIsInstance(decay_key, tuple)
                self.assertIsInstance(decay_key, Iterable)
                self.assertEqual(len(decay_key), 8)

                # Unpack the tuple key contents
                self.assertIsInstance(decay_key[0], str)
                self.assertIsInstance(decay_key[1], int)
                self.assertIsInstance(decay_key[2], int)
                self.assertIsInstance(decay_key[3], int)
                try:
                    self.assertIsInstance(decay_key[4], float)
                except AssertionError:
                    self.assertIsInstance(decay_key[4], str)
                self.assertIsInstance(decay_key[5], str)
                self.assertIsInstance(decay_key[6], int)
                self.assertIsInstance(decay_key[7], int)
                
                # Unpack the list value contents
                self.assertIsInstance(decay_value, list)
                self.assertIsInstance(decay_value, Iterable)
                self.assertEqual(len(decay_value), 3)
                try:
                    self.assertIsInstance(decay_value[0], float)
                    self.assertIsInstance(decay_value[1], float)
                    self.assertIsInstance(decay_value[2], str)
                except AssertionError:
                    # Several alpha decays are reported without T1/2:
                    # 58Ni (E=16795.0) -> 54Fe;
                    # 165Re (E=0.0) -> 161Ta;
                    # 216At (E=57.11) -> 212Bi;
                    # 216At (E=400.0) -> 212Bi;
                    # 215Fr (E=835.5) -> 211At;
                    # 215Fr (E=1121.5) -> 211At;
                    # 237Cm (E=0.0) -> 233Pu;
                    # 271Hs (E=0.0) -> 267Sg.
                    if decay_value[0] is None:
                        self.assertIsNone(decay_value[0])
                        self.assertIsNone(decay_value[1])
                        self.assertIsNone(decay_value[2])

