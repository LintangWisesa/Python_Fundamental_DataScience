import imageio
from mlxtend.image import EyepadAlign


### Fit EyepadAlign on a single target image

eyepad = EyepadAlign()
target_image = imageio.imread('celeba-subset/000001.jpg')
print('Target image shape: ', target_image.shape)

eyepad.fit_image(target_image);