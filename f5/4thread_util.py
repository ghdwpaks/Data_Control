from threading import Thread
from queue import Queue
import time

queue = Queue(1)  # 크기가 1인 버퍼


def consumer():
    time.sleep(0.1)  # 대기
    queue.get()  # 두 번째로 실행함
    print('Consumer got 1')
    queue.get()  # 네 번째로 실행함
    print('Consumer got 2')


thread = Thread(target=consumer)
thread.start()

""" 대기 결과로 consumer 스레드에서 get을 호출하기 전에 생산 스레드에서 put으로 객체 두 개를 큐에 집어넣는 동작이 일어나야 함
하지만 Queue의 크기가 1임. 다시 말해 두 번째 put 호출이 블록된 상태에서 빠져나와서 두 번째 아이템을 큐에 넣을 수 있으려면, 큐에 아이템을
추가하는 생산자는 소비 스레드에서 적어도 한 번은 get을 호출하기를 기다려야 함"""

queue.put(object())  # 첫 번째로 실행
print('Producer put 1')
queue.put(object())  # 세 번째로 실행
print('Producer put 2')
thread.join()
print('Producer done')

# 결과
# Producer put 1
# Consumer got 1
# Producer put 2
# Consumer got 2
# Producer done