# Copyright 2016 The Gemmlowp Authors. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Generates the arm32 headers used by the gemm/gemv lib."""

import cc_emitter
import common
import neon_emitter_64
import streams_common


def Main():
  """."""
  cc = cc_emitter.CCEmitter()
  common.GenerateHeader(cc, 'gemmlowp_meta_streams_arm_64', 'GEMMLOWP_NEON_64')

  cc.EmitNamespaceBegin('gemmlowp')
  cc.EmitNamespaceBegin('meta')
  cc.EmitNewline()

  streams_common.GenerateUInt8x8Streams(cc, neon_emitter_64.NeonEmitter64(), 8)

  cc.EmitNamespaceEnd()
  cc.EmitNamespaceEnd()
  cc.EmitNewline()

  common.GenerateFooter(cc, 'Meta gemm for arm64 requires: GEMMLOWP_NEON_64!')


if __name__ == '__main__':
  Main()
