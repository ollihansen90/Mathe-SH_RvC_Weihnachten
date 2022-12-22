import numpy as np
import matplotlib.pyplot as plt

def steckbrief(tier, label):
    l = "Rentier" if label else "Caribou"
    print(f"Tier: {l}\nSchulterhöhe: {tier[0]} m\nLänge: {tier[1]} m\nGewicht: {tier[2]} kg\nHufbreite: {tier[3]} cm\nAlter: {tier[-2]} Jahre\nFelldichte: {tier[-1]} Haare/cm^2\nFellfarbe:")
    color = np.stack([tier[4]*np.ones([5,5]), tier[5]*np.ones([5,5]), tier[6]*np.ones([5,5])]).transpose(1,2,0)
    plt.figure()
    plt.imshow(color)
    plt.axis("off")
    plt.show()
