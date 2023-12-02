# -*- coding: utf-8 -*-
"""generate image.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/126sL_mgzsh82l-YvkfrDXWgKCxH9N-kW
"""

import torch
from diffusers import StableDiffusionPipeline

pipe = StableDiffusionPipeline.from_pretrained(
    "CompVis/stable-diffusion-v1-4", torch_dtype=torch.float16
)

prompt = "a photograph of an astronaut riding a horse"
image = pipe(prompt).images[
    0
]  # image here is in [PIL format](https://pillow.readthedocs.io/en/stable/)

# Now to display an image you can either save it such as:
image.save(f"astronaut_rides_horse.png")