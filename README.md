# Image Grid

Displays images and predictions in a grid:

```python
from image_grid import save_image_grid

images = ...       # numpy array of shape (n, h, w, c)
predictions = ...  # numpy array of shape (n,)

save_image_grid("grid.png", images, predictions)
```
