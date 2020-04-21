
| Programming task | #2                                                           |
| :--------------: | :----------------------------------------------------------- |
|      **By**      | **- Adel Moustafa**                                                                                                                                   **- Mahmoud Abdelrhman**                                                                                                                  **- Mohamed Kamal**                                                                                                                                    **- Mohamed Yasser** |
|      **To**      | **Prof/ Inas A. Yassine**                                    |



# Bulk magnetization vector
 ​There are three used functions to rotate the bulk magnetization vector and plot its trajectory:

**1.Excitation:** It's used to rotate the bulk magnetization and it's trajectory during excitation process.

**2.Relaxation:** It's used to rotate the bulk magnetization and it's trajectory during relaxation process.

**3.Update_line:** It's used to update the plotted data.

In addition to **get_parametesrs()**, used to get parameters by console.

**because of the nonuniformity effect which spins in the same box and has different Larmor frequency, so the spins will have different trajectory**

This GIFs is to simulate Bulk magnetization vector rotation.



**Exitation GIF**


![Image](Images/Exitation.gif)

**Relaxition GIF**


![Image](Images/Relaxition.gif)




# K-space

The K-space of this Image is calculated using the function **image_to_kspace()**.

- First, we shift the image by N/2. It is simply done by the function, **np.fft.ifftshift()**.
- Then we get Fourier for the result by **np.fft.fftn()**. 
- After that, we apply shifting on Fourier by N/2 using **np.fft.ifftshift()**. 
- The result is k-space.

**The used image in the k-space**

![Image](Images/brain_mri.jpeg)

**And this is the k-space image.** 

![Image](Images/kspace_brain.png)


