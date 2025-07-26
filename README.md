Sorting Algorithm Visualizer


A Python-based sorting algorithm visualizer built with Tkinter and Matplotlib to help users visualize how different sorting algorithms work in real-time. This project showcases multiple sorting algorithms, including Bubble Sort, Quick Sort, Merge Sort, Insertion Sort, and Heap Sort. It allows users to watch how these algorithms manipulate data step-by-step, providing a better understanding of sorting mechanics.




Features


Multiple Sorting Algorithms: Visualize popular sorting algorithms like:

Bubble Sort

Quick Sort

Merge Sort

Insertion Sort

Heap Sort

Interactive User Interface: Built with Tkinter for a smooth and interactive experience.

Customizable Data Size: Adjust the number of data points you want to sort.

Control Sorting Speed: Control the speed of the sorting process with an adjustable slider.

Real-time Visualization: Watch the data being sorted in real-time.

Reset: Reset the visualization to generate new random data.

Color-Coded Sorting Steps: Each step of the sorting process is highlighted using different colors for clarity:

Red: Elements being swapped.

Blue: Pivot (for Quick Sort).

Green: Sorted elements.






Prerequisites


Before you run this project, you need to have Python 3.x installed on your machine. You also need to install the required dependencies:

Tkinter (for the GUI)

Matplotlib (for real-time charting)

Time (to simulate the sorting speed)

To install these dependencies, you can use pip:

bash
Copy
Edit
pip install matplotlib
Note: Tkinter comes pre-installed with Python, so no need to install it separately.

How to Run the Project
Clone the Repository:

First, clone the repository to your local machine using the following command:

bash
Copy
Edit
git clone https://github.com/yourusername/sortingAlgoVisualizer.git
Navigate to the Project Directory:

bash
Copy
Edit
cd sortingAlgoVisualizer
Run the Python Script:

bash
Copy
Edit
python sortingVisualizer.py
This will open the GUI, where you can select the algorithm, adjust the data size, speed, and watch the sorting process unfold.





How It Works


Generate Random Data: When you click the Generate button, random data is created based on the size and range values that you set.

Select a Sorting Algorithm: Choose one of the available sorting algorithms from the dropdown menu.

Start the Sorting Process: Click the Start button to begin the sorting visualization. You can see how the algorithm sorts the data step-by-step.

Control Sorting Speed: Adjust the speed slider to make the sorting process slower or faster. If you want to watch the sorting in slow motion, move the slider to the left.

Reset: After completion, you can click the Reset button to generate new random data and start over.

Supported Sorting Algorithms
Bubble Sort: Repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The process repeats until no more swaps are needed.

Quick Sort: Selects a 'pivot' element and partitions the array into elements less than the pivot and greater than the pivot. The same process is applied recursively to the subarrays.

Merge Sort: Divides the array into halves, sorts each half recursively, and merges the sorted halves.

Insertion Sort: Builds the sorted array one item at a time by repeatedly picking the next element and inserting it into its correct position.

Heap Sort: Converts the list into a binary heap, then extracts the maximum element and places it in the sorted array.

Screenshots
Initial State (Random Data)

Sorting in Action

Example
1. Select the sorting algorithm.
2. Set data size and value range.
3. Adjust the sorting speed.
4. Click Start to see the algorithm in action.
Contributing
Contributions to this project are welcome! If you find a bug or have suggestions for improvements, feel free to open an issue or submit a pull request.

Steps to contribute:

Fork the repository.

Create a new branch.

Make your changes.

Push your changes to your forked repository.

Open a pull request.

License
This project is open-source and available under the MIT License.

Acknowledgements
Tkinter: Used for the graphical user interface.

Matplotlib: Used for real-time visualization of the sorting algorithms.

Python: Programming language used for the implementation of the project.

Contact
GitHub: @kraftankaran

Email: your-kc291684@gmail.com
