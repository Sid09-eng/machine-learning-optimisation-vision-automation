# Conditional Generative Design

## Problem

I trained a model to generate Fashion-MNIST-like images while controlling the class label, then looked at how the label changed the output.

## Approach

I normalised the images, encoded the labels, and trained a convolutional conditional VAE. I used PCA and t-SNE to look at the latent space, then decoded the same latent vectors with different labels to see the change.

## Skills

- TensorFlow/Keras modelling
- Convolutional encoder/decoder design
- Conditional variational autoencoders
- Latent-space visualisation with PCA and t-SNE

## Source and data

I load Fashion-MNIST through Keras. I left out local caches and trained weights; the data can be downloaded through the loader.

## Reproduce

Create the Python environment, let Keras download Fashion-MNIST on the first run, set the seed, and train the smaller configuration. Save fresh image grids instead of relying on files from my machine.

## Limits

The generated images are for exploration, not finished designs. Quality changes with training time, model shape, seed, class balance, and hardware. A few good-looking grids do not prove the model generalises.
