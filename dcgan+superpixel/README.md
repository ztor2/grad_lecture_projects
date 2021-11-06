- 프로젝트 세부 사항은 PDF 파일(dcgan+superpixel_presentation.pdf)을 참고해주시기 바랍니다.

<br>

<p align="center"> <img src="https://i.esdrop.com/d/fha5flk1blzo/BZzXPoAyZh.png" width="75%" align="center"> </p>
<p align="center"> <img src="https://i.esdrop.com/d/fha5flk1blzo/3xZFXkbjmR.png" width="75%" align="center"> </p>


#### 코드 파일 설명

<br>

- **cvd_19:** COVID-19 X-ray 이미지 데이터셋 폴더.
- **skincancer:** 피부암 조직 이미지 데이터셋 폴더.
- **DCGAN.ipynb:** 이미지 생성을 위한 DCGAN 노트북 파일.
- **CNN.ipynb:** 성능 평가를 위한 CNN 분류기 노트북 파일.
- **results_analysis.ipynb:** 결과 분석을 위한 노트북 파일(평균과 표준편차 계산, learning curve 그리기).
- **skin_dataset.py:** 피부암 조직 이미지 데이터를 불러오기 위한 custom dataset 파일.
- **covid_dataset.py:**  COVID-19 X-ray 이미지 데이터를 불러오기 위한 custom dataset 파일.
- 각 데이터셋은 데이터셋 이름 - train or test 폴더 - label 명 폴더로 이루어져 있어야 정상적으로 데이터 로드가 가능합니다.
- pytorch 버전: 1.8.1+cu111
