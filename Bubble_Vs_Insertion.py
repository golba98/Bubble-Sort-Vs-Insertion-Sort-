import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

N = 200 
SPEED = 1

def bubble_sort(arr):
    """Generator for Bubble Sort steps."""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
           
            yield arr, [j, j + 1], -1 
            
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
                yield arr, [j, j + 1], -1

    yield arr, [], -1

def insertion_sort(arr):
    """Generator for Insertion Sort steps."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        
        yield arr, [i], j 
        
        while j >= 0 and key < arr[j]:
        
            yield arr, [j, j + 1], i 
            
            arr[j + 1] = arr[j]
            j -= 1
            yield arr, [j + 1], i 
            
        arr[j + 1] = key
        yield arr, [j + 1], i 
    yield arr, [], -1


data_source = [random.randint(1, 100) for _ in range(N)]
data_bubble = data_source.copy()
data_insertion = data_source.copy()


gen_bubble = bubble_sort(data_bubble)
gen_insertion = insertion_sort(data_insertion)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
fig.suptitle(f'Sorting Visualization (N={N})')


bar_rects1 = ax1.bar(range(len(data_bubble)), data_bubble, align="edge", color='skyblue')
ax1.set_title("Bubble Sort")
ax1.set_xlim(0, N)
ax1.set_ylim(0, 110)
text_bubble = ax1.text(0.02, 0.95, "", transform=ax1.transAxes)


bar_rects2 = ax2.bar(range(len(data_insertion)), data_insertion, align="edge", color='lightgreen')
ax2.set_title("Insertion Sort")
ax2.set_xlim(0, N)
ax2.set_ylim(0, 110)
text_insert = ax2.text(0.02, 0.95, "", transform=ax2.transAxes)

iteration_count = [0]

def update_plot(rects, text_obj, data, active_indices, label):
    """Helper to update bars and colors."""
    for i, rect in enumerate(rects):
        rect.set_height(data[i])
        
        rect.set_color('skyblue' if label == "Bubble" else 'lightgreen')
        
      
        if i in active_indices:
            rect.set_color('red')

def animate(frame):
    iteration_count[0] += 1
    

    try:
        b_data, b_active, _ = next(gen_bubble)
        update_plot(bar_rects1, text_bubble, b_data, b_active, "Bubble")
    except StopIteration:
       
        update_plot(bar_rects1, text_bubble, data_bubble, [], "Bubble")
        
   
    try:
        i_data, i_active, _ = next(gen_insertion)
        update_plot(bar_rects2, text_insert, i_data, i_active, "Insertion")
    except StopIteration:
        update_plot(bar_rects2, text_insert, data_insertion, [], "Insertion")

    return bar_rects1, bar_rects2


anim = animation.FuncAnimation(
    fig, 
    animate, 
    frames=None,  
    interval=SPEED, 
    cache_frame_data=False,
    repeat=False
)

plt.show()