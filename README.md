# YSCEC_video_download
you can download streaming video from YSCEC

1. 필요한 것
  - python3 이상
  - requests
  - Chrome
 
2. 사용 방법
  윈도우는 cmd, macos는 터미널을 여시고 git clone https://github.com/HyoungjooChae/YSCEC_video_download.git 로 코드를 다운받으세요.</br>
  크롬으로 YSCEC에 접속하여 다운받고 싶은 강의 영상을 재생시킵니다.
  이 때 빈공간 우클릭 > 검사 > 네트워크 탭으로 가시면 목록이 뜹니다. media_*.ts 파일들이 매우 많이 나올텐데 아무거나 우클릭 > copy > copy link address 해주세요.
  cd YSCEC_video_download/ 명령어를 이용해 폴더에 들어가신 뒤 python download_video.py 명령어를 입력하시면 됩니다.(macos는 python3 입니다.)
  아까 복사해둔 url에서 /media_*.ts부분을 지운뒤 입력해주세요.
  생성할 동영상 파일명을 입력해 주세요.
  조금 기다리면 동영상 다운로드가 완료됩니다.(40초 정도 소요)
  
