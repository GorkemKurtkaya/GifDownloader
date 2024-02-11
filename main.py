import imageio.v3 as iio

filenames = ['1.png', '2.png','3.png']
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('KomutanLogarınDedesi.gif', images, duration = 500, loop = 0)
