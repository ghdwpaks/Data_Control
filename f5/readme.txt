a399bd679f5006635317a358d2baff185b178cc0의 시점에서 작성된 readme.txt 파일입니다.


멀티 스레드를 사용한 main.py의구동속도보다 싱글 스레드를 사용하는 main_nomul.py의 실행속도가 더 빠른 최악의 사태가 일어났습니다.

이 문제를 해결하기 위하여 multiprocess 패키지를 가져올 예정입니다.

현재 이는 10mutiproc.py 문서에서 활발히 진행중입니다.
10mutiproc.py의 멀티스레드는 정상적으로 작동하지만, Queue 형식의 t 변수가 다른 함수에서도 접근할 수 있게 바꿔줘야만 합니다.





.





A readme.txt file created at the time of a399bd679f5006635317a358d2baff185b178cc0.


main_nomul with single thread rather than main.py with multi thread.There was a worst-case scenario where py ran faster.

To solve this problem, we are going to import multiprocess package.

This is currently active in the 10mutiproc.py document.
Multithreads on 10mutiproc.py work normally, but the t variable in Queue format must be changed so that other functions can access it.




