import random
import math

NO_OF_PRISONERS = 100
TIMES = 1000


def main():
    boxes = []
    picked_boxes = []
    for i in range(1, 101):
        boxes.append(i)

    # shuffling
    for i in range(len(boxes)):
        random_index = random.randint(0, 99)
        boxes[i], boxes[random_index] = boxes[random_index], boxes[i]

    for i in range(1, NO_OF_PRISONERS + 1):
        val, previous = None, i
        for j in range(1, NO_OF_PRISONERS // 2 + 1):
            val = boxes[previous - 1]
            if val == i:
                break
            previous = val

        picked_boxes.clear()
        if val != i:
            return "Execute"

    return "Free"


if __name__ == "__main__":
    avg = 0
    for x in range(TIMES):
        c = 0
        for y in range(100):
            if main() == "Free":
                c += 1
        avg += c
        print("\r|", "█" * math.ceil(x / TIMES * 100), "=" * math.ceil((TIMES - x - 1) / TIMES * 100), "|",
              math.ceil(x / TIMES * 100), "% done", end="")
    print()
    print(f"Average number of times prisoners are freed: {avg / TIMES}%")
