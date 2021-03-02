```python
# The numbers in data.txt represent pixels in black color (0,0,0)

from PIL import Image

data = eval(open('data.txt').read())
new = Image.new('RGB',(800,200),'white')
new_pixels = new.load()
for i in data:
    new_pixels[i[0],i[1]] = (0,0,0)

new.save("misc.png")
```

![](../Rev/images/misc.png)
