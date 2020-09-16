# YSCEC_video_download
now you can download streaming videos from YSCEC

1. <h1>필요한 것</h1>
  - python3 이상
  - requests (pip/ pip3 install requests 해주세요)
  - Chrome
  - **자기 신상이 걱정된다면 VPN 사용하세요**
 
2. <h1>사용 방법</h1></br>
  - 윈도우는 cmd, macos는 터미널을 여시고 git clone https://github.com/HyoungjooChae/YSCEC_video_download.git 로 코드를 다운받으세요.</br>
  크롬으로 YSCEC에 접속하여 다운받고 싶은 강의 영상을 재생시킵니다.</br>
  - 이 때 빈공간 우클릭 > 검사 > 네트워크 탭으로 가시면 목록이 뜹니다. media_xx.ts 파일들이 매우 많이 나올텐데 아무거나 우클릭 > copy > copy link address 해주세요.</br>
  - cd YSCEC_video_download/ 명령어를 이용해 폴더에 들어가신 뒤 python download_video.py 명령어를 입력하시면 됩니다.(macos는 python3 입니다.)</br>
  - 아까 복사해둔 url에서 /media_xx.ts부분을 지운뒤 입력해주세요.</br>
  - 생성할 동영상 파일명을 입력해 주세요.</br>
  - 조금 기다리면 동영상 다운로드가 완료됩니다.(40초 정도 소요)
  ![image](https://user-images.githubusercontent.com/51402122/93301858-00956500-f834-11ea-936a-b788976144dd.png)
  ![image](https://user-images.githubusercontent.com/51402122/93301930-1f93f700-f834-11ea-83e3-33b349f23609.png)

  
