from tkinter import *
from tkinter import ttk
import random
import time

# Bubble Sort
def bubble_sort(data, drawData, timeTick):
    for i in range(len(data) - 1):
        for j in range(len(data) - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                drawData(data, getColorArray(len(data), 0, len(data) - 1, j, j + 1, True))
                time.sleep(timeTick)
    drawData(data, ['green' for x in range(len(data))])

# Quick Sort
def partition(data, head, tail, drawData, timeTick):
    border = head
    pivot = data[tail]

    drawData(data, getColorArray(len(data), head, tail, border, border))
    time.sleep(timeTick)

    for j in range(head, tail):
        if data[j] < pivot:
            drawData(data, getColorArray(len(data), head, tail, border, j, True))
            time.sleep(timeTick)

            data[border], data[j] = data[j], data[border]
            border += 1

        drawData(data, getColorArray(len(data), head, tail, border, j))
        time.sleep(timeTick)

    drawData(data, getColorArray(len(data), head, tail, border, tail, True))
    time.sleep(timeTick)

    data[border], data[tail] = data[tail], data[border]
    
    return border

def quick_sort(data, head, tail, drawData, timeTick):
    if head < tail:
        partitionIdx = partition(data, head, tail, drawData, timeTick)
        quick_sort(data, head, partitionIdx - 1, drawData, timeTick)
        quick_sort(data, partitionIdx + 1, tail, drawData, timeTick)

# Merge Sort
def merge_sort(data, drawData, timeTick):
    def merge(left, right):
        result = []
        while left and right:
            if left[0] < right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        result.extend(left)
        result.extend(right)
        return result

    if len(data) > 1:
        mid = len(data) // 2
        left = data[:mid]
        right = data[mid:]

        merge_sort(left, drawData, timeTick)
        merge_sort(right, drawData, timeTick)

        data[:] = merge(left, right)
        drawData(data, ['green' for x in range(len(data))])

# Heap Sort
def heapify(data, n, i, drawData, timeTick):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and data[left] > data[largest]:
        largest = left

    if right < n and data[right] > data[largest]:
        largest = right

    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        drawData(data, getColorArray(len(data), 0, len(data) - 1, i, largest, True))
        time.sleep(timeTick)

        heapify(data, n, largest, drawData, timeTick)

def heap_sort(data, drawData, timeTick):
    n = len(data)

    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i, drawData, timeTick)

    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        drawData(data, getColorArray(len(data), 0, len(data) - 1, 0, i, True))
        time.sleep(timeTick)

        heapify(data, i, 0, drawData, timeTick)

# Insertion Sort
def insertion_sort(data, drawData, timeTick):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
        drawData(data, getColorArray(len(data), 0, len(data) - 1, j, j + 1, True))
        time.sleep(timeTick)
    drawData(data, ['green' for x in range(len(data))])

# Function to get the color array for visualization
def getColorArray(dataLen, head, tail, border, currIdx, isSwapping=False):
    colorArray = []
    for i in range(dataLen):
        if i >= head and i <= tail:
            colorArray.append('gray')
        else:
            colorArray.append('white')

        if i == tail:
            colorArray[i] = 'blue'
        elif i == border:
            colorArray[i] = 'red'
        elif i == currIdx:
            colorArray[i] = 'yellow'

        if isSwapping:
            if i == border or i == currIdx:
                colorArray[i] = 'green'

    return colorArray

# Tkinter GUI setup
root = Tk()
root.title('Sorting Algorithm Visualisation')
root.maxsize(900, 600)
root.config(bg='black')

# Global variables
selected_alg = StringVar()
data = []

# Function to draw the data on the canvas
def drawData(data, colorArray):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data) + 1)
    offset = 30
    spacing = 10
    normalizedData = [i / max(data) for i in data]
    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0 + 2, y0, anchor=SW, text=str(data[i]))

    root.update_idletasks()

# Function to generate random data
def Generate():
    global data

    minVal = int(minEntry.get())
    maxVal = int(maxEntry.get())
    size = int(sizeEntry.get())

    data = []
    for _ in range(size):
        data.append(random.randrange(minVal, maxVal+1))

    drawData(data, ['red' for x in range(len(data))])

# Function to start the selected sorting algorithm
def StartAlgorithm():
    global data
    if not data: return

    if algMenu.get() == 'Quick Sort':
        quick_sort(data, 0, len(data) - 1, drawData, speedScale.get())

    elif algMenu.get() == 'Bubble Sort':
        bubble_sort(data, drawData, speedScale.get())

    elif algMenu.get() == 'Merge Sort':
        merge_sort(data, drawData, speedScale.get())

    elif algMenu.get() == 'Heap Sort':
        heap_sort(data, drawData, speedScale.get())

    elif algMenu.get() == 'Insertion Sort':
        insertion_sort(data, drawData, speedScale.get())

    drawData(data, ['green' for x in range(len(data))])

# Function to reset the array and canvas
def Reset():
    global data
    minVal = int(minEntry.get())
    maxVal = int(maxEntry.get())
    size = int(sizeEntry.get())

    data = []
    for _ in range(size):
        data.append(random.randrange(minVal, maxVal + 1))

    drawData(data, ['red' for x in range(len(data))])

# Tkinter layout for the GUI
UI_frame = Frame(root, width=600, height=200, bg='grey')
UI_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=600, height=380, bg='white')
canvas.grid(row=1, column=0, padx=10, pady=5)

# User Interface
Label(UI_frame, text="Algorithm: ", bg='grey').grid(row=0, column=0, padx=5, pady=5, sticky=W)
algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Bubble Sort', 'Quick Sort', 'Merge Sort', 'Heap Sort', 'Insertion Sort'])
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)

speedScale = Scale(UI_frame, from_=0.001, to=5.0, length=200, digits=5, resolution=0.001, orient=HORIZONTAL, label="Select Speed [s]")
speedScale.grid(row=0, column=2, padx=5, pady=5)
Button(UI_frame, text="Start", command=StartAlgorithm, bg='red').grid(row=0, column=3, padx=5, pady=5)

sizeEntry = Scale(UI_frame, from_=3, to=25, resolution=1, orient=HORIZONTAL, label="Data Size")
sizeEntry.grid(row=1, column=0, padx=5, pady=5)

minEntry = Scale(UI_frame, from_=0, to=10, resolution=1, orient=HORIZONTAL, label="Min Value")
minEntry.grid(row=1, column=1, padx=5, pady=5)

maxEntry = Scale(UI_frame, from_=10, to=100, resolution=1, orient=HORIZONTAL, label="Max Value")
maxEntry.grid(row=1, column=2, padx=5, pady=5)

Button(UI_frame, text="Generate", command=Generate, bg='white').grid(row=1, column=3, padx=5, pady=5)

Button(UI_frame, text="Reset", command=Reset, bg='yellow').grid(row=2, column=3, padx=5, pady=5)

root.mainloop()
