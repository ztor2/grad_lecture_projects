opts.py
- 구현한 모델(Newton, BFGS, SR1)을 import 할 수 있도록 각 모델을 포함한 파일.
- L-BFGS는 SciPy로 구현.

execution.ipynb
- 각 모델의 results를 얻기 위한 주피터 노트북 파일.
- test function의 plot 포함.

requirement libraries
- sympy(pip install sympy)
- memory profiler(pip install memory_profiler)

test function 출처 참고 링크
https://en.wikipedia.org/wiki/Test_functions_for_optimization

damp-update(for curvature condition) 참고 링크
https://github.com/scipy/scipy/blob/v1.6.3/scipy/optimize/_hessian_update_strategy.py#L239-L374
363 ~ 374 line



