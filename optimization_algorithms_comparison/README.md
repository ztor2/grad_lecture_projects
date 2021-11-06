#### 프로젝트 세부 내용은 PDF 파일을 참고해주시기 바랍니다.

<p align="center"> <img src="https://i.esdrop.com/d/fha5flk1blzo/gcBbjy78Kx.png" width="70%" align="center"> </p>

#### 코드 파일 설명
- opts.py: 구현한 모델(Newton, BFGS, SR1)을 import 할 수 있도록 각 모델을 포함한 파일. L-BFGS는 SciPy로 구현.
- execution.ipynb: 각 모델의 results를 얻기 위한 노트북 파일. test function의 plot 포함.

#### 주요 라이브러리
- sympy(pip install sympy)
- memory profiler(pip install memory_profiler)

#### 참고
- test function reference: https://en.wikipedia.org/wiki/Test_functions_for_optimization
- damp-update(for curvature condition) 참고 링크: https://github.com/scipy/scipy/blob/v1.6.3/scipy/optimize/_hessian_update_strategy.py#L239-L374 363 ~ 374 line



