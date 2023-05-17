# Copyright (c) 2023 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import textwrap

from apibase import APIBase

obj = APIBase("torch.dstack")


def _test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        a = torch.tensor([1, 2, 3])
        b = torch.tensor([4, 5, 6])
        result = torch.dstack((a, b))
        """
    )
    obj.run(pytorch_code, ["result"])


def _test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        a = torch.tensor([[1],[2],[3]])
        b = torch.tensor([[4],[5],[6]])
        result = torch.dstack((a, b))
        """
    )
    obj.run(pytorch_code, ["result"])


def _test_case_3():
    pytorch_code = textwrap.dedent(
        """
        import torch
        a = torch.tensor([[[1, 1],[2, 2],[3, 3]]])
        b = torch.tensor([[[4],[5],[6]]])
        result = torch.dstack((a, b))
        """
    )
    obj.run(pytorch_code, ["result"])


def _test_case_4():
    pytorch_code = textwrap.dedent(
        """
        import torch
        result = torch.dstack((torch.tensor([[[1, 1],[2, 2],[3, 3]]]), torch.tensor([[[4],[5],[6]]])))
        """
    )
    obj.run(pytorch_code, ["result"])


def _test_case_5():
    pytorch_code = textwrap.dedent(
        """
        import torch
        out = torch.tensor([[[1, 1],[2, 2],[3, 3]]])
        result = torch.dstack((torch.tensor([[[1, 1],[2, 2],[3, 3]]]), torch.tensor([[[4],[5],[6]]])), out=out)
        """
    )
    obj.run(pytorch_code, ["result", "out"])
