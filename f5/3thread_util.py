from threading import Thread
from queue import Queue

queue = Queue()


def consumer():
    print('Consumer waiting')  # 뒤에 나오는 put() 이후에 실행함        
    print("queue.get() :",queue.get())
    print('Consumer done')

num = 1

thread = Thread(target=consumer)
thread.start()

# 스레드가 처음으로 실행할 때도 Queue 인스턴스에 아이템이 들어가서 get 메서드에서 반환할 아이템이 생기기 전에는 마치지 못함
print('Producer putting')
queue.put(num)  # 앞에 나온 get() 이전에 실행
thread.join()
print('Producer done')

# 결과
# Consumer waiting
# Producer putting
# Consumer done
# Producer done