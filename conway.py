import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Conway:
    def __init__(self, rows=50, cols=50, gen=1000, prob=0.2):
        self.rows = rows
        self.cols = cols
        self.prob = prob
        self.generations = gen
        self.grid = self.initialize_grid(rows, cols, prob)
        self.current_generation = 0
    
    def initialize_grid(self, rows, cols, prob=0.2):
        return np.random.choice([0, 1], size=(rows, cols), p=[1-prob, prob])
    
    def update_grid(self):
        rows, cols = self.grid.shape
        new_grid = np.zeros((rows, cols), dtype=int)

        for row in range(rows):
            for col in range(cols):
                live_neighbors = np.sum(self.grid[max(row-1, 0):min(row+2, rows), max(col-1, 0):min(col+2, cols)]) - self.grid[row, col]
                if self.grid[row, col] == 1 and live_neighbors in [2, 3]:
                    new_grid[row, col] = 1
                elif self.grid[row, col] == 0 and live_neighbors == 3:
                    new_grid[row, col] = 1
        self.grid = new_grid

    def animate(self, i, img, gen_text):
        self.update_grid()
        
        img.set_array(self.grid)
        gen_text.set_text(f"Generation: {self.generations}/{self.current_generation}") 
        self.current_generation += 1  
        return img, gen_text

    def main(self):
        fig, ax = plt.subplots()

        plt.subplots_adjust(bottom=0.2)

        img = ax.imshow(self.grid, cmap='binary')
        ax.axis('off')

        gen_ax = fig.add_axes([0.4, 0.05, 0.2, 0.1])  
        gen_ax.axis('off') 
        gen_text = gen_ax.text(
            0.5, 0.5, "", ha="center", va="center", fontsize=12, transform=gen_ax.transAxes
        )

        self.anim = animation.FuncAnimation(
            fig, self.animate, fargs=(img, gen_text), frames=self.generations, interval=100, repeat=False
        )

        plt.show()