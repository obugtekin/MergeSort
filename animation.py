import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.animation import FuncAnimation
import numpy as np
from matplotlib.widgets import Button


def merge_sort(ax, arr, start, end):
    if end - start <= 1:
        return [arr[start]]

    mid = (start + end) // 2

    left = merge_sort(ax, arr, start, mid)
    right = merge_sort(ax, arr, mid, end)

    merged = merge(ax, arr, left, right, start, mid, end)

    return merged


def merge(ax, arr, left, right, start, mid, end):
    merged = []
    l = r = 0

    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            merged.append(left[l])
            l += 1
        else:
            merged.append(right[r])
            r += 1

    while l < len(left):
        merged.append(left[l])
        l += 1

    while r < len(right):
        merged.append(right[r])
        r += 1

    ax.clear()
    ax.bar(range(len(arr)), arr, color='blue', alpha=0.5)
    ax.add_patch(Rectangle((start - 0.5, 0), mid - start, max(arr), edgecolor='red', fill=False))
    ax.add_patch(Rectangle((mid - 0.5, 0), end - mid, max(arr), edgecolor='green', fill=False))
    ax.set_title('Merge Sort')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    ax.set_xlim(-1, len(arr))
    ax.set_ylim(0, max(arr) + 1)
    plt.pause(1)  # Adjust the pause duration here

    ax.clear()
    ax.bar(range(start, end), merged, color='blue', alpha=0.5)
    ax.add_patch(Rectangle((start - 0.5, 0), mid - start, max(merged), edgecolor='red', fill=False))
    ax.add_patch(Rectangle((mid - 0.5, 0), end - mid, max(merged), edgecolor='green', fill=False))
    ax.set_title('Merge Sort')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    ax.set_xlim(-1, len(arr))
    ax.set_ylim(0, max(merged) + 1)
    plt.pause(1)  # Adjust the pause duration here

    for i in range(start, end):
        arr[i] = merged[i - start]
    return merged


def start_animation(event):
    merge_sort(ax, arr, 0, len(arr))
    print("Sorted Array:", arr)
    plt.show()


# Generate random array
array_length = 10
arr = np.random.randint(1, 100, array_length)

print("Original Array:", arr)

fig, ax = plt.subplots()

ax.bar(range(len(arr)), arr, color='blue', alpha=0.5)
ax.set_title('Merge Sort')
ax.set_xlabel('Index')
ax.set_ylabel('Value')
ax.set_xlim(-1, len(arr))
ax.set_ylim(0, max(arr) + 1)

# Create start button
button_ax = plt.axes([0.7, 0.05, 0.1, 0.05])  # [left, bottom, width, height]
button = Button(button_ax, 'Start')
button.on_clicked(start_animation)

plt.show()