import sys
import os
sys.path.append(os.path.dirname(__file__) + '/../')
import textwrap
from tests.apibase import APIBase


obj = APIBase('torch.fmod')

def test_case_1():
    pytorch_code = textwrap.dedent(
        '''
        import torch
        a = torch.tensor([1., 2., 3., 4., 5.])
        result = torch.fmod(a, 1.5)
        '''
    )
    obj.run(pytorch_code, ['result'])

def test_case_2():
    pytorch_code = textwrap.dedent(
        '''
        import torch
        result = torch.fmod(torch.tensor([3., 2, 1, 1, 2, 3]), 2)
        '''
    )
    obj.run(pytorch_code, ['result'])

def test_case_3():
    pytorch_code = textwrap.dedent(
        '''
        import torch
        a = torch.tensor([1., 2., 3., 4., 5.])
        out = torch.tensor([1., 2., 3., 4., 5.])
        result = torch.fmod(a, 1.5, out=out)
        '''
    )
    obj.run(pytorch_code, ['out'])

def test_case_4():
    pytorch_code = textwrap.dedent(
        '''
        import torch
        result = torch.fmod(input=torch.tensor([3., 2, 1, 1, 2, 3]), other=torch.tensor([2]))
        '''
    )
    obj.run(pytorch_code, ['result'])

def test_case_5():
    pytorch_code = textwrap.dedent(
        '''
        import torch
        result = torch.fmod(input=torch.tensor([[3., 2, 1], [1, 2, 3]]), other=torch.tensor([2, 3, 1]))
        '''
    )
    obj.run(pytorch_code, ['result'])