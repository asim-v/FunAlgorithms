import ray
import cv2
import numpy as np
import time


def test(img: np.ndarray):
    orb = cv2.AKAZE_create()
    kp = orb.detect(img, None)
    kp, des = orb.compute(img, kp)

    return des


if __name__ == '__main__':
    ray.init(address='auto')
    start_time = time.time()

    img = cv2.imread('./data/cimat1.jpg')

    img_id = ray.put(img)
    futures = [test.remote(img_id) for i in range(100)]

    ray.get(futures)

    print(time.time() - start_time)
