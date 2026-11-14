# Conditional Generative Design

## Problem

Learn a conditional latent representation of Fashion-MNIST images and inspect how labels influence generated samples.

## Approach

The workflow normalises images, encodes class labels, trains a convolutional conditional variational autoencoder, and inspects latent structure with PCA and t-SNE. Fixed latent vectors are decoded across label conditions to make condition-dependent changes visible.

## Skills

- TensorFlow/Keras modelling
- Convolutional encoder/decoder design
- Conditional variational autoencoders
- Latent-space visualisation with PCA and t-SNE

## Source and data

Fashion-MNIST is loaded through the Keras dataset interface. No local training cache or serialized weights are included; obtain data through the documented loader.

## Reproduce

Create the documented Python environment, download Fashion-MNIST through Keras on first run, set a fixed seed, and execute the compact training configuration. Save generated grids as new artefacts rather than relying on local cache files.

## Limits

Generated images are exploratory samples, not production-ready designs. Visual quality depends on training duration, architecture, random seed, class balance, and hardware; sample grids alone do not establish generalisation.
