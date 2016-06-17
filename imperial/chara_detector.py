#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Imperial
#  ======
#  Copyright (C) 2015 FTG-Reversal
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

import imperial.featureextractor
import imperial.onlinedetector

class CharaDetector(imperial.onlinedetector.Detector):
    def __init__(self, word_num, surf_thresh=5, n_jobs=4):
        SURF_extractor = imperial.featureextractor.SurfExtractor(surf_thresh=surf_thresh)
        BoF_extractor = imperial.onlinedetector.BagofFeaturesDetector(SURF_extractor, word_num=word_num, n_jobs=n_jobs)
        RF_classifier = imperial.onlinedetector.RFDetector(BoF_extractor, n_estimators=1000)
        self.classifier = RF_classifier

    def update(self, raw_img, key):
        self.classifier.update(raw_img, key)

    def train(self):
        self.classifier.train()

    def classify(self, raw_img):
        return self.classifier.classify(raw_img)

    def classify_proba(self, raw_img):
        return self.classifier.classify_proba(raw_img)
