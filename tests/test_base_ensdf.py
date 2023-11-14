import pytest
import unittest
import numpy as np
import pandas as pd
from collections.abc import Iterable

import paceENSDF as pe
e = pe.ENSDF()
edata = e.load_ensdf()
cdata = e.load_pace()

class LoadData(unittest.TestCase):

    __doc__="""Unit tests for the `load_ensdf` and `load_pace` methods of the 
    BaseENSDF class."""

    # ENSDF (Archive: September 2023)
    def test_load_ensdf_returns_list(self):
        self.assertIsInstance(edata, list)
        self.assertIsInstance(edata, Iterable)

    def test_load_ensdf_returned_list_length_is_3254(self):
        self.assertEqual(len(edata), 3254)

    def test_load_ensdf_returned_contents_of_list(self):
        total_gammas = 0
        total_levels = 0
        total_particles = 0
        for element in edata:
            self.assertIsInstance(element, dict)
            self.assertEqual(len(element), 17)
            
            for k,v in element.items():
                if k == "totalNumberGammas":
                    total_gammas = total_gammas+v
                if k == "totalNumberLevels":
                    total_levels = total_levels+v
                if k == "totalNumberParticleDecays":
                    total_particles = total_particles+v

        # Totals reflect ENSDF archive: September 2023
        self.assertEqual(total_gammas, 92264)
        self.assertEqual(total_levels, 41094)
        self.assertEqual(total_particles, 28942)

    # COINC (generated from ENSDF archive: September 2023)
    def test_load_pace_returns_list(self):
        self.assertIsInstance(cdata, list)
        self.assertIsInstance(cdata, Iterable)

    # Only including GG and GX (i.e. PG files removed for now)
    def test_load_pace_returned_list_length_is_4788(self):
        self.assertEqual(len(cdata), 4788)

    def test_load_pace_returned_contents_of_list(self):
        # GG
        total_gammas = []
        total_levels = []
        total_gammagamma = []
        # GX
        total_x = []
        total_gammax = []
        # Number coinc datasets
        num_coinc_a_gg = 0
        num_coinc_a_gx = 0
        num_coinc_a_pg = 0
        num_coinc_bm_gg = 0
        num_coinc_bm_gx = 0
        num_coinc_bm_pg = 0
        num_coinc_ecbp_gg = 0
        num_coinc_ecbp_gx = 0
        num_coinc_ecbp_pg = 0
        
        for d in cdata:
            self.assertIsInstance(d, dict)
            self.assertGreater(len(d), 0)

            if d["datasetID"] == "GG":
                total_gammas.append(d["totalNumberGammas"])
                total_levels.append(d["totalNumberLevels"])
                total_gammagamma.append(d["totalNumberGammaCoincidences"])
            if d["datasetID"] == "GX":
                total_x.append(d["totalNumberKshellXrays"])
                total_gammax.append(d["totalNumberKshellXrayCoincidences"])

            if d["decayMode"] == "alphaDecay" and d["datasetID"] == "GG":
                num_coinc_a_gg = num_coinc_a_gg + 1
            if d["decayMode"] == "alphaDecay" and d["datasetID"] == "GX":
                num_coinc_a_gx = num_coinc_a_gx + 1
            if d["decayMode"] == "alphaDecay" and d["datasetID"] == "PG":
                num_coinc_a_pg = num_coinc_a_pg + 1
                
            if d["decayMode"] == "betaMinusDecay" and d["datasetID"] == "GG":
                num_coinc_bm_gg = num_coinc_bm_gg + 1
            if d["decayMode"] == "betaMinusDecay" and d["datasetID"] == "GX":
                num_coinc_bm_gx = num_coinc_bm_gx + 1
            if d["decayMode"] == "betaMinusDecay" and d["datasetID"] == "PG":
                num_coinc_bm_pg = num_coinc_bm_pg + 1
                
            if d["decayMode"] == "electronCaptureBetaPlusDecay" and d["datasetID"] == "GG":
                num_coinc_ecbp_gg = num_coinc_ecbp_gg + 1
            if d["decayMode"] == "electronCaptureBetaPlusDecay" and d["datasetID"] == "GX":
                num_coinc_ecbp_gx = num_coinc_ecbp_gx + 1
            if d["decayMode"] == "electronCaptureBetaPlusDecay" and d["datasetID"] == "PG":
                num_coinc_ecbp_pg = num_coinc_ecbp_pg + 1

        self.assertEqual(sum(total_gammas), 90122)
        self.assertEqual(sum(total_levels), 37509)
        self.assertEqual(sum(total_gammagamma), 497171)
        self.assertEqual(sum(total_x), 14364)
        self.assertEqual(sum(total_gammax), 511650)
        #self.assertEqual(num_coinc_a/3, 279)
        #self.assertEqual(num_coinc_bm/3, 1026)
        #self.assertEqual(num_coinc_ecbp/3, 1089)

        self.assertEqual(num_coinc_a_gg, 279)
        self.assertEqual(num_coinc_a_gg, num_coinc_a_gx)
        #self.assertEqual(num_coinc_a_gg, num_coinc_a_pg)

        self.assertEqual(num_coinc_bm_gg, 1026)
        self.assertEqual(num_coinc_bm_gg, num_coinc_bm_gx)
        #self.assertEqual(num_coinc_bm_gg, num_coinc_bm_pg)

        self.assertEqual(num_coinc_ecbp_gg, 1089)
        self.assertEqual(num_coinc_ecbp_gg, num_coinc_ecbp_gx)
        #self.assertEqual(num_coinc_ecbp_gg, num_coinc_ecbp_pg)
        
        
