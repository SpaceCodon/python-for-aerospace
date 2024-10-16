from astropy.io import fits
from astropy.visualization import astropy_mpl_style
from astropy.utils.data import get_pkg_data_filename
import matplotlib.pyplot as plt

with fits.open("M6707HH.fits") as file:
    file.info()
    print(file[0].header)                                           # prints out header information for the primary HDU

image_file = get_pkg_data_filename("M6707HH.fits")
image_data = fits.getdata(image_file, ext=0)

print(f"\nThe dimensions of this FITS image are {image_data.shape}.")  # prints the dimensions of the FITS image

# Visualize the FITS file
plt.style.use(astropy_mpl_style)
plt.figure()
plt.imshow(image_data)
plt.colorbar()
plt.show()