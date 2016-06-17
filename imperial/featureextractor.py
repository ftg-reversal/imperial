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

import cv2
import scipy

class FeatureExtractor(object):
    def extract_feature(self, raw_feature):
        raise NotImplementedError

class TrainedFeatureExtractor(FeatureExtractor):
    def train(self):
        raise NotImplementedError

class SurfExtractor(FeatureExtractor):
    def __init__(self, surf_thresh=100, upright=False):
        self.surf_detector = cv2.xfeatures2d.SURF_create(surf_thresh, 4, 2, True, upright)

    def extract_feature(self, raw_feature):
        """
        :type raw_feature: scipy.array
        """
        if raw_feature == None:
            return []
        mono_img = cv2.cvtColor(raw_feature, cv2.COLOR_BGR2GRAY)
        keypoints, descriptors = self.surf_detector.detectAndCompute(mono_img, None)
        if descriptors is None:
            print("None from SURF !!!!")
            return []
        else:
            return [descriptor for descriptor in descriptors]
