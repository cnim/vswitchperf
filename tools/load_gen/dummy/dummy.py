# Copyright 2015 Intel Corporation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Class with implementation of wrapper of dummy load generator"""

from tools.load_gen.load_gen import ILoadGenerator

class DummyLoadGen(ILoadGenerator):
    """Dummy load generator, which doesn't generate any load"""
    def __init__(self, stress_config):
        """Initialise process state."""
        pass

    def start(self):
        """Start stress load if it was requested"""
        pass

    def kill(self):
        """Kill stress load if it is active"""
        pass
